# Problem

Given a binary tree, return a list of strings containing all root to leaf paths.

Ex: Given the following tree…

<pre>
   1
 /   \
2     3
return ["1->2", "1->3"]
</pre>

Ex: Given the following tree…

<pre>
    8
   / \
  2  29
    /  \
   3    9
return ["8->2", "8->29->3", "8->29->9"]
</pre>

## [[python]]

```python
def binaryTreePath(root):
    if not root:
        return []
    res, stack = [] ,[(root,"")]
    while stack:
        node, ls = stack.pop()
        if not node.left and not node.right:
            res.append(ls + str(node.val))
        if node.right:
            stack.append((node.right, ls+str(node.val) + "->"))
        if node.left:
            stack.append((node.left, ls+str(node.val) + "->"))
    return res
```
## [[go]]

## [[rust]]
