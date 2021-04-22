#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   363.矩形区域不超过-k-的最大数值和.py
@Time    :   2021/04/22 22:44:12
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=363 lang=python3
#
# [363] 矩形区域不超过 K 的最大数值和
#
# https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/description/
#
# algorithms
# Hard (47.96%)
# Likes:    295
# Dislikes: 0
# Total Accepted:    24.7K
# Total Submissions: 51.4K
# Testcase Example:  '[[1,0,1],[0,-2,3]]\n2'
#
# 给你一个 m x n 的矩阵 matrix 和一个整数 k ，找出并返回矩阵内部矩形区域的不超过 k 的最大数值和。
#
# 题目数据保证总会存在一个数值和不超过 k 的矩形区域。
#
#
#
# 示例 1：
#
#
# 输入：matrix = [[1,0,1],[0,-2,3]], k = 2
# 输出：2
# 解释：蓝色边框圈出来的矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
#
#
# 示例 2：
#
#
# 输入：matrix = [[2,2,-1]], k = 3
# 输出：3
#
#
#
#
# 提示：
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -100 <= matrix[i][j] <= 100
# -10^5 <= k <= 10^5
#
#
#
#
# 进阶：如果行数远大于列数，该如何设计解决方案？
#
#
from typing import List
"""
方法一：有序集合
思路

我们枚举矩形的上下边界，并计算出该边界内每列的元素和，则原问题转换成了如下
一维问题：

给定一个整数数组和一个整数 k，计算该数组的最大区间和，要求区间和不超过 k。

定义长度为 n 的数组 a 的前缀和

    S[i] = 0,                            i = 0
    S[i] = a[0] + a[1] + ... + a[i-1],   1 <= i <= n

则区间 [l,r) 的区间和 a[l] + a[l+1] + ... + a[r-1] 可以表示为 S[r]-S[l]。

枚举 r，上述问题的约束 S[r]-S[l] <= k 可以转换为 S[l] >= S[r]-k。要使
S[r]-S[l] 尽可能大，则需要寻找最小的满足 S[l] >= S[r]-k 的 S[l]。我们可以
在枚举 r 的同时维护一个存储 S[i] (i<r) 的有序集合，则可以在 O(logn) 的时间
内二分找到符合要求的 S[l]。
"""

# @lc code=start
from sortedcontainers import SortedList  # noqa E402


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ans = -0x80000000
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            arr = [0] * n
            for j in range(i, m):
                for c in range(n):
                    arr[c] += matrix[j][c]

                ss = SortedList([0])
                total = 0
                for val in arr:
                    total += val
                    idx = ss.bisect_left(total - k)
                    if idx != len(ss):
                        ans = max(ans, total - ss[idx])
                    ss.add(total)

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.maxSumSubmatrix(matrix=[[1, 0, 1], [0, -2, 3]], k=2))
    print(solu.maxSumSubmatrix(matrix=[[2, 2, -1]], k=3))

    matrix = [[5, -4, -3, 4], [-3, -4, 4, 5], [5, 1, 5, -4]]
    print(solu.maxSumSubmatrix(matrix, k=-2))
