#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   216.组合总和-iii.py
@Time    :   2020/09/11 13:33:03
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#
# https://leetcode-cn.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (73.48%)
# Likes:    182
# Dislikes: 0
# Total Accepted:    42.2K
# Total Submissions: 57.4K
# Testcase Example:  '3\n7'
#
# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
#
# 说明：
#
#
# 所有数字都是正整数。
# 解集不能包含重复的组合。
#
#
# 示例 1:
#
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
#
#
# 示例 2:
#
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
#
#
#
from typing import List


# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k > 9 or n > 45:
            return []

        def dfs(c: int, k: int, n: int) -> None:
            if k == 0:
                if n == 0:
                    ans.append(stack[:])
                return
            for i in range(c, 10):
                if i <= n:
                    stack.append(i)
                    dfs(i + 1, k - 1, n - i)
                    stack.pop()

        ans, stack = [], []
        dfs(1, k, n)
        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.combinationSum3(3, 7))
    print(solu.combinationSum3(3, 9))
    print(solu.combinationSum3(25, 9))
