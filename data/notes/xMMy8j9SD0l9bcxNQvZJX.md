
# Problem
Given a binary tree, return the sum of all left leaves of the tree. Ex: Given the following tree…

<pre
    5
   / \
  2   12
     /  \
    3    8
return 5 (i.e. 2 + 3)
</pre>

Ex: Given the following tree…

<pre>
       2
      / \
    4    2
   / \
  3   9
return 3
</pre>

## [[python]]

```python
def isLeaf(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    return False

def leftLeavesSum(root):
    res = 0
    if root is not None:
        if isLeaf(root):
            res += root.left.key
        else:
            res += leftLeavesSum(root.left)
        res += leftLeavesSum(root.right)
    return res
```

## [[go]]

## [[rust]]

