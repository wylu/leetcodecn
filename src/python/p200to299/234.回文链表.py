#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   234.回文链表.py
@Time    :   2020/09/16 09:00:43
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# https://leetcode-cn.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (43.34%)
# Likes:    634
# Dislikes: 0
# Total Accepted:    127K
# Total Submissions: 293.1K
# Testcase Example:  '[1,2]'
#
# 请判断一个链表是否为回文链表。
#
# 示例 1:
#
# 输入: 1->2
# 输出: false
#
# 示例 2:
#
# 输入: 1->2->2->1
# 输出: true
#
#
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
#
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @lc code=start
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse(head: ListNode) -> ListNode:
            pre, cur = None, head
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        p1, p2 = head, reverse(slow)
        while p1 != slow:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True


# @lc code=end
