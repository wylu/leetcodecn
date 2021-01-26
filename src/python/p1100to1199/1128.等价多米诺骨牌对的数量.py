#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1128.等价多米诺骨牌对的数量.py
@Time    :   2021/01/26 09:40:35
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1128 lang=python3
#
# [1128] 等价多米诺骨牌对的数量
#
# https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs/description/
#
# algorithms
# Easy (47.08%)
# Likes:    58
# Dislikes: 0
# Total Accepted:    13.2K
# Total Submissions: 25.9K
# Testcase Example:  '[[1,2],[2,1],[3,4],[5,6]]'
#
# 给你一个由一些多米诺骨牌组成的列表 dominoes。
#
# 如果其中某一张多米诺骨牌可以通过旋转 0 度或 180 度得到另一张多米诺骨牌，我们就认为这两张牌是等价的。
#
# 形式上，dominoes[i] = [a, b] 和 dominoes[j] = [c, d] 等价的前提是 a==c 且 b==d，或是 a==d 且
# b==c。
#
# 在 0 <= i < j < dominoes.length 的前提下，找出满足 dominoes[i] 和 dominoes[j] 等价的骨牌对 (i,
# j) 的数量。
#
#
#
# 示例：
#
# 输入：dominoes = [[1,2],[2,1],[3,4],[5,6]]
# 输出：1
#
#
#
#
# 提示：
#
#
# 1 <= dominoes.length <= 40000
# 1 <= dominoes[i][j] <= 9
#
#
#
from typing import List
"""
方法一：二元组表示 + 计数
思路及解法

本题中我们需要统计所有等价的多米诺骨牌，其中多米诺骨牌使用二元对
代表，「等价」的定义是，在允许翻转两个二元对的的情况下，使它们的
元素一一对应相等。

于是我们不妨直接让每一个二元对都变为指定的格式，即第一维必须不大于
第二维。这样两个二元对「等价」当且仅当两个二元对完全相同。

注意到二元对中的元素均不大于 9，因此我们可以将每一个二元对拼接成
一个两位的正整数，即 (x,y) -> 10x + y。这样就无需使用哈希表统计
元素数量，而直接使用长度为 100 的数组即可。
"""


# @lc code=start
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt = [0] * 100
        ans = 0
        for x, y in dominoes:
            if x > y:
                x, y = y, x
            idx = x * 10 + y
            ans += cnt[idx]
            cnt[idx] += 1
        return ans


# @lc code=end

# class Solution:
#     def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
#         for domino in dominoes:
#             if domino[0] > domino[1]:
#                 domino[0], domino[1] = domino[1], domino[0]

#         dominoes.append([10, 10])  # 尾哨兵
#         dominoes.sort()

#         ans, j = 0, 0
#         for i in range(1, len(dominoes)):
#             if dominoes[i] == dominoes[j]:
#                 continue
#             if j + 1 != i:
#                 ans += (i - j) * (i - j - 1) // 2
#             j = i

#         return ans

if __name__ == "__main__":
    solu = Solution()
    print(solu.numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]))
