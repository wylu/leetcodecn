#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   879.盈利计划.py
@Time    :   2021/06/09 08:58:26
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=879 lang=python3
#
# [879] 盈利计划
#
# https://leetcode-cn.com/problems/profitable-schemes/description/
#
# algorithms
# Hard (44.97%)
# Likes:    93
# Dislikes: 0
# Total Accepted:    4.3K
# Total Submissions: 9.8K
# Testcase Example:  '5\n3\n[2,2]\n[2,3]'
#
# 集团里有 n 名员工，他们可以完成各种各样的工作创造利润。
#
# 第 i 种工作会产生 profit[i] 的利润，它要求 group[i] 名成员共同参与。如果成员参与了其中一项工作，就不能参与另一项工作。
#
# 工作的任何至少产生 minProfit 利润的子集称为 盈利计划 。并且工作的成员总数最多为 n 。
#
# 有多少种计划可以选择？因为答案很大，所以 返回结果模 10^9 + 7 的值。
#
#
#
#
#
# 示例 1：
#
#
# 输入：n = 5, minProfit = 3, group = [2,2], profit = [2,3]
# 输出：2
# 解释：至少产生 3 的利润，该集团可以完成工作 0 和工作 1 ，或仅完成工作 1 。
# 总的来说，有两种计划。
#
# 示例 2：
#
#
# 输入：n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
# 输出：7
# 解释：至少产生 5 的利润，只要完成其中一种工作就行，所以该集团可以完成任何工作。
# 有 7 种可能的计划：(0)，(1)，(2)，(0,1)，(0,2)，(1,2)，以及 (0,1,2) 。
#
#
#
#
#
# 提示：
#
#
# 1 <= n <= 100
# 0 <= minProfit <= 100
# 1 <= group.length <= 100
# 1 <= group[i] <= 100
# profit.length == group.length
# 0 <= profit[i] <= 100
#
#
#
from typing import List
"""
方法一：动态规划
本题与经典背包问题非常相似。两者不同点在于经典背包问题只有一种容量限制，
而本题却有两种限制：集团员工人数上限 n，以及工作产生的利润下限 minProfit。

通过经典背包问题的练习，我们已知经典背包问题可以使用二维动态规划求解：
两个维度分别代表物品和容量的限制标准。对于本题上述的两种限制，我们可以想到
使用三维动态规划求解。本题解法的三个维度分别为：当前可选择的工作，已选择的
小组员工人数，以及目前状态的工作获利下限。

根据上述分析，我们可以定义一个三维数组 dp 作为动态规划的状态，其中
dp[i][j][k] 表示在前 i 个工作中选择了 j 个员工，并且满足工作利润至少为 k
的情况下的盈利计划的总数目。假设 group 数组长度为 len，那么不考虑取模运算
的情况下，最终答案为：

   sum(dp[len][j][minProfit]),  0 <= j <= n

所以我们可以新建一个三维数组 dp[len+1][n+1][minProfit+1]，初始化
dp[0][0][0] = 1。接下来分析状态转移方程，对于每个工作 i，我们根据当前工作
人数上限 j，有能够开展当前工作和无法开展当前工作两种情况：

如果无法开展当前工作 i，那么显然：

  dp[i][j][k] = dp[i-1][j][k]

如果能够开展当前工作 i，设当前小组人数为 group[i]，工作获利为 profit[i]，
那么不考虑取模运算的情况下，则有：

  dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-group[i]][max(0,k-profit[i])]

由于我们定义的第三维是工作利润至少为 k 而不是 工作利润恰好为 k，因此上述
状态转移方程中右侧的第三维是 max(0, k-profit[i]) 而不是 k - profit[i]。
读者可以思考这一步的妙处所在。
"""


# @lc code=start
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int],
                          profit: List[int]) -> int:
        MOD = 10**9 + 7
        m = len(group)
        f = [[[0] * (minProfit + 1) for _ in range(n + 1)]
             for _ in range(m + 1)]
        f[0][0][0] = 1

        for i in range(1, m + 1):
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    f[i][j][k] = f[i - 1][j][k]
                    if j >= group[i - 1]:
                        earn = max(0, k - profit[i - 1])
                        f[i][j][k] += f[i - 1][j - group[i - 1]][earn]
                    f[i][j][k] %= MOD

        return sum(f[m][j][minProfit] for j in range(n + 1)) % MOD


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    n = 5
    minProfit = 3
    group = [2, 2]
    profit = [2, 3]
    print(solu.profitableSchemes(n, minProfit, group, profit))

    n = 10
    minProfit = 5
    group = [2, 3, 5]
    profit = [6, 7, 8]
    print(solu.profitableSchemes(n, minProfit, group, profit))
