#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   803.打砖块.py
@Time    :   2021/01/16 22:06:38
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=803 lang=python3
#
# [803] 打砖块
#
# https://leetcode-cn.com/problems/bricks-falling-when-hit/description/
#
# algorithms
# Hard (47.07%)
# Likes:    155
# Dislikes: 0
# Total Accepted:    7.8K
# Total Submissions: 16.7K
# Testcase Example:  '[[1,0,0,0],[1,1,1,0]]\n[[1,0]]'
#
# 有一个 m x n 的二元网格，其中 1 表示砖块，0 表示空白。砖块 稳定（不会掉落）的前提是：
#
#
# 一块砖直接连接到网格的顶部，或者
# 至少有一块相邻（4 个方向之一）砖块 稳定 不会掉落时
#
#
# 给你一个数组 hits ，这是需要依次消除砖块的位置。每当消除 hits[i] = (rowi, coli)
# 位置上的砖块时，对应位置的砖块（若存在）会消失，然后其他的砖块可能因为这一消除操作而掉落。一旦砖块掉落，它会立即从网格中消失（即，它不会落在其他稳定的砖块上）。
#
# 返回一个数组 result ，其中 result[i] 表示第 i 次消除操作对应掉落的砖块数目。
#
# 注意，消除可能指向是没有砖块的空白位置，如果发生这种情况，则没有砖块掉落。
#
#
#
# 示例 1：
#
#
# 输入：grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
# 输出：[2]
# 解释：
# 网格开始为：
# [[1,0,0,0]，
# ⁠[1,1,1,0]]
# 消除 (1,0) 处加粗的砖块，得到网格：
# [[1,0,0,0]
# ⁠[0,1,1,0]]
# 两个加粗的砖不再稳定，因为它们不再与顶部相连，也不再与另一个稳定的砖相邻，因此它们将掉落。得到网格：
# [[1,0,0,0],
# ⁠[0,0,0,0]]
# 因此，结果为 [2] 。
#
#
# 示例 2：
#
#
# 输入：grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
# 输出：[0,0]
# 解释：
# 网格开始为：
# [[1,0,0,0],
# ⁠[1,1,0,0]]
# 消除 (1,1) 处加粗的砖块，得到网格：
# [[1,0,0,0],
# ⁠[1,0,0,0]]
# 剩下的砖都很稳定，所以不会掉落。网格保持不变：
# [[1,0,0,0],
# ⁠[1,0,0,0]]
# 接下来消除 (1,0) 处加粗的砖块，得到网格：
# [[1,0,0,0],
# ⁠[0,0,0,0]]
# 剩下的砖块仍然是稳定的，所以不会有砖块掉落。
# 因此，结果为 [0,0] 。
#
#
#
# 提示：
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# grid[i][j] 为 0 或 1
# 1 <= hits.length <= 4 * 10^4
# hits[i].length == 2
# 0 <= xi <= m - 1
# 0 <= yi <= n - 1
# 所有 (xi, yi) 互不相同
#
#
#
from copy import deepcopy
from typing import List
"""
方法一：逆序思维 + 并查集
思路

我们可以将问题抽象成一张图。每个网格上的砖块为图中的一个节点；如果某个
砖块的 4 个相邻位置中的一个位置有另外的砖块，就在相应的两个节点之间添加
一条边，以维护砖块之间的相邻关系。

根据题意，所有与网格顶部直接相邻的砖块都不会掉落。因此，可以抽象出一个
特殊的节点 X：任何与网格顶部直接相邻的砖块对应的节点，都与 X 有一条
直接相邻的边。

当消除一个砖块时，相当于从图中直接移除掉对应的节点，以及所有与它相邻
的边。如果在移除节点之后，某一节点 p 不再与 X 连通，则说明对应的砖块
「掉落」。于是，任意时刻留在网格中的砖块数量，就等于图中与 XX 连通的
节点数量。

第一眼看上去，读者不难想到利用并查集来维护节点的连通关系。然而，此问题
的难点在于，并查集只能支持对两个连通分支的合并，而无法将一个连通分支
拆成两个。

我们不妨从后向前考虑这一过程。初始时，图中具有多个独立的连通分支；每次
操作会在网格中添加一个砖块，于是在图中添加一个新的节点以及对应的边。
注意到这一操作可能会使得更多的节点与 X 相连，这些多出来的节点数量，
就为从前向后考虑问题时，该操作掉落的砖块数量。

算法细节

设矩阵为 h 行 w 列，则可以每个网格中的位置 (i,j) 映射成整数 i*w+j，
并为特殊节点 X 映射到整数 h*w。

我们首先正序遍历 hits 数组，得到 grid 经一系列操作后得到的状态 status，
在 status 中将每个被消除的位置（即 hits 的每个元素代表的位置）的值设为
0，并根据 status 的砖块情况构建初始并查集。

随后，我们逆序遍历 hits 数组中的每一项：

如果该位置在 grid 数组的取值为 0，说明此次操作根本没有消除砖块，因此
一定只消除了 0 个砖块。

否则，此次操作添加了一个新砖块。于是，我们首先统计与 X 相邻的节点数量
prev；随后，在将新节点与新边添加到并查集后，统计此时与 X 相邻的节点
数量 size。这就说明，该次操作消除的砖块数量为 max{0,size−prev−1}（注意
新添加的砖块本身不计入答案中）。最后，我们要更新网格的状态 status。

上面的操作要求我们在并查集中实时维护与 X 相邻的节点数目，因此在并查集的
代码中，除了父亲数组 f 外，还需要额外维护节点数量数组 sz，其中数组 sz[i]
的取值只有当 i 为某个连通分支的祖先时才有效，并代表着以 i 为祖先的连通
分支的节点数量。

每次在将两个不同分支的节点加入到并查集中时，需要同时更新 sz 中对应元素的
取值。具体而言，在合并两个节点 x,y 时，我们首先找出它们的祖先 fx, fy；
随后，如果要令 f[fx] = fy，则也要同步更新 sz[fy] += sz[fx]。

最后，注意到题目描述中约定「所有 (xi, yi) 互不相同」。稍加思考就会发现，
如果去除这条约定，那么在逆序遍历时遇到 hits 数组中的某一项时，即使 grid
数组中对应位置的元素为 1，我们也无法添加新的节点和新的边，因为该位置可能
会在此后（即正序考虑时的「此前」）才应当被添加到图中。

通过对这一问题的思考，读者应当能够对逆序思路有更加深刻的理解。
"""


# @lc code=start
class UnionFind:
    def __init__(self, n: int):
        self.par = list(range(n))
        self.sz = [1] * n

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> None:
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        self.par[fx] = fy
        self.sz[fy] += self.sz[fx]

    def count(self, x: int) -> int:
        return self.sz[self.find(x)]


class Solution:
    def hitBricks(self, grid: List[List[int]],
                  hits: List[List[int]]) -> List[int]:
        status = deepcopy(grid)
        for i, j in hits:
            status[i][j] = 0

        h, w = len(grid), len(grid[0])
        uf = UnionFind(h * w + 1)
        for i in range(h):
            for j in range(w):
                if status[i][j] == 0:
                    continue
                if i == 0:
                    uf.union(i * w + j, h * w)
                if i > 0 and status[i - 1][j] == 1:
                    uf.union(i * w + j, (i - 1) * w + j)
                if j > 0 and status[i][j - 1] == 1:
                    uf.union(i * w + j, i * w + j - 1)

        d = (0, 1, 0, -1, 0)
        n = len(hits)
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            r, c = hits[i]
            if grid[r][c] == 0:
                continue

            pre = uf.count(h * w)

            if r == 0:
                uf.union(c, h * w)

            for j in range(4):
                nr, nc = r + d[j], c + d[j + 1]
                if 0 <= nr < h and 0 <= nc < w and status[nr][nc] == 1:
                    uf.union(r * w + c, nr * w + nc)

            cur = uf.count(h * w)
            ans[i] = max(0, cur - pre - 1)
            status[r][c] = 1

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    grid = [[1, 0, 0, 0], [1, 1, 1, 0]]
    hits = [[1, 0]]
    print(solu.hitBricks(grid, hits))

    # grid = [[1, 0, 0, 0], [1, 1, 0, 0]]
    # hits = [[1, 1], [1, 0]]
    # print(solu.hitBricks(grid, hits))
