---
title: Stack It Up
date: 2026-04-17
description: Build and manipulate a stack using arrays, then level up by implementing your own stack class
---

# Stack It Up

A **stack** is a data structure that follows a simple rule: **last in, first out (LIFO)**. Think of it like a stack of plates — you add to the top and remove from the top.

## Part 1: Build a stack ⭐ Easy

Using a built-in list or array in your language, do the following:

- Create an empty stack
- **Push** three numbers onto it
- **Pop** one number off
- Print the final stack

```
stack = []
push 1 → [1]
push 2 → [1, 2]
push 3 → [1, 2, 3]
pop    → [1, 2]
print stack
```

> 💡 Most languages have a built-in array or list type that supports push and pop operations out of the box. No extra data structures needed!

## Part 2: Build a stack class ⭐ Medium

Recreate the same behavior from Part 1, but this time wrap it in a **class**. Your class should have at least these three methods:

- `push(item)` — adds an item to the top
- `pop()` — removes and returns the top item
- `print_stack()` — prints the current contents

```
s = new Stack()
s.push(1)
s.push(2)
s.push(3)
s.pop()
s.print_stack()  // [1, 2]
```

> 💡 Inside your class, store the stack as a private list or array. Each method should then call the same push and pop logic from Part 1 on that internal list.

## Any Language!

You can use **any programming language** you want — Python, JavaScript, C++, Java, etc.

## Concepts Practiced

- Lists and arrays
- Push and pop operations
- Stack / LIFO logic
- Classes and methods