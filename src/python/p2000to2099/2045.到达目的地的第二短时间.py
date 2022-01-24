#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2045.到达目的地的第二短时间.py
@Time    :   2022/01/24 22:32:12
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=2045 lang=python3
#
# [2045] 到达目的地的第二短时间
#
# https://leetcode-cn.com/problems/second-minimum-time-to-reach-destination/description/
#
# algorithms
# Hard (52.16%)
# Likes:    101
# Dislikes: 0
# Total Accepted:    11.8K
# Total Submissions: 22.6K
# Testcase Example:  '5\n[[1,2],[1,3],[1,4],[3,4],[4,5]]\n3\n5'
#
# 城市用一个 双向连通 图表示，图中有 n 个节点，从 1 到 n 编号（包含 1 和 n）。图中的边用一个二维整数数组 edges 表示，其中每个
# edges[i] = [ui, vi] 表示一条节点 ui 和节点 vi 之间的双向连通边。每组节点对由 最多一条
# 边连通，顶点不存在连接到自身的边。穿过任意一条边的时间是 time 分钟。
#
# 每个节点都有一个交通信号灯，每 change 分钟改变一次，从绿色变成红色，再由红色变成绿色，循环往复。所有信号灯都 同时 改变。你可以在 任何时候
# 进入某个节点，但是 只能 在节点 信号灯是绿色时 才能离开。如果信号灯是  绿色 ，你 不能 在节点等待，必须离开。
#
# 第二小的值 是 严格大于 最小值的所有值中最小的值。
#
#
# 例如，[2, 3, 4] 中第二小的值是 3 ，而 [2, 2, 4] 中第二小的值是 4 。
#
#
# 给你 n、edges、time 和 change ，返回从节点 1 到节点 n 需要的 第二短时间 。
#
# 注意：
#
#
# 你可以 任意次 穿过任意顶点，包括 1 和 n 。
# 你可以假设在 启程时 ，所有信号灯刚刚变成 绿色 。
#
#
#
#
# 示例 1：
#
# ⁠
#
#
# 输入：n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5
# 输出：13
# 解释：
# 上面的左图展现了给出的城市交通图。
# 右图中的蓝色路径是最短时间路径。
# 花费的时间是：
# - 从节点 1 开始，总花费时间=0
# - 1 -> 4：3 分钟，总花费时间=3
# - 4 -> 5：3 分钟，总花费时间=6
# 因此需要的最小时间是 6 分钟。
#
# 右图中的红色路径是第二短时间路径。
# - 从节点 1 开始，总花费时间=0
# - 1 -> 3：3 分钟，总花费时间=3
# - 3 -> 4：3 分钟，总花费时间=6
# - 在节点 4 等待 4 分钟，总花费时间=10
# - 4 -> 5：3 分钟，总花费时间=13
# 因此第二短时间是 13 分钟。
#
#
# 示例 2：
#
#
#
#
# 输入：n = 2, edges = [[1,2]], time = 3, change = 2
# 输出：11
# 解释：
# 最短时间路径是 1 -> 2 ，总花费时间 = 3 分钟
# 最短时间路径是 1 -> 2 -> 1 -> 2 ，总花费时间 = 11 分钟
#
#
#
# 提示：
#
#
# 2 <= n <= 10^4
# n - 1 <= edges.length <= min(2 * 10^4, n * (n - 1) / 2)
# edges[i].length == 2
# 1 <= ui, vi <= n
# ui != vi
# 不含重复边
# 每个节点都可以从其他节点直接或者间接到达
# 1 <= time, change <= 10^3
#
#
#
import heapq
from typing import List


# @lc code=start
class Solution:

    def secondMinimum(self, n: int, edges: List[List[int]], time: int,
                      change: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            u -= 1
            v -= 1
            graph[u].append(v)
            graph[v].append(u)

        dist1, dist2 = [0x7FFFFFFF] * n, [0x7FFFFFFF] * n
        # 最短路初始值为 0，次短路无穷大
        dist1[0] = 0
        q = [(0, 0)]

        while q:
            # 弹出最小值，或许是最短路，或许是次短路
            d1, u = heapq.heappop(q)
            # 弹出来的值比当前的次短路大，就可以跳过这个
            if dist2[u] < d1:
                continue

            a, b = divmod(d1, change)
            cost = time
            if a % 2 == 1:
                cost += change - b

            for v in graph[u]:
                # u 到 v 的花费
                d2 = d1 + cost
                # 花费小于原来的最小值，更新最短路
                if dist1[v] > d2:
                    dist1[v], d2 = d2, dist1[v]
                    heapq.heappush(q, (dist1[v], v))

                # 交换次短路（严格次短路，因此需要判断 dist1[v] < d2）
                if dist1[v] < d2 < dist2[v]:
                    dist2[v] = d2
                    heapq.heappush(q, (dist2[v], v))

        return dist2[n - 1]


# @lc code=end
