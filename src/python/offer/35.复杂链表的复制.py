#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   35.复杂链表的复制.py
@Time    :   2020/09/03 17:40:03
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
第一步根据原链表的每个结点 N 复制对应的 N'，把 N' 链接在 N 的后面，如：
原链表：Ａ -> B -> C -> D -> E
复制后：Ａ -> A' -> B -> B' -> C -> C' -> D -> D' -> E -> E'

第二步设置复制结点的 random 域，假设原链表的 N 的 random 指向 S，那么
其对应复制结点 N' 是 N 的 random 指向的结点，同样 S' 也是 S 的 random
指向的结点。

第三步将这个长链表拆分两个链表。
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return

        node = head
        while node:
            node.next = Node(node.val, node.next)
            node = node.next.next

        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next

        node, copy = head, head.next
        while node:
            tmp = node.next
            node.next = tmp.next
            if tmp.next:
                tmp.next = tmp.next.next
            node = node.next

        return copy
