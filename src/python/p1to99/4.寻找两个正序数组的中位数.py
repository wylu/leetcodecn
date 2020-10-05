#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   4.寻找两个正序数组的中位数.py
@Time    :   2020/10/05 19:02:38
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (38.80%)
# Likes:    3266
# Dislikes: 0
# Total Accepted:    267.8K
# Total Submissions: 690K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。
#
# 进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
#
#
#
# 示例 1：
#
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#
#
# 示例 2：
#
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#
#
# 示例 3：
#
# 输入：nums1 = [0,0], nums2 = [0,0]
# 输出：0.00000
#
#
# 示例 4：
#
# 输入：nums1 = [], nums2 = [1]
# 输出：1.00000
#
#
# 示例 5：
#
# 输入：nums1 = [2], nums2 = []
# 输出：2.00000
#
#
#
#
# 提示：
#
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
#
#
#
from typing import List
"""
二分查找

https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/
"""


# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        totLeft = (m + n + 1) // 2

        left, right = 0, m
        while left < right:
            i = (left + right + 1) // 2
            j = totLeft - i
            if nums1[i - 1] <= nums2[j]:
                left = i
            else:
                right = i - 1

        i = (left + right + 1) // 2
        j = totLeft - i
        INT_MIN, INT_MAX = -0x8FFFFFFF, 0x7FFFFFFF
        maxLeft1 = INT_MIN if i == 0 else nums1[i - 1]
        minRight1 = INT_MAX if i == m else nums1[i]
        maxLeft2 = INT_MIN if j == 0 else nums2[j - 1]
        minRight2 = INT_MAX if j == n else nums2[j]

        if (m + n) % 2 == 0:
            return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
        return max(maxLeft1, maxLeft2)


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.findMedianSortedArrays([1, 3], [2]))
    print(solu.findMedianSortedArrays([1, 2], [3, 4]))
    print(solu.findMedianSortedArrays([0, 0], [0, 0]))
    print(solu.findMedianSortedArrays([], [1]))
    print(solu.findMedianSortedArrays([2], []))
