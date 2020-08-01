#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   删除链表的倒数第N个节点.py
@Time    :   2020/08/01 21:55:18
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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or n <= 0:
            return

        # 添加头指针，避免过多判断
        dummy = ListNode(0)
        dummy.next = head

        slow, fast = dummy, head
        for _ in range(n):
            fast = fast.next

        while fast:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next
        return dummy.next
