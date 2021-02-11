#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   703.数据流中的第-k-大元素.py
@Time    :   2021/02/11 22:42:38
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第 K 大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/description/
#
# algorithms
# Easy (49.72%)
# Likes:    227
# Dislikes: 0
# Total Accepted:    44.5K
# Total Submissions: 89.5K
# Testcase Example:
# '["KthLargest","add","add","add","add","add"]\n'
# + '[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]'
#
# 设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。
#
# 请实现 KthLargest 类：
#
#
# KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
# int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。
#
#
#
#
# 示例：
#
#
# 输入：
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# 输出：
# [null, 4, 5, 5, 8, 8]
#
# 解释：
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // return 4
# kthLargest.add(5);   // return 5
# kthLargest.add(10);  // return 5
# kthLargest.add(9);   // return 8
# kthLargest.add(4);   // return 8
#
#
#
# 提示：
#
#
# 1 <= k <= 10^4
# 0 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# -10^4 <= val <= 10^4
# 最多调用 add 方法 10^4 次
# 题目数据保证，在查找第 k 大元素时，数组中至少有 k 个元素
#
#
#
import heapq
from typing import List
"""
方法一：优先队列
我们可以使用一个大小为 k 的优先队列来存储前 k 大的元素，其中优先队列
的队头为队列中最小的元素，也就是第 k 大的元素。

在单次插入的操作中，我们首先将元素 val 加入到优先队列中。如果此时优先
队列的大小大于 k，我们需要将优先队列的队头元素弹出，以保证优先队列的
大小为 k。
"""


# @lc code=start
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)
        if len(self.pq) > self.k:
            heapq.heappop(self.pq)
        return self.pq[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end
