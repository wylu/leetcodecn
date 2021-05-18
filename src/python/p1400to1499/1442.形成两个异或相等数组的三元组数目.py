#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1442.形成两个异或相等数组的三元组数目.py
@Time    :   2021/05/18 16:13:39
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1442 lang=python3
#
# [1442] 形成两个异或相等数组的三元组数目
#
# https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/description/
#
# algorithms
# Medium (78.67%)
# Likes:    118
# Dislikes: 0
# Total Accepted:    21.4K
# Total Submissions: 27.2K
# Testcase Example:  '[2,3,1,6,7]'
#
# 给你一个整数数组 arr 。
#
# 现需要从数组中取三个下标 i、j 和 k ，其中 (0 <= i < j <= k < arr.length) 。
#
# a 和 b 定义如下：
#
#
# a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
# b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
#
#
# 注意：^ 表示 按位异或 操作。
#
# 请返回能够令 a == b 成立的三元组 (i, j , k) 的数目。
#
#
#
# 示例 1：
#
# 输入：arr = [2,3,1,6,7]
# 输出：4
# 解释：满足题意的三元组分别是 (0,1,2), (0,2,2), (2,3,4) 以及 (2,4,4)
#
#
# 示例 2：
#
# 输入：arr = [1,1,1,1,1]
# 输出：10
#
#
# 示例 3：
#
# 输入：arr = [2,3]
# 输出：0
#
#
# 示例 4：
#
# 输入：arr = [1,3,5,7,9]
# 输出：3
#
#
# 示例 5：
#
# 输入：arr = [7,11,12,9,5,2,7,17,22]
# 输出：8
#
#
#
#
# 提示：
#
#
# 1 <= arr.length <= 300
# 1 <= arr[i] <= 10^8
#
#
#
# import bisect

from collections import Counter
# from collections import defaultdict
from typing import List
"""
前言

用 ^ 表示按位异或运算。

定义长度为 n 的数组 arr 的异或前缀和

    S[i] = 0,  i = 0
    s[i] = arr[0] ^ arr[1] ^ ... ^ arr[i-1],  1 <= i <= n

由该定义可得

    S[i] = 0,  i = 0
    s[i] = S[i-1] ^ arr[i-1],  1 <= i <= n

这是一个关于 S[i] 的递推式，根据该递推式我们可以用 O(n) 的时间得到数组
arr 的异或前缀和数组。

对于两个下标不同的异或前缀和 S[i] 和 S[j]，设 0 < i < j，有

    S[i] ^ S[j] = (arr[0] ^ arr[1] ^ ... ^ arr[i-1])
                  ^ (arr[0] ^ arr[1] ^ ... ^ arr[j-1])

由于异或运算满足结合律和交换律，且任意数异或自身等于 0，上式可化简为

    S[i] ^ S[j] = arr[i] ^ ... ^ arr[j-1]

从而，数组 arr 的子区间 [i,j] 的元素异或和为可表示为

    S[i] ^ S[j+1]

因此问题中的 a 和 b 可表示为

    a = S[i] ^ S[j]
    b = S[j] ^ S[k+1]

若 a = b，则有 S[i] ^ S[j] = S[j] ^ S[k+1] 即 S[i] = S[k+1]

方法二：二重循环

当等式 S[i] = S[k+1] 成立时，[i+1, k] 的范围内的任意 j 都是符合
要求的，对应的三元组个数为 k-i。因此我们只需枚举下标 i 和 k。


方法三：哈希表（一重循环）

对于下标 k，若下标 i = i1, i2, ..., im 时均满足 S[i] = S[k+1]，
根据方法二，这些二元组 (i1,k),(i2,k),...,(im,k) 对答案的贡献之和为

    (k-i1)+(k-i2)+...+(k-im) = m*k-(i1+i2+...+im)

也就是说，当遍历下标 k 时，我们需要知道所有满足 S[i] = S[k+1] 的

- 下标 i 的出现次数 m
- 下标 i 之和

这可以借助两个哈希表来做到，在遍历下标 k 的同时，一个哈希表统计
S[k] 的出现次数，另一个哈希表统计值为 S[k] 的下标之和。
"""


# @lc code=start
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        xors = [0] * (n + 1)
        for i in range(n):
            xors[i + 1] = xors[i] ^ arr[i]

        ans = 0
        cnt, tot = Counter(), Counter()
        for k in range(n):
            if xors[k + 1] in cnt:
                ans += cnt[xors[k + 1]] * k - tot[xors[k + 1]]
            cnt[xors[k]] += 1
            tot[xors[k]] += k

        return ans


# @lc code=end

# class Solution:
#     def countTriplets(self, arr: List[int]) -> int:
#         n = len(arr)
#         xors = [0] * (n + 1)
#         for i in range(n):
#             xors[i + 1] = xors[i] ^ arr[i]

#         ans = 0
#         for i in range(n - 1):
#             for k in range(i + 1, n):
#                 if xors[i] == xors[k + 1]:
#                     ans += k - i

#         return ans

# class Solution:
#     def countTriplets(self, arr: List[int]) -> int:
#         n = len(arr)
#         xors = [0] * (n + 1)
#         for i in range(n):
#             xors[i + 1] = xors[i] ^ arr[i]

#         indices = defaultdict(list)
#         for i in range(n):
#             indices[xors[i + 1]].append(i)

#         ans = 0
#         for i in range(n - 1):
#             for j in range(i + 1, n):
#                 k = bisect.bisect_left(indices[xors[i]], j)
#                 ans += len(indices[xors[i]]) - k

#         return ans

# class Solution:
#     def countTriplets(self, arr: List[int]) -> int:
#         n = len(arr)
#         xors = [0] * (n + 1)
#         for i in range(n):
#             xors[i + 1] = xors[i] ^ arr[i]

#         ans = 0
#         for i in range(n - 1):
#             for j in range(i + 1, n):
#                 a = xors[j] ^ xors[i]
#                 for k in range(j, n):
#                     b = xors[k + 1] ^ xors[j]
#                     if a == b:
#                         ans += 1

#         return ans

if __name__ == '__main__':
    solu = Solution()
    print(solu.countTriplets(arr=[2, 3, 1, 6, 7]))
    print(solu.countTriplets(arr=[1, 1, 1, 1, 1]))
    print(solu.countTriplets(arr=[2, 3]))
    print(solu.countTriplets(arr=[1, 3, 5, 7, 9]))
    print(solu.countTriplets(arr=[7, 11, 12, 9, 5, 2, 7, 17, 22]))
