#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   148.排序链表.py
@Time    :   2020/11/21 21:40:57
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# https://leetcode-cn.com/problems/sort-list/description/
#
# algorithms
# Medium (67.73%)
# Likes:    878
# Dislikes: 0
# Total Accepted:    118.4K
# Total Submissions: 174.8K
# Testcase Example:  '[4,2,1,3]'
#
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
#
# 进阶：
#
#
# 你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
#
#
#
#
# 示例 1：
#
#
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
#
#
# 示例 2：
#
#
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
#
#
# 示例 3：
#
#
# 输入：head = []
# 输出：[]
#
#
#
#
# 提示：
#
#
# 链表中节点的数目在范围 [0, 5 * 10^4] 内
# -10^5
#
#
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return self.mergeSort(head, None)

    def mergeSort(self, head: ListNode, tail: ListNode) -> ListNode:
        if not head:
            return head

        if head.next == tail:
            head.next = None
            return head

        slow = fast = head
        while fast != tail:
            slow = slow.next
            fast = fast.next
            if fast != tail:
                fast = fast.next

        h1 = self.mergeSort(head, slow)
        h2 = self.mergeSort(slow, tail)
        return self.merge(h1, h2)

    def merge(self, head1: ListNode, head2: ListNode) -> ListNode:
        dummy = ListNode(0)
        i, j, k = head1, head2, dummy

        while i and j:
            if i.val <= j.val:
                k.next = i
                i = i.next
            else:
                k.next = j
                j = j.next
            k = k.next

        if i:
            k.next = i

        if j:
            k.next = j

        return dummy.next


# @lc code=end

if __name__ == "__main__":
    from typing import List

    def mklist(*args: int) -> ListNode:
        dummy = cur = ListNode(0)
        for arg in args:
            cur.next = ListNode(arg)
            cur = cur.next
        return dummy.next

    def tolist(head: ListNode) -> List[int]:
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        return ans

    solu = Solution()

    def runCase(cid: str, *args: int) -> None:
        print(f'Case {cid}: ', end='')
        head = mklist(*args)
        print(tolist(head), end=' -> ')
        head = solu.sortList(head)
        print(tolist(head))

    runCase('1', 4, 2, 1, 3)
    runCase('2', -1, 5, 3, 4, 0)
    runCase('3')
    runCase('4', 1)
    runCase('5', 2, 1)
