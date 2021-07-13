#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   218.天际线问题.py
@Time    :   2021/07/13 14:43:37
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=218 lang=python3
#
# [218] 天际线问题
#
# https://leetcode-cn.com/problems/the-skyline-problem/description/
#
# algorithms
# Hard (50.84%)
# Likes:    466
# Dislikes: 0
# Total Accepted:    21.3K
# Total Submissions: 41.8K
# Testcase Example:  '[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]'
#
# 城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回由这些建筑物形成的 天际线 。
#
# 每个建筑物的几何信息由数组 buildings 表示，其中三元组 buildings[i] = [lefti, righti, heighti]
# 表示：
#
#
# lefti 是第 i 座建筑物左边缘的 x 坐标。
# righti 是第 i 座建筑物右边缘的 x 坐标。
# heighti 是第 i 座建筑物的高度。
#
#
# 天际线 应该表示为由 “关键点” 组成的列表，格式 [[x1,y1],[x2,y2],...] ，并按 x 坐标 进行 排序
# 。关键点是水平线段的左端点。列表中最后一个点是最右侧建筑物的终点，y 坐标始终为 0
# ，仅用于标记天际线的终点。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。
#
# 注意：输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...]
# 是不正确的答案；三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]
#
#
#
# 示例 1：
#
#
# 输入：buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# 输出：[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
# 解释：
# 图 A 显示输入的所有建筑物的位置和高度，
# 图 B 显示由这些建筑物形成的天际线。图 B 中的红点表示输出列表中的关键点。
#
# 示例 2：
#
#
# 输入：buildings = [[0,2,3],[2,5,3]]
# 输出：[[0,3],[5,0]]
#
#
#
#
# 提示：
#
#
# 1 <= buildings.length <= 10^4
# 0 <= lefti < righti <= 2^31 - 1
# 1 <= heighti <= 2^31 - 1
# buildings 按 lefti 非递减排序
#
#
#
from typing import List
"""
方法一：扫描线 + 优先队列
思路及算法

题目要我们 输出每个矩形的“上边”的左端点，同时跳过可由前一矩形“上边”延展
而来的那些边。

因此我们需要实时维护一个最大高度，可以使用优先队列（堆）。

实现时，我们可以先记录下 buildings 中所有的左右端点横坐标及高度，并根据
端点横坐标进行从小到大排序。

在从前往后遍历处理时（遍历每个矩形），根据当前遍历到的点进行分情况讨论：

- 左端点：因为是左端点，必然存在一条从右延展的边，但不一定是需要被记录的边，
  因为在同一矩形中，我们只需要记录最上边的边。这时候可以将高度进行入队；
- 右端点：此时意味着之前某一条往右延展的线结束了，这时候需要将高度出队
  （代表这结束的线不被考虑）。

然后从优先队列中取出当前的最大高度，为了防止当前的线与前一矩形“上边”延展
而来的线重合，我们需要使用一个变量 prev 记录上一个记录的高度。
"""

# @lc code=start
from sortedcontainers import SortedList  # noqa E402


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # 预处理所有的点，为了方便排序，对于左端点，令高度为负；对于右端点令高度为正
        boundaries = []
        for left, right, height in buildings:
            boundaries.append((left, -height))
            boundaries.append((right, height))

        boundaries.sort()

        ans = []
        prev = 0
        pq = SortedList([prev])
        for x, h in boundaries:
            if h < 0:
                # 如果是左端点，说明存在一条往右延伸的可记录的边，将高度存入优先队列
                pq.add(-h)
            else:
                # 如果是右端点，说明这条边结束了，将当前高度从队列中移除
                pq.remove(h)

            # 取出最高高度，如果当前不与前一矩形“上边”延展而来的那些边重合，则可以被记录
            if pq[-1] != prev:
                ans.append([x, pq[-1]])
                prev = pq[-1]

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10],
                 [19, 24, 8]]
    print(solu.getSkyline(buildings))

    buildings = [[0, 2, 3], [2, 5, 3]]
    print(solu.getSkyline(buildings))
