# CCA Coding Club — Challenges

This repo holds all coding challenges for the club. The website reads from this repo automatically.

## How to Add a Challenge

1. Create a folder — name it with **lowercase and hyphens** (this becomes the challenge ID)
2. Add a `challenge.md` file inside it
3. Push to `main` — the website picks it up automatically

```
my-challenge-name/
├── challenge.md              ← required
└── solutions.md              ← optional, added after the challenge
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

## solutions.md Format (Optional)

Add a `solutions.md` to a challenge folder when you're ready to share official solutions. Use `--LanguageName` to separate solutions by language:

```markdown
--Python

​```python
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
​```

--JavaScript

​```javascript
for (let i = 1; i <= 100; i++) {
  if (i % 15 === 0) console.log("FizzBuzz");
  else if (i % 3 === 0) console.log("Fizz");
  else if (i % 5 === 0) console.log("Buzz");
  else console.log(i);
}
​```
```

The website shows a dropdown to switch between languages. If there's only one language, no dropdown appears. If there's no `solutions.md`, the button shows "No solutions yet."

## Rules

- **Folder name = challenge ID**
- **`challenge.md` is required** - `solutions.md` is optional
- **Keep folder names lowercase with hyphens** - no spaces, no uppercase
- **Don't rename folders after students have submitted** - submissions are linked by folder name (challenge id). we could change this in the future, but it would be a hassle to update all the submissions.