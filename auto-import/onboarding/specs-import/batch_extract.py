#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量从 Markdown 规格书中提取规格属性，输出为 JSON。

用法：
    python batch_extract.py                          # 默认扫描 en-old/ 下的 *_next.md
    python batch_extract.py 待导入/第三批-520        # 扫描指定目录下的所有 *.md

改进点：
1. 支持 Group + Leaf 两层结构（表格内分类标题行作为 Group）
2. 默认按列位置解析（第 0 列=name，第 1 列=value）
3. 自动跳过订货信息表、PIN 定义表等无效表格
4. 清理 HTML 标签和 markdown 加粗标记
5. 支持命令行指定任意输入目录
"""

import re
import json
from pathlib import Path

# 路径配置
BASE_DIR = Path(__file__).parent
EN_OLD_DIR = BASE_DIR / "en-old"
OUTPUT_DIR = BASE_DIR / "output" / "batch"


def clean_text(text: str) -> str:
    """清理单元格中的 HTML 标签、markdown 加粗等"""
    # 先把 <br> 类标签换成换行
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<[^>]+>', '', text)
    text = text.replace('**', '').replace('*', '')
    text = text.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"')
    text = text.replace('&#x003C;', '<').replace('&#x003E;', '>')
    return text.strip()


def is_valid_separator_line(line: str) -> bool:
    """检查是否是 Markdown 表格的分隔行"""
    cells = [c.strip() for c in line.split('|') if c.strip() != '']
    if not cells:
        return False
    return all(re.match(r'^[-:]+$', c.replace(' ', '')) for c in cells)


def parse_markdown_table(lines: list, start_idx: int) -> tuple:
    """
    从指定位置开始解析一个 Markdown 表格。
    返回 (table_dict, header_idx, end_idx)
    """
    i = start_idx
    header_line = None
    header_idx = start_idx
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped.startswith('|'):
            header_line = stripped
            header_idx = i
            break
        i += 1

    if header_line is None:
        return None, start_idx, start_idx + 1

    headers = [clean_text(c) for c in header_line.split('|') if c.strip() != '']
    if len(headers) < 2:
        return None, header_idx, i + 1

    i += 1
    if i >= len(lines) or not lines[i].strip().startswith('|'):
        return None, header_idx, i + 1

    sep_line = lines[i].strip()
    if not is_valid_separator_line(sep_line):
        return None, header_idx, i + 1

    sep_cells = [c.strip() for c in sep_line.split('|') if c.strip() != '']
    if len(sep_cells) != len(headers):
        return None, header_idx, i + 1

    i += 1

    rows = []
    while i < len(lines):
        stripped = lines[i].strip()
        if not stripped.startswith('|'):
            break
        cells = [clean_text(c) for c in stripped.split('|') if c.strip() != '']
        if len(cells) >= 1:
            rows.append(cells)
        i += 1

    if not rows:
        return None, header_idx, i

    return {'headers': headers, 'rows': rows}, header_idx, i


def extract_table_title(lines: list, table_start_idx: int) -> str:
    """从表格上方的行中提取最近的 Markdown 标题作为表格标题"""
    for i in range(table_start_idx - 1, -1, -1):
        line = lines[i].strip()
        if not line:
            continue
        # 跳过表格分隔行，它属于当前表格但不代表新表格
        if is_valid_separator_line(line):
            continue
        match = re.match(r'^#{1,3}\s+(.+)$', line)
        if match:
            title = match.group(1)
            title = re.sub(r'<[^>]+>', '', title)
            title = title.replace('**', '').strip()
            # 去掉前导的数字编号，如 "3. Hardware Specifications" / "4.1 5G/4G Cellular Network"
            title = re.sub(r'^\d+(\.\d+)*[.\s]*', '', title)
            if title:
                return title
        if line.startswith('|'):
            break
    return None


# 常见规格参数关键词（中英文）
SPEC_KEYWORDS = {
    'cpu', 'ram', 'flash', 'memory', 'storage', 'dimension', 'dimensions',
    'weight', 'power', 'voltage', 'current', 'temperature', 'humidity',
    'protection', 'ethernet', 'wifi', 'wireless', 'bluetooth', 'gnss',
    'cellular', 'network', 'interface', 'port', 'antenna', 'sim', 'usb',
    'serial', 'can', 'io', 'certification', 'warranty', 'operating',
    'input', 'output', 'frequency', 'bandwidth', 'protocol', 'throughput',
    'speed', 'display', 'resolution', 'touch', 'led', 'button', 'mounting',
    'housing', 'cooling', 'connector', 'model', 'type', 'standard', 'size',
    'length', 'width', 'height', 'depth', 'gnss', 'gps', 'positioning',
    'battery', 'charging', 'material', 'format', 'codec', 'audio', 'video',
    'camera', 'sensor', 'processor', 'gpu', 'npu', 'os', 'platform',
    'management', 'cloud', 'vpn', 'firewall', 'routing', 'switching',
    'forwarding', 'duplex', 'polarity', 'poe', 'reset', 'ground',
    'standby', 'peak', 'consumption', 'supply', 'range', 'accuracy',
    'sensitivity', 'update', 'tracking', 'dead', 'reckoning', 'adr',
    'mimo', 'encryption', 'security', 'access', 'control', 'mode',
    'sdk', 'api', 'ide', 'docker', 'python', 'programmable', 'features',
    'dashboard', 'logs', 'events', 'alarms', 'tools', 'diagnostic',
    'link', 'backup', 'redundancy', 'watchdog', 'offline', 'built-in',
    'integration', 'openness', 'standards', 'impact', 'salt', 'mist',
    'esd', 'rfi', 'surge', 'conducted', 'shock', 'vibration', 'fall',
    'ingress', 'emc', 'multi-app', 'analytics', 'adas', 'dms',
    'speaker', 'microphone', 'fingerprint', 'nfc', 'expansion',
    'humidity', 'ip', 'mac', 'address', 'table', 'capacity',
    'supply', 'connector', 'pin', 'definition', 'ignition',
    # 中文规格关键词
    '规格', '参数', '技术指标', '指标', '性能', '特性',
    '尺寸', '重量', '电源', '功率', '电压', '电流', '温度', '湿度',
    '接口', '端口', '网口', '网络', '无线', '蜂窝', '天线', 'sim',
    '认证', '安装', '工作', '存储', '保护', '防护',
    '处理器', '内存', '存储', '硬盘', '系统',
    '功耗', '输入', '输出', '频率', '带宽', '速率',
    '协议', '管理', '安全', '加密', '防火墙', 'vpn',
    'led', '指示灯', '按键', '复位',
    '环境', '机械', '电气', '电磁',
}


def looks_like_spec_name(name: str) -> bool:
    if not name:
        return False
    n_lower = name.lower()
    for kw in SPEC_KEYWORDS:
        if kw in n_lower:
            return True
    if ' ' in name and len(name) >= 4:
        return True
    if name.isupper() and 2 <= len(name) <= 8:
        return True
    if ('-' in name or '/' in name) and len(name) >= 3:
        return True
    return False


def looks_like_model_or_code(name: str) -> bool:
    if not name:
        return False
    if re.match(r'^\d+$', name):
        return True
    if re.match(r'^[A-Z]{2,4}\d{5,7}$', name):
        return True
    if re.match(r'^[A-Z]{2,6}\d{1,4}[A-Z]?(-[A-Z0-9]+)*$', name):
        return True
    return False


def is_spec_table(table: dict) -> bool:
    rows = table['rows']
    if not rows:
        return False

    headers = [h.lower() for h in table['headers']]
    header_text = ' '.join(headers)

    if len(headers) >= 3:
        ordering_signals = ['region', 'area', 'order code', 'part number',
                            'ordering', 'product models', 'model', '型号', '区域']
        # 解决方案组件/部署清单（组件、数量、描述）也不是规格表
        deploy_signals = ['组件', '数量', '部署', 'component', 'quantity', 'deployment',
                          '典型客户', '关键需求', '价值主张', '应用场景', '场景']
        if any(s in header_text for s in ordering_signals + deploy_signals):
            return False

    names = [row[0] for row in rows if row and row[0]]
    if not names:
        return False

    total = len(names)

    digit_count = sum(1 for n in names if re.match(r'^\d+$', n))
    if digit_count / total > 0.4:
        return False

    code_count = sum(1 for n in names if looks_like_model_or_code(n))
    if code_count / total > 0.3:
        return False

    spec_like_count = sum(1 for n in names if looks_like_spec_name(n))
    if spec_like_count / total < 0.2:
        return False

    return True


def is_category_header_row(row: list) -> bool:
    """判断某行是否是分类标题行（第一列有内容，第二列为空，或整行只有一列）"""
    if len(row) == 1:
        # 只有一列且有内容，是典型的分类标题行（如 | **Category** | |）
        return bool(row[0].strip())
    if len(row) < 2:
        return False
    first = row[0].strip()
    second = row[1].strip() if len(row) > 1 else ''
    return bool(first and not second)


def generate_slug(name: str) -> str:
    """生成 slug，WooCommerce 限制最大 28 字符"""
    import hashlib
    slug = name.lower()
    slug = re.sub(r'[^\w\s-]', ' ', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    slug = slug.strip('-')
    # 如果 slug 包含非 ASCII 字符（如中文），用 hash 代替
    if not slug or any(ord(c) > 127 for c in slug):
        h = hashlib.md5(name.encode()).hexdigest()[:12]
        slug = f'spec-{h}'
    if len(slug) > 28:
        slug = slug[:28].rstrip('-')
    return slug


def extract_specs_from_table(table: dict, default_group: str = None) -> list:
    """
    从表格中提取规格属性，支持 Group + Leaf 两层结构。
    - 有内部分类的表格：Group = 分类标题，Leaf = 参数名，Value = 描述
    - 无内部分类的表格：如果提供了 default_group，则 Group = default_group
    """
    rows = table['rows']
    has_category_rows = any(is_category_header_row(row) for row in rows)

    # 按 Group 收集 Leaf 数据
    # group_specs: {group_name: {leaf_name: leaf_value, ...}}
    group_specs = {}
    current_group = default_group

    for row in rows:
        # 先检查分类标题行（可能只有 1 个 cell）
        if is_category_header_row(row):
            current_group = row[0].strip()
            continue

        if len(row) < 2:
            continue

        leaf_name = row[0].strip()
        leaf_value = row[1].strip() if len(row) > 1 else ''

        if not leaf_name or not leaf_value:
            continue

        # 决定使用哪个 group
        if has_category_rows and current_group:
            group_name = current_group
        elif default_group:
            group_name = default_group
        else:
            # 没有 group，每个 leaf 独立成属性（扁平结构）
            group_name = leaf_name

        if group_name not in group_specs:
            group_specs[group_name] = {}

        group_specs[group_name][leaf_name] = leaf_value

    # 转换为 ProductAttribute 格式
    specs = []
    for group_name, leaves in group_specs.items():
        if not leaves:
            continue

        # 如果 group_name == leaf_name 且只有一个 leaf，说明是扁平结构
        # 此时 group_name 本身就是参数名，不需要额外处理
        slug = generate_slug(group_name)
        options = list(leaves.keys())
        option_values = leaves

        specs.append({
            'name': group_name,
            'slug': slug,
            'options': options,
            'optionValues': option_values,
            'visible': True,
            'variation': False,
        })

    return specs


def parse_markdown_tables(content: str) -> list:
    """解析 Markdown 内容中的所有表格，提取规格属性"""
    lines = content.split('\n')
    all_specs = []
    i = 0

    while i < len(lines):
        table, table_start, i = parse_markdown_table(lines, i)
        if table is None:
            i += 1
            continue

        if not is_spec_table(table):
            continue

        # 获取表格标题作为默认 group
        table_title = extract_table_title(lines, table_start)
        if is_marketing_table(table_title) or is_ordering_model_table(table_title):
            continue

        specs = extract_specs_from_table(table, default_group=table_title)
        all_specs.extend(specs)

    # 分配 position
    for idx, spec in enumerate(all_specs):
        spec['position'] = idx

    return all_specs


def parse_html_table(table_html: str):
    """解析一个 HTML <table>，返回与 markdown 表格相同的 {headers, rows} 结构"""
    trs = re.findall(r'<tr[^>]*>([\s\S]*?)</tr>', table_html, flags=re.IGNORECASE)
    if not trs:
        return None

    headers = []
    rows = []
    for tr in trs:
        ths = re.findall(r'<th[^>]*>([\s\S]*?)</th>', tr, flags=re.IGNORECASE)
        tds = re.findall(r'<td[^>]*>([\s\S]*?)</td>', tr, flags=re.IGNORECASE)
        cells = [clean_text(c) for c in (ths if ths else tds)]
        if not cells:
            continue
        if ths and not headers:
            headers = cells
        else:
            rows.append(cells)

    if not rows:
        return None
    if not headers:
        # 无 <th> 的表格，用两列默认头
        headers = ['参数', '规格']

    return {'headers': headers, 'rows': rows}


def find_html_tables(lines: list):
    """找到所有 HTML <table> 块，返回 [(table_html, table_start_idx)]"""
    tables = []
    i = 0
    while i < len(lines):
        if '<table' in lines[i].lower():
            start_idx = i
            buf = [lines[i]]
            i += 1
            while i < len(lines) and '</table>' not in lines[i].lower():
                buf.append(lines[i])
                i += 1
            if i < len(lines):
                buf.append(lines[i])
                i += 1
            tables.append(('\n'.join(buf), start_idx))
        else:
            i += 1
    return tables


def is_marketing_table(table_title: str) -> bool:
    """判断表格是否营销类（功能与优势、应用场景等），这类不是硬件规格，应排除。
    注意：'主要硬件优势'（硬件规格章节下）属于规格，需保留。
    """
    if not table_title:
        return False
    # 中文营销章节：功能与优势
    if '功能与优势' in table_title or ('功能' in table_title and '优势' in table_title):
        return True
    # 中文应用场景
    if '应用场景' in table_title or '场景' in table_title:
        return True
    # 英文营销章节
    t = table_title.lower()
    if 'application scenario' in t or 'scenario' in t:
        return True
    if 'features and advantages' in t or ('feature' in t and 'advantage' in t):
        return True
    return False


def is_ordering_model_table(table_title: str) -> bool:
    """判断表格是否为订购型号表（如 ODU302-NAC4 / IR925-LQA3），应排除。
    型号表标题通常是产品型号代码，如 'ODU302-NAC4 (For North America, LTE CAT4)'。
    """
    if not table_title:
        return False
    # 标题含产品型号代码模式，如 ODU302-NAC4、IR925-LQA3、IG502-LITE-LQA3
    if re.match(r'^[A-Za-z]{1,4}\d{1,4}(-[A-Za-z0-9]+)+', table_title):
        return True
    # 含订购/ordering/model code 关键词
    t = table_title.lower()
    if 'ordering' in t or 'model code' in t or '订购' in table_title or '型号' in table_title:
        return True
    return False


def parse_html_tables(content: str) -> list:
    """解析内容中的 HTML <table>，提取规格属性（markdown 表格解析失败时的降级方案）"""
    lines = content.split('\n')
    all_specs = []
    found_tables = find_html_tables(lines)

    for table_html, table_start in found_tables:
        table = parse_html_table(table_html)
        if table is None:
            continue
        if not is_spec_table(table):
            continue

        table_title = extract_table_title(lines, table_start)
        if is_marketing_table(table_title) or is_ordering_model_table(table_title):
            continue
        specs = extract_specs_from_table(table, default_group=table_title)
        all_specs.extend(specs)

    for idx, spec in enumerate(all_specs):
        spec['position'] = idx

    return all_specs


def parse_tables(content: str) -> list:
    """
    统一入口：先按 markdown `|` 表格解析，若提取不到规格，
    再降级按 HTML <table> 解析（适配两种规格书格式）。
    """
    specs = parse_markdown_tables(content)
    if specs:
        return specs
    return parse_html_tables(content)


def get_all_md_files(directory: Path, pattern: str = '*_next.md') -> list:
    results = []
    for item in directory.rglob(pattern):
        if 'images' in item.parts or '四图' in item.parts or '三图' in item.parts:
            continue
        results.append(item)
    return sorted(results)


def main():
    import sys
    if len(sys.argv) > 1:
        raw_path = sys.argv[1]
        input_dir = Path(raw_path)
        if not input_dir.is_absolute():
            input_dir = BASE_DIR / raw_path
        pattern = '*.md'  # 自定义目录扫描所有 .md
    else:
        input_dir = EN_OLD_DIR
        pattern = '*_next.md'

    if not input_dir.exists():
        print(f"Directory not found: {input_dir}")
        sys.exit(1)

    # 输出目录：默认用 output/batch，自定义目录用 output/<dirname>
    if input_dir == EN_OLD_DIR:
        out_dir = OUTPUT_DIR
    else:
        out_dir = BASE_DIR / "output" / input_dir.name

    out_dir.mkdir(parents=True, exist_ok=True)

    files = get_all_md_files(input_dir, pattern=pattern)
    print(f"Found {len(files)} files in {input_dir}\n")

    total = 0
    for file_path in files:
        content = file_path.read_text(encoding='utf-8')
        attributes = parse_markdown_tables(content)

        rel_path = file_path.relative_to(input_dir)
        base_name = file_path.stem
        output_file = out_dir / f"{base_name}.json"

        output_file.write_text(
            json.dumps(attributes, ensure_ascii=False, indent=2),
            encoding='utf-8'
        )

        count = len(attributes)
        total += count
        print(f"  {rel_path} -> {count} groups")

    print(f"\nDone. {len(files)} files, {total} total groups extracted.")
    print(f"Output: {out_dir}")


if __name__ == '__main__':
    main()
