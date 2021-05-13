#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1269.停在原地的方案数.py
@Time    :   2021/05/13 22:56:30
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1269 lang=python3
#
# [1269] 停在原地的方案数
#
# https://leetcode-cn.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/description/
#
# algorithms
# Hard (48.89%)
# Likes:    163
# Dislikes: 0
# Total Accepted:    24.6K
# Total Submissions: 50.4K
# Testcase Example:  '3\n2'
#
# 有一个长度为 arrLen 的数组，开始有一个指针在索引 0 处。
#
# 每一步操作中，你可以将指针向左或向右移动 1 步，或者停在原地（指针不能被移动到数组范围外）。
#
# 给你两个整数 steps 和 arrLen ，请你计算并返回：在恰好执行 steps 次操作以后，指针仍然指向索引 0 处的方案数。
#
# 由于答案可能会很大，请返回方案数 模 10^9 + 7 后的结果。
#
#
#
# 示例 1：
#
# 输入：steps = 3, arrLen = 2
# 输出：4
# 解释：3 步后，总共有 4 种不同的方法可以停在索引 0 处。
# 向右，向左，不动
# 不动，向右，向左
# 向右，不动，向左
# 不动，不动，不动
#
#
# 示例  2：
#
# 输入：steps = 2, arrLen = 4
# 输出：2
# 解释：2 步后，总共有 2 种不同的方法可以停在索引 0 处。
# 向右，向左
# 不动，不动
#
#
# 示例 3：
#
# 输入：steps = 4, arrLen = 2
# 输出：8
#
#
#
#
# 提示：
#
#
# 1 <= steps <= 500
# 1 <= arrLen <= 10^6
#
#
#
"""
方法一：动态规划
对于计算方案数的题目，常用的方法是动态规划。对于这道题，需要计算在 steps
步操作之后，指针位于下标 0 的方案数。

用 dp[i][j] 表示在 i 步操作之后，指针位于下标 j 的方案数。其中，i 的取值
范围是 0 <= i <= steps，j 的取值范围是 0 <= j <= arrLen-1。

由于一共执行 steps 步操作，因此指针所在下标一定不会超过 steps / 2 + 1，
可以将 j 的取值范围进一步缩小到 0 <= j <= min(arrLen-1, steps/2 + 1)。

当没有进行任何操作时，指针一定位于下标 0，因此动态规划的边界条件是
dp[0][0] = 1，当 0 <= j <= min(arrLen-1, steps/2 + 1) 时有 dp[0][j] = 0。

每一步操作中，指针可以向左或向右移动 1 步，或者停在原地。因此，
当 1 <= i <= steps 时，状态 dp[i][j] 可以从 dp[i-1][j-1]、dp[i-1][j]
和 dp[i-1][j+1] 这三个状态转移得到。状态转移方程如下：

    dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]

由于指针不能移动到数组范围外，因此对于上述状态转移方程，需要注意下标边界情况。
当 j=0 时，dp[i-1][j-1] = 0；当 j=min(arrLen-1, steps/2 + 1) 时，
dp[i-1][j+1] = 0。具体实现时，需要对下标进行判断，避免下标越界。

计算过程中需要对每个状态的值计算模 10^9 + 7 后的结果。最终得到 dp[steps][0]
的值即为答案。

上述实现的时间复杂度是 O(steps * min(arrLen, steps/2))，空间复杂度是
O(steps * min(arrLen, steps/2))。

注意到 dp 的每一行只和上一行有关，因此可以将空间复杂度降低到
O(min(arrLen, steps/2))。
"""


# @lc code=start
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        n = min(arrLen - 1, steps // 2 + 1)
        f = [[0] * (n + 2) for _ in range(steps + 1)]
        f[0][0] = 1

        for i in range(1, steps + 1):
            f[i][0] = (f[i - 1][0] + f[i - 1][1]) % MOD
            for j in range(1, n + 1):
                f[i][j] = (f[i - 1][j - 1] + f[i - 1][j] +
                           f[i - 1][j + 1]) % MOD

        return f[steps][0]


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.numWays(steps=3, arrLen=2))
    print(solu.numWays(steps=2, arrLen=4))
    print(solu.numWays(steps=4, arrLen=2))
