

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