---
id: DvmbT3vPCATaSEHoFRCEF
title: Convert Binary Search Tree to Sorted Linked List
desc: ''
updated: 1630507587787
created: 1630507048471
nav_order: 30
---
## Problem

Given a binary search tree, rearrange the tree such that it forms a linked list where all its values are in ascending order.

Ex: Given the following tree...

<pre>
        5
       / \
      1   6
</pre>

return...

<pre>
 1
  \
   5
    \
     6
</pre>

Ex: Given the following tree...

<pre>
       5
      / \
    2    9
   / \
  1   3
</pre>

return...

<pre>
 1
  \
   2
    \
     3
      \
       5
        \
         9
</pre>

Ex: Given the following tree...

<pre>
 5
  \
   6
</pre>

return...

<pre>
 5
  \
   6
</pre>

## [[python]]

```python
class Node:
    def __init__(self):
        self.key = 0
        self.left = None
        self.right = None

def newNode(key):
    node = Node()
    node.key = key
    node.left = node.right = None
    return (node)

def flatten(root):
    if (root == None or root.left == None and
                        root.right == None):
        return

    if (root.left != None):

        flatten(root.left)

        tmpRight = root.right
        root.right = root.left
        root.left = None

        t = root.right
        while (t.right != None):
            t = t.right

        t.right = tmpRight

    flatten(root.right)


```

## [[go]]

## [[rust]]

