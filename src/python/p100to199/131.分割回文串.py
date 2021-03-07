#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   131.分割回文串.py
@Time    :   2021/03/07 11:54:30
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
# https://leetcode-cn.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (71.37%)
# Likes:    558
# Dislikes: 0
# Total Accepted:    72.1K
# Total Submissions: 101K
# Testcase Example:  '"aab"'
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
#
# 返回 s 所有可能的分割方案。
#
# 示例:
#
# 输入: "aab"
# 输出:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
#
#
from typing import List
"""
方法一：回溯 + 动态规划预处理
思路与算法

由于需要求出字符串 s 的所有分割方案，因此我们考虑使用搜索 + 回溯的方法
枚举所有可能的分割方法并进行判断。

假设我们当前搜索到字符串的第 i 个字符，且 s[0..i-1] 位置的所有字符已经
被分割成若干个回文串，并且分割结果被放入了答案数组 ans 中，那么我们就
需要枚举下一个回文串的右边界 j，使得 s[i..j] 是一个回文串。

因此，我们可以从 i 开始，从小到大依次枚举 j。对于当前枚举的 j 值，我们
使用双指针的方法判断 s[i..j] 是否为回文串：如果 s[i..j] 是回文串，那么
就将其加入答案数组 ans 中，并以 j+1 作为新的 i 进行下一层搜索，并在未来
的回溯时将 s[i..j] 从 ans 中移除。

如果我们已经搜索完了字符串的最后一个字符，那么就找到了一种满足要求的分割
方法。

细节

当我们在判断 s[i..j] 是否为回文串时，常规的方法是使用双指针分别指向
i 和 j，每次判断两个指针指向的字符是否相同，直到两个指针相遇。然而这种
方法会产生重复计算，例如下面这个例子：

当 s = aaba 时，对于前 2 个字符 aa，我们有 22 种分割方法 [aa] 和 [a,a]，
当我们每一次搜索到字符串的第 i = 2 个字符 b 时，都需要对于每个 s[i..j]
使用双指针判断其是否为回文串，这就产生了重复计算。

因此，我们可以将字符串 s 的每个子串 s[i..j] 是否为回文串预处理出来，使用
动态规划即可。设 f(i, j) 表示 s[i..j] 是否为回文串，那么有状态转移方程：

    f(i, j) = True,                          i >= j
    f(i, j) = f(i+1, j−1) ∧ (s[i] = s[j]),   otherwise


其中 ∧ 表示逻辑与运算，即 s[i..j] 为回文串，当且仅当其为空串（i > j），
其长度为 1（i = j），或者首尾字符相同且 s[i+1..j-1] 为回文串。

预处理完成之后，我们只需要 O(1) 的时间就可以判断任意 s[i..j] 是否为回文串了。
"""


# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 预处理
        n = len(s)
        f = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

        def dfs(i: int) -> None:
            if i == n:
                ans.append(stack[::])
                return

            for j in range(i, n):
                if f[i][j]:
                    stack.append(s[i:j + 1])
                    dfs(j + 1)
                    stack.pop()

        ans = []
        stack = []
        dfs(0)
        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.partition("aab"))
