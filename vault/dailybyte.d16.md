---
id: 6ywEeMzNQG1KazrhY8KFk
title: Remove nth to last node
desc: ''
updated: 1629157816193
created: 1629157708624
nav_order: 16
---

# Problem

This question is asked by Facebook.

Given a linked list and a value n, remove the nth to last node and return the resulting list.

Ex: Given the following linked lists...

>1->2->3->null, n = 1, return 1->2->null
>
>1->2->3->null, n = 2, return 1->3->null
>
>1->2->3->null, n = 3, return 2->3->null

## [[python]]

```python
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head
```
## [[go]]

## [[rust]]