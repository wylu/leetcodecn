#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   710.黑名单中的随机数.py
@Time    :   2022/06/26 11:19:35
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=710 lang=python3
#
# [710] 黑名单中的随机数
#
# https://leetcode.cn/problems/random-pick-with-blacklist/description/
#
# algorithms
# Hard (40.83%)
# Likes:    137
# Dislikes: 0
# Total Accepted:    14.3K
# Total Submissions: 35.2K
# Testcase Example:
# '["Solution","pick","pick","pick","pick","pick","pick","pick"]\n'
# + '[[7,[2,3,5]],[],[],[],[],[],[],[]]'
#
# 给定一个整数 n 和一个 无重复 黑名单整数数组 blacklist 。设计一种算法，从 [0, n - 1] 范围内的任意整数中选取一个 未加入 黑名单
# blacklist 的整数。任何在上述范围内且不在黑名单 blacklist 中的整数都应该有 同等的可能性 被返回。
#
# 优化你的算法，使它最小化调用语言 内置 随机函数的次数。
#
# 实现 Solution 类:
#
#
# Solution(int n, int[] blacklist) 初始化整数 n 和被加入黑名单 blacklist 的整数
# int pick() 返回一个范围为 [0, n - 1] 且不在黑名单 blacklist 中的随机整数
#
#
#
#
# 示例 1：
#
#
# 输入
# ["Solution", "pick", "pick", "pick", "pick", "pick", "pick", "pick"]
# [[7, [2, 3, 5]], [], [], [], [], [], [], []]
# 输出
# [null, 0, 4, 1, 6, 1, 0, 4]
#
# 解释
# Solution solution = new Solution(7, [2, 3, 5]);
# solution.pick(); // 返回0，任何[0,1,4,6]的整数都可以。注意，对于每一个pick的调用，
# ⁠                // 0、1、4和6的返回概率必须相等(即概率为1/4)。
# solution.pick(); // 返回 4
# solution.pick(); // 返回 1
# solution.pick(); // 返回 6
# solution.pick(); // 返回 1
# solution.pick(); // 返回 0
# solution.pick(); // 返回 4
#
#
#
#
# 提示:
#
#
# 1 <= n <= 10^9
# 0 <= blacklist.length <= min(10^5, n - 1)
# 0 <= blacklist[i] < n
# blacklist 中所有值都 不同
# pick 最多被调用 2 * 10^4 次
#
#
#
from random import randrange
from typing import List


# @lc code=start
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        m = len(blacklist)
        self.bound = w = n - m
        black = {b for b in blacklist if b >= w}
        self.b2w = {}
        for b in blacklist:
            if b < self.bound:
                while w in black:
                    w += 1
                self.b2w[b] = w
                w += 1

    def pick(self) -> int:
        x = randrange(self.bound)
        return self.b2w.get(x, x)


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
# @lc code=end
