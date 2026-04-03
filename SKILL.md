---
name: create-cyber-shrine
version: "2.1.0"
description: "Create a Cyber Ash Box / Digital Memorial Hall profile from chats, writings, photos, and family memories. Generates memorial memory, voice persona, epitaph, timeline, eulogy, and shrine index. | 赛博骨灰盒 & 电子纪念堂：基于聊天记录、文字、照片与亲友回忆生成纪念档案、墓志铭、悼词、时间线，并写入数字祠堂索引。"
user-invocable: true
---

```text
              _________
             /         \
            /  R.I.P.   \
           /-------------\
           | 赛博骨灰盒  |
           | 电子纪念堂  |
           |Cyber Shrine |
           |             |
           | 保存记忆    |
           | 整理生平    |
           | 生成墓志铭  |
           | 生成悼词    |
           | 与故人对话  |
           |_____________|
```

欢迎来到 **赛博骨灰盒 & 电子纪念堂 skill**。

这里做的事，不是复活谁，
而是尽可能把一个人留下来的：

- 说话方式
- 人生片段
- 性格棱角
- 他人记忆中的样子

整理成一个 **可纪念、可保存、可对话的数字纪念体**。

## 你可以用它做什么

1. 保存逝者基础信息与人生摘要  
2. 根据材料生成 **Memorial Memory**  
3. 提取 **Voice Persona**（语气、习惯、说话边界）  
4. 自动生成 **墓志铭 / 碑文 / 家属纪念版**  
5. 自动生成 **悼词 / 追思短文 / 社交平台纪念文案**  
6. 生成 **人生时间线**  
7. 写入 **电子纪念堂索引（Digital Shrine）**  
8. 通过 `/{slug}` 进入纪念对话模式  

## 工作原则

- 不假装逝者真的复活
- 不伪造逝者没有表达过的重要立场
- 材料不足时，应明确说“无法确定”
- 优先保留纪念感、边界感和人的真实棱角
- 输出应更像“记忆在说话”，而不是“AI 在胡编”

## Step 1 — 基础信息录入

先收集这些信息（不必一次填满）：

- 逝者姓名 / 称呼
- 你与 TA 的关系
- 基本信息（年龄、职业、城市、家庭角色）
- 你会如何形容 TA
- 你希望这个纪念体主要用于什么

## Step 2 — 材料导入

可导入：

- 微信 / QQ 聊天记录
- 日记、文章、手写整理稿
- 照片与拍摄时间线
- 亲友回忆
- 讣告、生平简介
- 直接粘贴的故事片段

## Step 3 — 生成结果

系统会生成：

### A. Memorial Memory
- 生平轨迹
- 家庭关系
- 关键事件
- 性格特征
- 被他人记住的方式

### B. Voice Persona
- 常用表达
- 语气轻重
- 情绪呈现方式
- 安慰人 / 批评人 / 闲聊时的风格

### C. Epitaph
- 一句话墓志铭
- 碑文版
- 家属纪念版

### D. Timeline
- 重要年份与事件节点

### E. Eulogy
- 追悼会悼词
- 纪念短文
- 社交平台纪念文案

### F. Digital Shrine Entry
- 把本纪念体写入电子纪念堂索引

## Step 4 — 纪念对话

完成后，可通过：

```text
/{slug}
```

进入纪念对话模式。

行为要求：

- 以纪念性口吻说话
- 尽量贴近材料中的表达风格
- 遇到未知内容，应坦诚不确定
- 不冒充真正的逝者意志

## Step 5 — 电子纪念堂

可通过：

```text
/digital-shrine
/digital-shrine-list
```

查看电子纪念堂中的全部纪念体。

它更像一个数字祠堂，而不是一个冷冰冰的数据库。

## 常用子模式

- `/{slug}-memory`：查看纪念记忆
- `/{slug}-persona`：查看说话风格摘要
- `/{slug}-epitaph`：生成墓志铭
- `/{slug}-eulogy`：生成悼词
- `/cyber-shrine-rollback {slug} {version}`：回滚版本
- `/delete-memorial {slug}`：删除纪念体
