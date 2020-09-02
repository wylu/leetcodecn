#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   877.石子游戏.py
@Time    :   2020/09/02 21:28:03
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=877 lang=python3
#
# [877] 石子游戏
#
# https://leetcode-cn.com/problems/stone-game/description/
#
# algorithms
# Medium (71.01%)
# Likes:    180
# Dislikes: 0
# Total Accepted:    20.9K
# Total Submissions: 29.4K
# Testcase Example:  '[5,3,4,5]'
#
# 亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。
#
# 游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。
#
# 亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。
# 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。
#
# 假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false 。
#
#
#
# 示例：
#
# 输入：[5,3,4,5]
# 输出：true
# 解释：
# 亚历克斯先开始，只能拿前 5 颗或后 5 颗石子 。
# 假设他取了前 5 颗，这一行就变成了 [3,4,5] 。
# 如果李拿走前 3 颗，那么剩下的是 [4,5]，亚历克斯拿走后 5 颗赢得 10 分。
# 如果李拿走后 5 颗，那么剩下的是 [3,4]，亚历克斯拿走后 4 颗赢得 9 分。
# 这表明，取前 5 颗石子对亚历克斯来说是一个胜利的举动，所以我们返回 true 。
#
#
#
#
# 提示：
#
#
# 2 <= piles.length <= 500
# piles.length 是偶数。
# 1 <= piles[i] <= 500
# sum(piles) 是奇数。
#
#
#
from typing import List
"""
方法一：动态规划

dp[i][j]：表示当数组剩下的部分为下标 i 到下标 j 时，当前玩家与另一个玩家的石子数
          之差的最大值，注意当前玩家不一定是先手。

只有当 i <= j 时，数组剩下的部分才有意义，因此当 i > j 时，dp[i][j] = 0。

当 i = j 时，只剩一个数字，当前玩家只取走这堆石子，因此对于所有
0 <= i < len(piles)，都有 dp[i][i] = piles[i]。

当 i < j 时，当前玩家可以选择 piles[i] 或 piles[j]，然后轮到另一个玩家在数组
剩下的部分选取数字。在两种方案中，当前玩家会选择最优的方案，使得自己的石子数最大化。
因此可以得到如下状态转移方程：

dp[i][j] = max(piles[i] − dp[i+1][j], piles[j] − dp[i][j−1])

最后判断 dp[0][len(piles)−1] 的值，如果大于或等于 0，则先手得分大于或等于后手得分，
因此先手成为赢家，否则后手成为赢家。

方法二：数学

这道题是「486. 预测赢家」的特例。和第 486 题相比，这道题增加了两个限制条件：

  - 数组的长度是偶数；
  - 数组的元素之和是奇数，所以没有平局。

假设有 n 堆石子，n 是偶数，则每堆石子的下标从 0 到 n−1。根据下标将 n 堆
石子分成两组，每组有 n/2 堆石子，下标为偶数的石子堆属于第一组，下标为奇数
的石子堆属于第二组。

初始时，行的开始处的石子堆位于下标 0，属于第一组，行的结束处的石子堆位于
下标 n−1，属于第二组，因此作为先手的 Alex 可以自由选择取走第一组的一堆
石子或者第二组的一堆石子。如果 Alex 取走第一组的一堆石子，则剩下的部分在行
的开始处和结束处的石子堆都属于第二组，因此 Lee 只能取走第二组的一堆石子。
如果 Alex 取走第二组的一堆石子，则剩下的部分在行的开始处和结束处的石子堆
都属于第一组，因此 Lee 只能取走第一组的一堆石子。无论 Lee 取走的是开始处
还是结束处的一堆石子，剩下的部分在行的开始处和结束处的石子堆一定是属于
不同组的，因此轮到 Alex 取走石子时，Alex 又可以在两组石子之间进行自由选择。

根据上述分析可知，作为先手的 Alex 可以在第一次取走石子时就决定取走哪一组
的石子，并全程取走同一组的石子。既然如此，Alex 是否有必胜策略？

答案是肯定的。将石子分成两组之后，可以计算出每一组的石子数量，同时知道
哪一组的石子数量更多。Alex 只要选择取走数量更多的一组石子即可。因此，
Alex 总是可以赢得比赛。
"""


# @lc code=start
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True


# @lc code=end

# 方法一
# class Solution:
#     def stoneGame(self, piles: List[int]) -> bool:
#         n = len(piles)
#         dp = [[0] * n for _ in range(n)]

#         for i in range(n):
#             dp[i][i] = piles[i]

#         for i in range(n - 2, -1, -1):
#             for j in range(i + 1, n):
#                 dp[i][j] = max(piles[i] - dp[i + 1][j],
#                                piles[j] - dp[i][j - 1])

#         return dp[0][n - 1] > 0

# class Solution:
#     def stoneGame(self, piles: List[int]) -> bool:
#         def dfs(i: int, j: int) -> int:
#             if cache[i][j] != -1:
#                 return cache[i][j]
#             if i == j:
#                 return piles[i]
#             cache[i][j] = max(piles[i] - dfs(i + 1, j),
#                               piles[j] - dfs(i, j - 1))
#             return cache[i][j]

#         n = len(piles)
#         cache = [[-1] * n for _ in range(n)]
#         return dfs(0, n - 1) > 0

if __name__ == '__main__':
    solu = Solution()
    print(solu.stoneGame([5, 3, 4, 5]))
    print(solu.stoneGame([5, 6, 7, 5]))
