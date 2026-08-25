#!/usr/bin/env node
/**
 * 产品克隆 + 闪光点导入脚本
 *
 * 功能：从模板产品克隆一个新产品，并把规格书提取的闪光点（标题/一句话卖点/特性卡片+图标）写入新产品。
 * 只改闪光点部分（标题 heading + 5 张特性卡片），其他内容（规格短代码、订购、相关案例、FAQ、3D 等）一律不动。
 *
 * 用法：
 *   node clone_highlights.js --template <模板产品ID> --config <JSON配置>
 *
 * JSON 配置示例：
 * {
 *   "name": "IG532",
 *   "title": "IG532 系列边缘网关",
 *   "oneLiner": "多串口边缘网关，打破数据壁垒，为工业数字化赋能",
 *   "cards": [
 *     {"icon": "MultiDevice.svg", "title": "多串口采集", "desc": "支持 4×RS485，满足多设备并行接入"},
 *     ...
 *   ]
 * }
 *
 * 说明：
 * - 模板产品当前为 FV680 (product-post 类型)，用 Elementor 编辑
 * - 克隆会复制 meta_data（含 _elementor_data、_wp_page_template 等），保证模板和 Elementor 结构完整
 * - 只替换标题 heading（widget id 2bcccbd8 / 25983c80）和卡片容器（8d5edc3）内的 5 张卡片
 * - 新产品状态为 draft（草稿），等待人工审核后再发布
 */
const https = require('https');

// 站点配置（支持 zh/en 双站点，通过 --site 选择，默认 zh）
const args = process.argv.slice(2);
const siteArg = args.find(a => a.startsWith('--site='));
const SITE = siteArg ? siteArg.split('=')[1] : 'zh';
const CONFIG = require('./config.json')[SITE];

const A = Buffer.from(`${CONFIG.username}:${CONFIG.appPassword}`).toString('base64');
const H = CONFIG.wpUrl.replace(/^https?:\/\//, '');

// 图标基准路径
const ICON_URL = CONFIG.iconUrl;

// 模板产品里这些 meta 不需要复制（会自动重新生成）
const SKIP_META = ['_elementor_css', '_elementor_element_cache', '_elementor_controls_usage', '_elementor_page_assets'];

function req(path, data, method) {
  return new Promise(r => {
    const body = data ? JSON.stringify(data) : null;
    const opts = {hostname: H, path, method: method || (body ? 'POST' : 'GET'), headers: {'Authorization': `Basic ${A}`}};
    if (body) opts.headers['Content-Type'] = 'application/json';
    const req = https.request(opts, res => { let d=''; res.on('data',c=>d+=c); res.on('end',()=>{ if(res.statusCode>=400) console.error(`[API ${res.statusCode}] ${method||'GET'} ${path}: ${d.slice(0,200)}`); try{r(JSON.parse(d))}catch(e){r(d)} }); });
    req.on('error', e => { console.error(`[API ERROR] ${e.message} (${method||'GET'} ${path})`); r(null); });
    if (body) req.write(body);
    req.end();
  });
}

function findContainer(elements, id) {
  for (const el of elements || []) {
    if (el.id === id) return el;
    if (el.elements) { const r = findContainer(el.elements, id); if (r) return r; }
  }
  return null;
}
function findByWidgetId(elements, id) {
  for (const el of elements || []) {
    if (el.id === id) return el;
    if (el.elements) { const r = findByWidgetId(el.elements, id); if (r) return r; }
  }
  return null;
}

async function main() {
  const tmplArg = args.find(a => a.startsWith('--template='));
  const cfgArg = args.find(a => a.startsWith('--config='));
  if (!cfgArg) {
    console.log('用法: node clone_highlights.js --site=zh|en [--template=<模板ID>] --config=<JSON文件>');
    process.exit(1);
  }
  // 模板 ID 默认用 config.json 里对应站点的 templateProductId
  const TEMPLATE_ID = tmplArg ? parseInt(tmplArg.split('=')[1]) : CONFIG.templateProductId;
  // 兼容绝对路径和相对路径
  const path = require('path');
  const cfgPath = cfgArg.split('=')[1];
  const resolvedCfg = path.isAbsolute(cfgPath) ? cfgPath : path.resolve(cfgPath);
  const productConfig = require(resolvedCfg);

  console.log('=== 克隆产品: ' + productConfig.name + ' ===');

  // 1. 读取模板产品
  const tmpl = await req('/wp-json/wc/v3/products/' + TEMPLATE_ID);
  if (!tmpl) { console.log('模板产品不存在'); process.exit(1); }
  const baseMeta = (tmpl.meta_data || []).filter(m => !SKIP_META.includes(m.key));

  // 2. 克隆
  const clone = {
    name: productConfig.name,
    type: tmpl.type,
    status: 'draft', // 强制草稿，需人工审核
    description: tmpl.description,
    short_description: productConfig.oneLiner,
    categories: tmpl.categories,
    images: tmpl.images.map(img => ({id: img.id})),
    attributes: tmpl.attributes || [],
    meta_data: baseMeta,
  };
  const created = await req('/wp-json/wc/v3/products', clone, 'POST');
  const newId = created.id;
  console.log('  新ID: ' + newId + ' (草稿)');

  // 3. 替换闪光点
  const newProd = await req('/wp-json/wc/v3/products/' + newId);
  const edMeta = (newProd.meta_data || []).find(m => m.key === '_elementor_data');
  const d = JSON.parse(edMeta.value);

  // 3.1 标题（widget id 2bcccbd8 = 产品名，25983c80 = 一句话卖点，6e44a6f4 = 产品分类/场景标题）
  function replaceHeadings(elements) {
    for (const el of elements || []) {
      if (el.widgetType === 'heading') {
        if (el.id === '2bcccbd8') el.settings.title = productConfig.title;
        else if (el.id === '25983c80') el.settings.title = productConfig.oneLiner;
        else if (el.id === '6e44a6f4' && productConfig.sectionTitle) el.settings.title = productConfig.sectionTitle;
      }
      if (el.elements) replaceHeadings(el.elements);
    }
  }
  replaceHeadings(d);

  // 3.2 预先构建图标 ID 映射（查目标站点媒体库，避免 ID 错位）
  const iconIdMap = {};
  async function buildIconIdMap(cards) {
    const uniqueIcons = [...new Set(cards.map(c => c.icon).filter(Boolean))];
    for (const iconName of uniqueIcons) {
      const searchName = iconName.replace(/\.svg$/i, '');
      const data = await req('/wp-json/wp/v2/media?search=' + encodeURIComponent(searchName) + '&per_page=50');
      if (data && Array.isArray(data)) {
        for (const item of data) {
          const src = item.source_url || '';
          if (src.endsWith('/' + iconName)) {
            iconIdMap[iconName] = item.id;
            break;
          }
        }
      }
    }
  }

  // 3.3 特性卡片（容器 8d5edc3 内，按 item 顺序）
  const cardsContainer = findContainer(d, '8d5edc3');
  if (cardsContainer) {
    const items = [];
    function collectItems(elements) {
      for (const el of elements || []) {
        if (el.elType === 'container' && el.id.startsWith('aed190d_item_')) items.push(el);
        if (el.elements) collectItems(el.elements);
      }
    }
    collectItems(cardsContainer.elements);
    const count = Math.min(items.length, productConfig.cards.length);
    // 查目标站点的图标真实 ID
    await buildIconIdMap(productConfig.cards.slice(0, count));
    for (let i = 0; i < count; i++) {
      const item = items[i];
      const card = productConfig.cards[i];
      const img = findByWidgetId(item.elements, 'c29d2c2');
      if (img) {
        img.settings.image.url = ICON_URL + card.icon;
        // 用目标站点的真实 ID（避免克隆自其他站点时 ID 指向别的图片）
        if (card.icon && iconIdMap[card.icon]) {
          img.settings.image.id = iconIdMap[card.icon];
        }
      }
      const titleW = findByWidgetId(item.elements, '9c03f4c');
      if (titleW) titleW.settings.editor = '<p>' + card.title + '</p>';
      const descW = findByWidgetId(item.elements, 'e3ba02a');
      if (descW) descW.settings.editor = '<p>' + card.desc + '</p>';
    }
    console.log('  特性卡片已替换: ' + count + ' 张');
  }

  // 4. 写回 meta_data（必须用 PUT 更新现有产品，POST 会静默失败）
  const newMeta = (newProd.meta_data || []).map(m => m.key === '_elementor_data' ? {...m, value: JSON.stringify(d)} : m);
  await req('/wp-json/wc/v3/products/' + newId, {meta_data: newMeta}, 'PUT');

  console.log('  完成! 后台编辑: ' + CONFIG.wpUrl + '/wp-admin/post.php?post=' + newId + '&action=elementor');
}

main().catch(e => console.error(e));
