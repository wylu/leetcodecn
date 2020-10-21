#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   143.重排链表.py
@Time    :   2020/10/20 08:59:11
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
# https://leetcode-cn.com/problems/reorder-list/description/
#
# algorithms
# Medium (56.55%)
# Likes:    340
# Dislikes: 0
# Total Accepted:    43.4K
# Total Submissions: 76K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 示例 1:
#
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
#
# 示例 2:
#
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
#
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        i, j = 0, len(nodes) - 1
        dummy = ListNode(0)
        cur = dummy
        while i < j:
            cur.next = nodes[i]
            cur = cur.next
            i += 1
            cur.next = nodes[j]
            cur = cur.next
            j -= 1

        if i == j:
            cur.next = nodes[i]
            cur.next.next = None
        else:
            cur.next = None


# @lc code=end

if __name__ == "__main__":
    from typing import List

    def mklist(nums: List[int]) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        for num in nums:
            cur.next = ListNode(num)
            cur = cur.next
        return dummy.next

    def tolist(head: ListNode) -> List[int]:
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        return ans

    solu = Solution()
    head = mklist([1, 2, 3, 4])
    solu.reorderList(head)
    print(tolist(head))

    head = mklist([1, 2, 3, 4, 5])
    solu.reorderList(head)
    print(tolist(head))

    head = mklist([1])
    solu.reorderList(head)
    print(tolist(head))

    head = mklist([])
    solu.reorderList(head)
    print(tolist(head))
