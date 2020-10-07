#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   215.数组中的第k个最大元素.py
@Time    :   2020/10/07 23:23:04
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (64.37%)
# Likes:    732
# Dislikes: 0
# Total Accepted:    209.4K
# Total Submissions: 325.3K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 示例 1:
#
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
#
#
# 示例 2:
#
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
#
# 说明:
#
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
#
#
import heapq
from typing import List


# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            heapq.heappush(pq, num)
            if len(pq) > k:
                heapq.heappop(pq)
        return pq[0]


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.findKthLargest([3, 2, 1, 5, 6, 4], 2))
    print(solu.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
