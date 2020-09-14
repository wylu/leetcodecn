#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   环形链表.py
@Time    :   2020/09/14 22:40:49
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
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow, fast = head, head.next
        while fast and fast.next and fast != slow:
            fast = fast.next.next
            slow = slow.next

        return slow == fast
