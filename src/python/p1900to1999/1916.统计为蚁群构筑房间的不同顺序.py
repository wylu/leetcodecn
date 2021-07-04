#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1916.统计为蚁群构筑房间的不同顺序.py
@Time    :   2021/07/04 20:34:25
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1916 lang=python3
#
# [1916] 统计为蚁群构筑房间的不同顺序
#
# https://leetcode-cn.com/problems/count-ways-to-build-rooms-in-an-ant-colony/description/
#
# algorithms
# Hard (55.22%)
# Likes:    17
# Dislikes: 0
# Total Accepted:    913
# Total Submissions: 1.7K
# Testcase Example:  '[-1,0,1]'
#
# 你是一只蚂蚁，负责为蚁群构筑 n 间编号从 0 到 n-1 的新房间。给你一个 下标从 0 开始 且长度为 n 的整数数组 prevRoom
# 作为扩建计划。其中，prevRoom[i] 表示在构筑房间 i 之前，你必须先构筑房间 prevRoom[i] ，并且这两个房间必须 直接 相连。房间 0
# 已经构筑完成，所以 prevRoom[0] = -1 。扩建计划中还有一条硬性要求，在完成所有房间的构筑之后，从房间 0 可以访问到每个房间。
#
# 你一次只能构筑 一个 房间。你可以在 已经构筑好的 房间之间自由穿行，只要这些房间是 相连的 。如果房间 prevRoom[i]
# 已经构筑完成，那么你就可以构筑房间 i。
#
# 返回你构筑所有房间的 不同顺序的数目 。由于答案可能很大，请返回对 10^9 + 7 取余 的结果。
#
#
#
# 示例 1：
#
#
# 输入：prevRoom = [-1,0,1]
# 输出：1
# 解释：仅有一种方案可以完成所有房间的构筑：0 → 1 → 2
#
#
# 示例 2：
#
#
#
# 输入：prevRoom = [-1,0,0,1,2]
# 输出：6
# 解释：
# 有 6 种不同顺序：
# 0 → 1 → 3 → 2 → 4
# 0 → 2 → 4 → 1 → 3
# 0 → 1 → 2 → 3 → 4
# 0 → 1 → 2 → 4 → 3
# 0 → 2 → 1 → 3 → 4
# 0 → 2 → 1 → 4 → 3
#
#
#
#
# 提示：
#
#
# n == prevRoom.length
# 2 <= n <= 10^5
# prevRoom[0] == -1
# 对于所有的 1 <= i < n ，都有 0 <= prevRoom[i] < n
# 题目保证所有房间都构筑完成后，从房间 0 可以访问到每个房间
#
#
#
from typing import List


# @lc code=start
class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(prevRoom)

        inv = [0] * (n + 1)
        fac = [0] * (n + 1)
        ifac = [0] * (n + 1)

        inv[0] = inv[1] = fac[0] = ifac[0] = 1
        for i in range(2, n + 1):
            inv[i] = (MOD - MOD // i) * inv[MOD % i] % MOD
        for i in range(1, n + 1):
            fac[i] = fac[i - 1] * i % MOD
            ifac[i] = ifac[i - 1] * inv[i] % MOD

        def combine(n: int, m: int) -> int:
            return fac[n] * ifac[m] % MOD * ifac[n - m] % MOD

        graph = [[] for _ in range(n + 1)]
        size = [0] * (n + 1)
        # dp[u]: 表示以 u 为根构建这个子树的方案数
        # dp[u] = all{dp[v] * 将子树构建序列组合起来的方案数}, v 是 u 的子树
        dp = [1] * (n + 1)
        for i in range(1, n):
            graph[prevRoom[i]].append(i)

        def dfs(u: int, fa: int) -> int:
            for v in graph[u]:
                dfs(v, u)
                dp[u] = dp[u] * dp[v] % MOD
                dp[u] = dp[u] * combine(size[u] + size[v], size[v]) % MOD
                size[u] += size[v]
            size[u] += 1
            return dp[u]

        return dfs(0, -1)


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.waysToBuildRooms(prevRoom=[-1, 0, 1]))
    print(solu.waysToBuildRooms(prevRoom=[-1, 0, 0, 1, 2]))
