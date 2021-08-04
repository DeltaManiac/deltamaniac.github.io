---
id: mOU2cIc7wX12zgdN
title: maxDepth
desc: ''
updated: 1627953310187
created: 1627784241720
---

# Maximum Depth of Binary Tree

Given the `root` of a binary tree, return its maximum depth


## Binary Tree
![](/assets/images/2021-07-17-12-08-23.png)

## Solution

### Python

```python
def maxDepth(root:TreeNode)-> int:
    if not root:
        return 0
    else:
        max(self.maxDepth(root.left),self.maxDepth(root.right))+1
```

### Go

```go
import(
"math"
)
func maxDepth(root *TreeNode) int {
    if root == nil{
        return 0
    }
    return int(math.Max(float64(maxDepth(root.Left)),float64(maxDepth(root.Right)))) +1
}
```

### Rust
```rust
fn maxDepth(root:Option<Rc<RefCell<TreeNode>>>>>)-> i32{
 match root {
            Some(a) => {
                let l = Solution::max_depth(a.borrow().left.clone());
                let r = Solution::max_depth(a.borrow().right.clone());
                return std::cmp::max(l, r) + 1;
            }
            None => return 0,
        }
}
```