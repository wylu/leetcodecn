#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   336.回文对.py
@Time    :   2020/08/06 22:16:53
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=336 lang=python3
#
# [336] 回文对
#
# https://leetcode-cn.com/problems/palindrome-pairs/description/
#
# algorithms
# Hard (34.50%)
# Likes:    143
# Dislikes: 0
# Total Accepted:    14.4K
# Total Submissions: 37.5K
# Testcase Example:  '["abcd","dcba","lls","s","sssll"]'
#
# 给定一组 互不相同 的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j]
# ，可拼接成回文串。
#
#
#
# 示例 1：
#
# 输入：["abcd","dcba","lls","s","sssll"]
# 输出：[[0,1],[1,0],[3,2],[2,4]]
# 解释：可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
#
#
# 示例 2：
#
# 输入：["bat","tab","cat"]
# 输出：[[0,1],[1,0]]
# 解释：可拼接成的回文串为 ["battab","tabbat"]
#
#
from typing import List
"""
枚举前缀和后缀

思路及算法:

假设存在两个字符串 s1 和 s2，s1+s2 是一个回文串，记这两个字符串的长度分别为
len1 和 len2，我们分三种情况进行讨论：

  1. len1 = len2，这种情况下 s1 是 s2 的翻转。
  2. len1 > len2，这种情况下我们可以将 s1 拆成左右两部分：t1 和 t2，其中
     t1 是 s2 的翻转，t2 是一个回文串。
  3. len1 < len2，这种情况下我们可以将 s2 拆成左右两部分：t1 和 t2，其中
     t2 是 s1 的翻转，t1 是一个回文串。

这样，对于每一个字符串，我们令其为 s1 和 s2 中较长的那一个，然后找到可能和
它构成回文串的字符串即可。

具体地说，我们枚举每一个字符串 k，令其为 s1 和 s2 中较长的那一个，那么 k
可以被拆分为两部分，t1 和 t2。

当 t1 是回文串时，符合情况 3，我们只需要查询给定的字符串序列中是否包含 t2
的翻转。
当 t2 是回文串时，符合情况 2，我们只需要查询给定的字符串序列中是否包含 t1
的翻转。

总的来说，我们要枚举字符串 k 的每一个前缀和后缀，判断其是否为回文串。如果是
回文串，我们就查询其剩余部分的翻转是否在给定的字符串序列中出现即可。

注意到空串也是回文串，所以我们可以将 k 拆解为 k+∅ 或 ∅+k，这样我们就能
将情况 1 也解释为特殊的情况 2 或情况 3。

而要实现这些操作，我们只需要设计一个能够在一系列字符串中查询「某个字符串的
子串的翻转」是否存在的数据结构，有两种实现方法：

  - 我们可以使用字典树存储所有的字符串。在进行查询时，我们将待查询串的子串
    逆序地在字典树上进行遍历，即可判断其是否存在。
  - 我们可以使用哈希表存储所有字符串的翻转串。在进行查询时，我们判断带查询
    串的子串是否在哈希表中出现，就等价于判断了其翻转是否存在。
"""


# @lc code=start
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def findWord(s: str, left: int, right: int) -> int:
            return indices.get(s[left:right + 1], -1)

        def isPalindrome(s: str, left: int, right: int) -> bool:
            return (sub := s[left:right+1]) == sub[::-1]

        n = len(words)
        indices = {words[i][::-1]: i for i in range(n)}

        ans = []
        for i in range(n):
            m = len(words[i])
            for j in range(m + 1):
                # 判断后缀是否为回文
                if isPalindrome(words[i], j, m-1):
                    leftId = findWord(words[i], 0, j - 1)
                    if leftId != -1 and leftId != i:
                        ans.append([i, leftId])

                # 判断前缀是否为回文
                if j and isPalindrome(words[i], 0, j - 1):
                    rightId = findWord(words[i], j, m - 1)
                    if rightId != -1 and rightId != i:
                        ans.append([rightId, i])

        return ans


# @lc code=end
