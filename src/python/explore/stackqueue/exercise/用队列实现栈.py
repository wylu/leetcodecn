#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   用队列实现栈.py
@Time    :   2020/09/19 19:12:44
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import deque


class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()
        self.t = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)
        self.t = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.q1) > 1:
            self.t = self.q1.popleft()
            self.q2.append(self.t)
        self.q1, self.q2 = self.q2, self.q1
        return self.q2.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.t

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q1 and not self.q2


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
