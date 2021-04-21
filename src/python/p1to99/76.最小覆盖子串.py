#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   76.最小覆盖子串.py
@Time    :   2021/04/21 22:24:42
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (41.23%)
# Likes:    1123
# Dislikes: 0
# Total Accepted:    129.9K
# Total Submissions: 315.1K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
#
# 注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。
#
#
#
# 示例 1：
#
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
#
#
# 示例 2：
#
#
# 输入：s = "a", t = "a"
# 输出："a"
#
#
#
#
# 提示：
#
#
# 1 <= s.length, t.length <= 10^5
# s 和 t 由英文字母组成
#
#
#
# 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？
#
from collections import defaultdict
"""
方法一：滑动窗口
思路和算法

本问题要求我们返回字符串 s 中包含字符串 t 的全部字符的最小窗口。我们称
包含 t 的全部字母的窗口为「可行」窗口。

我们可以用滑动窗口的思想解决这个问题。在滑动窗口类型的问题中都会有两个指针，
一个用于「延伸」现有窗口的 r 指针，和一个用于「收缩」窗口的 l 指针。在任意
时刻，只有一个指针运动，而另一个保持静止。我们在 s 上滑动窗口，通过移动 r
指针不断扩张窗口。当窗口包含 t 全部所需的字符后，如果能收缩，我们就收缩窗口
直到得到最小窗口。

如何判断当前的窗口包含所有 t 所需的字符呢？我们可以用一个哈希表表示 t 中
所有的字符以及它们的个数，用一个哈希表动态维护窗口中所有的字符以及它们的
个数，如果这个动态表中包含 t 的哈希表中的所有字符，并且对应的个数都不小于
t 的哈希表中各个字符的个数，那么当前的窗口是「可行」的。

注意：这里 t 中可能出现重复的字符，所以我们要记录字符的个数。

考虑如何优化？ 如果 s=XX...XABCXXXX，t=ABC，那么显然 XX...XABC 是第一个
得到的「可行」区间，得到这个可行区间后，我们按照「收缩」窗口的原则更新左边
界，得到最小区间。我们其实做了一些无用的操作，就是更新右边界的时候「延伸」
进了很多无用的 XX，更新左边界的时候「收缩」扔掉了这些无用的 XX，做了这么多
无用的操作，只是为了得到短短的 ABCABC。没错，其实在 s 中，有的字符我们是
不关心的，我们只关心 t 中出现的字符，我们可不可以先预处理 s，扔掉那些 t 中
没有出现的字符，然后再做滑动窗口呢？也许你会说，这样可能出现 XXABXXCXXABXXC
的情况，在统计长度的时候可以扔掉前两个 XX，但是不扔掉中间的 XX，怎样解决
这个问题呢？优化后的时空复杂度又是多少？
"""


# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sFreq, tFreq = defaultdict(int), defaultdict(int)
        for ch in t:
            tFreq[ch] += 1

        def check():
            for k, v in tFreq.items():
                if sFreq[k] < v:
                    return False
            return True

        k, n, size = -1, len(s), 0x7FFFFFFF
        i = j = 0
        while j < n:
            if s[j] in tFreq:
                sFreq[s[j]] += 1

            while i <= j and check():
                if j - i + 1 < size:
                    size = j - i + 1
                    k = i
                sFreq[s[i]] -= 1
                i += 1

            j += 1

        return '' if k == -1 else s[k:k + size]


# @lc code=end

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         sFreq, tFreq = defaultdict(int), defaultdict(int)
#         for ch in t:
#             tFreq[ch] += 1

#         def check():
#             for k, v in tFreq.items():
#                 if sFreq[k] < v:
#                     return False
#             return True

#         k, n, size = -1, len(s), 0x7FFFFFFF
#         i = j = 0
#         while i < n or j < n:
#             while i < n and check():
#                 if j - i < size:
#                     size = j - i
#                     k = i
#                 sFreq[s[i]] -= 1
#                 i += 1

#             if j < n:
#                 sFreq[s[j]] += 1
#                 j += 1
#             elif not check():
#                 break

#         return '' if k == -1 else s[k:k + size]

if __name__ == "__main__":
    solu = Solution()
    # print(solu.minWindow(s="", t="a"))  # invalid case
    # print(solu.minWindow(s="a", t=""))  # invalid case

    print(solu.minWindow(s="ADOBECODEBANC", t="ABC"))
    print(solu.minWindow(s="a", t="a"))
    print(solu.minWindow(s="a", t="aa"))
    print(solu.minWindow(s="ab", t="b"))
