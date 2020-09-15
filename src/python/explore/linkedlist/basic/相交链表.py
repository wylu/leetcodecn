#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   相交链表.py
@Time    :   2020/09/15 18:04:04
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
    def getIntersectionNode(self, ha: ListNode, hb: ListNode) -> ListNode:
        ca, cb = ha, hb
        while ca != cb:
            ca = ca.next if ca else hb
            cb = cb.next if cb else ha
        return ca
