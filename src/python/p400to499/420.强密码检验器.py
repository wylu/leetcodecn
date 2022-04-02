#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   420.强密码检验器.py
@Time    :   2022/04/02 20:34:58
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=420 lang=python3
#
# [420] 强密码检验器
#
# https://leetcode-cn.com/problems/strong-password-checker/description/
#
# algorithms
# Hard (35.93%)
# Likes:    161
# Dislikes: 0
# Total Accepted:    12.4K
# Total Submissions: 34.5K
# Testcase Example:  '"a"'
#
#
# 如果一个密码满足下述所有条件，则认为这个密码是强密码：
#
#
# 由至少 6 个，至多 20 个字符组成。
# 至少包含 一个小写 字母，一个大写 字母，和 一个数字 。
# 同一字符 不能 连续出现三次 (比如 "...aaa..." 是不允许的, 但是 "...aa...a..." 如果满足其他条件也可以算是强密码)。
#
#
# 给你一个字符串 password ，返回 将 password 修改到满足强密码条件需要的最少修改步数。如果 password 已经是强密码，则返回 0
# 。
#
# 在一步修改操作中，你可以：
#
#
# 插入一个字符到 password ，
# 从 password 中删除一个字符，或
# 用另一个字符来替换 password 中的某个字符。
#
#
#
#
# 示例 1：
#
#
# 输入：password = "a"
# 输出：5
#
#
# 示例 2：
#
#
# 输入：password = "aA1"
# 输出：3
#
#
# 示例 3：
#
#
# 输入：password = "1337C0d3"
# 输出：0
#
#
#
#
# 提示：
#
#
# 1 <= password.length <= 50
# password 由字母、数字、点 '.' 或者感叹号 '!'
#
#
#


# @lc code=start
class Solution:

    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        has_lower = any(ch.islower() for ch in password)
        has_upper = any(ch.isupper() for ch in password)
        has_digit = any(ch.isdigit() for ch in password)
        categories = has_lower + has_upper + has_digit

        if n < 6:
            return max(6 - n, 3 - categories)

        password += '#'
        if n <= 20:
            replace, cnt = 0, 1
            for i in range(1, n + 1):
                if password[i] != password[i - 1]:
                    replace, cnt = replace + cnt // 3, 0
                cnt += 1
            return max(replace, 3 - categories)

        # 替换次数和删除次数
        replace, remove = 0, n - 20
        # k mod 3 = 1 的组数，即删除 2 个字符可以减少 1 次替换操作
        rm2, cnt = 0, 1

        for i in range(1, n + 1):
            if password[i] != password[i - 1]:
                if remove > 0 and cnt >= 3:
                    if cnt % 3 == 0:
                        # 如果是 k % 3 = 0 的组，那么优先删除 1 个字符，减少 1 次替换操作
                        remove -= 1
                        replace -= 1
                    elif cnt % 3 == 1:
                        # 如果是 k % 3 = 1 的组，那么存下来备用
                        rm2 += 1
                    # k % 3 = 2 的组无需显式考虑
                replace, cnt = replace + cnt // 3, 0
            cnt += 1

        use2 = min(rm2, remove // 2)
        replace -= use2
        remove -= use2 * 2

        use3 = remove // 3
        replace -= use3
        remove -= use3 * 3

        return (n - 20) + max(replace, 3 - categories)


# @lc code=end
