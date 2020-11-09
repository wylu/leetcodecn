#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   973.最接近原点的-k-个点.py
@Time    :   2020/11/09 13:55:14
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=973 lang=python3
#
# [973] 最接近原点的 K 个点
#
# https://leetcode-cn.com/problems/k-closest-points-to-origin/description/
#
# algorithms
# Medium (58.82%)
# Likes:    166
# Dislikes: 0
# Total Accepted:    37K
# Total Submissions: 59.2K
# Testcase Example:  '[[1,3],[-2,2]]\n1'
#
# 我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。
#
# （这里，平面上两点之间的距离是欧几里德距离。）
#
# 你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。
#
#
#
# 示例 1：
#
# 输入：points = [[1,3],[-2,2]], K = 1
# 输出：[[-2,2]]
# 解释：
# (1, 3) 和原点之间的距离为 sqrt(10)，
# (-2, 2) 和原点之间的距离为 sqrt(8)，
# 由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
# 我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
#
#
# 示例 2：
#
# 输入：points = [[3,3],[5,-1],[-2,4]], K = 2
# 输出：[[3,3],[-2,4]]
# （答案 [[-2,4],[3,3]] 也会被接受。）
#
#
#
#
# 提示：
#
#
# 1 <= K <= points.length <= 10000
# -10000 < points[i][0] < 10000
# -10000 < points[i][1] < 10000
#
#
#
import heapq
from typing import List


# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for p in points:
            d = p[0] * p[0] + p[1] * p[1]
            heapq.heappush(pq, (-d, p))
            if len(pq) > k:
                heapq.heappop(pq)

        return [p for _, p in pq]


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.kClosest([[1, 3], [-2, 2]], 1))
    print(solu.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
