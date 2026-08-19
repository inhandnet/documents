#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将提取的规格 JSON 上传到 WooCommerce 产品。
用法：
    python upload_specs.py <product-id> <json-file>
    示例：python upload_specs.py 6642 "output/batch/VT310_Vehicle_Telematics_Specifications_V1.4_next.json"

需要先配置以下环境变量：
    export WP_URL="https://www.inhand.com/"
    export WP_USER="admin"
    export WP_APP_PASSWORD="ldZJ 0D72 uuAK vgoH Atll LclY"
"""

import os
import sys
import json
import base64
from pathlib import Path


def get_creds():
    wp_url = os.environ.get('WP_URL')
    username = os.environ.get('WP_USER')
    app_password = os.environ.get('WP_APP_PASSWORD')
    site = os.environ.get('WP_SITE', 'en')  # 通过 WP_SITE 选择站点（en/zh）

    # 也尝试读取配置文件：优先当前目录 config.json，再回退 ~/.wordpress/config.json
    if not (wp_url and username and app_password):
        config_candidates = [
            Path(__file__).resolve().parent / 'config.json',
            Path.home() / '.wordpress' / 'config.json',
        ]
        for config_path in config_candidates:
            if config_path.exists():
                data = json.loads(config_path.read_text(encoding='utf-8'))
                # 支持多站点结构 {"en": {...}, "zh": {...}}
                if site in data and isinstance(data[site], dict):
                    data = data[site]
                wp_url = wp_url or data.get('wpUrl')
                username = username or data.get('username')
                app_password = app_password or data.get('appPassword')
            if wp_url and username and app_password:
                break

    if not (wp_url and username and app_password):
        print("错误：缺少 WordPress API 认证信息")
        print("请设置环境变量 WP_URL, WP_USER, WP_APP_PASSWORD")
        print("或配置文件（当前目录 config.json 或 ~/.wordpress/config.json）")
        sys.exit(1)

    return wp_url.rstrip('/'), username, app_password


def basic_auth(username, password):
    return "Basic " + base64.b64encode(f"{username}:{password}".encode()).decode()


import requests

session = requests.Session()
session.trust_env = False  # 禁用环境变量代理


def api_get(url, headers):
    r = session.get(url, headers=headers)
    r.raise_for_status()
    return r.json()


def api_put(url, headers, data):
    r = session.put(url, headers=headers, json=data)
    r.raise_for_status()
    return r.json()


def api_post(url, headers, data):
    r = session.post(url, headers=headers, json=data)
    if r.status_code == 400:
        err = r.json()
        if err.get('code') == 'term_exists':
            return {'id': err.get('data', {}).get('resource_id')}
    r.raise_for_status()
    return r.json()


def get_or_create_attribute(wp_url, auth_header, slug, name):
    """获取或创建全局产品属性，返回属性 ID"""
    clean_slug = slug.replace('pa_', '')
    target_slug = f'pa_{clean_slug}'

    headers = {'Authorization': auth_header, 'Content-Type': 'application/json'}

    # 获取所有属性
    url = f"{wp_url}/wp-json/wc/v3/products/attributes?per_page=500"
    attrs = api_get(url, headers)

    for attr in attrs:
        if attr['slug'] == target_slug or attr['slug'] == clean_slug:
            return attr['id']

    # 创建属性
    create_url = f"{wp_url}/wp-json/wc/v3/products/attributes"
    resp = api_post(create_url, headers, {
        'name': name,
        'slug': clean_slug,
        'type': 'select',
        'order_by': 'menu_order',
        'has_archives': False,
    })
    print(f'  创建属性 "{name}" (id={resp["id"]})')
    return resp['id']


def get_or_create_term(wp_url, auth_header, attr_id, term_name):
    """获取或创建属性值(term)，返回 term ID"""
    headers = {'Authorization': auth_header, 'Content-Type': 'application/json'}

    # 分页获取所有 terms
    all_terms = []
    page = 1
    while True:
        url = f"{wp_url}/wp-json/wc/v3/products/attributes/{attr_id}/terms?per_page=100&page={page}"
        terms = api_get(url, headers)
        if not terms:
            break
        all_terms.extend(terms)
        page += 1

    for term in all_terms:
        if term['name'] == term_name:
            return term['id']

    # 创建 term
    create_url = f"{wp_url}/wp-json/wc/v3/products/attributes/{attr_id}/terms"
    try:
        resp = api_post(create_url, headers, {'name': term_name})
        print(f'    创建值 "{term_name}" (id={resp["id"]})')
        return resp['id']
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 400:
            err = e.response.json()
            if err.get('code') == 'term_exists':
                tid = err.get('data', {}).get('resource_id')
                print(f'    值 "{term_name}" 已存在 (id={tid})')
                return tid
        raise


def update_product_attributes(wp_url, username, app_password, product_id, attributes):
    auth_header = basic_auth(username, app_password)
    headers = {'Authorization': auth_header, 'Content-Type': 'application/json'}

    # 1. 获取现有产品
    product_url = f"{wp_url}/wp-json/wc/v3/products/{product_id}"
    product = api_get(product_url, headers)

    existing_meta = product.get('meta_data', [])
    stale_meta = [m for m in existing_meta if str(m.get('key', '')).startswith('_attr_desc_')]
    keep_meta = [m for m in existing_meta if not str(m.get('key', '')).startswith('_attr_desc_')]
    print(f'  发现 {len(stale_meta)} 个旧的 _attr_desc_ 条目需要清理')

    new_attr_desc_meta = []

    # 2. 处理每个属性
    for attr in attributes:
        option_values = attr.get('optionValues', {})
        if not option_values:
            continue

        attr_id = get_or_create_attribute(wp_url, auth_header, attr['slug'], attr['name'])
        attr['id'] = attr_id

        for option_name, value in option_values.items():
            term_id = get_or_create_term(wp_url, auth_header, attr_id, option_name)
            meta_key = f"_attr_desc_pa_{attr['slug']}_{term_id}"
            new_attr_desc_meta.append({'key': meta_key, 'value': value})

    # 3. 更新 meta_data
    meta_body = {
        'meta_data': (
            [{'id': m['id']} for m in stale_meta if m.get('id')] +
            [{'id': m.get('id'), 'key': m['key'], 'value': m['value']} for m in keep_meta] +
            new_attr_desc_meta
        )
    }

    meta_result = api_put(product_url, headers, meta_body)
    attr_desc_after = [m for m in meta_result.get('meta_data', []) if str(m.get('key', '')).startswith('_attr_desc_')]
    print(f'  Meta 更新: 删除 {len(stale_meta)} 个, 新建 {len(new_attr_desc_meta)} 个, 现有 {len(attr_desc_after)} 个 _attr_desc_')

    # 4. 更新 attributes
    attr_body = {
        'attributes': [
            {
                'id': attr['id'],
                'name': attr['name'],
                'slug': attr['slug'],
                'position': attr.get('position', 0),
                'visible': attr.get('visible', True),
                'variation': attr.get('variation', False),
                'options': attr['options'],
            }
            for attr in attributes if 'id' in attr
        ]
    }

    attr_result = api_put(product_url, headers, attr_body)
    print(f'  产品规格更新成功')
    print(f'    名称: {attr_result.get("name", "N/A")}')
    print(f'    属性数量: {len(attr_result.get("attributes", []))}')


def main():
    if len(sys.argv) != 3:
        print(f"用法: python {sys.argv[0]} <product-id> <json-file>")
        sys.exit(1)

    product_id = sys.argv[1]
    json_file = sys.argv[2]

    if not os.path.exists(json_file):
        print(f'文件不存在: {json_file}')
        sys.exit(1)

    with open(json_file, 'r', encoding='utf-8') as f:
        attributes = json.load(f)

    print(f'读取到 {len(attributes)} 条规格')

    wp_url, username, app_password = get_creds()
    print(f'连接到: {wp_url}')
    print(f'产品 ID: {product_id}')
    print('开始上传...')

    update_product_attributes(wp_url, username, app_password, product_id, attributes)
    print('完成！')


if __name__ == '__main__':
    main()
