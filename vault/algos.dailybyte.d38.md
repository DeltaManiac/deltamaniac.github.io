---
id: 5GsjtpVi5R49cqEt35d0t
title: Bottoms Up
desc: ''
updated: 1631327449947
created: 1631327233940
nav_order: 38
---

# Problem
Given a binary tree, returns of all its levels in a bottom-up fashion (i.e. last level towards the root). Ex: Given the following tree…

<pre>
        2
       / \
      1   2
return [[1, 2], [2]]
</pre>

Ex: Given the following tree…
<pre>
       7
      / \
    6    2
   / \
  3   3
return [[3, 3], [6, 2], [7]]
</pre>

## [[python]]
```python
def bottomToTop(root):
    if not root:
        return []
    q = q[root]
    view = []
    while len(q):
        temp_arr =[]
        n = len(q)
        for i in range(1,n+1):
            temp = q[0]
            q.pop(0)

            temp_arr.append(temp.data)

            if temp.left:
                temp_arr.append(temp.left)

            if temp.right:
                temp_arr.append(temp.right)
        view.append(temp_arr)
    return view[::-1]
```
## [[go]]

## [[rust]]
