---
id: HHRv3Y3IE4GqSELhFZWvL
title: Find Value in BST
desc: ''
updated: 1630116182853
created: 1630115795114
nav_order: 29
---

# Problem

This question is asked by Google.

Given the reference to the root of a binary search tree and a search value, return the reference to the node that contains the value if it exists and null otherwise.

Note: all values in the binary search tree will be unique.

Ex: Given the tree...

>        3
>       / \
>      1   4

and the search value 1 return a reference to the node containing 1.

Ex: Given the following tree...

>         7
>        / \
>       5   9
>          / \
>         8   10

and the search value 9 return a reference to the node containing 9.

Ex: Given the following tree...

 >        8
 >       / \
 >      6   9

and the search value 7 return null.

## [[python]]

```python

def search(self, root, val):
        def search_rec(root):
            if root:
                if root.val == val: return root
                elif root.val < val: return search_rec(root.right)
                return search_rec(root.left)

        return rec(root)

```

## [[go]]

## [[rust]]