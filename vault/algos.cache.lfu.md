---
id: C5ybTwOXmAqV4XdcTA06w
title: Least Frequently Used Cache
desc: ''
updated: 1630977472958
created: 1630944372362
---


```python
from collections import defaultdict
from collections import OrderedDict


class Node:
    def __init__(self,key,val,count) -> None:
        self.key = key
        self.val = val
        self.count = count

class LFUCache(object):
    def __init__(self,capacity) -> None:
        self.cap = capacity
        self.key_to_node = {}
        self.count_to_node = defaultdict(OrderedDict)
        self.minCount = None

    def get(self, key):
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]
        del self.count_to_node[node.count][key]

        if not self.count_to_node[node.count]:
            del self.count_to_node[node.count]

        node.count +=1
        self.count_to_node[node.count][key] = node

        if not self.count_to_node[self.minCount]:
            self.minCount += 1

        return node.val

    def put(self, key, value):

        if not self.cap:
            return

        if key in self.key_to_node:
            self.key_to_node[key].val = value
            self.get(key)
            return

        if len (self.key_to_node) == self.cap:
            k,n = self.count_to_node[self.minCount].popitem(last = False)
            del self.key_to_node[k]

        self.count_to_node[1][key] = self.key_to_node[key] = Node(key,value,1)
        self.minCount = 1
        return


lfu =  LFUCache(2)
lfu.put(1, 1);
lfu.put(2, 2);
lfu.get(1);
lfu.put(3, 3);
lfu.get(2);
lfu.get(3);
lfu.put(4, 4);
lfu.get(1);
lfu.get(3);
lfu.get(4);
```