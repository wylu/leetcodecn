#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   292.nim-游戏.py
@Time    :   2020/09/02 00:17:53
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=292 lang=python3
#
# [292] Nim 游戏
#
# https://leetcode-cn.com/problems/nim-game/description/
#
# algorithms
# Easy (69.37%)
# Likes:    362
# Dislikes: 0
# Total Accepted:    56.7K
# Total Submissions: 81.8K
# Testcase Example:  '4'
#
# 你和你的朋友，两个人一起玩 Nim 游戏：桌子上有一堆石头，每次你们轮流拿掉 1 - 3 块石头。 拿掉最后一块石头的人就是获胜者。你作为先手。
#
# 你们是聪明人，每一步都是最优解。 编写一个函数，来判断你是否可以在给定石头数量的情况下赢得游戏。
#
# 示例:
#
# 输入: 4
# 输出: false
# 解释: 如果堆中有 4 块石头，那么你永远不会赢得比赛；
# 因为无论你拿走 1 块、2 块 还是 3 块石头，最后一块石头总是会被你的朋友拿走。
#
#
#


# @lc code=start
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


# @lc code=end
