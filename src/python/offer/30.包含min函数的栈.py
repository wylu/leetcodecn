#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   30.包含min函数的栈.py
@Time    :   2020/08/31 23:54:48
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st1 = []
        self.st2 = []

    def push(self, x: int) -> None:
        self.st1.append(x)
        if self.st2:
            self.st2.append(min(self.st2[-1], x))
        else:
            self.st2.append(x)

    def pop(self) -> None:
        self.st1.pop()
        self.st2.pop()

    def top(self) -> int:
        return self.st1[-1]

    def min(self) -> int:
        return self.st2[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
