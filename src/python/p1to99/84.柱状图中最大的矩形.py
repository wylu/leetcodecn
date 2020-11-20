#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   84.柱状图中最大的矩形.py
@Time    :   2020/11/20 23:30:13
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (41.93%)
# Likes:    1022
# Dislikes: 0
# Total Accepted:    100.5K
# Total Submissions: 239.6K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
#
#
#
#
# 以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
#
#
#
#
#
# 图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
#
#
#
# 示例:
#
# 输入: [2,1,5,6,2,3]
# 输出: 10
#
#
from typing import List


# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        ans, stack, n = 0, [0], len(heights)

        for i in range(1, n):
            while heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.largestRectangleArea([2, 1, 5, 6, 2, 3]))
    print(solu.largestRectangleArea([1]))
    print(solu.largestRectangleArea([0]))
    print(solu.largestRectangleArea([2, 2]))
    print(solu.largestRectangleArea([2, 1, 2]))
    print(solu.largestRectangleArea([]))
    print(solu.largestRectangleArea([5, 4, 1, 2]))
    print(solu.largestRectangleArea([4, 2, 0, 3, 2, 5]))
