---
id: 3HX0EpU6Mix3n7Fn0PBMQ
title: Binary Tree Traversal
desc: ''
updated: 1626504708724
created: 1626502788225
---
# Graph
![](/assets/images/2021-07-17-12-08-23.png)

# PreOrder

## Root --> Left --> Right

## F B A D C E G I H

## Code
```python
def preorderTraversal(self, root: TreeNode) -> List[int]:
    if root == None :
        return []
    res= []
    res.append(root.val)
    if root.left!= None:
        res = res + self.preorderTraversal(root.left)
    if root.right!= None:
        res = res + self.preorderTraversal(root.right)
    return res
```

# InOrder

## Left --> Root --> Right

## A B C D E F G I J

## Code
```python
def inorderTraversal(self, root: TreeNode) -> List[int]:
    if root == None :
        return []
    res = []
    if root.left!= None:
        res = res + self.inorderTraversal(root.left)
    res.append(root.val)
    if root.right!= None:
        res = res + self.inorderTraversal(root.right)
    return res
```


# Post Order

## Left --> Right --> Root

## A C E D B H I G F

## Code

```python
def postorderTraversal(self, root: TreeNode) -> List[int]:
    if root == None :
        return []
    res= []
    if root.left!= None:
        res = res + self.postorderTraversal(root.left)
    if root.right!= None:
        res = res + self.postorderTraversal(root.right)
    res.append(root.val)
    return res
```

# Iterative Tree

## Use Stack

1. Push Root to stack
2. Pop From Stack
3. Push Popped Item left tree
4. Push Popped Item right tree

# Level Order

## Use Queue

1. Take Node
2. Push Children into Queue
3. Remove From Queue
4. Go to Step 1

## F, B G, A D I, C E H

## Code
```python
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    res, temp, queue, flag=[], [], [root], 1
    while queue:
        for i in iter(range(len(queue))):
            ptr = queue.pop(0)
            temp+=[ptr.val]
            if ptr.left: queue+=[ptr.left]
            if ptr.right: queue+=[ptr.right]
        res+=[temp[::flag]]
        temp=[]
        flag = flag*-1
    return res
```
