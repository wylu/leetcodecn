#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   765.情侣牵手.py
@Time    :   2021/02/14 11:09:55
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=765 lang=python3
#
# [765] 情侣牵手
#
# https://leetcode-cn.com/problems/couples-holding-hands/description/
#
# algorithms
# Hard (62.92%)
# Likes:    159
# Dislikes: 0
# Total Accepted:    13.2K
# Total Submissions: 21K
# Testcase Example:  '[0,2,1,3]'
#
# N 对情侣坐在连续排列的 2N 个座位上，想要牵到对方的手。 计算最少交换座位的次数，以便每对情侣可以并肩坐在一起。
# 一次交换可选择任意两人，让他们站起来交换座位。
#
# 人和座位用 0 到 2N-1 的整数表示，情侣们按顺序编号，第一对是 (0, 1)，第二对是 (2, 3)，以此类推，最后一对是 (2N-2,
# 2N-1)。
#
# 这些情侣的初始座位  row[i] 是由最初始坐在第 i 个座位上的人决定的。
#
# 示例 1:
#
#
# 输入: row = [0, 2, 1, 3]
# 输出: 1
# 解释: 我们只需要交换row[1]和row[2]的位置即可。
#
#
# 示例 2:
#
#
# 输入: row = [3, 2, 0, 1]
# 输出: 0
# 解释: 无需交换座位，所有的情侣都已经可以手牵手了。
#
#
# 说明:
#
#
# len(row) 是偶数且数值在 [4, 60]范围内。
# 可以保证row 是序列 0...len(row)-1 的一个全排列。
#
#
#
from typing import List
"""
方法一：并查集
假定第一对情侣的男生与第二对情侣的女生坐在了一起，而第二对情侣的男生与
第三对情侣的女生坐在了一起。根据题意，要想让第二对情侣之间能够成功牵手，
要么交换第一对情侣的男生与第二对情侣的男生，要么交换第二对情侣的女生与
第三对情侣的女生。

既然存在这两种交换方式，那么有必要两种方式都考虑吗？答案是无需都考虑。
不难注意到，无论采用了两种交换方式中的哪一种，最后的结局都是「第二对情侣
坐在了一起，且第一对情侣的男生与第三对情侣的女生坐在了一起」，因此两种
交换方式是等价的。

因此，我们将 N 对情侣看做图中的 N 个节点；对于每对相邻的位置，如果是
第 i 对与第 j 对坐在了一起，则在 i 号节点与 j 号节点之间连接一条边，
代表需要交换这两对情侣的位置。

如果图中形成了一个大小为 k 的环：i->j->k->...->l->i，则我们沿着环
的方向，先交换 i,j 的位置，再交换 j,k 的位置，以此类推。在进行了 k-1
次交换后，这 k 对情侣就都能够彼此牵手了。

故我们只需要利用并查集求出图中的每个连通分量；对于每个连通分量而言，
其大小减 1 就是需要交换的次数。

最后在计算交换次数时实际可以进行一点小简化： 假定一共有x个连通分量，
每个分量大小（情侣对数）为 S0，S1，...，Sx-1，则交换次数为
(S0-1) + (S1-1) + ... + (Sx-1 - 1) = (S0+S1+...+Sx-1)-x = N - x。
其中 N 为总共的情侣对数。因此只要算出连通分量个数即可直接得出答案。
"""


# @lc code=start
class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.cnt = n

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> None:
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        self.par[fx] = fy
        self.cnt -= 1


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        uf = UnionFind(n // 2)
        for i in range(0, n, 2):
            uf.union(row[i] // 2, row[i + 1] // 2)
        return n // 2 - uf.cnt


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.minSwapsCouples([0, 2, 1, 3]))
    print(solu.minSwapsCouples([3, 2, 0, 1]))
