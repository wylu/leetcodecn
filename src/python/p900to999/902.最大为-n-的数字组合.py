#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   902.最大为-n-的数字组合.py
@Time    :   2022/10/18 21:37:00
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
#
# @lc app=leetcode.cn id=902 lang=python3
#
# [902] 最大为 N 的数字组合
#
# https://leetcode.cn/problems/numbers-at-most-n-given-digit-set/description/
#
# algorithms
# Hard (39.03%)
# Likes:    207
# Dislikes: 0
# Total Accepted:    19.5K
# Total Submissions: 43.8K
# Testcase Example:  '["1","3","5","7"]\n100'
#
# 给定一个按 非递减顺序 排列的数字数组 digits 。你可以用任意次数 digits[i] 来写的数字。例如，如果 digits =
# ['1','3','5']，我们可以写数字，如 '13', '551', 和 '1351315'。
#
# 返回 可以生成的小于或等于给定整数 n 的正整数的个数 。
#
#
#
# 示例 1：
#
#
# 输入：digits = ["1","3","5","7"], n = 100
# 输出：20
# 解释：
# 可写出的 20 个数字是：
# 1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
#
#
# 示例 2：
#
#
# 输入：digits = ["1","4","9"], n = 1000000000
# 输出：29523
# 解释：
# 我们可以写 3 个一位数字，9 个两位数字，27 个三位数字，
# 81 个四位数字，243 个五位数字，729 个六位数字，
# 2187 个七位数字，6561 个八位数字和 19683 个九位数字。
# 总共，可以使用D中的数字写出 29523 个整数。
#
# 示例 3:
#
#
# 输入：digits = ["7"], n = 8
# 输出：1
#
#
#
#
# 提示：
#
#
#
# 1 <= digits.length <= 9
# digits[i].length == 1
# digits[i] 是从 '1' 到 '9' 的数
# digits 中的所有值都 不同
# digits 按 非递减顺序 排列
# 1 <= n <= 10^9
#
#
#
from functools import cache
from typing import List


# @lc code=start
class Solution:

    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)

        @cache
        def f(i: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s):
                # 如果填了数字，则为 1 种合法方案
                return int(is_num)

            res = 0
            if not is_num:
                # 前面不填数字，那么可以跳过当前数位，也不填数字
                # is_limit 改为 False，因为没有填数字，位数都比 n 要短，自然不会受到 n 的约束
                # is_num 仍然为 False，因为没有填任何数字
                res = f(i + 1, False, False)

            # 根据是否受到约束，决定可以填的数字的上限
            up = s[i] if is_limit else '9'

            for d in digits:
                if d > up:
                    break
                # is_limit：如果当前受到 n 的约束，且填的数字等于上限，那么后面仍然会受到 n 的约束
                # is_num 为 True，因为填了数字
                res += f(i + 1, is_limit and d == up, True)

            return res

        return f(0, True, False)


# @lc code=end
