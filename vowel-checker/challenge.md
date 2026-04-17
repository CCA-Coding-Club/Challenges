---
title: Vowel Checker
date: 2026-04-17
description: Use list comprehensions and binary flags to filter words by their starting letter
---

# Vowel Checker

Build a program that scans a list of words and uses **binary flags** to identify which ones start with a vowel.

## Part 1: Build your word list

Use a **list comprehension** to create a list of exactly **7 words** of your choice. Make sure at least a few of them start with a vowel (a, e, i, o, u).

```python
words = [w for w in ["apple", "banana", "orange", ...]]
```

## Part 2: Create a binary flags list

Create a **second list** the same length as your word list. For each word, store:

- `1` if the word starts with a vowel
- `0` if it does not

Index positions must match — `flags[0]` corresponds to `words[0]`, and so on.

```python
# "apple" starts with 'a' → 1
# "banana" starts with 'b' → 0
flags = [1, 0, 1, ...]
```

> 💡 **Hint:** Use a conditional expression inside your list comprehension: `1 if condition else 0`. Check whether `word[0]` is in `"aeiou"`.

## Part 3: Print the vowel-starting words ⭐ Medium

Using **only** the `flags` list, find and print every word whose flag is `1`. Do not re-check for vowels here — let the flags do the work.

```
# Expected output (example):
apple
orange
...
```

> 💡 **Hint:** Python's `zip()` function lets you loop over two lists at once: `for word, flag in zip(words, flags)`. Then check `if flag == 1` before printing.

## Concepts Practiced

- List comprehensions
- String indexing
- Conditionals
- Parallel lists
- `zip()`
- For loops