#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   36.二叉搜索树与双向链表.py
@Time    :   2020/09/03 19:20:31
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return

        pre = None

        def inorder(cur: 'Node') -> None:
            nonlocal pre
            if not cur:
                return

            inorder(cur.left)
            if pre:
                pre.right = cur
                cur.left = pre
            pre = cur
            inorder(cur.right)

        inorder(root)

        head = pre
        while head.left:
            head = head.left

        pre.right = head
        head.left = pre

        return head
