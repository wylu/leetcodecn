#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   22.链表中倒数第k个节点.py
@Time    :   2020/08/24 19:30:27
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
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head or k <= 0:
            return

        # 1->2->3->4->5  k = 2
        slow, fast = head, head
        for _ in range(k):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        return slow
