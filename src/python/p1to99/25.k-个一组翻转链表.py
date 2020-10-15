#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   25.k-个一组翻转链表.py
@Time    :   2020/10/15 19:43:35
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (63.31%)
# Likes:    769
# Dislikes: 0
# Total Accepted:    108.7K
# Total Submissions: 171.6K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。
#
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
#
#
# 示例：
#
# 给你这个链表：1->2->3->4->5
#
# 当 k = 2 时，应当返回: 2->1->4->3->5
#
# 当 k = 3 时，应当返回: 3->2->1->4->5
#
#
#
# 说明：
#
#
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(cur: ListNode) -> None:
            pre = None
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre

        dummy = ListNode(0)
        cur = dummy
        tail = head

        while tail:
            head, t = tail, k - 1
            while tail and t > 0:
                tail = tail.next
                t -= 1

            if tail:
                tmp = tail.next
                tail.next = None
                cur.next = reverse(head)
                cur = head
                tail = tmp
            else:
                cur.next = head

        return dummy.next


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
    res = solu.reverseKGroup(mklist([1, 2, 3, 4, 5]), 2)
    print(tolist(res))

    res = solu.reverseKGroup(mklist([1, 2, 3, 4, 5]), 1)
    print(tolist(res))

    res = solu.reverseKGroup(mklist([1]), 1)
    print(tolist(res))
