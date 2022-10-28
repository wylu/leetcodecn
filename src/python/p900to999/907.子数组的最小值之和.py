#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   907.子数组的最小值之和.py
@Time    :   2022/10/28 14:53:56
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
#
# @lc app=leetcode.cn id=907 lang=python3
#
# [907] 子数组的最小值之和
#
# https://leetcode.cn/problems/sum-of-subarray-minimums/description/
#
# algorithms
# Medium (35.17%)
# Likes:    517
# Dislikes: 0
# Total Accepted:    31.7K
# Total Submissions: 86.2K
# Testcase Example:  '[3,1,2,4]'
#
# 给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。
#
# 由于答案可能很大，因此 返回答案模 10^9 + 7 。
#
#
#
# 示例 1：
#
#
# 输入：arr = [3,1,2,4]
# 输出：17
# 解释：
# 子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
# 最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
#
# 示例 2：
#
#
# 输入：arr = [11,81,94,43,3]
# 输出：444
#
#
#
#
# 提示：
#
#
# 1 <= arr.length <= 3 * 10^4
# 1 <= arr[i] <= 3 * 10^4
#
#
from typing import List


# @lc code=start
class Solution:

    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        stk, dp = [], [0] * n
        ans, MOD = 0, 10**9 + 7

        for i, x in enumerate(arr):
            while stk and arr[stk[-1]] > x:
                stk.pop()

            k = i - stk[-1] if stk else i + 1
            dp[i] = k * x + (dp[i - k] if stk else 0)
            ans = (ans + dp[i]) % MOD
            stk.append(i)

        return ans


# @lc code=end

# class Solution:

#     def sumSubarrayMins(self, arr: List[int]) -> int:
#         n = len(arr)
#         # 以当前元素为最右边且最小的元素，计算左右边界
#         lefts, rights = [0] * n, [n - 1] * n

#         sl, sr = [0], [n - 1]
#         for i in range(1, n):
#             while sl and arr[sl[-1]] >= arr[i]:
#                 sl.pop()
#             while sr and arr[sr[-1]] > arr[n - i - 1]:
#                 sr.pop()
#             if sl:
#                 lefts[i] = sl[-1] + 1
#             if sr:
#                 rights[n - i - 1] = sr[-1] - 1
#             sl.append(i)
#             sr.append(n - i - 1)

#         ans, MOD = 0, 10**9 + 7
#         for i in range(n):
#             lt = i - lefts[i] + 1
#             rt = rights[i] - i + 1
#             ans = (ans + lt * rt * arr[i]) % MOD

#         return ans

if __name__ == '__main__':
    solu = Solution()
    print(solu.sumSubarrayMins(arr=[3, 1, 2, 4]))
    print(solu.sumSubarrayMins(arr=[11, 81, 94, 43, 3]))
    print(solu.sumSubarrayMins(arr=[71, 55, 82, 55]))
