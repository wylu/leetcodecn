#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   83.删除排序链表中的重复元素.py
@Time    :   2021/01/05 23:11:17
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (51.82%)
# Likes:    445
# Dislikes: 0
# Total Accepted:    170.5K
# Total Submissions: 329K
# Testcase Example:  '[1,1,2]'
#
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
#
# 示例 1:
#
# 输入: 1->1->2
# 输出: 1->2
#
#
# 示例 2:
#
# 输入: 1->1->2->3->3
# 输出: 1->2->3
#
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @lc code=start
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return

        pre, cur = head, head.next
        while cur:
            if cur.val != pre.val:
                pre.next = cur
                pre = cur
            cur = cur.next

        pre.next = None
        return head


# @lc code=end
