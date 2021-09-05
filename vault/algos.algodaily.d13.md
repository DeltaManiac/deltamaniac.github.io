---
id: BTLbjy2oU8Dy7nHAlKH4e
title: Dollar Sign Deletion
desc: ''
updated: 1630827989175
created: 1630827283094
nav_order: 13
---

## Problem

You're given an array of strings containing alphabetical characters and certain `$` characters.

A `$` represents a DELETE action whereby the character before it is deleted.

Each of these strings will be run through a method to operate on the `$` DELETE action.

We want to find out if the final string is the same for all of them.

Let's take an example:

```
const input = ["f$st", "st"]
isDollarDeleteEqual(input);
// true
// true because both become "st"
```
Given the below function signature, can you find a solution in O(n) time and constant space?

```
function isDollarDeleteEqual(arr) {
  return;
}
```
Constraints

    The input arrays can be of any size
    Every string has at least a single character
    The string will consist of dollar signs and lowercase alphabets
    Expected overall time complexity : O(n)
    Expected space complexity : O(n)

## [python]
```python

```