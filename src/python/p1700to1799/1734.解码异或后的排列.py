#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1734.解码异或后的排列.py
@Time    :   2021/05/11 11:21:24
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1734 lang=python3
#
# [1734] 解码异或后的排列
#
# https://leetcode-cn.com/problems/decode-xored-permutation/description/
#
# algorithms
# Medium (67.42%)
# Likes:    59
# Dislikes: 0
# Total Accepted:    10.8K
# Total Submissions: 16K
# Testcase Example:  '[3,1]'
#
# 给你一个整数数组 perm ，它是前 n 个正整数的排列，且 n 是个 奇数 。
#
# 它被加密成另一个长度为 n - 1 的整数数组 encoded ，满足 encoded[i] = perm[i] XOR perm[i + 1]
# 。比方说，如果 perm = [1,3,2] ，那么 encoded = [2,1] 。
#
# 给你 encoded 数组，请你返回原始数组 perm 。题目保证答案存在且唯一。
#
#
#
# 示例 1：
#
# 输入：encoded = [3,1]
# 输出：[1,2,3]
# 解释：如果 perm = [1,2,3] ，那么 encoded = [1 XOR 2,2 XOR 3] = [3,1]
#
#
# 示例 2：
#
# 输入：encoded = [6,5,4,6]
# 输出：[2,4,1,5,3]
#
#
#
#
# 提示：
#
#
# 3 <= n < 10^5
# n 是奇数。
# encoded.length == n - 1
#
#
#
from typing import List
"""
方法一：利用异或运算解码
这道题规定了数组 perm 是前 n 个正整数的排列，其中 n 是奇数，只有充分
利用给定的条件，才能得到答案。

为了得到原始数组 perm，应首先得到数组 perm 的第一个元素（即下标为 0
的元素），这也是最容易得到的。如果能得到数组 perm 的全部元素的异或
运算结果，以及数组 perm 除了 perm[0] 以外的全部元素的异或运算结果，
即可得到 perm[0] 的值。

由于数组 perm 是前 n 个正整数的排列，因此数组 perm 的全部元素的异或
运算结果即为从 1 到 n 的全部正整数的异或运算结果。用 total 表示数组
perm 的全部元素的异或运算结果，则有

    total = 1 ^ 2 ^ ... ^ n
          = perm[0] ^ perm[1] ^ ... ^ perm[n−1]

其中 ^ 是异或运算符。

如何得到数组 perm 除了 perm[0] 以外的全部元素的异或运算结果？

由于 n 是奇数，除了 perm[0] 以外，数组 perm 还有 n-1 个其他元素，
注意 n-1 是一个偶数。又由于数组 encoded 的每个元素都是数组 perm
的两个元素异或运算的结果，因此数组 encoded 中存在 (n-1)/2 个元素，
这些元素的异或运算的结果等于数组 perm 除了 perm[0] 以外的全部元素
的异或运算结果。

具体而言，数组 encoded 的所有下标为奇数的元素的异或运算结果即为数组
perm 除了 perm[0] 以外的全部元素的异或运算结果。用 odd 表示数组
encoded 的所有下标为奇数的元素的异或运算结果，则有

    odd = encoded[1] ^ encoded[3] ^ ... ^ encoded[n−2]
        = perm[1] ^ perm[2] ^ ... ^ perm[n]

根据 total 和 odd 的值，即可计算得到 perm[0] 的值：

perm[0] = (perm[0] ^ ... ^ perm[n]) ^ (perm[1] ^ ... ^ perm[n])
        = total ^ odd

当 1 <= i < n 时，有 encoded[i-1] = perm[i-1] ^ perm[i]。在等号两边
同时异或 perm[i−1]，即可得到 perm[i] = perm[i-1] ^ encoded[i-1]。
计算过程见「1720. 解码异或后的数组的官方题解」。

由于 perm[0] 已知，因此对 i 从 1 到 n-1 依次计算 perm[i] 的值，
即可得到原始数组 perm。
"""


# @lc code=start
class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        total = 0
        for i in range(1, n + 1):
            total ^= i

        odd = 0
        for i in range(1, n - 1, 2):
            odd ^= encoded[i]

        perm = [0] * n
        perm[0] = total ^ odd
        for i in range(n - 1):
            perm[i + 1] = perm[i] ^ encoded[i]

        return perm


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.decode(encoded=[3, 1]))
    print(solu.decode(encoded=[6, 5, 4, 6]))
