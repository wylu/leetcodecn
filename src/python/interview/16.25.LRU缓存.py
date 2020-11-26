#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   16.25.LRU缓存.py
@Time    :   2020/11/26 09:58:24
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class DLinkedNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move2tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move2tail(node)
        else:
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self._add2tail(node)
            self.size += 1
            if self.size > self.capacity:
                del self.cache[self.head.next.key]
                self._del_node(self.head.next)
                self.size -= 1

    def _move2tail(self, node: DLinkedNode) -> None:
        self._del_node(node)
        self._add2tail(node)

    def _add2tail(self, node: DLinkedNode) -> None:
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def _del_node(self, node: DLinkedNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
