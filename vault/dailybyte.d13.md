---
id: Ca7OMVPVMEBpr8rb3Xy94
title: Intersection Of Two Arrays
desc: ''
updated: 1629045919578
created: 1628702202317
nav_order: 13
---
# Problem

This question is asked by Google. Given two integer arrays, return their intersection.

Note: the intersection is the set of elements that are common to both arrays.

Ex: Given the following arrays...

> nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
>
> nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
>
> nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []`

## [[python]]
```python
def intersection(nums1,nums2):
    return set(nums1).intersection(set(nums2))
```

## [[go]]

## [[rust]]
