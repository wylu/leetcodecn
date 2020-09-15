#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   203.移除链表元素.py
@Time    :   2020/09/15 23:39:19
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#
# https://leetcode-cn.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (46.31%)
# Likes:    443
# Dislikes: 0
# Total Accepted:    102.2K
# Total Submissions: 220.7K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# 删除链表中等于给定值 val 的所有节点。
#
# 示例:
#
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5
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
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        pre, cur = dummy, head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = pre.next

        return dummy.next


# @lc code=end
