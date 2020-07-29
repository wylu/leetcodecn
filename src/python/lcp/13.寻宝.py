#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   13.寻宝.py
@Time    :   2020/07/29 21:23:47
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :   https://leetcode-cn.com/problems/xun-bao/
状态压缩动态规划

题意概述

一个人在迷宫中，要从起点 S 走到终点 T。迷宫有两类特殊点，分别是：

  - M：机关点，需要用石头触发
  - O：石头点，一次可以搬一块石头

只有当所有 M 点均被触发以后，终点才可到达，问起点走到终点的最小代价。

思路与算法

虽然迷宫有很多格子，但是我们实际上的走法只有几种：

  - 从 S 走到 O，我们不会从 S 直接走到 M，因为触发机关要先搬石头
  - 从 O 走到 M
  - 从 M 走到 O
  - 从 M 走到 T

有一点性质很重要，不论我们触发机关还是搬运石头，都不会改变迷宫的连通状态。
因此，两个点的最短距离一旦计算出，就不会再改变了。 于是第一步，我们可以
做一步预处理——我们计算所有特殊点（包括 M，O，S，T）互相之间的最短距离，
即对这里面的每个点做一次 BFS。这样我们就不需要考虑其他点了。为什么要预处理
出这些特殊点两两之间的距离，这个问题会在在下文中解释。

解决这个问题的关键是理解我们要以什么样的策略来取石头和触发机关：

  - 在最开始，我们一定会从 S，经过某一个 O，到达某一个 M。那么对于特定的
    M 来说，我们枚举 O 就可以计算 S−O−M 的最短距离。那么如果我们要从起点
    S 到达 M，一定会选择这条距离最短的路。这样，我们首先得到了 S 到每一个
    M 的最短距离。

  - 假定我们已经从起点到达了某个 M 了，接下来需要去其他的 O 点搬石头接着
    触发其他的机关，这是一个 M-O-M' 的路线。同样的道理，对于给定的 M'，
    中间的 O 也是固定的。即给定 M 和 M'，我们可以确定一个 O，使得 M-O-M'
    距离最短。我们同样可以记录下这个最短距离，即得到了所有 M 到 M' 的最短
    距离。

  - 最后，所有 M 到 T 的距离在前面已经计算出了。

我们需要所有的 M 都被触发，M 的触发顺序不同会导致行走的路径长度不同。假设
这里一共有 n 个 M，我们用 d(i,j) 表示第 i 个 M 到第 j 个 M 经过某一个 O
的最短距离。因为这里的 n 不大于 16，我们可以使用一个 16 位的二进制数表示
状态，这个二进制数的第 i 位为 1 表示第 i 个 M 已经触发，为 0 表示第 i 个
M 还未被触发，记这个二进制数为 mask。记 M[i] 为第 i 个 M（下标从 1 开始），
每一个 mask 都可以表示成两个集合，一个已触发集合、一个未触发集合，例如
n = 16，mask = 0000 1100 0001 0001 的已触发集合就可以表示为
T = {M[1], M[5], M[11], M[12]}，剩下的元素都在未触发集合 U-T 中。

我们定义 f(mask,i) 表示当前在第 i 个 M 处，触发状态为 mask 的最小步数，
如果当前 mask 代表的已触发集合为 T，未触发集合为 U−T，则我们可以推出这样
的动态规划转移方程：

f(mask,i) = min{f(mask xor 2^i, j) + d(j,i)}   (j 属于 T 且 j != i)

其中 mask xor 2^i 表示把 M[i] 从已触发的集合当中去掉，即 mask 这个状态
可以由 mask xor 2^i 状态转移得到，转移时我们除了关注触发状态 mask 的变化，
我们还关注是从哪一个 M 转移到了 M[i]，我们可以枚举 mask 当中已触发的所有的
M[j] (j != i) 作为上一个位置，而 d(j,i) 就是我们从 j 转移到 i 行走的最短
步数，我们可以在预处理之后按照我们的策略得到所有的 d(j,i)（如果 i,j 不可达
可以设为正无穷），然后 O(1) 查询，这就是预处理的目的。

实际上，在实现的时候，如果我们用记忆化搜索的方式实现，那么我们用到的是上面
的转移方程；如果我们使用循环实现的话，也可以使用下面的转移方程，写法类似递推：

f(mask|2^j,j) = min{f(mask,i) + d(i,j)}

本题边界情况较多，比如迷宫没有 M、M 不可达等。

题型小结
这道题是一个非常经典的状态压缩动态规划模型：有 n 个任务
{M[1], M[2], ..., M[n]}，每两个任务之间有一个 c(M[i], M[j]) 表示在 M[i]
之后（下一个）做 M[j] 的花费，让你求解把 n 个任务都做完需要的最小花费。通常
这个 n 会非常的小，因为需要构造 2^n 种状态，c(M[i], M[j]) 可能是题目给出，
也可能是可以在很短的时间内计算出来的一个值。这类问题的状态设计一般都是
f(mask,i) 表示当前任务完成的状态是 mask，当前位置是 i，考虑转移的时候我们
只需要考虑当前任务的上一个任务即可。可以使用记忆化搜索和循环两种方式实现。
"""
from queue import Queue
from typing import List


class Solution:
    def minimalSteps(self, maze: List[str]) -> int:
        m, n = len(maze), len(maze[0])
        sx, sy, tx, ty = -1, -1, -1, -1

        # 机关 & 石头
        buttons, stones = [], []

        # 记录所有特殊信息的位置
        for i in range(m):
            for j in range(n):
                if maze[i][j] == 'S':
                    sx, sy = i, j
                elif maze[i][j] == 'T':
                    tx, ty = i, j
                elif maze[i][j] == 'O':
                    stones.append((i, j))
                elif maze[i][j] == 'M':
                    buttons.append((i, j))

        s2a = self.bfs(maze, m, n, sx, sy)

        lm, lo = len(buttons), len(stones)

        # 若没有机关，最短距离就是(sx, sy) 到(tx, ty)的距离
        if lm == 0:
            return s2a[tx][ty]

        # 记录第 i 个机关到第 j 个机关的最短距离
        # dist[i][lm] 表示到起点的距离，dist[i][lm+1] 表示到终点的距离
        dist = [[-1] * (lm + 2) for _ in range(lm)]

        # 遍历所有机关，计算其和其他点的距离
        m2a = []
        for i in range(lm):
            mx, my = buttons[i]
            # 记录第 i 个机关到其他点的距离
            i2a = self.bfs(maze, m, n, mx, my)
            m2a.append(i2a)
            # 第 i 个机关到终点的距离就是 (mx, my) 到 (tx, ty)的距离
            dist[i][lm + 1] = i2a[tx][ty]

        for i in range(lm):
            # 计算第 i 个机关到 (sx, sy) 的距离
            # 即从第 i 个机关出发，通过每个石头 (ox, oy)，到 (sx, sy) 的最短距离
            tmp = -1
            for j in range(lo):
                ox, oy = stones[j]
                if m2a[i][ox][oy] != -1 and s2a[ox][oy] != -1:
                    if tmp == -1 or tmp > m2a[i][ox][oy] + s2a[ox][oy]:
                        tmp = m2a[i][ox][oy] + s2a[ox][oy]
            dist[i][lm] = tmp

            # 计算第 i 个机关到第 j 个机关的距离
            # 即从第 i 个机关出发，通过每个石头 (ox, oy)，到第 j 个机关的最短距离
            for j in range(i + 1, lm):
                tmp = -1
                for k in range(lo):
                    ox, oy = stones[k]
                    if m2a[i][ox][oy] != -1 and m2a[j][ox][oy] != -1:
                        if tmp == -1 or tmp > m2a[i][ox][oy] + m2a[j][ox][oy]:
                            tmp = m2a[i][ox][oy] + m2a[j][ox][oy]
                # 距离是无向图，对称的
                dist[i][j] = tmp
                dist[j][i] = tmp

        # 若有任意一个机关到起点或终点没有路径(即为-1)，则说明无法达成，返回-1
        for i in range(lm):
            if dist[i][lm] == -1 or dist[i][lm + 1] == -1:
                return -1

        # dp 数组，-1 代表没有遍历到, 1<<lm 表示题解中提到的 mask,
        # dp[mask][j] 表示当前处于第 j 个机关，总的触发状态为 mask 所需要的
        # 最短路径, 由于有 2^lm 个状态，因此 1<<lm 的开销必不可少
        dp = [[-1] * lm for _ in range(1 << lm)]
        # 初始状态，即从 start 到第 i 个机关，此时 mask 的第 i 位为1，其余位为0
        for i in range(lm):
            dp[1 << i][i] = dist[i][lm]

        # 二进制中数字大的 mask 的状态肯定比数字小的 mask 的状态多，所以直接
        # 从小到大遍历更新即可
        for mask in range(1, 1 << lm):
            for i in range(lm):
                # 若当前位置是正确的，即 mask 的第 i 位是 1
                if mask & (1 << i) != 0:
                    for j in range(lm):
                        # 选择下一个机关 j，要使得机关 j 目前没有到达，
                        # 即 mask 的第 j 位是 0
                        if mask & (1 << j) == 0:
                            nmk = mask | (1 << j)
                            if (dp[nmk][j] == -1
                                    or dp[nmk][j] > dp[mask][i] + dist[i][j]):
                                dp[nmk][j] = dp[mask][i] + dist[i][j]

        # 最后一个机关到终点
        ans = -1
        fmk = (1 << lm) - 1
        for i in range(lm):
            if ans == -1 or ans > dp[fmk][i] + dist[i][lm + 1]:
                ans = dp[fmk][i] + dist[i][lm + 1]

        return ans

    def bfs(self, maze: List[str], m: int, n: int, x: int,
            y: int) -> List[List[int]]:
        # 计算 (x,y) 到 maze 中其它点的距离
        dist = [[-1] * n for _ in range(m)]
        dist[x][y] = 0

        d = [0, 1, 0, -1, 0]

        q = Queue()
        q.put((x, y))
        while q.qsize():
            x, y = q.get()
            for i in range(4):
                nx, ny = x + d[i], y + d[i + 1]
                if (0 <= nx < m and 0 <= ny < n and maze[nx][ny] != '#'
                        and dist[nx][ny] == -1):
                    dist[nx][ny] = dist[x][y] + 1
                    q.put((nx, ny))

        return dist


if __name__ == '__main__':
    solu = Solution()
    print(solu.minimalSteps(["S#O", "M..", "M.T"]))
