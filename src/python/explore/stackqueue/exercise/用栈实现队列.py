#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   用栈实现队列.py
@Time    :   2020/09/19 19:03:22
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.st1 = []
        self.st2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.st1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.st2:
            while self.st1:
                self.st2.append(self.st1.pop())
        return self.st2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.st2:
            while self.st1:
                self.st2.append(self.st1.pop())
        return self.st2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.st1 and not self.st2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
