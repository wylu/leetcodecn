#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5601.设计有序流.py
@Time    :   2020/11/15 10:30:57
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class OrderedStream:
    def __init__(self, n: int):
        self.stream = [None] * (n + 1)
        self.ptr = 1

    def insert(self, id: int, value: str) -> List[str]:
        self.stream[id] = value
        if self.stream[self.ptr] is None:
            return []

        ans, i = [self.stream[self.ptr]], self.ptr + 1
        while (i < len(self.stream) and self.stream[i]):
            ans.append(self.stream[i])
            i += 1
        self.ptr = i

        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)

if __name__ == "__main__":
    solu = OrderedStream(9)
    print(solu.insert(9, "nghbm"))
    print(solu.insert(7, "hgeob"))
    print(solu.insert(6, "mwlrz"))
    print(solu.insert(4, "oalee"))
    print(solu.insert(2, "bouhq"))
    print(solu.insert(1, "mnknb"))
    print(solu.insert(5, "qkxbj"))
    print(solu.insert(8, "iydkk"))
    print(solu.insert(3, "oqdnf"))
