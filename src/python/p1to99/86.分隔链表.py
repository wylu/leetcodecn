#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   86.分隔链表.py
@Time    :   2021/01/03 10:20:01
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#
# https://leetcode-cn.com/problems/partition-list/description/
#
# algorithms
# Medium (60.91%)
# Likes:    310
# Dislikes: 0
# Total Accepted:    66.5K
# Total Submissions: 109.2K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# 给你一个链表和一个特定值 x ，请你对链表进行分隔，使得所有小于 x 的节点都出现在大于或等于 x 的节点之前。
#
# 你应当保留两个分区中每个节点的初始相对位置。
#
#
#
# 示例：
#
#
# 输入：head = 1->4->3->2->5->2, x = 3
# 输出：1->2->2->4->3->5
#
#
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @lc code=start
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        h1, h2 = ListNode(0), ListNode(0)
        c1, c2 = h1, h2

        while head:
            if head.val < x:
                c1.next = head
                c1 = c1.next
            else:
                c2.next = head
                c2 = c2.next
            head = head.next

        c1.next = h2.next
        c2.next = None
        return h1.next


# @lc code=end
