#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   486.预测赢家.py
@Time    :   2020/09/01 22:28:04
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=486 lang=python3
#
# [486] 预测赢家
#
# https://leetcode-cn.com/problems/predict-the-winner/description/
#
# algorithms
# Medium (57.73%)
# Likes:    301
# Dislikes: 0
# Total Accepted:    26K
# Total Submissions: 45.1K
# Testcase Example:  '[1,5,2]'
#
# 给定一个表示分数的非负整数数组。 玩家 1 从数组任意一端拿取一个分数，随后玩家 2 继续从剩余数组任意一端拿取分数，然后玩家 1 拿，……
# 。每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束。最终获得分数总和最多的玩家获胜。
#
# 给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。
#
#
#
# 示例 1：
#
# 输入：[1, 5, 2]
# 输出：False
# 解释：一开始，玩家1可以从1和2中进行选择。
# 如果他选择 2（或者 1 ），那么玩家 2 可以从 1（或者 2 ）和 5 中进行选择。如果玩家 2 选择了 5 ，那么玩家 1 则只剩下 1（或者 2
# ）可选。
# 所以，玩家 1 的最终分数为 1 + 2 = 3，而玩家 2 为 5 。
# 因此，玩家 1 永远不会成为赢家，返回 False 。
#
#
# 示例 2：
#
# 输入：[1, 5, 233, 7]
# 输出：True
# 解释：玩家 1 一开始选择 1 。然后玩家 2 必须从 5 和 7 中进行选择。无论玩家 2 选择了哪个，玩家 1 都可以选择 233 。
# ⁠    最终，玩家 1（234 分）比玩家 2（12 分）获得更多的分数，所以返回 True，表示玩家 1 可以成为赢家。
#
#
#
#
# 提示：
#
#
# 1 <= 给定的数组长度 <= 20.
# 数组里所有分数都为非负数且不会大于 10000000 。
# 如果最终两个玩家的分数相等，那么玩家 1 仍为赢家。
#
#
#
from typing import List
"""
方法一：记忆化递归

https://leetcode-cn.com/problems/predict-the-winner/solution/ling-he-bo-yi-ji-yi-hua-0ms-gao-ding-by-time-limit/

什么是零和博弈? 无论采取何种策略，博弈双方的总得分不变。即一个人得分变多，
另一个必然减少。在本题中，双方得分的总和即为 nums 的累加和。

在零和博弈中，让自己最优和让对手最差其实是相同的目标！不妨先转变一下思路，
把问题变为，先手如何让对手的最终得分最少。在零和博弈问题中，一般会存在
先手优势和后手劣势：

  先手优势：因为先手可以先走，所以可决定后手将要面对的局面。因此，后手
           虽然也会做出最优解，但是先手可以根据先发的优势，让后手进入
           最优解最差的局面。
  后手劣势：当先手走完后，虽然后手也会成为下一回合的先手，也可以做出
           最优解，但后手无法选择下一回合的局面。

所以一般零和博弈问题的关键都是要找出如何让后手陷入更差的局面的方法。

例如：

设 optimal(L, R) 为在 nums[L:R] 这种局面上，先手的最优得分。注意，这里的
先手抛开了自己或者对手的概念，先手就是指在这种局面上第一个出手的那个人！

当 L == R 时，因为只有一个数字，显然不需要做抉择了，optimal(L, R)
即为 nums[L]。

当 L < R 时，先手有两种选择：
  - 先手选择 nums[L], 让该回合的后手进入 optimal(L+1, R) 局面。
  - 先手选择 nums[R], 让该回合的后手进入 optimal(L, R-1) 局面。

后手在下一回合面临 optimal(L+1, R) 或者 optimal(L, R-1) 局面时，虽然
都能拿到最高分，但是该回合的先手却可以让对方进入最高分最低的那个局面！
这就是后手劣势。

那么最终，第一回合先手的最高得分是多少呢？显然为 optimal(0, len(nums)-1)，
假设下标从 0 开始。

那么如何计算 optimal(L, R) 呢？

当 L == R，optimal(L, R) 显然等于 nums[L]。
当 L < R 时，optimal(L, R) = sum(L, R) - min(optimal(L+1, R), optimal(L, R-1))

sum(L, R) 表示 nums[L:R] 的累加和，min() 表示让对手进入最高分最低的那个局面。

方法二：动态规划

dp[i][j]：表示当数组剩下的部分为下标 i 到下标 j 时，当前玩家与另一个玩家的分数之差
          的最大值，注意当前玩家不一定是先手。

只有当 i <= j 时，数组剩下的部分才有意义，因此当 i > j 时，dp[i][j] = 0。

当 i = j 时，只剩一个数字，当前玩家只能拿取这个数字，因此对于所有 0 <= i < len(nums)，
都有 dp[i][i] = nums[i]。

当 i < j 时，当前玩家可以选择 nums[i] 或 nums[j]，然后轮到另一个玩家在数组剩下的
部分选取数字。在两种方案中，当前玩家会选择最优的方案，使得自己的分数最大化。因此
可以得到如下状态转移方程：

dp[i][j] = max(nums[i] − dp[i+1][j], nums[j] − dp[i][j−1])

最后判断 dp[0][len(nums)−1] 的值，如果大于或等于 0，则先手得分大于或等于后手得分，
因此先手成为赢家，否则后手成为赢家。
"""


# @lc code=start
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

        return dp[0][n - 1] >= 0


# @lc code=end

# 方法一
# class Solution:
#     def PredictTheWinner(self, nums: List[int]) -> bool:
#         def dfs(l: int, r: int) -> int:  # noqa: E741
#             if dp[l][r] != -1:
#                 return dp[l][r]

#             if l == r:  # noqa: E741
#                 return nums[l]

#             dp[l][r] = ps[r + 1] - ps[l] - min(dfs(l + 1, r), dfs(l, r - 1))
#             return dp[l][r]

#         n = len(nums)
#         ps = [0]
#         for i in range(n):
#             ps.append(ps[i] + nums[i])

#         dp = [[-1] * n for _ in range(n)]
#         return dfs(0, n - 1) * 2 >= ps[n]

if __name__ == '__main__':
    solu = Solution()
    print(solu.PredictTheWinner([1, 5, 2]))
    print(solu.PredictTheWinner([1, 5, 233, 7]))
