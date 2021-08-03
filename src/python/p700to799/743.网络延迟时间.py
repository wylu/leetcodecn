#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   743.网络延迟时间.py
@Time    :   2021/08/03 11:18:05
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=743 lang=python3
#
# [743] 网络延迟时间
#
# https://leetcode-cn.com/problems/network-delay-time/description/
#
# algorithms
# Medium (51.06%)
# Likes:    392
# Dislikes: 0
# Total Accepted:    48K
# Total Submissions: 94K
# Testcase Example:  '[[2,1,1],[2,3,1],[3,4,1]]\n4\n2'
#
# 有 n 个网络节点，标记为 1 到 n。
#
# 给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点，
# wi 是一个信号从源节点传递到目标节点的时间。
#
# 现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。
#
#
#
# 示例 1：
#
#
#
#
# 输入：times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# 输出：2
#
#
# 示例 2：
#
#
# 输入：times = [[1,2,1]], n = 2, k = 1
# 输出：1
#
#
# 示例 3：
#
#
# 输入：times = [[1,2,1]], n = 2, k = 2
# 输出：-1
#
#
#
#
# 提示：
#
#
# 1 <= k <= n <= 100
# 1 <= times.length <= 6000
# times[i].length == 3
# 1 <= ui, vi <= n
# ui != vi
# 0 <= wi <= 100
# 所有 (ui, vi) 对都 互不相同（即，不含重复边）
#
#
#
from typing import List


# @lc code=start
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = 0x7FFFFFFF // 2
        graph = [[INF] * n for _ in range(n)]
        for u, v, t in times:
            graph[u - 1][v - 1] = t

        dist = [INF] * n
        dist[k - 1] = 0

        used = [False] * n
        for _ in range(n):
            u = -1
            for v in range(n):
                if not used[v] and (u == -1 or dist[v] < dist[u]):
                    u = v

            used[u] = True
            for v in range(n):
                dist[v] = min(dist[v], dist[u] + graph[u][v])

        ans = max(dist)
        return -1 if ans == INF else ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    print(solu.networkDelayTime(times, n, k))

    times = [[1, 2, 1]]
    n = 2
    k = 1
    print(solu.networkDelayTime(times, n, k))

    times = [[1, 2, 1]]
    n = 2
    k = 2
    print(solu.networkDelayTime(times, n, k))
