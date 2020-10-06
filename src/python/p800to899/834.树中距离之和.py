#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   834.树中距离之和.py
@Time    :   2020/10/06 11:14:18
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=834 lang=python3
#
# [834] 树中距离之和
#
# https://leetcode-cn.com/problems/sum-of-distances-in-tree/description/
#
# algorithms
# Hard (35.87%)
# Likes:    132
# Dislikes: 0
# Total Accepted:    3.8K
# Total Submissions: 8.6K
# Testcase Example:  '6\n[[0,1],[0,2],[2,3],[2,4],[2,5]]'
#
# 给定一个无向、连通的树。树中有 N 个标记为 0...N-1 的节点以及 N-1 条边 。
#
# 第 i 条边连接节点 edges[i][0] 和 edges[i][1] 。
#
# 返回一个表示节点 i 与其他所有节点距离之和的列表 ans。
#
# 示例 1:
#
#
# 输入: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# 输出: [8,12,6,10,10,10]
# 解释:
# 如下为给定的树的示意图：
# ⁠  0
#  ⁠/ \
# 1   2
# ⁠   /|\
# ⁠  3 4 5
#
# 我们可以计算出 dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# 也就是 1 + 1 + 2 + 2 + 2 = 8。 因此，answer[0] = 8，以此类推。
#
#
# 说明: 1 <= N <= 10000
#
#
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def sumOfDistancesInTree(self, n: int,
                             edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(u: int, parent: int) -> None:
            for v in graph[u]:
                if v != parent:
                    dfs(v, u)
                    cnt[u] += cnt[v]
                    ans[u] += ans[v] + cnt[v]

        def dfs2(u: int, parent: int) -> None:
            for v in graph[u]:
                if v != parent:
                    ans[v] = ans[u] + (n - cnt[v]) - cnt[v]
                    dfs2(v, u)

        ans, cnt = [0] * n, [1] * n
        # 1.求出 ans[0] 并统计出每个子树的节点数目
        dfs(0, -1)
        # 2.根据公式和 ans[0] 计算其余结果
        dfs2(0, -1)

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
    print(solu.sumOfDistancesInTree(6, edges))
