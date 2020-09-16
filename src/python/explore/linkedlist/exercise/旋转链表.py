#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   旋转链表.py
@Time    :   2020/09/16 22:37:13
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return

        tail, cur, n = None, head, 0
        while cur:
            tail = cur
            cur = cur.next
            n += 1

        k %= n
        if k == 0:
            return head

        pre, cur = None, head
        for _ in range(n - k):
            pre = cur
            cur = cur.next

        pre.next = None
        tail.next = head
        return cur
