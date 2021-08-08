---
id: diI4VBMv8iMMUStWIFnUE
title: Day 6
desc: ''
updated: 1628434973356
created: 1628398041141
nav_order: 6
---
# Problem

This question is asked by Microsoft. Given an array of strings, return the longest common prefix that is shared amongst all strings.
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
