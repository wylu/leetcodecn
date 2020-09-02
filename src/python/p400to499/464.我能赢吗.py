#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   464.我能赢吗.py
@Time    :   2020/09/02 10:55:14
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=464 lang=python3
#
# [464] 我能赢吗
#
# https://leetcode-cn.com/problems/can-i-win/description/
#
# algorithms
# Medium (34.30%)
# Likes:    160
# Dislikes: 0
# Total Accepted:    6.4K
# Total Submissions: 18.5K
# Testcase Example:  '10\n11'
#
# 在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和达到或超过 100 的玩家，即为胜者。
#
# 如果我们将游戏规则改为 “玩家不能重复使用整数” 呢？
#
# 例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。
#
# 给定一个整数 maxChoosableInteger （整数池中可选择的最大数）和另一个整数
# desiredTotal（累计和），判断先出手的玩家是否能稳赢（假设两位玩家游戏时都表现最佳）？
#
# 你可以假设 maxChoosableInteger 不会大于 20， desiredTotal 不会大于 300。
#
# 示例：
#
# 输入：
# maxChoosableInteger = 10
# desiredTotal = 11
#
# 输出：
# false
#
# 解释：
# 无论第一个玩家选择哪个整数，他都会失败。
# 第一个玩家可以选择从 1 到 10 的整数。
# 如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
# 第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
# 同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。
#
#
#
"""
方法一：记忆化回溯（也称为递归+备忘录），自顶向下

采用记忆化后的时间复杂度为 O(2^n) (若不进行记忆，时间复杂度将是O(n!))

例如，已选择 [2,3] 或 [3,2] 后玩家的状态是一样的，都是可以从除了 2,3
之外的数字进行选择，那么就可以对选择 2 和 3 后第一个玩家能不能赢进行
记忆存储。

这里采用 state[] 数组存储每个数字是否都被选过，选过则记录为 '1'，然后将
state 转成字符串，使得已选择 [2,3] 或 [3,2] 后它们的状态都是 "0011"，
将其作为 key，存储在字典中，value 是选了 2 和 3 后第一个玩家是否稳赢。

方法二：状态压缩 DP
"""


# @lc code=start
class Solution:
    def canIWin(self, maxChoosableInt: int, desiredTotal: int) -> bool:
        def dfs(state: int, total: int) -> bool:
            if cache[state] != -1:
                return cache[state]

            for i in range(1, maxChoosableInt + 1):
                j = (1 << (i - 1))
                if state & j != 0:
                    continue

                if total - i <= 0 or not dfs(state | j, total - i):
                    cache[state] = True
                    return True

            cache[state] = False
            return False

        if maxChoosableInt >= desiredTotal:
            return True

        if (1 + maxChoosableInt) * maxChoosableInt // 2 < desiredTotal:
            return False

        cache = [-1] * ((1 << maxChoosableInt) - 1)
        return dfs(0, desiredTotal)


# @lc code=end

# 方法一
# class Solution:
#     def canIWin(self, maxChoosableInt: int, desiredTotal: int) -> bool:
#         def dfs(total: int) -> bool:
#             key = ''.join(state)
#             if key in cache:
#                 return cache[key]

#             for i in range(1, len(state)):
#                 if state[i] == '1':
#                     continue

#                 state[i] = '1'
#                 if total - i <= 0 or not dfs(total - i):
#                     cache[key] = True
#                     state[i] = '0'
#                     return True
#                 state[i] = '0'

#             cache[key] = False
#             return False

#         if maxChoosableInt >= desiredTotal:
#             return True

#         if (1 + maxChoosableInt) * maxChoosableInt // 2 < desiredTotal:
#             return False

#         state = ['0'] * (maxChoosableInt + 1)
#         cache = {}

#         return dfs(desiredTotal)

if __name__ == '__main__':
    solu = Solution()
    print(solu.canIWin(5, 6))
    print(solu.canIWin(5, 7))
    print(solu.canIWin(5, 8))
    print(solu.canIWin(5, 9))
    print(solu.canIWin(5, 10))
    print(solu.canIWin(10, 40))
