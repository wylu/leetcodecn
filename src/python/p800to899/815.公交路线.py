#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   815.公交路线.py
@Time    :   2021/06/28 15:43:44
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=815 lang=python3
#
# [815] 公交路线
#
# https://leetcode-cn.com/problems/bus-routes/description/
#
# algorithms
# Hard (39.83%)
# Likes:    178
# Dislikes: 0
# Total Accepted:    16.4K
# Total Submissions: 41.3K
# Testcase Example:  '[[1,2,7],[3,6,7]]\n1\n6'
#
# 给你一个数组 routes ，表示一系列公交线路，其中每个 routes[i] 表示一条公交线路，第 i 辆公交车将会在上面循环行驶。
#
#
# 例如，路线 routes[0] = [1, 5, 7] 表示第 0 辆公交车会一直按序列 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1
# -> ... 这样的车站路线行驶。
#
#
# 现在从 source 车站出发（初始时不在公交车上），要前往 target 车站。 期间仅可乘坐公交车。
#
# 求出 最少乘坐的公交车数量 。如果不可能到达终点车站，返回 -1 。
#
#
#
# 示例 1：
#
#
# 输入：routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# 输出：2
# 解释：最优策略是先乘坐第一辆公交车到达车站 7 , 然后换乘第二辆公交车到车站 6 。
#
#
# 示例 2：
#
#
# 输入：routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
# 输出：-1
#
#
#
#
# 提示：
#
#
# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 10^5
# routes[i] 中的所有值 互不相同
# sum(routes[i].length) <= 10^5
# 0 <= routes[i][j] < 10^6
# 0 <= source, target < 10^6
#
#
#
from collections import defaultdict
from collections import deque
from typing import List


# @lc code=start
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int,
                              target: int) -> int:
        acceptable = set()

        station2route = defaultdict(set)
        for idx, route in enumerate(routes):
            for station in route:
                if station == target:
                    acceptable.add(idx)
                station2route[station].add(idx)

        graph = defaultdict(set)
        for u, route in enumerate(routes):
            for station in route:
                for v in station2route[station]:
                    if v != u:
                        graph[u].add(v)
                        graph[v].add(u)

        initial = list(station2route[source])
        if initial and source == target:
            return 0

        que = deque(initial)
        seen = set(initial)
        ans = 1

        while que:
            for _ in range(len(que)):
                u = que.popleft()
                if u in acceptable:
                    return ans

                for v in graph[u]:
                    if v not in seen:
                        que.append(v)
                        seen.add(v)

            ans += 1

        return -1


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    routes = [[1, 2, 7], [3, 6, 7]]
    source = 1
    target = 6
    print(solu.numBusesToDestination(routes, source, target))

    routes = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]]
    source = 15
    target = 12
    print(solu.numBusesToDestination(routes, source, target))

    routes = [[25, 33], [3, 5, 13, 22, 23, 29, 37, 45, 49], [15, 16, 41, 47],
              [5, 11, 17, 23, 33], [10, 11, 12, 29, 30, 39, 45],
              [2, 5, 23, 24, 33], [1, 2, 9, 19, 20, 21, 23, 32, 34, 44],
              [7, 18, 23, 24], [1, 2, 7, 27, 36, 44], [7, 14, 33]]
    source = 7
    target = 47
    print(solu.numBusesToDestination(routes, source, target))

    routes = [[1, 7], [3, 5]]
    source = 5
    target = 5
    print(solu.numBusesToDestination(routes, source, target))
