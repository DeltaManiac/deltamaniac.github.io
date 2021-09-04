---
id: iy0XsO219wG3GO2TQhbSg
title: Find Mode
desc: ''
updated: 1630761153418
created: 1630760693504
nav_order: 35
---
## Problem

Given a binary search tree, return its mode (you may assume the answer is unique). If the tree is empty, return -1.

Note: the mode is the most frequently occurring value in the tree.

<pre>
Ex: Given the following tree...

        2
       / \
      1   2
return 2.
</pre>

<pre>
Ex: Given the following tree...

         7
        / \
      4     9
     / \   / \
    1   4 8   9
               \
                9
return 9.
</pre>

## [[python]]

```python
def findMode(root):
    counts = collections.Counter()
    modeValue = 0

    def helper(node):
        nonlocal modeValue
        if not node:
            return
        counts[node.val] +=1
        modeValue = max(mv,counts[node.val])
        helper(node.left)
        helper(node.right)
    helper(root)
    return [k for k,v in counts.items() if v == mv]
```

## [[go]]

## [[rust]]

