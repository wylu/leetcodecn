#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   85.最大矩形.py
@Time    :   2020/12/26 18:21:48
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#
# https://leetcode-cn.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (50.36%)
# Likes:    739
# Dislikes: 0
# Total Accepted:    56.9K
# Total Submissions: 113.1K
# Testcase Example:
# '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
#
#
# 示例 1：
#
#
# 输入：matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。
#
#
# 示例 2：
#
#
# 输入：matrix = []
# 输出：0
#
#
# 示例 3：
#
#
# 输入：matrix = [["0"]]
# 输出：0
#
#
# 示例 4：
#
#
# 输入：matrix = [["1"]]
# 输出：1
#
#
# 示例 5：
#
#
# 输入：matrix = [["0","0"]]
# 输出：0
#
#
#
#
# 提示：
#
#
# rows == matrix.length
# cols == matrix[0].length
# 0
# matrix[i][j] 为 '0' 或 '1'
#
#
#
from typing import List
"""
参考 84. 柱状图中最大的矩形
"""


# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights: List[int]) -> int:
            ans, stack = 0, [0]
            for i in range(1, len(heights)):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    ans = max(ans, h * w)
                stack.append(i)
            return ans

        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        ans, heights = 0, [0] * (n + 2)

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    heights[j + 1] = 0
                else:
                    heights[j + 1] += 1

            ans = max(ans, largestRectangleArea(heights))

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    print(solu.maximalRectangle(matrix))

    matrix = []
    print(solu.maximalRectangle(matrix))

    matrix = [["0"]]
    print(solu.maximalRectangle(matrix))

    matrix = [["1"]]
    print(solu.maximalRectangle(matrix))

    matrix = [["0", "0"]]
    print(solu.maximalRectangle(matrix))

    matrix = [["0", "1"], ["1", "0"]]
    print(solu.maximalRectangle(matrix))
