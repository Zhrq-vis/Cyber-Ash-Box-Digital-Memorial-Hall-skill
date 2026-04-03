#!/usr/bin/env python3
"""赛博骨灰盒 / 电子纪念堂 版本管理器

Usage:
    python3 version_manager.py --action <backup|rollback|list> --slug <slug> --base-dir <path> [--version <v>]
"""

import argparse
import json
import os
import shutil
import sys
from datetime import datetime

FILES_TO_BACKUP = [
    'memorial.md', 'persona.md', 'epitaph.md', 'timeline.md', 'eulogy.md', 'SKILL.md', 'meta.json', 'shrine.json'
]


def backup(base_dir: str, slug: str):
    skill_dir = os.path.join(base_dir, slug)
    versions_dir = os.path.join(skill_dir, 'versions')
    meta_path = os.path.join(skill_dir, 'meta.json')
    if not os.path.exists(meta_path):
        print('错误：meta.json 不存在', file=sys.stderr)
        sys.exit(1)
    with open(meta_path, 'r', encoding='utf-8') as f:
        meta = json.load(f)
    current_version = meta.get('version', 'v0')
    stamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_name = f'{current_version}_{stamp}'
    backup_dir = os.path.join(versions_dir, backup_name)
    os.makedirs(backup_dir, exist_ok=True)
    for fname in FILES_TO_BACKUP:
        src = os.path.join(skill_dir, fname)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(backup_dir, fname))
    print(f'已备份版本 {backup_name} 到 {backup_dir}')
    return backup_name


def rollback(base_dir: str, slug: str, version: str):
    skill_dir = os.path.join(base_dir, slug)
    versions_dir = os.path.join(skill_dir, 'versions')
    target_dir = None
    if not os.path.isdir(versions_dir):
        print('错误：没有历史版本', file=sys.stderr)
        sys.exit(1)
    for vname in os.listdir(versions_dir):
        if vname == version or vname.startswith(version):
            target_dir = os.path.join(versions_dir, vname)
            break
    if not target_dir:
        print(f'错误：找不到版本 {version}', file=sys.stderr)
        list_versions(base_dir, slug)
        sys.exit(1)
    backup(base_dir, slug)
    for fname in FILES_TO_BACKUP:
        src = os.path.join(target_dir, fname)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(skill_dir, fname))
    print(f'已回滚到版本 {version}')


def list_versions(base_dir: str, slug: str):
    versions_dir = os.path.join(base_dir, slug, 'versions')
    if not os.path.isdir(versions_dir):
        print('没有历史版本。')
        return
    versions = sorted(os.listdir(versions_dir), reverse=True)
    if not versions:
        print('没有历史版本。')
        return
    print(f'历史版本（共 {len(versions)} 个）：\n')
    for v in versions:
        print(f'  {v}')


def main():
    parser = argparse.ArgumentParser(description='赛博骨灰盒 / 电子纪念堂 版本管理器')
    parser.add_argument('--action', required=True, choices=['backup', 'rollback', 'list'])
    parser.add_argument('--slug', required=True, help='纪念体代号')
    parser.add_argument('--base-dir', default='./.claude/skills', help='基础目录（默认：./.claude/skills）')
    parser.add_argument('--version', help='回滚目标版本')
    args = parser.parse_args()
    if args.action == 'backup':
        backup(args.base_dir, args.slug)
    elif args.action == 'rollback':
        if not args.version:
            print('错误：rollback 需要 --version 参数', file=sys.stderr)
            sys.exit(1)
        rollback(args.base_dir, args.slug, args.version)
    else:
        list_versions(args.base_dir, args.slug)


if __name__ == '__main__':
    main()
