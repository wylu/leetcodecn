#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1447.最简分数.py
@Time    :   2022/02/10 09:17:07
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1447 lang=python3
#
# [1447] 最简分数
#
# https://leetcode-cn.com/problems/simplified-fractions/description/
#
# algorithms
# Medium (65.68%)
# Likes:    33
# Dislikes: 0
# Total Accepted:    11K
# Total Submissions: 16.8K
# Testcase Example:  '2'
#
# 给你一个整数 n ，请你返回所有 0 到 1 之间（不包括 0 和 1）满足分母小于等于  n 的 最简 分数 。分数可以以 任意 顺序返回。
#
#
#
# 示例 1：
#
# 输入：n = 2
# 输出：["1/2"]
# 解释："1/2" 是唯一一个分母小于等于 2 的最简分数。
#
# 示例 2：
#
# 输入：n = 3
# 输出：["1/2","1/3","2/3"]
#
#
# 示例 3：
#
# 输入：n = 4
# 输出：["1/2","1/3","1/4","2/3","3/4"]
# 解释："2/4" 不是最简分数，因为它可以化简为 "1/2" 。
#
# 示例 4：
#
# 输入：n = 1
# 输出：[]
#
#
#
#
# 提示：
#
#
# 1 <= n <= 100
#
#
#
import math
from typing import List


# @lc code=start
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []

        for i in range(1, n):
            for j in range(i + 1, n + 1):
                if math.gcd(i, j) == 1:
                    ans.append(f'{i}/{j}')

        return ans


# @lc code=end

# class Solution:
#     def simplifiedFractions(self, n: int) -> List[str]:
#         ans = []

#         def gcd(a: int, b: int) -> int:
#             if a < b:
#                 a, b = b, a
#             return gcd(b, a % b) if b else a

#         for i in range(1, n):
#             for j in range(i + 1, n + 1):
#                 if gcd(i, j) == 1:
#                     ans.append(f'{i}/{j}')

#         return ans

if __name__ == '__main__':
    solu = Solution()
    print(solu.simplifiedFractions(1))
    print(solu.simplifiedFractions(2))
    print(solu.simplifiedFractions(3))
    print(solu.simplifiedFractions(4))
