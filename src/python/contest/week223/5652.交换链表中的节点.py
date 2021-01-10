#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5652.交换链表中的节点.py
@Time    :   2021/01/10 10:40:00
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        first, cur = dummy, head
        for i in range(k - 1):
            first = first.next
            cur = cur.next

        second = dummy
        while cur.next:
            second = second.next
            cur = cur.next

        if first == second:
            return dummy.next

        def insert(pos: ListNode, node: ListNode) -> None:
            tmp = pos.next
            pos.next = node
            node.next = tmp

        if first.next == second or second.next == first:
            if second.next == first:
                first, second = second, first
            rest1 = first.next
            first.next = second.next
            rest2 = second.next.next
            second.next.next = rest1
            rest1.next = rest2
        else:
            node1 = first.next
            first.next = node1.next
            node2 = second.next
            second.next = node2.next
            insert(first, node2)
            insert(second, node1)

        return dummy.next
