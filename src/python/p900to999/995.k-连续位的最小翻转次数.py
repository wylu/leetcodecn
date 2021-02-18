#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   995.k-连续位的最小翻转次数.py
@Time    :   2021/02/18 21:03:37
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=995 lang=python3
#
# [995] K 连续位的最小翻转次数
#
# https://leetcode-cn.com/problems/minimum-number-of-k-consecutive-bit-flips/description/
#
# algorithms
# Hard (51.95%)
# Likes:    164
# Dislikes: 0
# Total Accepted:    14.5K
# Total Submissions: 28K
# Testcase Example:  '[0,1,0]\n1'
#
# 在仅包含 0 和 1 的数组 A 中，一次 K 位翻转包括选择一个长度为 K 的（连续）子数组，同时将子数组中的每个 0 更改为 1，而每个 1 更改为
# 0。
#
# 返回所需的 K 位翻转的最小次数，以便数组没有值为 0 的元素。如果不可能，返回 -1。
#
#
#
# 示例 1：
#
#
# 输入：A = [0,1,0], K = 1
# 输出：2
# 解释：先翻转 A[0]，然后翻转 A[2]。
#
#
# 示例 2：
#
#
# 输入：A = [1,1,0], K = 2
# 输出：-1
# 解释：无论我们怎样翻转大小为 2 的子数组，我们都不能使数组变为 [1,1,1]。
#
#
# 示例 3：
#
#
# 输入：A = [0,0,0,1,0,1,1,0], K = 3
# 输出：3
# 解释：
# 翻转 A[0],A[1],A[2]: A变成 [1,1,1,1,0,1,1,0]
# 翻转 A[4],A[5],A[6]: A变成 [1,1,1,1,1,0,0,0]
# 翻转 A[5],A[6],A[7]: A变成 [1,1,1,1,1,1,1,1]
#
#
#
#
# 提示：
#
#
# 1 <= A.length <= 30000
# 1 <= K <= A.length
#
#
#
from typing import List
"""
方法一：差分数组
由于对同一个子数组执行两次翻转操作不会改变该子数组，所以对每个长度为
K 的子数组，应至多执行一次翻转操作。

对于若干个 K 位翻转操作，改变先后顺序并不影响最终翻转的结果。不妨从
A[0] 开始考虑，若 A[0] = 0，则必定要翻转从位置 0 开始的子数组；
若 A[0] = 1，则不翻转从位置 0 开始的子数组。

按照这一策略，我们从左到右地执行这些翻转操作。由于翻转操作是唯一的，
若最终数组元素均为 1，则执行的翻转次数就是最小的。

用 N 表示数组 A 的长度。若直接模拟上述过程，复杂度将会是 O(NK) 的。
如何优化呢？

考虑不去翻转数字，而是统计每个数字需要翻转的次数。对于一次翻转操作，
相当于把子数组中所有数字的翻转次数加 1。

这启发我们用差分数组的思想来计算当前数字需要翻转的次数。我们可以维护
一个差分数组 diff，其中 diff[i] 表示两个相邻元素 A[i−1] 和 A[i]
的翻转次数的差，对于区间 [l,r]，将其元素全部加 1，只会影响到 l 和
r+1 处的差分值，故 diff[l] 增加 1，diff[r+1] 减少 1。

通过累加差分数组可以得到当前位置需要翻转的次数，我们用变量 revCnt
来表示这一累加值。

遍历到 A[i] 时，若 A[i]+revCnt 是偶数，则说明当前元素的实际值为 0，
需要翻转区间 [i,i+K-1]，我们可以直接将 revCnt 增加 1，diff[i+K]
减少 1。

注意到若 i+K > n 则无法执行翻转操作，此时应返回 -1。

方法二：滑动窗口
能否将空间复杂度优化至 O(1) 呢？

回顾方法一的代码，当遍历到位置 i 时，若能知道位置 i-K 上发生了翻转
操作，便可以直接修改 revCnt，从而去掉 diff 数组。

注意到 0 <= A[i] <= 1，我们可以用 A[i] 范围之外的数来表达「是否
翻转过」的含义。

具体来说，若要翻转从位置 i 开始的子数组，可以将 A[i] 加 2，这样当
遍历到位置 i' 时，若有 A[i'-K] > 1，则说明在位置 i'-K 上发生了
翻转操作。
"""


# @lc code=start
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        ans = cnt = 0
        for i in range(n):
            if i >= K and A[i - K] > 1:
                cnt ^= 1
                A[i - K] -= 2  # 复原数组元素，若允许修改数组 A，则可以省略
            if A[i] == cnt:
                if i + K > n:
                    return -1
                ans += 1
                cnt ^= 1
                A[i] += 2
        return ans


# @lc code=end

# class Solution:
#     def minKBitFlips(self, A: List[int], K: int) -> int:
#         n = len(A)
#         diff = [0] * (n + 1)
#         ans = cnt = 0
#         for i in range(n):
#             cnt += diff[i]
#             if (A[i] + cnt) % 2 == 0:
#                 if i + K > n:
#                     return -1
#                 ans += 1
#                 cnt += 1
#                 diff[i + K] -= 1
#         return ans

if __name__ == "__main__":
    solu = Solution()
    print(solu.minKBitFlips(A=[0, 1, 0, 0, 1, 0], K=4))
    print(solu.minKBitFlips(A=[1, 0, 0, 0, 0], K=2))
    print(solu.minKBitFlips(A=[0, 1, 0], K=1))
    print(solu.minKBitFlips(A=[1, 1, 0], K=2))
    print(solu.minKBitFlips(A=[0, 0, 0, 1, 0, 1, 1, 0], K=3))
