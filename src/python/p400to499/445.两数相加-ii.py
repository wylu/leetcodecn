#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   445.两数相加-ii.py
@Time    :   2020/11/29 20:52:48
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#
# https://leetcode-cn.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (58.07%)
# Likes:    307
# Dislikes: 0
# Total Accepted:    56K
# Total Submissions: 96.5K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
#
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
#
#
#
# 进阶：
#
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
#
#
#
# 示例：
#
# 输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 8 -> 0 -> 7
#
#
#
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @lc code=start
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nums1, nums2 = [], []

        def fill(nums: List[int], head: ListNode) -> None:
            while head:
                nums.append(head.val)
                head = head.next

        fill(nums1, l1)
        fill(nums2, l2)

        ans, carry = None, 0
        while nums1 or nums2 or carry:
            if nums1:
                carry += nums1.pop()
            if nums2:
                carry += nums2.pop()
            node = ListNode(carry % 10)
            node.next = ans
            ans = node
            carry //= 10

        return ans


# @lc code=end
