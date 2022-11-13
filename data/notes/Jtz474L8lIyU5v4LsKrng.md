# Problem
Given a binary tree, return its zig-zag level order traversal (i.e. its level order traversal from left to right the first level, right to left the level the second, etc.).

Ex: Given the following tree…

<pre>
    1
   / \
  2   3
return [[1], [3, 2]]
</pre>

Ex: Given the following tree…
<pre>
    8
   / \
  2  29
    /  \
   3    9
return [[8], [29, 2], [3, 9]]
</pre>
## [[python]]
```python
def zigZagOrderTraversal(root):
    if not root:
        return []
    q = [root]
    view = []
    order = 1
    while len(q):
        temp_arr =[]
        n = len(q)
        for i in range(1,n+1):
            temp = q[0]
            q.pop(0)

            temp_arr.append(temp.data)

            if temp.left:
                q.append(temp.left)

            if temp.right:
                q.append(temp.right)
        view.append(temp_arr[::order])
        order = order * -1
    return view
```

## [[go]]

## [[rust]]
