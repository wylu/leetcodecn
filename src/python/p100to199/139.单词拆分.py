#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   139.单词拆分.py
@Time    :   2020/11/04 22:09:26
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
# https://leetcode-cn.com/problems/word-break/description/
#
# algorithms
# Medium (48.25%)
# Likes:    744
# Dislikes: 0
# Total Accepted:    101.6K
# Total Submissions: 209.9K
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# 给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
#
# 说明：
#
#
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
#
#
# 示例 1：
#
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
#
#
# 示例 2：
#
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
# 注意你可以重复使用字典中的单词。
#
#
# 示例 3：
#
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
#
#
#
from typing import List
"""
方法一：动态规划

思路和算法

我们定义 dp[i] 表示字符串 s 前 i 个字符组成的字符串 s[0..i-1] 是否
能被空格拆分成若干个字典中出现的单词。从前往后计算考虑转移方程，每次转移
的时候我们需要枚举包含位置 i−1 的最后一个单词，看它是否出现在字典中以及
除去这部分的字符串是否合法即可。

公式化来说，我们需要枚举 s[0..i−1] 中的分割点 j ，看 s[0..j−1] 组成
的字符串 s1（默认 j=0 时 s1 为空串）和 s[j..i-1] 组成的字符串 s2 是
否都合法，如果两个字符串均合法，那么按照定义 s1 和 s2 拼接成的字符串也
同样合法。

由于计算到 dp[i] 时我们已经计算出了 dp[0..i−1] 的值，因此字符串 s1
是否合法可以直接由 dp[j] 得知，剩下的我们只需要看 s2 是否合法即可，
因此我们可以得出如下转移方程：

  dp[i] = dp[j] && check(s[j..i−1])

其中 check(s[j..i−1]) 表示子串 s[j..i-1] 是否出现在字典中。

对于检查一个字符串是否出现在给定的字符串列表里一般可以考虑哈希表来快速
判断，同时也可以做一些简单的剪枝，枚举分割点的时候倒着枚举，如果分割点
j 到 i 的长度已经大于字典列表里最长的单词的长度，那么就结束枚举，但是
需要注意的是下面的代码给出的是不带剪枝的写法。

对于边界条件，我们定义 dp[0] = true 表示空串且合法。
"""


# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)

        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[n]


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.wordBreak("leetcode", ["leet", "code"]))
    print(solu.wordBreak("applepenapple", ["apple", "pen"]))
    print(solu.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
