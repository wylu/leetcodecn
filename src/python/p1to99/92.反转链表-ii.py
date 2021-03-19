#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   92.反转链表-ii.py
@Time    :   2021/03/18 20:15:54
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (52.74%)
# Likes:    800
# Dislikes: 0
# Total Accepted:    133K
# Total Submissions: 248.1K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left。请你反转从位置 left 到位置 right 的链表节点，返回
# 反转后的链表 。
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
#
#
# 示例 2：
#
#
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
#
#
#
#
# 提示：
#
#
# 链表中节点数目为 n
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
#
#
#
#
# 进阶： 你可以使用一趟扫描完成反转吗？
#
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
class Solution:
    def reverseBetween(self, head: ListNode, left: int,
                       right: int) -> ListNode:
        if right <= left:
            return head

        dummy = ListNode(next=head)
        mark1 = mark2 = None
        pre, cur = dummy, head
        i = 1
        while cur:
            if i <= left:
                if i == left:
                    mark1, mark2 = pre, cur
                pre, cur = cur, cur.next
            elif i == right:
                tmp = cur.next
                cur.next = pre
                mark1.next, mark2.next = cur, tmp
                break
            else:
                tmp = cur.next
                cur.next = pre
                pre, cur = cur, tmp

            i += 1

        return dummy.next


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    dummy = cur = ListNode()
    for val in (1, 2, 3, 4, 5):
        cur.next = ListNode(val)
        cur = cur.next
    solu.reverseBetween(dummy.next, 2, 4)

    dummy = cur = ListNode()
    for val in (3, 5):
        cur.next = ListNode(val)
        cur = cur.next
    solu.reverseBetween(dummy.next, 1, 1)
