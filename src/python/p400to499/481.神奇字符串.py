#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   481.神奇字符串.py
@Time    :   2022/10/31 22:44:33
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=481 lang=python3
#
# [481] 神奇字符串
#
# https://leetcode.cn/problems/magical-string/description/
#
# algorithms
# Medium (57.51%)
# Likes:    161
# Dislikes: 0
# Total Accepted:    29.9K
# Total Submissions: 46.8K
# Testcase Example:  '6'
#
# 神奇字符串 s 仅由 '1' 和 '2' 组成，并需要遵守下面的规则：
#
#
# 神奇字符串 s 的神奇之处在于，串联字符串中 '1' 和 '2' 的连续出现次数可以生成该字符串。
#
#
# s 的前几个元素是 s = "1221121221221121122……" 。如果将 s 中连续的若干 1 和 2 进行分组，可以得到 "1 22 11
# 2 1 22 1 22 11 2 11 22 ......" 。每组中 1 或者 2 的出现次数分别是 "1 2 2 1 1 2 1 2 2 1 2 2
# ......" 。上面的出现次数正是 s 自身。
#
# 给你一个整数 n ，返回在神奇字符串 s 的前 n 个数字中 1 的数目。
#
#
#
# 示例 1：
#
#
# 输入：n = 6
# 输出：3
# 解释：神奇字符串 s 的前 6 个元素是 “122112”，它包含三个 1，因此返回 3 。
#
#
# 示例 2：
#
#
# 输入：n = 1
# 输出：1
#
#
#
#
# 提示：
#
#
# 1 <= n <= 10^5
#
#
#


# @lc code=start
class Solution:

    def magicalString(self, n: int) -> int:
        s = [1, 2, 2]
        i, j, d = 2, 0, (1, 2)

        while len(s) < n:
            s.append(d[j])
            if s[i] == 2:
                s.append(d[j])
            i += 1
            j ^= 1

        return s[:n].count(1)


# @lc code=end

# class Solution:

#     def magicalString(self, n: int) -> int:
#         s1, s2 = [1], [1]

#         while len(s1) <= n:
#             if s1[-1] == 1:
#                 s1.append(2)
#                 if s1[len(s2)] == 2:
#                     s1.append(2)
#             else:
#                 s1.append(1)
#                 if s1[len(s2)] == 2:
#                     s1.append(1)

#             s2.append(s1[len(s2)])

#         return sum(num == 1 for num in s1[:n])

if __name__ == '__main__':
    solu = Solution()
    print(solu.magicalString(n=1))
    print(solu.magicalString(n=6))
    print(solu.magicalString(n=7))
    print(solu.magicalString(n=9))
    print(solu.magicalString(n=10))
