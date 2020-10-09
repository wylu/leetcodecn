#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   23.合并k个升序链表.py
@Time    :   2020/10/09 14:24:43
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (53.32%)
# Likes:    942
# Dislikes: 0
# Total Accepted:    176.6K
# Total Submissions: 331.2K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 给你一个链表数组，每个链表都已经按升序排列。
#
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
#
#
#
# 示例 1：
#
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
#
#
# 示例 2：
#
# 输入：lists = []
# 输出：[]
#
#
# 示例 3：
#
# 输入：lists = [[]]
# 输出：[]
#
#
#
#
# 提示：
#
#
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] 按 升序 排列
# lists[i].length 的总和不超过 10^4
#
#
#
import heapq
from typing import List
"""
使用优先队列合并

思路:

我们需要维护当前每个链表没有被合并的元素的最前面一个，k 个链表就最多有
k 个满足这样条件的元素，每次在这些元素里面选取 val 属性最小的元素合并
到答案中。在选取最小元素的时候，我们可以用优先队列来优化这个过程。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
class CmpNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pq = []
        for head in lists:
            if head:
                heapq.heappush(pq, CmpNode(head))

        dummy = ListNode(0)
        cur = dummy
        while pq:
            node = heapq.heappop(pq).node
            if node.next:
                heapq.heappush(pq, CmpNode(node.next))
            cur.next = node
            cur = cur.next

        cur.next = None
        return dummy.next


# @lc code=end
