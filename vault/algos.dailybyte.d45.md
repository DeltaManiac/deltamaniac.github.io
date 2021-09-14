---
id: O4LlF44bqvlxcNHZawnaE
title: Is Symmetric Tree
desc: ''
updated: 1631628481687
created: 1631626786647
nav_order: 45
---
# Problem

Given a binary tree, return whether or not it forms a reflection across its center (i.e. a line drawn straight down starting from the root).
Note: a reflection is when an image, flipped across a specified line, forms the same image.

Ex: Given the following tree…
<pre>
   2
 /   \
1     1
</pre>
return true as when the tree is reflected across its center all the nodes match.

Ex: Given the following tree…
<pre>
    1
   / \
  5   5
   \    \
    7    7
</pre>
return false as when the tree is reflected across its center the nodes containing sevens do not match.

## [[python]]

```python
def isSymmetric(root):
    return self.isMirror(root.left, root.right)

def isMirror(t1,t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return True
    return t1.val == t2.val and isMirror(t1.right,t2.left) and isMirror(t1.right,t2.left)
```

## [[go]]

## [[rust]]