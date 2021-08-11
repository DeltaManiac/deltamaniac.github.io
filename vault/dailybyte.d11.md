---
id: MK4zqoIqZbpAulNuIoBLk
title: Day 11
desc: ''
updated: 1628702602884
created: 1628522961878
nav_order: 11
---
# Problem
This question is asked by Microsoft.

Given a string, return the index of its first unique character.
If a unique character does not exist, return -1.

Ex: Given the following strings...

> "abcabd", return 2
>
> "thedailybyte", return 1
>
> "developer", return 0

## [[python]]
```python
def first_unique_char(s):
    for i,j in OrderedDict(Counter(s)).items():
        if j == 1:
            return s.index(i)
    return -1
```

## [[go]]

## [[rust]]
