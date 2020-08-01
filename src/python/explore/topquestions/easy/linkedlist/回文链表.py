#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   回文链表.py
@Time    :   2020/08/01 22:20:10
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
        if not head or not head.next:
            return True

        # 快慢指针寻找链表中点
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        l1, l2 = head, self.reverse(slow)
        while l1 != slow:
            if l1.val != l2.val:
                return False
            l1, l2 = l1.next, l2.next

        return True

    def reverse(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
