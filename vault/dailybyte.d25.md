---
id: 6keo0GNJTy31TX50W2gGi
title: Next Greater Element
desc: ''
updated: 1629876324437
created: 1629875166729
nav_order: 25
---

# Problem

This question is asked by Amazon.

Given two arrays of numbers, where the first array is a subset of the second array, return an array containing all the next greater elements for each element in the first array, in the second array. If there is no greater element for any element, output -1 for that number.

Ex: Given the following arrays…


>nums1 = [4,1,2], nums2 = [1,3,4,2], return [-1, 3, -1] because no element in nums2 is greater than 4, 3 is the first number in nums2 greater than 1, and no element in nums2 is greater than 2.
>
>nums1 = [2,4], nums2 = [1,2,3,4], return [3, -1] because 3 is the first greater element that occurs in nums2 after 2 and no element is greater than 4.

## [[python]]

```python
def nextGreaterElement( nums1, nums2):
    map = dict()
    stk = nums2[0:1]

    for num in nums2[1:]:
        while stk and stk[-1] < num:
            map[stk.pop()] = num
        stk.append(num)
    return [map.get(num, -1) for num in nums1]
```

## [[go]]

## [[rust]]
