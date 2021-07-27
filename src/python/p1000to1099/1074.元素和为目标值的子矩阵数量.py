#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1074.元素和为目标值的子矩阵数量.py
@Time    :   2021/05/29 18:47:17
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1074 lang=python3
#
# [1074] 元素和为目标值的子矩阵数量
#
# https://leetcode-cn.com/problems/number-of-submatrices-that-sum-to-target/description/
#
# algorithms
# Hard (63.95%)
# Likes:    137
# Dislikes: 0
# Total Accepted:    12K
# Total Submissions: 18.7K
# Testcase Example:  '[[0,1,0],[1,1,1],[0,1,0]]\n0'
#
# 给出矩阵 matrix 和目标值 target，返回元素总和等于目标值的非空子矩阵的数量。
#
# 子矩阵 x1, y1, x2, y2 是满足 x1  且 y1  的所有单元 matrix[x][y] 的集合。
#
# 如果 (x1, y1, x2, y2) 和 (x1', y1', x2', y2') 两个子矩阵中部分坐标不同（如：x1 !=
# x1'），那么这两个子矩阵也不同。
#
#
#
# 示例 1：
#
#
#
#
# 输入：matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
# 输出：4
# 解释：四个只含 0 的 1x1 子矩阵。
#
#
# 示例 2：
#
#
# 输入：matrix = [[1,-1],[-1,1]], target = 0
# 输出：5
# 解释：两个 1x2 子矩阵，加上两个 2x1 子矩阵，再加上一个 2x2 子矩阵。
#
#
# 示例 3：
#
#
# 输入：matrix = [[904]], target = 0
# 输出：0
#
#
#
#
# 提示：
#
#
# 1 <= matrix.length <= 100
# 1 <= matrix[0].length <= 100
# -1000 <= matrix[i] <= 1000
# -10^8 <= target <= 10^8
#
#
#
from collections import defaultdict
from typing import List
"""
朴素二维前缀和

从题面来看显然是一道「二维前缀和」的题目，如果你还不了解「二维前缀和」，可以
看看 （题解）304. 二维区域和检索 - 矩阵不可变。本题预处理前缀和的复杂度为
O(m * n)。

搜索所有子矩阵需要枚举「矩形左上角」和「矩形右下角」，复杂度是 O(m^2 * n^2)。

因此，如果把本题当做二维前缀和模板题来做的话，整体复杂度是 O(m^2 * n^2)。

数据范围是 10^2，对应的计算量是 10^8，处于超时边缘，但当我们枚举「矩阵右下角」
(i,j) 的时候，我们只需要搜索位于 (i,j) 的左上方的点 (p,q) 作为「矩阵左上角」，
所以其实我们是取不满 m^2 * n^2 的，但仍然具有超时风险（Java 测试可通过）。

优化枚举 + 哈希表

上述分析是从「点」上来确定一个子矩阵，在 n 和 m 同阶的情况下，复杂度是
O(n^4) 的。

事实上，我们能从「边」的角度来确定一个子矩阵，通过枚举三条边，然后加速找
第四条边的过程，这样可以将复杂度降到 O(n^3)。

这个分析思路在 （题解）363. 矩形区域不超过 K 的最大数值和 详细讲过，没有
印象的同学可以翻翻。这道题一定程度上是那道题的简化版，在本题我们只需要找到
矩阵和为 target 的值，因此只需要使用「哈希表」来记录出现过的值即可，而在
（原题）363. 矩形区域不超过 K 的最大数值和 中，我们需要找到和不超过 k 的
最大子矩阵，因此还涉及「有序集合 + 二分」。

具体的，我们仍然需要先预处理出一个二维前缀和。然后通过枚举确定「子矩阵的
上下边界」，在将「子矩阵右边界」不断右移的过程中，把「子矩阵右边界」到
「原矩阵左边界」行程的矩阵和存入哈希表（因为要统计数量，存储格式为
{"面积”:"出现次数"} ），然后通过容斥原理来找到目标的「子矩阵左边界」。

假设当前我们「子矩阵的上下边界」已经固定，当枚举到某个「子矩阵右边界」时，
我们先通过二维前缀和计算出「子矩阵右边界」和「原矩阵左边界」形成的矩阵和
cur，由于我们希望找到矩阵和为 target 的子矩阵，即希望找到一个「子矩阵
左边界」使得矩阵和满足要求，这等价于从「哈希表」中找到一个 x，使得
cur - x = target，这是一个 O(1) 操作。
"""


# @lc code=start
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]],
                              target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                ps[i][j] = (ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1] +
                            matrix[i - 1][j - 1])

        ans = 0
        for i in range(1, m + 1):
            for j in range(i, m + 1):
                seen = defaultdict(int)
                for r in range(1, n + 1):
                    cur = ps[j][r] - ps[i-1][r]
                    if cur == target:
                        ans += 1
                    ans += seen[cur - target]
                    seen[cur] += 1

        return ans


# @lc code=end

# 暴力（超时）
# class Solution:
#     def numSubmatrixSumTarget(self, matrix: List[List[int]],
#                               target: int) -> int:
#         m, n = len(matrix), len(matrix[0])
#         ps = [[0] * (n + 1) for _ in range(m + 1)]
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 ps[i][j] = (ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1] +
#                             matrix[i - 1][j - 1])

#         ans = 0
#         for x1 in range(1, m + 1):
#             for y1 in range(1, n + 1):
#                 for x2 in range(x1, m + 1):
#                     for y2 in range(y1, n + 1):
#                         tot = (ps[x2][y2] - ps[x2][y1 - 1] - ps[x1 - 1][y2] +
#                                ps[x1 - 1][y1 - 1])
#                         if tot == target:
#                             ans += 1

#         return ans

if __name__ == '__main__':
    solu = Solution()
    print(solu.numSubmatrixSumTarget([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0))
    print(solu.numSubmatrixSumTarget(matrix=[[1, -1], [-1, 1]], target=0))
    print(solu.numSubmatrixSumTarget(matrix=[[904]], target=0))
