#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   142.环形链表-ii.py
@Time    :   2020/09/14 23:46:48
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#
# https://leetcode-cn.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (51.76%)
# Likes:    623
# Dislikes: 0
# Total Accepted:    115.5K
# Total Submissions: 223K
# Testcase Example:  '[3,2,0,-4]\n1'
#
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
#
# 说明：不允许修改给定的链表。
#
#
#
# 示例 1：
#
# 输入：head = [3,2,0,-4], pos = 1
# 输出：tail connects to node index 1
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
#
#
#
# 示例 2：
#
# 输入：head = [1,2], pos = 0
# 输出：tail connects to node index 0
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
#
#
#
# 示例 3：
#
# 输入：head = [1], pos = -1
# 输出：no cycle
# 解释：链表中没有环。
#
#
#
#
#
#
# 进阶：
# 你是否可以不用额外空间解决此题？
#
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @lc code=start
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        def hasCycle(head: ListNode) -> ListNode:
            if not head:
                return None

            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return slow

            return None

        fast = hasCycle(head)
        if not fast:
            return None

        slow = head
        while fast != slow:
            slow = slow.next
            fast = fast.next

        return slow


# @lc code=end
