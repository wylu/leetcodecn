#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   53.最大子序和.py
@Time    :   2020/09/23 16:48:46
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (52.40%)
# Likes:    2461
# Dislikes: 0
# Total Accepted:    332.5K
# Total Submissions: 634.5K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#
#
# 进阶:
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
#
#
from typing import List


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, pre = -0x80000000, 0
        for num in nums:
            if pre > 0:
                pre += num
            else:
                pre = num
            ans = max(ans, pre)
        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(solu.maxSubArray([-1]))
