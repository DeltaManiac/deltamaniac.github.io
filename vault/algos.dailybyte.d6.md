---
id: lf4b9qYd73ucvZmtfWbCe
title: Longest Common Shared Prefix
desc: ''
updated: 1629045544705
created: 1628398041141
nav_order: 6
---

# Problem

This question is asked by Microsoft.

Given an array of strings, return the longest common prefix that is shared amongst all strings.

Note: you may assume all strings only contain lowercase alphabetical characters.

Ex: Given the following arrays...

> ["colorado", "color", "cold"], return "col"
>
> ["a", "b", "c"], return ""
>
> ["spot", "spotty", "spotted"], return "spot"

## [[python]]
```python
def longestCommonPrefix(strs)->string:
        sz, ret = zip(*strs), ""
        for c in sz:
            if len(set(c)) > 1: break
            ret += c[0]
        return ret
```
## [[go]]

## [[rust]]