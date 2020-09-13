#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1578.避免重复字母的最小删除成本.py
@Time    :   2020/09/13 20:25:00
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1578 lang=python3
#
# [1578] 避免重复字母的最小删除成本
#
# https://leetcode-cn.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/description/
#
# algorithms
# Medium (59.48%)
# Likes:    9
# Dislikes: 0
# Total Accepted:    3.7K
# Total Submissions: 6.2K
# Testcase Example:  '"abaac"\n[1,2,3,4,5]'
#
# 给你一个字符串 s 和一个整数数组 cost ，其中 cost[i] 是从 s 中删除字符 i 的代价。
#
# 返回使字符串任意相邻两个字母不相同的最小删除成本。
#
# 请注意，删除一个字符后，删除其他字符的成本不会改变。
#
#
#
# 示例 1：
#
#
# 输入：s = "abaac", cost = [1,2,3,4,5]
# 输出：3
# 解释：删除字母 "a" 的成本为 3，然后得到 "abac"（字符串中相邻两个字母不相同）。
#
#
# 示例 2：
#
#
# 输入：s = "abc", cost = [1,2,3]
# 输出：0
# 解释：无需删除任何字母，因为字符串中不存在相邻两个字母相同的情况。
#
#
# 示例 3：
#
#
# 输入：s = "aabaa", cost = [1,2,3,4,1]
# 输出：2
# 解释：删除第一个和最后一个字母，得到字符串 ("aba") 。
#
#
#
#
# 提示：
#
#
# s.length == cost.length
# 1 <= s.length, cost.length <= 10^5
# 1 <= cost[i] <= 10^4
# s 中只含有小写英文字母
#
#
#
from typing import List
"""
方法一：Dynamic Programming （超时）

State:
  dp[i][j]: 表示处理了原字符串的前 i 个字符（i 从 1 开始编号），并且【处理后的
            字符串】的最后一个字符为 j (j = 0 ... 25) 的最小删除成本。

State Trasition:
 （i 从 1 开始编号）
  dp[i][j] = dp[i-1][j] + cost[i-1]
  dp[i][s[i]] = min(dp[i-1][j != s[i]])

Initial State:
  dp[0][j] = 0

方法二：贪心

对字符串中每部分连续子串进行如下操作：
（1）获取删除该部分子串的总成本，记为 sum
（2）获取删除该部分子串中某个字符的最大成本，记为 max
（3）则避免重复的最小删除成本为 sum - max

将所有连续子串的最小删除成本加起来即为最终结果。
"""


# @lc code=start
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ans, n = 0, len(s)
        sm, mx = cost[0], cost[0]
        for i in range(1, n):
            if s[i] != s[i - 1]:
                ans += sm - mx
                sm = cost[i]
                mx = cost[i]
            else:
                sm += cost[i]
                mx = max(mx, cost[i])

        ans += sm - mx
        return ans


# @lc code=end

# class Solution:
#     def minCost(self, s: str, cost: List[int]) -> int:
#         n = len(s)
#         f = [[0] * 26 for _ in range(n + 1)]
#         for i in range(1, n + 1):
#             for j in range(26):
#                 f[i][j] = f[i - 1][j] + cost[i - 1]
#             t = ord(s[i - 1]) - ord('a')
#             for j in range(26):
#                 if j != t:
#                     f[i][t] = min(f[i][t], f[i - 1][j])
#         return min(f[n])

if __name__ == '__main__':
    solu = Solution()
    print(solu.minCost('abaac', [1, 2, 3, 4, 5]))
    print(solu.minCost('abc', [1, 2, 3]))
    print(solu.minCost('aabaa', [1, 2, 3, 4, 1]))
