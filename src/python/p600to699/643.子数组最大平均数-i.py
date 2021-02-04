#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   643.子数组最大平均数-i.py
@Time    :   2021/02/04 21:55:44
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#
# https://leetcode-cn.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (44.95%)
# Likes:    160
# Dislikes: 0
# Total Accepted:    47.4K
# Total Submissions: 105.4K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
#
#
#
# 示例：
#
#
# 输入：[1,12,-5,-6,50,3], k = 4
# 输出：12.75
# 解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
#
#
#
#
# 提示：
#
#
# 1 <= k <= n <= 30,000。
# 所给数据范围 [-10,000，10,000]。
#
#
#
from typing import List


# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = tot = sum(nums[:k])

        for i in range(k, len(nums)):
            tot += nums[i] - nums[i - k]
            ans = max(ans, tot)

        return ans / k


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
