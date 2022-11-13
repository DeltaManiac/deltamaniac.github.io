## Problem

Given an array of numbers sorted in ascending order, return a height-balanced binary search tree using every number from the array.

Note: height-balanced meaning that the level of any node’s two subtrees should not differ by more than one.

Ex: Given the following nums...

<pre>
nums = [1, 2, 3] return a reference to the following tree...
       2
      /  \
     1    3
</pre>

Ex: Given the following nums...

<pre>
nums = [1, 2, 3, 4, 5, 6] return a reference to the following tree...
        3
       / \
      2   5
     /   / \
    1   4   6
</pre>

## [[python]]

```python
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def arrayToBST(arr):
    if not arr:
        return None
    mid = (len(arr))/2
    root = Node(arr[mid])
    root.left(arrToBST(arr[:mid]))
    root.left(arrToBST(arr[mid+1:]))
    return root

```

## [[go]]

## [[rust]]

