---
id: PFrP8aKT5l1JjVnRtPi3P
title:  Binary Path Sum
desc: ''
updated: 1631625877883
created: 1631625605586
nav_order: 44
---

# Problem

Given a binary tree and a target, return whether or not there exists a root to leaf path such that all values along the path sum to the target.

Ex: Given the following tree…
<pre>
      1
     / \
    5   2
   /   / \
  1  12   29
</pre>

and a target of 15, return true as the path 1->2->12 sums to 15.

Ex: Given the following tree…
<pre>
     104
    /   \
  39     31
 / \    /  \
32  1  9    10
and a target of 175, return true as the path 104->39->32 sums to 175.
</pre>

## [[python]]

```python
def hasPathSum(root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False

        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum==0
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right, targetSum)
```
## [[go]]

## [[rust]]