#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   829.连续整数求和.py
@Time    :   2020/08/20 21:49:57
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=829 lang=python3
#
# [829] 连续整数求和
#
# https://leetcode-cn.com/problems/consecutive-numbers-sum/description/
#
# algorithms
# Hard (33.42%)
# Likes:    76
# Dislikes: 0
# Total Accepted:    5.1K
# Total Submissions: 15.2K
# Testcase Example:  '5'
#
# 给定一个正整数 N，试求有多少组连续正整数满足所有数字之和为 N?
#
# 示例 1:
#
#
# 输入: 5
# 输出: 2
# 解释: 5 = 5 = 2 + 3，共有两组连续整数([5],[2,3])求和后为 5。
#
# 示例 2:
#
#
# 输入: 9
# 输出: 3
# 解释: 9 = 9 = 4 + 5 = 2 + 3 + 4
#
# 示例 3:
#
#
# 输入: 15
# 输出: 4
# 解释: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
#
# 说明: 1 <= N <= 10 ^ 9
#
#
"""
1个数时，必然有一个数可构成N；

2个数若要构成N，第2个数与第1个数差为1，N减掉这个1能整除2则能由商与商+1构成N；

3个数若要构成N，第2个数与第1个数差为1，第3个数与第1个数的差为2，N减掉1再减掉2
能整除3则能由商、商+1与商+2构成N；

...
以此类推，当商即第1个数小于等于0时结束;

时间复杂度：
N - 1 - 2 - 3 - 4 - 5 ... - K = 0
N = 1 + 2 + 3 + ... + k
(1 + k)k/2 = N
(1 + k)k = 2N
约等于k^2 = 2N
k = 根号下的2N
省略常数项，O(根号N)
"""


# @lc code=start
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ans, i = 0, 1
        while n > 0:
            ans += n % i == 0
            n -= i
            i += 1
        return ans


# @lc code=end
