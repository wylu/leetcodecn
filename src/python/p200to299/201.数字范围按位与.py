#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   201.数字范围按位与.py
@Time    :   2020/08/23 09:54:01
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=201 lang=python3
#
# [201] 数字范围按位与
#
# https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/description/
#
# algorithms
# Medium (47.14%)
# Likes:    162
# Dislikes: 0
# Total Accepted:    19.7K
# Total Submissions: 40.8K
# Testcase Example:  '5\n7'
#
# 给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。
#
# 示例 1:
#
# 输入: [5,7]
# 输出: 4
#
# 示例 2:
#
# 输入: [0,1]
# 输出: 0
#
#
"""
我们观察按位与运算的性质。对于一系列的位，例如 [1,1,0,1,1]，只要有一个零值的位，
那么这一系列位的按位与运算结果都将为零。

对于本题，首先我们可以对范围内的每个数字用二进制的字符串表示，例如 9 = 00001001，
然后我们将每个二进制字符串的位置对齐。

  9     00001 001
  10    00001 010
  11    00001 011
  12    00001 100

在上面的例子中，我们可以发现，对所有数字执行按位与运算的结果是所有对应二进制
字符串的公共前缀再用零补上后面的剩余位。

那么这个规律是否正确呢？我们可以进行简单的证明。假设对于所有这些二进制串，
前 i 位均相同，第 i+1 位开始不同，由于 [m,n] 连续，所以第 i+1 位在 [m,n]
的数字范围从小到大列举出来一定是前面全部是 0，后面全部是 1，在上图中对应
[9,11] 均为 0，[12,12] 均为 1。并且一定存在连续的两个数 x 和 x+1，满足
x 的第 i+1 位为 0，后面全为 1，x+1 的第 i+1 位为 1，后面全为 0，对应上图中
的例子即为 11 和 12。这种形如 0111... 和 1000... 的二进制串的按位与的结果
一定为 0000...，因此第 i+1 位开始的剩余位均为 0，前 i 位由于均相同，因此
按位与结果不变。最后的答案即为二进制字符串的公共前缀再用零补上后面的剩余位。

进一步来说，所有这些二进制字符串的公共前缀也即指定范围的起始和结束数字
m 和 n 的公共前缀（即在上面的示例中分别为 9 和 12）。

因此，最终我们可以将问题重新表述为：给定两个整数，我们要找到它们对应的
二进制字符串的公共前缀。

思路：
采用位移操作。我们的想法是将两个数字不断向右移动，直到数字相等，即数字
被缩减为它们的公共前缀。然后，通过将公共前缀向左移动，将零添加到公共前缀
的右边以获得最终结果。
"""


# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            n &= (n - 1)
        return n


# class Solution:
#     def rangeBitwiseAnd(self, m: int, n: int) -> int:
#         shift = 0
#         # 找到公共前缀
#         while m < n:
#             m >>= 1
#             n >>= 1
#             shift += 1
#         return m << shift

# class Solution:
#     def rangeBitwiseAnd(self, m: int, n: int) -> int:
#         if m == 0 or n == 0 or m == n:
#             return m

#         def left1idx(x: int) -> int:
#             i = 0
#             while x:
#                 x >>= 1
#                 i += 1
#             return i - 1

#         ln, lm = left1idx(n), left1idx(m)
#         if ln != lm:
#             return 0

#         ans, c = 0, ln
#         while c >= 0 and n & (1 << c) == m & (1 << c):
#             ans ^= n & (1 << c)
#             c -= 1

#         return ans

# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.rangeBitwiseAnd(5, 7))
    print(solu.rangeBitwiseAnd(0, 1))
    print(solu.rangeBitwiseAnd(6, 7))
    print(solu.rangeBitwiseAnd(10, 11))
