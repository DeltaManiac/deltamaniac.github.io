---
id: QWfFbHdElCWirOdCzK3Cw
title: Where Cycle ?!
desc: ''
updated: 1629418581949
created: 1629418355696
nav_order: 20
---
# Problem

This question is asked by Apple.

Given a potentially cyclical linked list where each value is unique, return the node at which the cycle starts. If the list does not contain a cycle, return null.

Ex: Given the following linked lists...

>1->2->3, return null
>
>1->2->3->4->5->2 (5 points back to 2), return a reference to the node containing 2
>
>1->9->3->7->7 (7 points to itself), return a reference to the node containing 7

## [[python]]

```python
def whereCycle(self, head)->Node:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    while head != slow:
        slow = slow.next
        head = head.next
    return head
```

## [[go]]

## [[rust]]

