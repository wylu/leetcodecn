#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   54.螺旋矩阵.py
@Time    :   2020/08/31 23:14:41
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode-cn.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (41.07%)
# Likes:    473
# Dislikes: 0
# Total Accepted:    78.2K
# Total Submissions: 190.4K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
#
# 示例 1:
#
# 输入:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
#
#
# 示例 2:
#
# 输入:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#
from typing import List
"""
用一个循环来打印矩阵，每次打印矩阵中的一个圈。

分析循环结束的条件：

假设这个矩阵的行数是 rows，列数是 cols，打印第一圈的左上角的坐标为(0,0)，
第二圈的左上角的坐标是(1,1)，以此类推。

可以发现，左上角的坐标中行标和列标总是相同的，于是在矩阵中选取左上角为
(start,start)的一圈作为分析的目标。

对于一个 5x5 的矩阵而言，最后一圈只有一个数字，对应的坐标为(2,2)。可以发现
5>2x2。对于一个 6x6 的矩阵而言，最后一圈有4个数字，其左上角的坐标任然为
(2,2)。可以发现 6>2x2 依然成立。

于是可以得出，让循环继续的条件是 cols > startX*2 并且 rows > startY*2

循环打印时，需要注意一些比较特殊的矩阵，如： 2x3，3x1，1x2
"""


# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        ans = []
        s, n, m = 0, len(matrix), len(matrix[0])
        while s <= (n - 1) // 2 and s <= (m - 1) // 2:
            self.prt_circle(matrix, s, n, m, ans)
            s += 1
        return ans

    def prt_circle(self, matrix: List[List[int]], s: int, n: int, m: int,
                   ans: List[int]) -> None:
        ex, ey = n - s, m - s

        # 从左到右打印一行
        for i in range(s, ey):
            ans.append(matrix[s][i])

        if s < ex - 1:
            # 从上到下打印一列
            for i in range(s + 1, ex):
                ans.append(matrix[i][ey - 1])

            if s < ey - 1:
                # 从右到左打印一行
                for i in range(ey - 2, s - 1, -1):
                    ans.append(matrix[ex - 1][i])

                if s < ex - 2:
                    # 从下到上打印一列
                    for i in range(ex - 2, s, -1):
                        ans.append(matrix[i][s])


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
    print(
        solu.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],
                          [13, 14, 15, 16]]))
