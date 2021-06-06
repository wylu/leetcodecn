#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   474.一和零.py
@Time    :   2021/06/06 09:27:08
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#
# https://leetcode-cn.com/problems/ones-and-zeroes/description/
#
# algorithms
# Medium (57.33%)
# Likes:    421
# Dislikes: 0
# Total Accepted:    44.6K
# Total Submissions: 77.8K
# Testcase Example:  '["10","0001","111001","1","0"]\n5\n3'
#
# 给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
#
#
# 请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。
#
# 如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。
#
#
#
#
# 示例 1：
#
#
# 输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
# 输出：4
# 解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
# 其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于
# n 的值 3 。
#
#
# 示例 2：
#
#
# 输入：strs = ["10", "0", "1"], m = 1, n = 1
# 输出：2
# 解释：最大的子集是 {"0", "1"} ，所以答案是 2 。
#
#
#
#
# 提示：
#
#
# 1 <= strs.length <= 600
# 1 <= strs[i].length <= 100
# strs[i] 仅由 '0' 和 '1' 组成
# 1 <= m, n <= 100
#
#
#
from typing import List
"""
（多维）01 背包
通常与「背包问题」相关的题考察的是 将原问题转换为「背包问题」的能力。

要将原问题转换为「背包问题」，往往需要从题目中抽象出「价值」与「成本」的概念。
这道题如果抽象成「背包问题」的话，应该是：

每个字符串的价值都是 1（对答案的贡献都是 1），选择的成本是该字符串中 1 的数量
和 0 的数量。问我们在 1 的数量不超过 m，0 的数量不超过 n 的条件下，最大价值
是多少。

由于每个字符串只能被选一次，且每个字符串的选与否对应了「价值」和「成本」，
求解的问题也是「最大价值」是多少。

因此可以直接套用 01 背包的「状态定义」来做：

f[k][i][j] 代表考虑前 k 件物品，在数字 1 容量不超过 i，数字 0 容量不超过 j
的条件下的「最大价值」（每个字符串的价值均为 1）。

有了「状态定义」之后，「转移方程」也很好推导：

f[k][i][j] = max(f[k - 1][i][j], f[k - 1][i - cnt[k][0]][j - cnt[k][1]] + 1)

其中 cnt 数组记录的是字符串中出现的 01 数量。
"""


# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        size = len(strs)
        f = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(size + 1)]

        def count(s: str):
            c1 = sum(1 for ch in s if ch == '1')
            return len(s) - c1, c1

        for k in range(1, size + 1):
            c0, c1 = count(strs[k - 1])

            for i in range(m + 1):
                for j in range(n + 1):
                    f[k][i][j] = f[k - 1][i][j]
                    if i >= c0 and j >= c1:
                        f[k][i][j] = max(f[k][i][j],
                                         f[k - 1][i - c0][j - c1] + 1)

        return f[size][m][n]


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=5, n=3))
    print(solu.findMaxForm(strs=["10", "0", "1"], m=1, n=1))
