<div align="center">

# 赛博骨灰盒 & 电子纪念堂 skill

> *“这里安放的不是尸骨，而是被记住的语气、故事与回忆。”*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

<br>

一个带点 **数字永生** 玩梗、但核心仍然克制而庄重的 AI Skill。<br>
它把逝者留下来的聊天记录、照片、手写文字、日记、亲友回忆，整理成一个<br>
**可保存、可追思、可对话的数字纪念体**。<br>

我们把它叫做：

## **赛博骨灰盒 & 电子纪念堂**

你可以把它理解成：

- 数字纪念馆
- AI 墓志铭生成器
- 电子纪念堂
- 轻度玩梗版「数字永生」

但它不是复活谁，也不会假装逝者真的回来。<br>
它只是尽可能根据材料，把那个人曾经的：**语气、习惯、故事、人生片段**，保存得更久一点。

[功能](#功能) · [安装](#安装) · [使用方式](#使用方式) · [项目结构](#项目结构) · [致谢](#致谢)

</div>

---

## 功能

### 1. 纪念体构建
输入逝者的基础信息与原始材料后，系统会生成一个完整的纪念档案，包括：

- **Memorial Memory**：生平轨迹、家庭关系、重要事件、性格标签
- **Voice Persona**：说话风格、常用表达、情绪气质、互动方式
- **Epitaph**：一句话墓志铭、碑文版、家属纪念版
- **Timeline**：人生时间线
- **Eulogy**：悼词、追思短文、朋友圈纪念文案

### 2. 数字祠堂系统
支持把多个纪念体整理进同一个 **电子纪念堂 / Digital Shrine**：

- 统一保存逝者名录
- 生成祠堂索引页
- 快速进入某位逝者的纪念对话
- 适合家庭纪念馆、家谱扩展、长期数字保存

### 3. 墓碑终端显示
Skill 启动时会显示一个 terminal 风格的小型墓碑：

```text
              _________
             /         \
            /  R.I.P.   \
           /-------------\
           | 赛博骨灰盒  |
           | 电子纪念堂  |
           | Cyber Shrine|
           |             |
           | 保存记忆    |
           | 生成墓志铭  |
           | 与故人对话  |
           |_____________|
```

### 4. 纪念对话
可用 `/{slug}` 进入纪念对话模式。AI 会：

- 尽量遵循逝者已有材料中的语气与表达习惯
- 尽量保持性格边界，不乱编重大立场
- 明确这是“纪念性对话”，不是“通灵式复活”

### 5. 墓志铭与悼词
支持额外生成：

- 一句话墓志铭
- 碑文版墓志铭
- 家属纪念版
- 追悼会悼词
- 朋友圈/社交平台纪念文案
- 家庭纪念册中的人物简介

---

## 安装

### Claude Code

> **Important**: Claude Code looks for skills in `.claude/skills/` from the **git repo root**. Run these commands in the correct location.

```bash
# Install in current project
mkdir -p .claude/skills
git clone https://github.com/YOUR_USERNAME/cyber-memorial-hall-skill .claude/skills/create-cyber-shrine

# Or install globally (available in all projects)
git clone https://github.com/YOUR_USERNAME/cyber-memorial-hall-skill ~/.claude/skills/create-cyber-shrine
```

### Dependencies (Optional)

```bash
pip install -r requirements.txt
```

---

## 使用方式

在 Claude Code 里输入：

```text
/create-cyber-shrine
```

系统会引导你：

1. 输入逝者基础信息
2. 选择或粘贴原始材料
3. 生成纪念档案与墓志铭
4. 写入电子纪念堂索引

之后可以用：

```text
/{slug}
```

进入该逝者的纪念对话模式。

### 管理命令

| 命令 | 说明 |
|------|------|
| `/create-cyber-shrine` | 创建新的赛博骨灰盒 / 纪念体 |
| `/digital-shrine` | 查看电子纪念堂索引 |
| `/digital-shrine-list` | 列出所有纪念体 |
| `/{slug}` | 与某位纪念体对话 |
| `/{slug}-memory` | 查看生平与纪念记忆 |
| `/{slug}-persona` | 查看说话风格与人格摘要 |
| `/{slug}-epitaph` | 生成或重写墓志铭 |
| `/{slug}-eulogy` | 生成悼词 |
| `/cyber-shrine-rollback {slug} {version}` | 回滚到某个版本 |
| `/delete-memorial {slug}` | 删除某个纪念体 |

---

## 原材料来源

| 来源 | 格式 | 说明 |
|------|------|------|
| WeChat history | WeChatMsg / LiuHen / PyWxDump export | 提取逝者常用表达与高频互动 |
| QQ history | txt / mht export | 适合更早期的表达风格 |
| 日记 / 文章 / 手写整理稿 | txt / md / pdf | 提取价值观、心态与叙事方式 |
| 社交媒体截图 | Screenshot / Markdown / TXT | 提取公开表达与兴趣偏好 |
| 照片 | JPEG / PNG (with EXIF if possible) | 辅助人生时间线与地点判断 |
| 亲友口述 / 回忆 | Plain text | 补全“别人如何记得他/她” |
| 讣告 / 生平简介 | Plain text / document | 适合补充正式、生平框架化信息 |

---

## 运行逻辑

Runtime logic:

```text
Receive message
→ Voice Persona decides how this person would likely respond
→ Memorial Memory provides life context and relationships
→ Epitaph / Shrine constraints keep tone respectful and bounded
→ Output as a memorial conversation, not a fake resurrection
```

---

## 项目结构

```text
create-cyber-shrine/
├── SKILL.md                       # 主入口 Skill
├── prompts/
│   ├── intake.md                  # 逝者资料录入引导
│   ├── self_analyzer.md           # Memorial Memory 提取
│   ├── persona_analyzer.md        # Voice Persona 提取
│   ├── self_builder.md            # memorial.md 模板
│   ├── persona_builder.md         # persona.md 模板
│   ├── epitaph_builder.md         # 墓志铭生成模板
│   ├── eulogy_builder.md          # 悼词生成模板
│   ├── timeline_builder.md        # 人生时间线模板
│   ├── shrine_builder.md          # 电子纪念堂索引模板
│   ├── merger.md                  # 增量合并逻辑
│   └── correction_handler.md      # “这不像他/她会说的话”纠正逻辑
├── tools/
│   ├── wechat_parser.py           # 微信解析
│   ├── qq_parser.py               # QQ 解析
│   ├── social_parser.py           # 社交媒体解析
│   ├── photo_analyzer.py          # 照片与时间线辅助分析
│   ├── skill_writer.py            # 纪念体文件写入与 SKILL 合并
│   ├── version_manager.py         # 版本存档与回滚
│   └── shrine_manager.py          # 电子纪念堂索引维护
├── memorials/example_elder/       # 示例纪念体
├── docs/PRD.md
├── requirements.txt
└── LICENSE
```

---

## 免责声明

- 本项目不宣称“复活”逝者
- 不应伪造逝者未表达过的重要观点
- 不应用于伪造遗嘱、法律意见、财务承诺等高风险场景
- 输出内容受原始材料质量影响很大
- 当材料不足时，系统应明确说“不确定”或“资料不足”

它的定位是：

> **以 AI 的方式保存纪念，而不是以幻觉的方式替代真实。**

---

## 致谢

本项目的架构灵感，延续并致敬如下项目：

- **前任.skill**
- **同事.skill**
- **yourself skill**

同时也致谢：

- **GPT-5.4** —— 负责结构设计、文案整理、Prompt 重写与项目重构思路
- **Claude Code** —— Skill 运行环境与交互入口
- **VS Code** —— 日常改造、调试、整理工程的主要编辑器

也感谢所有把“AI 纪念、数字记忆、人格归档”做成开源实验的人。

有些项目在认真做工具，
有些项目在认真做纪念，
而这个项目希望两者都沾一点。
