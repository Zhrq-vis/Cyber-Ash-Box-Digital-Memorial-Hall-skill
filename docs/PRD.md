# 赛博骨灰盒 & 电子纪念堂 skill — PRD

## 产品定位

本项目是一个运行在 Claude Code 上的 meta-skill。
用户提供逝者相关材料后，系统生成一套纪念型数字档案：

- **Memorial Memory**：事实与生平
- **Voice Persona**：表达方式与人物边界
- **Epitaph / Eulogy / Timeline**：纪念内容生成层
- **Digital Shrine**：电子纪念堂索引层

项目调性是：

> **带一点数字永生的玩梗，但本质上认真做纪念。**

它不承诺“复活”，不假装神秘主义，而是把“纪念、整理、保存、对话”做成一套结构化工作流。

## 核心目标

1. 让用户能低门槛地为逝者建立数字纪念体
2. 让纪念档案既可保存，也可对话
3. 让多个纪念体能进入同一个电子纪念堂系统
4. 让输出风格克制，不滑向玄学和滥情

## 两层主体 + 三个生成层

| 层级 | 名称 | 作用 |
|------|------|------|
| Part A | Memorial Memory | 生平、关系、价值观、习惯、关键事件 |
| Part B | Voice Persona | 说话方式、情绪气质、互动风格、边界 |
| Layer C | Epitaph | 墓志铭与碑文 |
| Layer D | Eulogy | 悼词与纪念短文 |
| Layer E | Timeline | 人生时间线 |
| System | Digital Shrine | 电子纪念堂名录与索引 |

## 用户旅程

```text
用户触发 /create-cyber-shrine
  ↓
[Step 1] 录入逝者基础信息
  ↓
[Step 2] 上传聊天、文字、照片、亲友回忆等材料
  ↓
[Step 3] 自动生成 Memorial Memory + Voice Persona
  ↓
[Step 4] 自动生成 Epitaph / Eulogy / Timeline
  ↓
[Step 5] 写入 .claude/skills/{slug}/
  ↓
[Step 6] 同步写入数字祠堂 shrine.json
  ↓
[Step 7] 用户通过 /{slug} 进入纪念对话
```

## 关键设计原则

- 纪念优先，不扮演“通灵”
- 有证据再写，无证据保守处理
- 保留人物棱角，不要抹平成万能温柔 AI
- 输出尽量“像记忆”，不要“像营销文案”
- 支持长期追加材料与版本回滚

## 文件结构

```text
.claude/skills/{slug}/
├── meta.json
├── memorial.md
├── persona.md
├── epitaph.md
├── timeline.md
├── eulogy.md
├── SKILL.md
├── versions/
└── shrine.json (optional, local or shared)
```

## 命令规划

- `/create-cyber-shrine`
- `/digital-shrine`
- `/digital-shrine-list`
- `/{slug}`
- `/{slug}-memory`
- `/{slug}-persona`
- `/{slug}-epitaph`
- `/{slug}-eulogy`
- `/cyber-shrine-rollback {slug} {version}`
- `/delete-memorial {slug}`

## 致谢

本项目在精神谱系上，向以下项目与工具致意：

- 前任.skill
- 同事.skill
- yourself skill
- GPT-5.4
- Claude Code
- VS Code
