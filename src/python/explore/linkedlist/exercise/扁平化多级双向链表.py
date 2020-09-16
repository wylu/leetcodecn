#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   扁平化多级双向链表.py
@Time    :   2020/09/16 23:00:36
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return

        stack = []
        cur = head
        while cur:
            if cur.child:
                if cur.next:
                    stack.append(cur.next)
                cur.next = cur.child
                cur.child.prev = cur
                cur = cur.child
                # reset to null
                cur.prev.child = None
                continue

            if not cur.next and stack:
                tmp = stack.pop()
                cur.next = tmp
                tmp.prev = cur

            cur = cur.next

        return head
