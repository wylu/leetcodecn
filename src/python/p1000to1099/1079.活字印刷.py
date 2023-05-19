#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1079.活字印刷.py
@Time    :   2023/05/19 23:53:47
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2023, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1079 lang=python3
#
# [1079] 活字印刷
#
# https://leetcode.cn/problems/letter-tile-possibilities/description/
#
# algorithms
# Medium (78.65%)
# Likes:    242
# Dislikes: 0
# Total Accepted:    30.2K
# Total Submissions: 38.4K
# Testcase Example:  '"AAB"'
#
# 你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。
#
# 注意：本题中，每个活字字模只能使用一次。
#
#
#
# 示例 1：
#
#
# 输入："AAB"
# 输出：8
# 解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。
#
#
# 示例 2：
#
#
# 输入："AAABBC"
# 输出：188
#
#
# 示例 3：
#
#
# 输入："V"
# 输出：1
#
#
#
# 提示：
#
#
# 1 <= tiles.length <= 7
# tiles 由大写英文字母组成
#
#
#
import math
from collections import Counter


# @lc code=start
class Solution:

    def numTilePossibilities(self, tiles: str) -> int:
        counts = Counter(tiles).values()
        n, m = len(tiles), len(counts)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        f[0][0] = 1
        for i, cnt in enumerate(counts, 1):
            for j in range(n + 1):
                for k in range(min(j, cnt) + 1):
                    f[i][j] += f[i - 1][j - k] * math.comb(j, k)
        return sum(f[m][1:])


# @lc code=end
