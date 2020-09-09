#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   46.全排列.py
@Time    :   2020/09/09 09:54:03
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (76.78%)
# Likes:    875
# Dislikes: 0
# Total Accepted:    186.8K
# Total Submissions: 243.3K
# Testcase Example:  '[1,2,3]'
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
#
#
from typing import List


# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(c: int) -> None:
            if c == n:
                ans.append(nums[:])
                return
            for i in range(c, n):
                nums[c], nums[i] = nums[i], nums[c]
                dfs(c + 1)
                nums[c], nums[i] = nums[i], nums[c]

        ans, n = [], len(nums)
        dfs(0)
        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.permute([1, 2, 3]))
