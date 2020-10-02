#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   209.长度最小的子数组.py
@Time    :   2020/10/02 17:44:40
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (44.37%)
# Likes:    463
# Dislikes: 0
# Total Accepted:    90.5K
# Total Submissions: 203.9K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续
# 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
#
#
#
# 示例：
#
# 输入：s = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
#
#
#
#
# 进阶：
#
#
# 如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
#
#
#
from typing import List
"""
双指针
"""


# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        i, j, tot = 0, 0, 0

        while j < n:
            tot += nums[j]
            while tot >= s:
                ans = min(ans, j - i + 1)
                tot -= nums[i]
                i += 1
            j += 1

        return 0 if ans == n + 1 else ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
