#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   复制带随机指针的链表.py
@Time    :   2020/09/16 22:24:28
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return

        cur = head
        while cur:
            node = Node(cur.val)
            node.next = cur.next
            cur.next = node
            cur = node.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        cur, copyHead = head, head.next
        while cur:
            tmp = cur.next
            cur.next = tmp.next
            cur = cur.next
            if cur:
                tmp.next = cur.next

        return copyHead
