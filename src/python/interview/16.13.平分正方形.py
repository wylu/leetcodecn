#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   16.13.平分正方形.py
@Time    :   2021/10/07 11:44:46
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :   https://leetcode-cn.com/problems/bisect-squares-lcci/
"""
from typing import List


class Solution:
    def cutSquares(self, square1: List[int],
                   square2: List[int]) -> List[float]:
        x1, y1 = square1[0] + square1[2] / 2, square1[1] + square1[2] / 2
        x2, y2 = square2[0] + square2[2] / 2, square2[1] + square2[2] / 2

        if x1 == x2:
            min_y = min(square1[1], square2[1])
            max_y = max(square1[1] + square1[2], square2[1] + square2[2])
            return [x1, min_y, x1, max_y]

        # Ax + By + C = 0
        # 两点代公式可得：
        # A*x1 + B*y1 = A*x2 + B*y2
        # A*(x1-x2) = B*(y2-y1)
        # 即 A = y2-y1, B = x1-x2
        # 故 C = x2*y1 - x1*y2

        ans = [0, 0, 0, 0]
        A, B, C = y2 - y1, x1 - x2, x2 * y1 - x1 * y2
        k = (y2 - y1) / (x2 - x1)
        if abs(k) > 1:
            # 斜率绝对值大于1，说明与正方形的上边和下边相交
            # 底边，也就是两个正方形左下坐标y的最小值
            ans[1] = min(square1[1], square2[1])
            ans[0] = (-C - B * ans[1]) / A
            # 顶边，也就是两个正方形左下坐标y+边长的最大值
            ans[3] = max(square1[1] + square1[2], square2[1] + square2[2])
            ans[2] = (-C - B * ans[3]) / A
        else:
            # 斜率绝对值小于等于1，说明与正方形的左边和右边相交
            # 左边
            ans[0] = min(square1[0], square2[0])
            ans[1] = (-C - A * ans[0]) / B
            # 右边
            ans[2] = max(square1[0] + square1[2], square2[0] + square2[2])
            ans[3] = (-C - A * ans[2]) / B

        # 题目要求 x1 < x2，如果结果不满足，我们交换两个点的坐标即可
        if ans[0] > ans[2]:
            ans[0], ans[2] = ans[2], ans[0]
            ans[1], ans[3] = ans[3], ans[1]

        return ans


if __name__ == '__main__':
    solu = Solution()
    square1 = [-1, -1, 2]
    square2 = [0, -1, 2]
    print(solu.cutSquares(square1, square2))

    square1 = [-1, 1, 5]
    square2 = [-2, -2, 7]
    print(solu.cutSquares(square1, square2))

    square1 = [-2, -2, 3]
    square2 = [0, 0, 4]
    print(solu.cutSquares(square1, square2))

    square1 = [68, 130, 64]
    square2 = [-230, 194, 7]
    print(solu.cutSquares(square1, square2))

# class Solution:
#     def cutSquares(self, square1: List[int],
#                    square2: List[int]) -> List[float]:
#         x1, y1 = square1[0] + square1[2] / 2, square1[1] + square1[2] / 2
#         x2, y2 = square2[0] + square2[2] / 2, square2[1] + square2[2] / 2

#         if x1 == x2:
#             min_y = min(square1[1], square2[1])
#             max_y = max(square1[1] + square1[2], square2[1] + square2[2])
#             return [x1, min_y, x1, max_y]

#         ans = [0, 0, 0, 0]
#         # 斜率存在，则计算斜率和系数，y = kx + b;
#         k = (y2 - y1) / (x2 - x1)
#         b = y1 - k * x1
#         if abs(k) > 1:
#             # 斜率绝对值大于1，说明与正方形的上边和下边相交
#             # 底边，也就是两个正方形左下坐标y的最小值
#             ans[1] = min(square1[1], square2[1])
#             ans[0] = (ans[1] - b) / k
#             # 顶边，也就是两个正方形左下坐标y+边长的最大值
#             ans[3] = max(square1[1] + square1[2], square2[1] + square2[2])
#             ans[2] = (ans[3] - b) / k
#         else:
#             # 斜率绝对值小于等于1，说明与正方形的左边和右边相交
#             # 左边
#             ans[0] = min(square1[0], square2[0])
#             ans[1] = ans[0] * k + b
#             # 右边
#             ans[2] = max(square1[0] + square1[2], square2[0] + square2[2])
#             ans[3] = ans[2] * k + b

#         # 题目要求 x1 < x2，如果结果不满足，我们交换两个点的坐标即可
#         if ans[0] > ans[2]:
#             ans[0], ans[2] = ans[2], ans[0]
#             ans[1], ans[3] = ans[3], ans[1]

#         return ans
