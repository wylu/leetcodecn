#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   设计循环队列.py
@Time    :   2020/09/17 23:18:24
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyCircularQueue:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue
        to be k.
        """
        self.capacity = k
        self.head = None
        self.tail = None
        self.length = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the
        operation is successful.
        """
        if self.length == self.capacity:
            return False

        if self.length == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            node = Node(value)
            self.tail.next = node
            self.tail = node

        self.length += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the
        operation is successful.
        """
        if self.length == 0:
            return False

        self.head = self.head.next
        self.length -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.length == 0:
            return -1
        return self.head.val

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.length == 0:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.length == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.length == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
