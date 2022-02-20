#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6013.合并零之间的节点.py
@Time    :   2022/02/20 10:34:34
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()

        while head.next:
            total = 0
            head = head.next
            while head.val:
                total += head.val
                head = head.next

            if total:
                cur.next = ListNode(val=total)
                cur = cur.next

        return dummy.next
