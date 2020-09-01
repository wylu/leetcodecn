#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   59.螺旋矩阵-ii.py
@Time    :   2020/09/02 00:22:53
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
# https://leetcode-cn.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (78.04%)
# Likes:    229
# Dislikes: 0
# Total Accepted:    45.1K
# Total Submissions: 57.8K
# Testcase Example:  '3'
#
# 给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
#
# 示例:
#
# 输入: 3
# 输出:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
#
#
from typing import List


# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        cur = 1
        ans = [[0] * n for _ in range(n)]

        for s in range((n + 1) // 2):
            e = n - s

            for i in range(s, e):
                ans[s][i] = cur
                cur += 1

            for i in range(s + 1, e):
                ans[i][e - 1] = cur
                cur += 1

            for i in range(e - 2, s - 1, -1):
                ans[e - 1][i] = cur
                cur += 1

            for i in range(e - 2, s, -1):
                ans[i][s] = cur
                cur += 1

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.generateMatrix(3))
    print(solu.generateMatrix(4))
    print(solu.generateMatrix(5))
