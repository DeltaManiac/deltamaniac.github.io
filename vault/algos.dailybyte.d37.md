---
id: PHHaN0NCzRlfDJqfdMUCi
title: Visible Values
desc: ''
updated: 1631327175329
created: 1631326172738
nav_order: 37
---

# Problem

Given a binary tree return all the values you’d be able to see if you were standing on the left side of it with values ordered from top to bottom.

Ex: Given the following tree…

<pre>
-->    4
      / \
-->  2   7
return [4, 2]
</pre>

Ex: Given the following tree…

<pre>
-->        7
         /  \
-->     4     9
       / \   / \
-->   1   4 8   9
                 \
-->               9
return [7, 4, 1, 9]
</pre>

## [[python]]

```python
def leftview(root):
    if not root:
        return []
    q = q[root]
    view = []
    while len(q):
        n = len(q)
        for i in range(1,n+1):
            temp = q[0]
            q.pop(0)

            if i is == 1:
                view.append(temp.data)

            if temp.left:
                q.append(temp.left)

            if temp.right:
                q.append(temp.right)
    return view
```
## [[go]]

## [[rust]]

