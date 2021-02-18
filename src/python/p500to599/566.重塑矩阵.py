#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   566.重塑矩阵.py
@Time    :   2021/02/17 10:45:02
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#
# https://leetcode-cn.com/problems/reshape-the-matrix/description/
#
# algorithms
# Easy (68.19%)
# Likes:    169
# Dislikes: 0
# Total Accepted:    33.8K
# Total Submissions: 49.5K
# Testcase Example:  '[[1,2],[3,4]]\n1\n4'
#
# 在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。
#
# 给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。
#
# 重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。
#
# 如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。
#
# 示例 1:
#
#
# 输入:
# nums =
# [[1,2],
# ⁠[3,4]]
# r = 1, c = 4
# 输出:
# [[1,2,3,4]]
# 解释:
# 行遍历nums的结果是 [1,2,3,4]。新的矩阵是 1 * 4 矩阵, 用之前的元素值一行一行填充新矩阵。
#
#
# 示例 2:
#
#
# 输入:
# nums =
# [[1,2],
# ⁠[3,4]]
# r = 2, c = 4
# 输出:
# [[1,2],
# ⁠[3,4]]
# 解释:
# 没有办法将 2 * 2 矩阵转化为 2 * 4 矩阵。 所以输出原矩阵。
#
#
# 注意：
#
#
# 给定矩阵的宽和高范围在 [1, 100]。
# 给定的 r 和 c 都是正数。
#
#
#
from typing import List


# @lc code=start
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int,
                      c: int) -> List[List[int]]:
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums

        ans = [[0] * c for _ in range(r)]
        for i in range(m * n):
            ans[i // c][i % c] = nums[i // n][i % n]
        return ans


# @lc code=end

# class Solution:
#     def matrixReshape(self, nums: List[List[int]], r: int,
#                       c: int) -> List[List[int]]:
#         m, n = len(nums), len(nums[0])
#         if m * n != r * c:
#             return nums

#         ans = [[]]
#         p = q = 0
#         for i in range(m):
#             for j in range(n):
#                 if q == c:
#                     ans.append([])
#                     q = 0
#                     p += 1

#                 ans[p].append(nums[i][j])
#                 q += 1

#         return ans

if __name__ == "__main__":
    solu = Solution()
    print(solu.matrixReshape(nums=[[1, 2], [3, 4]], r=1, c=4))
    print(solu.matrixReshape(nums=[[1, 2], [3, 4]], r=2, c=4))
