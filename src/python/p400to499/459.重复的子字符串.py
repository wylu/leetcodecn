#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   459.重复的子字符串.py
@Time    :   2020/08/24 09:52:17
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#
# https://leetcode-cn.com/problems/repeated-substring-pattern/description/
#
# algorithms
# Easy (47.73%)
# Likes:    274
# Dislikes: 0
# Total Accepted:    27.2K
# Total Submissions: 55.2K
# Testcase Example:  '"abab"'
#
# 给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。
#
# 示例 1:
#
#
# 输入: "abab"
#
# 输出: True
#
# 解释: 可由子字符串 "ab" 重复两次构成。
#
#
# 示例 2:
#
#
# 输入: "aba"
#
# 输出: False
#
#
# 示例 3:
#
#
# 输入: "abcabcabcabc"
#
# 输出: True
#
# 解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)
#
#
#
"""
方法一：枚举

如果一个长度为 n 的字符串 s 可以由它的一个长度为 n' 的子串 s' 重复多次构成，
那么：
  - n 一定是 n' 的倍数；
  - s' 一定是 s 的前缀；
  - 对于任意的 i∈[n',n)，有 s[i] = s[i-n']

也就是说，s 中长度为 n' 的前缀就是 s'，并且在这之后的每一个位置上的字符
s[i]，都需要与它之前的第 n' 个字符 s[i-n'] 相同。

因此，我们可以从小到大枚举 n'，并对字符串 s 进行遍历，进行上述的判断。
注意到一个小优化是，因为子串至少需要重复一次，所以 n' 不会大于 n 的一半，
我们只需要在 [1, n//2 + 1] 的范围内枚举 n' 即可。


方法二：字符串匹配

我们可以把字符串 s 写成 s's'...s's' 的形式，总计 n//n' 个 s'。但我们
如何在不枚举 n' 的情况下，判断 s 是否能写成上述的形式呢？

如果我们移除字符串 s 的前 n' 个字符（即一个完整的 s'），再将这些字符
保持顺序添加到剩余字符串的末尾，那么得到的字符串仍然是 s。由于
1 <= n' < n，那么如果将两个 s 连在一起，并移除第一个和最后一个字符，
那么得到的字符串一定包含 s，即 s 是它的一个子串。

因此我们可以考虑这种方法：我们将两个 s 连在一起，并移除第一个和最后一个
字符。如果 s 是该字符串的子串，那么 s 就满足题目要求。

注意到我们证明的是如果 s 满足题目要求，那么 s 有这样的性质，而我们使用
的方法却是如果 s 有这样的性质，那么 s 满足题目要求。因此，只证明了充分性
是远远不够的，我们还需要证明必要性。题解区的很多题解都忽略了这一点，
但它是非常重要的。证明需要使用一些同余运算的小技巧，详见：
https://leetcode-cn.com/problems/repeated-substring-pattern/solution/zhong-fu-de-zi-zi-fu-chuan-by-leetcode-solution/
"""


# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)


# @lc code=end

# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
#         n = len(s)
#         for i in range(1, n // 2 + 1):
#             if n % i != 0:
#                 continue
#             flag = True
#             for j in range(i, n):
#                 if s[j] != s[j - i]:
#                     flag = False
#                     break
#             if flag:
#                 return True
#         return False

if __name__ == '__main__':
    solu = Solution()
    print(solu.repeatedSubstringPattern('ababab'))
    print(solu.repeatedSubstringPattern('a'))
    print(solu.repeatedSubstringPattern('aba'))
    print(solu.repeatedSubstringPattern('abab'))
    print(solu.repeatedSubstringPattern('abcabcabcabc'))
    print(solu.repeatedSubstringPattern('abaababaab'))
