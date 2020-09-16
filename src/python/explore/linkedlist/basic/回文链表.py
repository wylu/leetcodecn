#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   回文链表.py
@Time    :   2020/09/16 08:44:09
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
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse(head: ListNode) -> ListNode:
            pre, cur = None, head
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        p1, p2 = head, reverse(slow)
        while p1 != slow:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True
