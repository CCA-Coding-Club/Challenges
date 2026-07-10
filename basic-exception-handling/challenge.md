---
title: Basic Exception Handling
date: 2026-07-10
description: Practice the syntax and logic of basic exception handling
---

# Basic Exception Handling

Practice the syntax and logic of basic exception handling.

Exception handling is essential to handling program-breaking data. It catches errors caused during run-time, prevents the program from crashing, and allows you to define actions based off the error.

It's syntax takes on different forms in many languages. For example, in Python, we use try and except:
```python
try:
    #try logic
except:
    #exception logic
```
but in Javascript we use try and catch. 

## Part 1: Catching Error(s) ⭐ Easy

Make a program that asks the user for an item number and returns the item from a list. You can make your own list or use this: 
`['banana', 'apple', 'orange', 'grape']`
Use exception handling to catch any errors that occur if the user asks for an invalid item number (like 5 in the above list). Display a friendly message instead of crashing.

Example 1 (no error):
```
The item is: banana
```

Example 2 (index error):
```
Something went wrong. Please try again.
```

## Part 2: Catching Specific Types of Errors ⭐ Medium

Make a program that asks for a user's birth year. If the input cannot be converted into an integer or the value is invalid, raise and catch a `ValueError`, then return a friendly message. If a different data type error occurs, catch a `TypeError` and return a different message.

Example 1 (no error):
```
Enter your birth year: 2005
You are 21 years old.
```

Example 2 (value error):
```
Enter your birth year: two thousand
Please enter a valid birth year.
```

Example 3 (value error):
```
Enter your birth year: -500
Please enter a valid birth year.
```

## Concepts Practiced

- Exception handling
- Catching specific errors 
- Handling invalid user input
- Type conversion
- Raising exceptions