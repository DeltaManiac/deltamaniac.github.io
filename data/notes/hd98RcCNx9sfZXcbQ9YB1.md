## Problem

Given a binary search tree, return the minimum difference between any two nodes in the tree.

<pre>
Ex: Given the following tree...
        2
       / \
      3   1
return 1.
</pre>

<pre>
Ex: Given the following tree...
        29
       /  \
     17   50
    /     / \
   1    42  59
return 8.
</pre>

<pre>
Ex: Given the following tree...
        2
         \
         100
return 98.
</pre>

## [[python]]

```python
def getMinDiff(root):
    def solve(node,low,high):
        if not node: return high-low
        left = solve(node.left,low,node.val)
        right = solve(node.right,node.val,high)
        return min(left,right)
   return solve(root,float('-inf'),float('inf'))

```

## [[go]]

## [[rust]]

