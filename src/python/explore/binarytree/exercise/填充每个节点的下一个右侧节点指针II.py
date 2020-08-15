#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   填充每个节点的下一个右侧节点指针II.py
@Time    :   2020/08/15 19:09:52
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


# Definition for a Node.
class Node:
    def __init__(self,
                 val: int = 0,
                 left: 'Node' = None,
                 right: 'Node' = None,
                 next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        cur = root
        while cur:
            head, pre = None, None

            while cur:
                if cur.left:
                    if pre:
                        pre.next = cur.left
                    else:
                        head = cur.left
                    pre = cur.left

                if cur.right:
                    if pre:
                        pre.next = cur.right
                    else:
                        head = cur.right
                    pre = cur.right

                cur = cur.next

            cur = head

        return root
