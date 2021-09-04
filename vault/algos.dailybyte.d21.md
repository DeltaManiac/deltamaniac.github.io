---
id: kctoRCv8BRIfKdZOP9Iuz
title: Reverse Linked List
desc: ''
updated: 1629418720325
created: 1629418596328
nav_order: 21
---
## Problem

This question is asked by Facebook.

Given a linked list, containing unique values, reverse it, and return the result.

Ex: Given the following linked lists...

> 1->2->3->null, return a reference to the node that contains 3 which points to a list that looks like the following: 3->2->1->null
>
> 7->15->9->2->null, return a reference to the node that contains 2 which points to a list that looks like the following: 2->9->15->7->null
>
> 1->null, return a reference to the node that contains 1 which points to a list that looks like the following: 1->null

## [[python]]

```python
def reverseList(self, head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev
```

## [[go]]

## [[rust]]

