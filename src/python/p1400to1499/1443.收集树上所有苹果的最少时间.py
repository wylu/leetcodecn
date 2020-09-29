#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1443.收集树上所有苹果的最少时间.py
@Time    :   2020/09/29 11:19:37
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1443 lang=python3
#
# [1443] 收集树上所有苹果的最少时间
#
# https://leetcode-cn.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/
#
# algorithms
# Medium (41.94%)
# Likes:    28
# Dislikes: 0
# Total Accepted:    3.7K
# Total Submissions: 8.9K
# Testcase Example:  '7\n' +
# '[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]\n' +
# '[false,false,true,false,true,true,false]'
#
# 给你一棵有 n 个节点的无向树，节点编号为 0 到 n-1 ，它们中有一些节点有苹果。通过树上的一条边，需要花费 1 秒钟。你从 节点 0
# 出发，请你返回最少需要多少秒，可以收集到所有苹果，并回到节点 0 。
#
# 无向树的边由 edges 给出，其中 edges[i] = [fromi, toi] ，表示有一条边连接 fromi 和 toi
# 。除此以外，还有一个布尔数组 hasApple ，其中 hasApple[i] = true 代表节点 i 有一个苹果，否则，节点 i 没有苹果。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple =
# [false,false,true,false,true,true,false]
# 输出：8
# 解释：上图展示了给定的树，其中红色节点表示有苹果。一个能收集到所有苹果的最优方案由绿色箭头表示。
#
#
# 示例 2：
#
#
#
# 输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple =
# [false,false,true,false,false,true,false]
# 输出：6
# 解释：上图展示了给定的树，其中红色节点表示有苹果。一个能收集到所有苹果的最优方案由绿色箭头表示。
#
#
# 示例 3：
#
# 输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple =
# [false,false,false,false,false,false,false]
# 输出：0
#
#
#
#
# 提示：
#
#
# 1 <= n <= 10^5
# edges.length == n-1
# edges[i].length == 2
# 0 <= fromi, toi <= n-1
# fromi < toi
# hasApple.length == n
#
#
#
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def minTime(self, n: int, edges: List[List[int]],
                hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(u: int, parent: int) -> int:
            if not graph[u]:
                return 2 if hasApple[u] else 0
            ans = 0
            for v in graph[u]:
                if v != parent:
                    ans += dfs(v, u)
            if hasApple[u] or ans > 0:
                ans += 2
            return ans

        ans = dfs(0, -1)
        return 0 if ans == 0 else ans - 2


# @lc code=end

if __name__ == "__main__":
    n = 4
    edges = [[0, 2], [0, 3], [1, 2]]
    hasApple = [False, True, False, False]

    solu = Solution()
    print(solu.minTime(n, edges, hasApple))
