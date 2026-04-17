# CCA Coding Club — Challenges

This repo holds all coding challenges for the club. The website reads from this repo automatically.

## How to Add a Challenge

1. Create a folder — name it with **lowercase and hyphens** (this becomes the challenge ID)
2. Add a `challenge.md` file inside it
3. Push to `main` — the website picks it up automatically

```
my-challenge-name/
└── challenge.md
```

## challenge.md Format

Each challenge is a markdown file. Put metadata at the top between `---` lines:

```markdown
---
title: My Challenge Title
date: 2026-04-17
description: A one-sentence summary shown on the card
---

# My Challenge Title

The full challenge description goes here. Use any markdown you want —
headings, code blocks, tables, links, images, etc.
```

### Metadata fields

| Field | Required? | What it does |
|-------|-----------|-------------|
| `title` | No | Card title on the website. If missing, the folder name is used |
| `date` | No | Sorts challenges (newest first). Format: `YYYY-MM-DD` |
| `description` | No | Short blurb on the card. Keep to 1-2 sentences |

If you do not use the `---` block, the folder name is auto-formatted as the title (e.g. `reverse-a-string` → "Reverse A String").

## Rules

- **Folder name = challenge ID**
- **One file per challenge** - just `challenge.md`, nothing else required, we may add support for additional resources for challenges in the future
- **Keep folder names lowercase with hyphens** - no spaces, no uppercase
- **Don't rename folders after students have submitted** - submissions are linked by folder name (challenge id). we could change this in the future, but it would be a hassle to update all the submissions.