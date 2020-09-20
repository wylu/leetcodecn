#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   78.子集.py
@Time    :   2020/09/20 15:52:21
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (78.53%)
# Likes:    786
# Dislikes: 0
# Total Accepted:    145.5K
# Total Submissions: 185K
# Testcase Example:  '[1,2,3]'
#
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: nums = [1,2,3]
# 输出:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
#
#
from typing import List


# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans, stack = [[]], []

        def dfs(c: int, t: int) -> None:
            if len(stack) == t:
                ans.append(stack[:])
                return
            for i in range(c, n):
                if n - i < t - len(stack):
                    continue
                stack.append(nums[i])
                dfs(i + 1, t)
                stack.pop()

        for i in range(1, n + 1):
            dfs(0, i)
        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.subsets([1, 2, 3]))
