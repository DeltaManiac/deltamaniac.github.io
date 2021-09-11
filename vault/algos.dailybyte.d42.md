---
id: 6SyXABwFD3MumOuo9WbRS
title: Max Depth
desc: ''
updated: 1631331312133
created: 1631331127512
nav_order: 42
---


# Problem

Given a binary tree, return its maximum depth.

Note: the maximum depth is defined as the number of nodes along the longest path from root node to leaf node.

Ex: Given the following tree…
<pre>
    9
   / \
  1   2
return 2
</pre>

Ex: Given the following tree…

<pre>
    5
   / \
  1  29
    /  \
   4   13

return 3
</pre>

## [[python]]
```python
def maxDepth(root):
    if root is None:
        return 0
    return Math.max(maxDepth(root.left),maxDepth(root.right))
```

## [[go]]

## [[rust]]