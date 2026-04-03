#!/usr/bin/env python3
"""数字祠堂索引管理器"""

import argparse
import json
import os
from datetime import datetime


def load_shrine(path: str):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"hall_name": "电子纪念堂", "entries": []}


def save_shrine(path: str, data: dict):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def add_entry(shrine_path: str, name: str, slug: str, relationship: str = '', birth_year: str = '', death_year: str = '', epitaph: str = ''):
    data = load_shrine(shrine_path)
    entries = [e for e in data['entries'] if e.get('slug') != slug]
    entries.append({
        'name': name,
        'slug': slug,
        'relationship': relationship,
        'birth_year': birth_year,
        'death_year': death_year,
        'one_line_epitaph': epitaph,
        'created_at': datetime.now().isoformat(),
    })
    data['entries'] = sorted(entries, key=lambda x: x.get('created_at', ''), reverse=True)
    save_shrine(shrine_path, data)
    print(f'已写入数字祠堂：/{slug} ({name})')


def list_entries(shrine_path: str):
    data = load_shrine(shrine_path)
    print(data.get('hall_name', '电子纪念堂'))
    for e in data.get('entries', []):
        years = f"{e.get('birth_year','')} — {e.get('death_year','')}".strip()
        print(f"- /{e.get('slug')} | {e.get('name')} | {e.get('relationship','')} | {years} | {e.get('one_line_epitaph','')}")


def main():
    parser = argparse.ArgumentParser(description='数字祠堂索引管理器')
    parser.add_argument('--action', required=True, choices=['add', 'list'])
    parser.add_argument('--shrine', default='./shrine.json')
    parser.add_argument('--name')
    parser.add_argument('--slug')
    parser.add_argument('--relationship', default='')
    parser.add_argument('--birth-year', default='')
    parser.add_argument('--death-year', default='')
    parser.add_argument('--epitaph', default='')
    args = parser.parse_args()
    if args.action == 'add':
        add_entry(args.shrine, args.name, args.slug, args.relationship, args.birth_year, args.death_year, args.epitaph)
    else:
        list_entries(args.shrine)


if __name__ == '__main__':
    main()
