<div align="center">

# Cyber Ash Box & Digital Memorial Hall skill

> *“What rests here is not a body, but a remembered voice, a life story, and the traces of being loved.”*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

<br>

A lightly tongue-in-cheek, but fundamentally respectful AI Skill for memorialization.<br>
It turns chats, photos, diaries, writings, and remembered stories into a<br>
**preservable, searchable, conversational memorial persona**.<br>

We call it:

## **Cyber Ash Box & Digital Memorial Hall**

You may think of it as:

- a digital shrine
- an AI epitaph generator
- a memorial archive
- a soft joke version of “digital immortality”

But it is **not** resurrection, and it does **not** claim to bring someone back.
It only tries to preserve, from available materials, a little of their:
**voice, habits, story, warmth, edges, and remembered presence**.

</div>

---

## Features

### 1. Memorial Persona Creation
Build a full memorial profile from source materials:

- **Memorial Memory**: life trajectory, family roles, key events, recurring traits
- **Voice Persona**: speech style, common phrases, emotional tone, interaction habits
- **Epitaph**: one-line epitaph, formal inscription, family version
- **Timeline**: structured life milestones
- **Eulogy**: funeral speech, tribute article, memorial captions

### 2. Digital Shrine System
Group multiple memorial personas into a shared **Digital Shrine / Memorial Hall**:

- maintain a memorial index
- browse the hall roster
- jump into a specific memorial conversation
- useful for family archives and long-term remembrance projects

### 3. Tombstone-style Terminal Intro
The Skill opens with a small terminal tombstone, reinforcing the memorial frame without pretending to be supernatural.

### 4. Memorial Conversation
Invoke `/{slug}` to enter a memorial conversation mode.
The system should:

- stay close to available voice evidence
- preserve personality boundaries
- avoid inventing major beliefs or commitments
- remain clearly a memorial simulation, not a literal return

### 5. Epitaphs and Eulogies
Generate:

- one-line epitaphs
- engraved-style inscriptions
- family memorial text
- funeral eulogies
- short social memorial captions

---

## Installation

### Claude Code

```bash
mkdir -p .claude/skills
git clone https://github.com/YOUR_USERNAME/cyber-memorial-hall-skill .claude/skills/create-cyber-shrine
```

Optional:

```bash
pip install -r requirements.txt
```

---

## Usage

In Claude Code, type:

```text
/create-cyber-shrine
```

Then follow the intake flow:

1. basic memorial info
2. upload or paste source materials
3. generate memory, persona, epitaph, timeline
4. write into the Digital Shrine index

Later, invoke:

```text
/{slug}
```

to talk to that memorial persona.

### Management Commands

| Command | Description |
|---------|-------------|
| `/create-cyber-shrine` | Create a new memorial persona |
| `/digital-shrine` | Open the Digital Shrine index |
| `/digital-shrine-list` | List all memorial personas |
| `/{slug}` | Memorial conversation mode |
| `/{slug}-memory` | Memory archive mode |
| `/{slug}-persona` | Voice/personality summary |
| `/{slug}-epitaph` | Generate or rewrite epitaph |
| `/{slug}-eulogy` | Generate eulogy |
| `/cyber-shrine-rollback {slug} {version}` | Roll back a previous version |
| `/delete-memorial {slug}` | Delete a memorial persona |

---

## Credits

This project openly acknowledges the lineage and inspiration of:

- **ex-partner skill**
- **colleague skill**
- **yourself skill**

And also thanks:

- **GPT-5.4**
- **Claude Code**
- **VS Code**

for making the redesign, prompt rewriting, and skill workflow refinement possible.
