#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5927.反转偶数长度组的节点.py
@Time    :   2021/11/14 10:36:09
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseEvenLengthGroups(
            self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head: ListNode, tail: ListNode) -> None:
            pre, cur = None, head
            while cur != tail:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next

        size = 2
        pre, t = head, head.next
        while t:
            i = 1
            while i < size and t.next:
                i += 1
                t = t.next

            nxt = t.next
            h = t
            if i % 2 == 0:
                reverse(pre.next, t.next)
                h = pre.next
                pre.next.next = nxt
                pre.next = t

            size += 1
            pre = h
            t = nxt

        return head


if __name__ == '__main__':
    solu = Solution()

    def mklist(*args) -> ListNode:
        dummy = cur = ListNode(0)
        for val in args:
            node = ListNode(val)
            cur.next = node
            cur = cur.next
        return dummy.next

    def tolist(head: ListNode) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

    head = mklist(1, 1, 0, 6)
    head = solu.reverseEvenLengthGroups(head)
    res = tolist(head)
    print(res)

    head = mklist(5, 2, 6, 3, 9, 1, 7, 3, 8, 4)
    head = solu.reverseEvenLengthGroups(head)
    res = tolist(head)
    print(res)

    head = mklist(2, 1)
    head = solu.reverseEvenLengthGroups(head)
    res = tolist(head)
    print(res)

    head = mklist(8)
    head = solu.reverseEvenLengthGroups(head)
    res = tolist(head)
    print(res)

    head = mklist(1, 2, 3, 4, 5, 6, 7, 8)
    head = solu.reverseEvenLengthGroups(head)
    res = tolist(head)
    print(res)

    head = mklist(1, 2, 3, 4, 5, 6, 7, 8, 9)
    head = solu.reverseEvenLengthGroups(head)
    res = tolist(head)
    print(res)

    head = mklist(0, 4, 2, 1, 3)
    head = solu.reverseEvenLengthGroups(head)
    res = tolist(head)
    print(res)
