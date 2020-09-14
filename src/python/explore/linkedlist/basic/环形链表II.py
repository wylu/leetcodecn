#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   环形链表II.py
@Time    :   2020/09/14 23:12:44
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
    def detectCycle(self, head: ListNode) -> ListNode:
        def hasCycle(head: ListNode) -> ListNode:
            if not head:
                return None

            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return slow

            return None

        fast = hasCycle(head)
        if not fast:
            return None

        slow = head
        while fast != slow:
            slow = slow.next
            fast = fast.next

        return slow
