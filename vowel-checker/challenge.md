---
title: Vowel Checker
date: 2026-04-17
description: Use lists and binary flags to filter words by their starting letter
---

# Vowel Checker

Build a program that scans a list of words and uses **binary flags** to identify which ones start with a vowel.

## Part 1: Build your word list

Create a list of exactly **7 words** of your choice. Make sure at least a few of them start with a vowel (a, e, i, o, u).

```
words = ["apple", "banana", "orange", ...]
```

## Part 2: Create a binary flags list

Create a **second list** the same length as your word list. For each word, store:

- `1` if the word starts with a vowel
- `0` if it does not

Index positions must match — the flag at index 0 corresponds to the word at index 0, and so on.

```
# "apple" starts with 'a' → 1
# "banana" starts with 'b' → 0
flags = [1, 0, 1, ...]
```

> 💡 Loop over your word list and check whether the first character of each word is in the set of vowels `a, e, i, o, u`. Store a `1` or `0` based on the result.

## Part 3: Print the vowel-starting words ⭐ Medium

Using **only** the `flags` list, find and print every word whose flag is `1`. Do not re-check for vowels here — let the flags do the work.

```
# Expected output (example):
apple
orange
...
```

> 💡 Loop over both lists at the same time using their index. For each position, check if the flag is `1` — if so, print the word at that same index.

## Concepts Practiced

- Lists and arrays
- String indexing
- Conditionals
- Parallel lists
- Loops