#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   862.和至少为-k-的最短子数组.py
@Time    :   2022/10/26 19:46:46
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
#
# @lc app=leetcode.cn id=862 lang=python3
#
# [862] 和至少为 K 的最短子数组
#
# https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/description/
#
# algorithms
# Hard (22.07%)
# Likes:    567
# Dislikes: 0
# Total Accepted:    37.3K
# Total Submissions: 151.9K
# Testcase Example:  '[1]\n1'
#
# 给你一个整数数组 nums 和一个整数 k ，找出 nums 中和至少为 k 的 最短非空子数组 ，并返回该子数组的长度。如果不存在这样的 子数组 ，返回
# -1 。
#
# 子数组 是数组中 连续 的一部分。
#
#
#
#
#
#
# 示例 1：
#
#
# 输入：nums = [1], k = 1
# 输出：1
#
#
# 示例 2：
#
#
# 输入：nums = [1,2], k = 4
# 输出：-1
#
#
# 示例 3：
#
#
# 输入：nums = [2,-1,2], k = 3
# 输出：3
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -10^5 <= nums[i] <= 10^5
# 1 <= k <= 10^9
#
#
#
from collections import deque
from itertools import accumulate
from typing import List


# @lc code=start
class Solution:

    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ans = 0x7FFFFFFF
        s = list(accumulate(nums, initial=0))
        q = deque()
        for i, cur in enumerate(s):
            while q and cur - s[q[0]] >= k:
                ans = min(ans, i - q.popleft())
            while q and s[q[-1]] >= cur:
                q.pop()
            q.append(i)
        return ans if ans < 0x7FFFFFFF else -1


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.shortestSubarray(nums=[1], k=1))
    print(solu.shortestSubarray(nums=[1, 2], k=4))
    print(solu.shortestSubarray(nums=[2, -1, 2], k=3))
    print(solu.shortestSubarray(nums=[84, -37, 32, 40, 95], k=167))
