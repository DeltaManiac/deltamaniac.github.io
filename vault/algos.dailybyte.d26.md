---
id: gNXgtNsLpO2mSV9CEO696
title: Call Counter
desc: ''
updated: 1629953103033
created: 1629876359628
nav_order: 26
---
## Problem

This question is asked by Google.

Create a class `CallCounter` that tracks the number of calls a client has made within the last 3 seconds.

Your class should contain one method, `ping(int t)` that receives the current timestamp (in milliseconds) of a new call being made and returns the number of calls made within the last 3 seconds.

Note: you may assume that the time associated with each subsequent call to `ping` is strictly increasing.

Ex: Given the following calls to ping…

> ping(1), return 1 (1 call within the last 3 seconds)
>
> ping(300), return 2 (2 calls within the last 3 seconds)
>
> ping(3000), return 3 (3 calls within the last 3 seconds)
>
> ping(3002), return 3 (3 calls within the last 3 seconds)
>
> ping(7000), return 1 (1 call within the last 3 seconds)

## [[python]]

```python
class CallCounter:

    def __init__(self):
        self.ts_dict = {}

    def ping(self,timestamp):
        if timestamp not in self.ts_dict:
            self.ts_dict[timestamp] = 1
        else:
            self.ts_dict[timestamp] += 1
        return self.getPings(timestamp)

    def getPings(self,timestamp):
        t1 = timestamp - 3000
        tc = 0
        for ts, c in self.ts_dict.items():
            if ts > t1:
                tc += c
        return tc
```

## [[go]]

## [[rust]]

