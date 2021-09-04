---
id: uAHrrPQGbQnXmrMZWRmzL
title: Middle Node of Linked List
desc: ''
updated: 1629418187686
created: 1629418076186
nav_order: 18
---
## Problem

This question is asked by Amazon.

Given a non-empty linked list, return the middle node of the list. If the linked list contains an even number of elements, return the node closer to the end.

Ex: Given the following linked lists...

> 1->2->3->null, return 2
>
> 1->2->3->4->null, return 3
>
> 1->null, return 1

## [[python]]

```python
def middleNode(self, head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

## [[go]]

## [[rust]]

