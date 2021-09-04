---
id: Xkc7XPLPXKzeXbspwLs5J
title: Gather Level
desc: ''
updated: 1630762378331
created: 1630761277740
nav_order: 36
---
## Problem

Given a binary tree, return its level order traversal where the nodes in each level are ordered from left to right.

<pre>
Ex: Given the following tree...

    4
   / \
  2   7
return [[4], [2, 7]]
</pre>

<pre>
Ex: Given the following tree...

    2
   / \
  10  15
        \
         20
return [[2], [10, 15], [20]]
</pre>

<pre>
Ex: Given the following tree...

    1
   / \
  9   32
 /      \
3        78
return [[1], [9, 32], [3, 78]]
</pre>

## [[python]]

```python
def levelOrder(root):
    if not root: return []
    result, temp, queue = [] [] [root]
    while queue:
        for x in iter(range(len(queue))):
            q = queue.pop(0)
            temp += [q.val]
            if q.left: queue.append(q.left )
            if q.right: queue.append(q.right )
            result += [temp]
            temp=[]
    return result
```

## [[go]]

## [[rust]]

