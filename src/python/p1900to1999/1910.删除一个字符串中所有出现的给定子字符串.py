#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1910.删除一个字符串中所有出现的给定子字符串.py
@Time    :   2021/07/04 09:46:57
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1910 lang=python3
#
# [1910] 删除一个字符串中所有出现的给定子字符串
#
# https://leetcode-cn.com/problems/remove-all-occurrences-of-a-substring/description/
#
# algorithms
# Medium (68.22%)
# Likes:    5
# Dislikes: 0
# Total Accepted:    2.6K
# Total Submissions: 3.8K
# Testcase Example:  '"daabcbaabcbc"\n"abc"'
#
# 给你两个字符串 s 和 part ，请你对 s 反复执行以下操作直到 所有 子字符串 part 都被删除：
#
#
# 找到 s 中 最左边 的子字符串 part ，并将它从 s 中删除。
#
#
# 请你返回从 s 中删除所有 part 子字符串以后得到的剩余字符串。
#
# 一个 子字符串 是一个字符串中连续的字符序列。
#
#
#
# 示例 1：
#
# 输入：s = "daabcbaabcbc", part = "abc"
# 输出："dab"
# 解释：以下操作按顺序执行：
# - s = "daabcbaabcbc" ，删除下标从 2 开始的 "abc" ，得到 s = "dabaabcbc" 。
# - s = "dabaabcbc" ，删除下标从 4 开始的 "abc" ，得到 s = "dababc" 。
# - s = "dababc" ，删除下标从 3 开始的 "abc" ，得到 s = "dab" 。
# 此时 s 中不再含有子字符串 "abc" 。
#
#
# 示例 2：
#
# 输入：s = "axxxxyyyyb", part = "xy"
# 输出："ab"
# 解释：以下操作按顺序执行：
# - s = "axxxxyyyyb" ，删除下标从 4 开始的 "xy" ，得到 s = "axxxyyyb" 。
# - s = "axxxyyyb" ，删除下标从 3 开始的 "xy" ，得到 s = "axxyyb" 。
# - s = "axxyyb" ，删除下标从 2 开始的 "xy" ，得到 s = "axyb" 。
# - s = "axyb" ，删除下标从 1 开始的 "xy" ，得到 s = "ab" 。
# 此时 s 中不再含有子字符串 "xy" 。
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 1000
# 1 <= part.length <= 1000
# s​​​​​​ 和 part 只包小写英文字母。
#
#
#
"""
方法一：模拟 + 暴力匹配
思路与算法

我们设字符串 part 的长度为 m。在从左到右遍历字符串 s 时，如果以当前字符
结尾的长度为 m 的子串与 part 相等，那么我们就需要删去该子串。

我们可以用一个初始为空的字符串 res 来模拟这一过程。我们从左到右遍历字符串
s，并将对应的字符添加至 res 的尾部。如果此时 res 中长度为 m 的后缀与 part
相等，那么我们删去该后缀。最终，res 即为 s 中删除所有 part 子串后得到的
剩余字符串。

方法二：KMP 算法
思路与算法

在方法一中，每一次匹配都需要暴力比较两个长度为 m 的字符串，时间复杂度为
O(m)。我们可以对暴力比较的过程进行优化。在这里，我们使用 KMP 算法对匹配
过程进行优化。如果读者不熟悉 KMP 算法，可以阅读「28. 实现 strStr() 的官方题解」
中的方法二。

在这里，除了需要保留 part 的前缀函数数组，我们还需要保留 res 的前缀函数数组。
当新插入字符对应的前缀函数值等于 m 时，代表 res 中长度为 m 的后缀与 part 相等，
此时我们需要删去该后缀以及对应的前缀函数值。

另外，由于 Python 等语言不支持删除字符串的元素，我们需要将字符串转化为数组进行操作。
"""


# @lc code=start
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        m = len(part)
        fp = [0] * m  # part 失配数组
        j = 0
        for i in range(1, m):
            while j > 0 and part[i] != part[j]:
                j = fp[j - 1]
            if part[i] == part[j]:
                j += 1
            fp[i] = j

        res = []
        fr = [0]  # res 失配数组
        for ch in s:
            # 模拟从左至右匹配的过程
            res.append(ch)

            # 更新 res 的失配数组
            j = fr[-1]
            while j > 0 and ch != part[j]:
                j = fp[j - 1]
            if ch == part[j]:
                j += 1
            fr.append(j)

            if j == m:
                # 如果匹配成功，那么删除对应后缀
                fr = fr[:-m]
                res = res[:-m]

        return ''.join(res)


# @lc code=end

# class Solution:
#     def removeOccurrences(self, s: str, part: str) -> str:
#         m = len(part)
#         res = []
#         for ch in s:
#             res.append(ch)
#             if len(res) >= m and ''.join(res[-m:]) == part:
#                 res = res[:-m]
#         return ''.join(res)

if __name__ == '__main__':
    solu = Solution()
    print(solu.removeOccurrences(s="daabcbaabcbc", part="abc"))
    print(solu.removeOccurrences(s="axxxxyyyyb", part="xy"))
    print(solu.removeOccurrences(s="abcdabef", part="abcdabef"))
