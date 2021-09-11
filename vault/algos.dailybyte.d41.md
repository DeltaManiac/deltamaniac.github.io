---
id: uSlHmjy4qGkkDP6oh5BTE
title: Gather Column
desc: ''
updated: 1631331107834
created: 1631330068859
nav_order: 41
---

# Problem
Given a binary tree, return its column order traversal from top to bottom and left to right.

 Note: if two nodes are in the same row and column, order them from left to right.

Ex: Given the following tree…
<pre>
    8
   / \
  2   29
     /  \
    3    9
return [[2], [8, 3], [29], [9]]
</pre>

Ex: Given the following tree…

<pre>
     100
    /   \
  53     78
 / \    /  \
32  3  9    20
return [[32], [53], [100, 3, 9], [78], [20]]
</pre>

## [[python]]
```python
def helper(self, placement,level, root, dic):
    if(not root):
        return
    dic[placement].append((level, root.val))
    self.helper(placement-1, level+1, root.left, dic)
    self.helper(placement+1, level+1, root.right, dic)

def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
    dic = defaultdict(list)
    self.helper(0,0, root, dic)
    result = []
    for i in sorted(dic.keys()):
        temp = []
        for j in sorted(dic[i]):
            temp.append(j[1])
        result.append(temp)
    return result
```
## [[go]]

## [[rust]]