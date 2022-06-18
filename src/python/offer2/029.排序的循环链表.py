#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   029.排序的循环链表.py
@Time    :   2022/06/18 09:59:59
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


# Definition for a Node.
class Node:

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:

    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if not head:
            node.next = node
            return node

        if head.next == head:
            head.next = node
            node.next = head
            return head

        cur, nxt = head, head.next
        while nxt != head:
            if cur.val <= insertVal <= nxt.val:
                break
            if cur.val > nxt.val:
                if insertVal > cur.val or insertVal < nxt.val:
                    break
            cur = cur.next
            nxt = nxt.next

        cur.next = node
        node.next = nxt
        return head


# class Solution:

#     def insert(self, head: 'Node', insertVal: int) -> 'Node':
#         if not head:
#             head = Node(insertVal)
#             head.next = head
#             return head

#         cur, first, last = head, head, head
#         while cur.next != head:
#             cur = cur.next
#             if cur.val < first.val:
#                 first = cur
#             if cur.val > last.val:
#                 last = cur

#         cur = flag = first if insertVal > first.val else last
#         while cur.next.val < insertVal and cur.next != flag:
#             cur = cur.next

#         cur.next = Node(insertVal, cur.next)
#         return head
