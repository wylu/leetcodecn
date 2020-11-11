#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   514.自由之路.py
@Time    :   2020/11/11 22:10:18
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=514 lang=python3
#
# [514] 自由之路
#
# https://leetcode-cn.com/problems/freedom-trail/description/
#
# algorithms
# Hard (48.64%)
# Likes:    154
# Dislikes: 0
# Total Accepted:    12.9K
# Total Submissions: 26.6K
# Testcase Example:  '"godding"\n"gd"'
#
# 电子游戏“辐射4”中，任务“通向自由”要求玩家到达名为“Freedom Trail Ring”的金属表盘，并使用表盘拼写特定关键词才能开门。
#
# 给定一个字符串 ring，表示刻在外环上的编码；给定另一个字符串 key，表示需要拼写的关键词。您需要算出能够拼写关键词中所有字符的最少步数。
#
# 最初，ring 的第一个字符与12:00方向对齐。您需要顺时针或逆时针旋转 ring 以使 key 的一个字符在 12:00
# 方向对齐，然后按下中心按钮，以此逐个拼写完 key 中的所有字符。
#
# 旋转 ring 拼出 key 字符 key[i] 的阶段中：
#
#
# 您可以将 ring 顺时针或逆时针旋转一个位置，计为1步。旋转的最终目的是将字符串 ring 的一个字符与 12:00 方向对齐，并且这个字符必须等于字符
# key[i] 。
# 如果字符 key[i] 已经对齐到12:00方向，您需要按下中心按钮进行拼写，这也将算作 1 步。按完之后，您可以开始拼写 key
# 的下一个字符（下一阶段）, 直至完成所有拼写。
#
#
# 示例：
#
#
# 输入: ring = "godding", key = "gd"
# 输出: 4
# 解释:
# ⁠对于 key 的第一个字符 'g'，已经在正确的位置, 我们只需要1步来拼写这个字符。
# ⁠对于 key 的第二个字符 'd'，我们需要逆时针旋转 ring "godding" 2步使它变成 "ddinggo"。
# ⁠当然, 我们还需要1步进行拼写。
# ⁠因此最终的输出是 4。
#
#
# 提示：
#
#
# ring 和 key 的字符串长度取值范围均为 1 至 100；
# 两个字符串中都只有小写字符，并且均可能存在重复字符；
# 字符串 key 一定可以由字符串 ring 旋转拼出。
#
#
#
"""
方法一：动态规划

定义 dp[i][j] 表示从前往后拼写出 key 的第 i 个字符，ring 的第 j 个字符与
12:00 方向对齐的最少步数（下标均从 0 开始）。

显然，只有当字符串 ring 的第 j 个字符需要和 key 的第 i 个字符相同时才能
拼写出 key 的第 i 个字符，因此对于 key 的第 i 个字符，需要考虑计算的 ring
的第 j 个字符只有 key[i] 在 ring 中出现的下标集合。我们对每个字符维护一个
位置数组 pos[i]，表示字符 i 在 ring 中出现的位置集合，用来加速计算转移的
过程。

对于状态 dp[i][j]，需要枚举上一次与 12:00 方向对齐的位置 k，因此可以列出
如下的转移方程：
  k ∈ pos[key[i−1]]
  dp[i][j] = min{ dp[i−1][k] + min{abs(j−k), n−abs(j−k)} + 1 }

其中 min{abs(j−k), n−abs(j−k)} + 1 表示在当前第 k 个字符与 12:00 方向
对齐时第 j 个字符旋转到 12:00 方向并按下拼写的最少步数。

最后答案即为 min{dp[m−1][i]}, i ∈ [0,n-1]

这样的做法需要开辟 O(mn) 的空间来存放 dp 值。考虑到每次转移状态 dp[i][]
只会从 dp[i−1][] 转移过来，因此我们可以利用滚动数组优化第一维的空间复杂度，
有能力的读者可以尝试实现。下面只给出最朴素的 O(mn) 空间复杂度的实现。
"""


# @lc code=start
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        m, n = len(key), len(ring)
        pos = [[] for _ in range(26)]
        for i in range(n):
            pos[ord(ring[i]) - ord('a')].append(i)

        dp = [[0x80000000] * n for _ in range(m)]
        for i in pos[ord(key[0]) - ord('a')]:
            dp[0][i] = min(i, n - i) + 1

        for i in range(m):
            for j in pos[ord(key[i]) - ord('a')]:
                for k in pos[ord(key[i - 1]) - ord('a')]:
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i - 1][k] + min(abs(j - k), n - abs(j - k)) + 1)

        return min(dp[m - 1])


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.findRotateSteps("godding", "gd"))
