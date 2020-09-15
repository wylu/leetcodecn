#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   160.相交链表.py
@Time    :   2020/09/15 17:26:52
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#
# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (56.47%)
# Likes:    818
# Dislikes: 0
# Total Accepted:    149.3K
# Total Submissions: 264.4K
# Testcase Example:  '8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3'
#
# 编写一个程序，找到两个单链表相交的起始节点。
#
# 如下面的两个链表：
#
#
#
# 在节点 c1 开始相交。
#
#
#
# 示例 1：
#
#
#
# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2,
# skipB = 3
# 输出：Reference of the node with value = 8
# 输入解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为
# [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
#
#
#
#
# 示例 2：
#
#
#
# 输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB =
# 1
# 输出：Reference of the node with value = 2
# 输入解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为
# [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
#
#
#
#
# 示例 3：
#
#
#
# 输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# 输出：null
# 输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为
# 0，而 skipA 和 skipB 可以是任意值。
# 解释：这两个链表不相交，因此返回 null。
#
#
#
#
# 注意：
#
#
# 如果两个链表没有交点，返回 null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
#
#
#
"""
双指针法

创建两个指针 ca 和 cb，分别初始化为链表 A 和 B 的头结点。
然后让它们同时向后逐结点遍历。
当 ca 到达链表的尾部时，将它重定位到链表 B 的头结点；
当 cb 到达链表的尾部时，将它重定位到链表 A 的头结点；
若在某一时刻 ca 和 cb 相遇，则 ca/cb 为相交结点。

为什么这样可行, 可以这样思考:

设 a 为链表 A 独有的部分，b 为链表 B 独有的部分，all 为 A 和 B
共有的部分。则有：
  a + all + b = b + all + a

距离相同，速度相同，ca 和 cb 最终必定相遇与相交结点（如果存在，
否则 ca 和 cb 都同时第二次导致链表尾部）
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @lc code=start
class Solution:
    def getIntersectionNode(self, ha: ListNode, hb: ListNode) -> ListNode:
        ca, cb = ha, hb
        while ca != cb:
            ca = ca.next if ca else hb
            cb = cb.next if cb else ha
        return ca


# @lc code=end
