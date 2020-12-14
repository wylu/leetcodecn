#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1690.石子游戏-vii.py
@Time    :   2020/12/14 22:23:40
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1690 lang=python3
#
# [1690] 石子游戏 VII
#
# https://leetcode-cn.com/problems/stone-game-vii/description/
#
# algorithms
# Medium (42.18%)
# Likes:    23
# Dislikes: 0
# Total Accepted:    2K
# Total Submissions: 4.7K
# Testcase Example:  '[5,3,1,4,2]'
#
# 石子游戏中，爱丽丝和鲍勃轮流进行自己的回合，爱丽丝先开始 。
#
# 有 n 块石子排成一排。每个玩家的回合中，可以从行中 移除 最左边的石头或最右边的石头，并获得与该行中剩余石头值之 和
# 相等的得分。当没有石头可移除时，得分较高者获胜。
#
# 鲍勃发现他总是输掉游戏（可怜的鲍勃，他总是输），所以他决定尽力 减小得分的差值 。爱丽丝的目标是最大限度地 扩大得分的差值 。
#
# 给你一个整数数组 stones ，其中 stones[i] 表示 从左边开始 的第 i 个石头的值，如果爱丽丝和鲍勃都 发挥出最佳水平 ，请返回他们
# 得分的差值 。
#
#
#
# 示例 1：
#
#
# 输入：stones = [5,3,1,4,2]
# 输出：6
# 解释：
# - 爱丽丝移除 2 ，得分 5 + 3 + 1 + 4 = 13 。游戏情况：爱丽丝 = 13 ，鲍勃 = 0 ，石子 = [5,3,1,4] 。
# - 鲍勃移除 5 ，得分 3 + 1 + 4 = 8 。游戏情况：爱丽丝 = 13 ，鲍勃 = 8 ，石子 = [3,1,4] 。
# - 爱丽丝移除 3 ，得分 1 + 4 = 5 。游戏情况：爱丽丝 = 18 ，鲍勃 = 8 ，石子 = [1,4] 。
# - 鲍勃移除 1 ，得分 4 。游戏情况：爱丽丝 = 18 ，鲍勃 = 12 ，石子 = [4] 。
# - 爱丽丝移除 4 ，得分 0 。游戏情况：爱丽丝 = 18 ，鲍勃 = 12 ，石子 = [] 。
# 得分的差值 18 - 12 = 6 。
#
#
# 示例 2：
#
#
# 输入：stones = [7,90,5,1,100,10,10,2]
# 输出：122
#
#
#
# 提示：
#
#
# n == stones.length
# 2
# 1
#
#
#
from typing import List
"""
动态规划

dp[i][j]：表示当数组剩下的部分为下标 i 到下标 j 时，当前玩家与另一个
          玩家的分数之差的最大值，注意当前玩家不一定是先手。

只有当 i <= j 时，数组剩下的部分才有意义，因此当 i > j 时，dp[i][j] = 0

当 i = j 时，只剩一个数字，当前玩家只能拿取这个数字，因此对于所有
0 <= i < len(nums)，都有 dp[i][i] = 0。

当 i < j 时，当前玩家可以选择 nums[i] 或 nums[j]，然后轮到另一个玩家
在数组剩下的部分选取数字。在两种方案中，当前玩家会选择最优的方案，使得
自己的分数最大化。因此可以得到如下状态转移方程：

dp[i][j] = max(sum(nums[i+1], ..., nums[j]) − dp[i+1][j],
               sum(nums[i], ..., nums[j-1]) − dp[i][j−1])

最后结果为 dp[0][n-1]
"""


# @lc code=start
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [[0] * n for _ in range(n)]
        ps = [0] * (n + 1)

        for i in range(n):
            ps[i + 1] = stones[i] + ps[i]

        def get_sum(left: int, right: int) -> int:
            return ps[right + 1] - ps[left]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(
                    get_sum(i + 1, j) - dp[i + 1][j],
                    get_sum(i, j - 1) - dp[i][j - 1])

        return dp[0][n - 1]


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.stoneGameVII([5, 3, 1, 4, 2]))
    print(solu.stoneGameVII([7, 90, 5, 1, 100, 10, 10, 2]))
