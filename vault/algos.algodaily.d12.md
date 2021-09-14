---
id: VlnBjpgWAwtVElgthI1rn
title: Detect Substring in String
desc: ''
updated: 1630824758300
created: 1630818583706
---

## Problem

How would you write a function to detect a substring in a string?

If the substring can be found in the string, return the index at which it starts. Otherwise, return -1.

```
function detectSubstring(str, subStr) {
  return -1;
}
```
Important-- do not use the native String class's built-in substring or substr method. This exercise is to understand the underlying implementation of that method.

Constraints

    Length of both the given strings <=100000
    The strings would never be null
    The strings will only consist of lowercase letters
    Expected time complexity : O(n)
    Expected space complexity : O(1)


## [python]
```python
def substr(haystack, needle):
    n, h = len(needle), len(haystack)
    i, j, nxt = 1, 0, [-1]+[0]*n
    while i < n:
        if j == -1 or needle[i] == needle[j]:
            i += 1
            j += 1
            nxt[i] = j
        else:
            j = nxt[j]
    i = j = 0
    while i < h and j < n:
        if j == -1 or haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            j = nxt[j]
    return i-j if j == n else -1
```