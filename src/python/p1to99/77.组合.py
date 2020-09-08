#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   77.组合.py
@Time    :   2020/09/08 23:07:11
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (75.66%)
# Likes:    377
# Dislikes: 0
# Total Accepted:    97.7K
# Total Submissions: 129.1K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
# 示例:
#
# 输入: n = 4, k = 2
# 输出:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
#
#
from typing import List


# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n:
            return []

        def dfs(s: int, c: int) -> None:
            if c == k:
                ans.append(stack[:])
                return

            for i in range(s, n + 1):
                if n - i >= k - c - 1:
                    stack.append(i)
                    dfs(i + 1, c + 1)
                    stack.pop()

        ans, stack = [], []
        dfs(1, 0)
        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.combine(4, 2))
