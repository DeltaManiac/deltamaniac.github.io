---
id: wQlIvY7nuhvKUdbd9Evns
title: Gather N-ary Tree Levels
desc: ''
updated: 1631330045750
created: 1631329453474
nav_order: 40
---

# Problem
Given an n-ary tree, return its level order traversal.
Note: an n-ary tree is a tree in which each node has no more than N children.

Ex: Give the following n-ary tree…
<pre>
    8
  / | \
 2  3  29
return [[8], [2, 3, 29]]
</pre>

Ex: Given the following n-ary tree…

<pre>
     2
   / | \
  1  6  9
 /   |   \
8    2    2
   / | \
 19 12 90
return [[2], [1, 6, 9], [8, 2, 2], [19, 12, 90]]
</pre>

## [[python]]
```python
def naryTreeLevel(root):
    if not root:
        return []
    q = [root]
    view = []
    while len(q):
        temp_arr =[]
        n = len(q)
        for i in range(1,n+1):
            temp = q[0]
            q.pop(0)

            temp_arr.append(temp.data)

            for child in temp.children:
                q.append(child)

        view.append(temp_arr)
    return view
```
## [[go]]

## [[rust]]