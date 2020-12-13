#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5627.石子游戏VII.py
@Time    :   2020/12/13 22:59:17
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
动态规划

dp[i][j]：表示当数组剩下的部分为下标 i 到下标 j 时，当前玩家与另一个玩家的分数之差
          的最大值，注意当前玩家不一定是先手。

只有当 i <= j 时，数组剩下的部分才有意义，因此当 i > j 时，dp[i][j] = 0。

当 i = j 时，只剩一个数字，当前玩家只能拿取这个数字，因此对于所有 0 <= i < len(nums)，
都有 dp[i][i] = 0。

当 i < j 时，当前玩家可以选择 nums[i] 或 nums[j]，然后轮到另一个玩家在数组剩下的
部分选取数字。在两种方案中，当前玩家会选择最优的方案，使得自己的分数最大化。因此
可以得到如下状态转移方程：

dp[i][j] = max(sum(nums[i+1], ..., nums[j]) − dp[i+1][j],
               sum(nums[i], ..., nums[j-1]) − dp[i][j−1])

最后结果为 dp[0][n-1]
"""
from typing import List


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


# 超时
# class Solution:
#     def stoneGameVII(self, stones: List[int]) -> int:
#         n = len(stones)
#         ps = [0] * (n + 1)

#         for i in range(n):
#             ps[i + 1] = stones[i] + ps[i]

#         @lru_cache(None)
#         def dfs(l: int, r: int) -> int:  # noqa E741
#             if l == r:  # noqa E741
#                 return 0
#             return max(ps[r + 1] - ps[l + 1] - dfs(l + 1, r),
#                        ps[r] - ps[l] - dfs(l, r - 1))

#         return dfs(0, n - 1)

if __name__ == "__main__":
    solu = Solution()
    print(solu.stoneGameVII([5, 3, 1, 4, 2]))
    print(solu.stoneGameVII([7, 90, 5, 1, 100, 10, 10, 2]))
