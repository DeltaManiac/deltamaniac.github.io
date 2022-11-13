## Problem

This question is asked by Google.

Given a linked list and a value, remove all nodes containing the provided value, and return the resulting list.

Ex: Given the following linked lists and values...

> 1->2->3->null, value = 3, return 1->2->null
>
> 8->1->1->4->12->null, value = 1, return 8->4->12->null
>
> 7->12->2->9->null, value = 7, return 12->2->9->null

## [[python]]

```python
def remove_nodes(head,val)
    while head and head.val == val:
        head = head.next
    if not head:
        return head
    prev, cur = head, head.next
    while cur:
        while cur and cur.val == val:
            cur = cur.next
        prev.next = cur
        if cur:
            prev, cur = prev.next, cur.next
    return head
```

## [[go]]

## [[rust]]

