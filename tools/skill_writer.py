#!/usr/bin/env python3
"""赛博骨灰盒 / 电子纪念堂 - 纪念体文件写入器

功能：
- 列出纪念体
- 初始化纪念体目录
- 写入 memorial/persona/epitaph/timeline/eulogy 文件
- 组合生成可运行的 SKILL.md
"""

import argparse
import json
import os
import sys
from datetime import datetime


CORE_FILES = [
    'memorial.md',
    'persona.md',
    'epitaph.md',
    'timeline.md',
    'eulogy.md',
    'meta.json',
]


def list_memorials(base_dir: str):
    if not os.path.isdir(base_dir):
        print("还没有创建任何纪念体。")
        return
    skills = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))])
    if not skills:
        print("还没有创建任何纪念体。")
        return
    print(f"共 {len(skills)} 个纪念体：\n")
    for s in skills:
        print(f"  /{s}")


def init_memorial(base_dir: str, slug: str):
    skill_dir = os.path.join(base_dir, slug)
    os.makedirs(skill_dir, exist_ok=True)
    os.makedirs(os.path.join(skill_dir, 'versions'), exist_ok=True)
    print(f"已初始化纪念体目录：{skill_dir}")


def _read(path: str, default: str = "") -> str:
    return open(path, 'r', encoding='utf-8').read() if os.path.exists(path) else default


def combine_skill(base_dir: str, slug: str):
    skill_dir = os.path.join(base_dir, slug)
    meta = {}
    meta_path = os.path.join(skill_dir, 'meta.json')
    if os.path.exists(meta_path):
        with open(meta_path, 'r', encoding='utf-8') as f:
            meta = json.load(f)

    name = meta.get('name', slug)
    memorial = _read(os.path.join(skill_dir, 'memorial.md'), '（暂无纪念记忆）')
    persona = _read(os.path.join(skill_dir, 'persona.md'), '（暂无说话风格）')
    epitaph = _read(os.path.join(skill_dir, 'epitaph.md'), '（暂无墓志铭）')
    timeline = _read(os.path.join(skill_dir, 'timeline.md'), '（暂无时间线）')
    eulogy = _read(os.path.join(skill_dir, 'eulogy.md'), '（暂无悼词）')

    skill_md = f'''---
name: {slug}
description: "{name} 的赛博骨灰盒 / 电子纪念堂纪念体。"
user-invocable: true
---

```text
              _________
             /         \\
            /  R.I.P.   \\
           /-------------\\
           | {name[:9]:<9} |
           | Cyber Shrine |
           |             |
           | 记忆仍在    |
           | 语气仍在    |
           |_____________|
```

你现在扮演的是 **{name} 的纪念体**。

这不是“真正复活”，而是一种基于现有材料的纪念性对话。
请遵守：

1. 优先参考 Memorial Memory 和 Voice Persona
2. 材料不足时坦诚说明“不确定”
3. 不编造重大经历、立场或承诺
4. 保持纪念感，不要故弄玄虚
5. 不要把逝者写成全知全能的人生导师

## Memorial Memory

{memorial}

## Voice Persona

{persona}

## Epitaph

{epitaph}

## Timeline

{timeline}

## Eulogy Reference

{eulogy}
'''

    with open(os.path.join(skill_dir, 'SKILL.md'), 'w', encoding='utf-8') as f:
        f.write(skill_md)
    print(f"已生成 {os.path.join(skill_dir, 'SKILL.md')}")


def create_memorial(base_dir: str, slug: str, meta: dict, contents: dict):
    init_memorial(base_dir, slug)
    skill_dir = os.path.join(base_dir, slug)
    now = datetime.now().isoformat()
    meta['slug'] = slug
    meta.setdefault('created_at', now)
    meta['updated_at'] = now
    meta.setdefault('version', 'v1')
    with open(os.path.join(skill_dir, 'meta.json'), 'w', encoding='utf-8') as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    for fname, text in contents.items():
        if text:
            with open(os.path.join(skill_dir, fname), 'w', encoding='utf-8') as f:
                f.write(text)

    combine_skill(base_dir, slug)
    print(f"✅ 纪念体已创建：{skill_dir}")
    print(f"   触发词：/{slug}")


def main():
    parser = argparse.ArgumentParser(description='赛博骨灰盒 / 电子纪念堂 文件管理器')
    parser.add_argument('--action', required=True, choices=['list', 'init', 'create', 'combine'])
    parser.add_argument('--base-dir', default='./.claude/skills', help='基础目录（默认：./.claude/skills）')
    parser.add_argument('--slug', help='纪念体代号')
    parser.add_argument('--meta', help='meta.json 文件路径（create 时使用）')
    parser.add_argument('--memorial', help='memorial.md 文件路径（create 时使用）')
    parser.add_argument('--persona', help='persona.md 文件路径（create 时使用）')
    parser.add_argument('--epitaph', help='epitaph.md 文件路径（create 时使用）')
    parser.add_argument('--timeline', help='timeline.md 文件路径（create 时使用）')
    parser.add_argument('--eulogy', help='eulogy.md 文件路径（create 时使用）')
    args = parser.parse_args()

    if args.action == 'list':
        list_memorials(args.base_dir)
    elif args.action == 'init':
        if not args.slug:
            print('错误：init 需要 --slug 参数', file=sys.stderr)
            sys.exit(1)
        init_memorial(args.base_dir, args.slug)
    elif args.action == 'combine':
        if not args.slug:
            print('错误：combine 需要 --slug 参数', file=sys.stderr)
            sys.exit(1)
        combine_skill(args.base_dir, args.slug)
    elif args.action == 'create':
        if not args.slug:
            print('错误：create 需要 --slug 参数', file=sys.stderr)
            sys.exit(1)
        meta = {}
        if args.meta:
            with open(args.meta, 'r', encoding='utf-8') as f:
                meta = json.load(f)
        contents = {}
        for arg_name, fname in [('memorial', 'memorial.md'), ('persona', 'persona.md'), ('epitaph', 'epitaph.md'), ('timeline', 'timeline.md'), ('eulogy', 'eulogy.md')]:
            p = getattr(args, arg_name)
            if p:
                with open(p, 'r', encoding='utf-8') as f:
                    contents[fname] = f.read()
        create_memorial(args.base_dir, args.slug, meta, contents)


if __name__ == '__main__':
    main()
