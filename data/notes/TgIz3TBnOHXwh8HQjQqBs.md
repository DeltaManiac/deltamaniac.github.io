
# Problem

Given two binary trees, return whether or not both trees have the same leaf sequence.

Two trees have the same leaf sequence if both trees’ leaves read the same from left to right.

Ex: Given the following trees…
<pre>
   1
 /   \
1     3
</pre>
and

<pre>
   7
 /   \
1     2
</pre>

return false as both the trees' leaves don't read the same from left to right (i.e. [1, 3] and [1, 2]).

Ex: Given the following trees…
<pre>
    8
   / \
  2   29
    /  \
   3    9
</pre>
and
<pre>
    8
   / \
  2  29
 /   /  \
2   3    9
     \
      3
</pre>

return true as both the trees' leaves read the same from left to right (i.e. [2, 3, 9] and [2, 3, 9]).

## [[python]]

```python
def sameleaves(root1, root2):
    output1 = []
    output2 = []
    get_leaves(root1, output1)
    get_leaves(root2, output2)

    if len(output1) != len(output2):
        return False


    for el1,el2 in zip(output1, output2):
        if el1 != el2:
            return False

    return True


def get_leaves(node, output):

    if not node:
        return

    if not node.left and not node.right:
        output.append(node.value)

    get_leaves(node.left, output)
    get_leaves(node.right, output)

```

## [[go]]

## [[rust]]