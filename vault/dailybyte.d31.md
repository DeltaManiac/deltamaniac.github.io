---
id: bGVpZyUeyyzYYpdZZRI9Z
title: Lowest Common Ancestor
desc: ''
updated: 1630508336493
created: 1630507688524
nav_order: 31
---
# Problem

Given a binary search tree that contains unique values and two nodes within the tree, a, and b, return their lowest common ancestor.

Note: the lowest common ancestor of two nodes is the deepest node within the tree such that both nodes are descendants of it.

Ex: Given the following tree...
<pre>
       7
      / \
    2    9
   / \
  1   5

and a = 1, b = 9, return a reference to the node containing 7.
</pre>

Ex: Given the following tree...

<pre>
        8
       / \
      3   9
     / \
    2   6

and a = 2, b = 6, return a reference to the node containing 3.
</pre>

Ex: Given the following tree...

<pre>
        8
       / \
      6   9

and a = 6, b = 8, return a reference to the node containing 8.
</pre>

## [[python]]
```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            if root in (None, p, q): return root
            left = self.lowestCommonAncestor(root.left,p,q)
            right = self.lowestCommonAncestor(root.right,p,q)
            return root if left and right else left or right
```

## [[go]]

## [[rust]]
