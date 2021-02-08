#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   978.最长湍流子数组.py
@Time    :   2021/02/08 23:00:32
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=978 lang=python3
#
# [978] 最长湍流子数组
#
# https://leetcode-cn.com/problems/longest-turbulent-subarray/description/
#
# algorithms
# Medium (46.74%)
# Likes:    143
# Dislikes: 0
# Total Accepted:    32.7K
# Total Submissions: 70.1K
# Testcase Example:  '[9,4,2,10,7,8,8,1,9]'
#
# 当 A 的子数组 A[i], A[i+1], ..., A[j] 满足下列条件时，我们称其为湍流子数组：
#
#
# 若 i <= k < j，当 k 为奇数时， A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]；
# 或 若 i <= k < j，当 k 为偶数时，A[k] > A[k+1] ，且当 k 为奇数时， A[k] < A[k+1]。
#
#
# 也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。
#
# 返回 A 的最大湍流子数组的长度。
#
#
#
# 示例 1：
#
# 输入：[9,4,2,10,7,8,8,1,9]
# 输出：5
# 解释：(A[1] > A[2] < A[3] > A[4] < A[5])
#
#
# 示例 2：
#
# 输入：[4,8,12,16]
# 输出：2
#
#
# 示例 3：
#
# 输入：[100]
# 输出：1
#
#
#
#
# 提示：
#
#
# 1 <= A.length <= 40000
# 0 <= A[i] <= 10^9
#
#
#
from typing import List
"""
方法一：滑动窗口
设数组 arr 的长度为 n，窗口 [left, right] (0 <= left <= right <= n−1)
为当前的窗口，窗口内构成了一个「湍流子数组」。随后，我们要考虑下一个窗口的
位置。

根据「湍流子数组」的定义，当 0 < right < n−1 时：

如果 arr[right−1] < arr[right] 且 arr[right] > arr[right+1]，则
[left, right+1] 也构成「湍流子数组」，因此需要将 right 右移一个单位；

如果 arr[right−1] > arr[right] 且 arr[right] < arr[right+1]，同理，
也需要将 right 右移一个单位；

否则，[right−1, right+1] 无法构成「湍流子数组」，当 left < right 时，
[left, right+1] 也无法构成「湍流子数组」，因此需要将 left 移到 right，
即令 left = right。

此外，我们还需要特殊考虑窗口长度为 1 (即 left 和 right 相等的情况)：
只要 arr[right] != arr[right+1]，就可以将 right 右移一个单位；
否则，left 和 right 都要同时右移。
"""


# @lc code=start
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 1
        left = right = 0

        while right < n - 1:
            if left == right:
                if arr[left] == arr[left + 1]:
                    left += 1
                right += 1
            else:
                if ((arr[right - 1] < arr[right]
                     and arr[right] > arr[right + 1])
                        or (arr[right - 1] > arr[right]
                            and arr[right] < arr[right + 1])):
                    right += 1
                else:
                    left = right
            ans = max(ans, right - left + 1)
        return ans


# @lc code=end
