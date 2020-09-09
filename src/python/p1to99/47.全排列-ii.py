#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   47.全排列-ii.py
@Time    :   2020/09/09 22:26:54
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (59.81%)
# Likes:    393
# Dislikes: 0
# Total Accepted:    87.4K
# Total Submissions: 146.1K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
# 示例:
#
# 输入: [1,1,2]
# 输出:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
#
#
from typing import List


# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        cnts = {}
        for num in nums:
            cnts[num] = cnts.get(num, 0) + 1

        ans, stack, n = [], [], len(nums)

        def dfs(c: int) -> None:
            if c == n:
                ans.append(stack[:])
                return
            for k, v in cnts.items():
                if v != 0:
                    cnts[k] -= 1
                    stack.append(k)
                    dfs(c + 1)
                    stack.pop()
                    cnts[k] += 1

        dfs(0)
        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.permuteUnique([1, 1, 2]))
    print(solu.permuteUnique([2, 2, 1, 1]))
