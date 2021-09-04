---
id: lEQkcBXYTfMOn5SK9BYtp
title: Identical Trees
desc: ''
updated: 1630509774482
created: 1630509479734
nav_order: 33
---
## Problem

Given two binary trees, return whether or not the two trees are identical.

Note: identical meaning they exhibit the same structure and the same values at each node.

Ex: Given the following trees...

<pre>
        2
       / \
      1   3

    2
   / \
  1   3


return true.
</pre>

Ex: Given the following trees...

<pre>

        1
         \
          9
           \
           18

    1
   /
  9
   \
    18


return false.
</pre>

Ex: Given the following trees...

<pre>
        2
       / \
      3   1

    2
   / \
  1   3


return false.
</pre>

## [[python]]

```python
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def isIdentical(r1,r2):
    if not r1 and not r2:
        return True
    if not r1 or not r2:
        return False
    if r1.val != r2.val:
        return False
    return isIdentical(r1.right, r2.right) and isIdentical(r1.left, r2.left)
```

## [[go]]

## [[rust]]

