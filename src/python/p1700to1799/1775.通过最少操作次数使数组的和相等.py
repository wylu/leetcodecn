#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1775.通过最少操作次数使数组的和相等.py
@Time    :   2022/12/07 16:02:22
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
#
# @lc app=leetcode.cn id=1775 lang=python3
#
# [1775] 通过最少操作次数使数组的和相等
#
# https://leetcode.cn/problems/equal-sum-arrays-with-minimum-number-of-operations/description/
#
# algorithms
# Medium (48.92%)
# Likes:    115
# Dislikes: 0
# Total Accepted:    14.7K
# Total Submissions: 26.7K
# Testcase Example:  '[1,2,3,4,5,6]\n[1,1,2,2,2,2]'
#
# 给你两个长度可能不等的整数数组 nums1 和 nums2 。两个数组中的所有值都在 1 到 6 之间（包含 1 和 6）。
#
# 每次操作中，你可以选择 任意 数组中的任意一个整数，将它变成 1 到 6 之间 任意 的值（包含 1 和 6）。
#
# 请你返回使 nums1 中所有数的和与 nums2 中所有数的和相等的最少操作次数。如果无法使两个数组的和相等，请返回 -1 。
#
#
#
# 示例 1：
#
# 输入：nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
# 输出：3
# 解释：你可以通过 3 次操作使 nums1 中所有数的和与 nums2 中所有数的和相等。以下数组下标都从 0 开始。
# - 将 nums2[0] 变为 6 。 nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2] 。
# - 将 nums1[5] 变为 1 。 nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2] 。
# - 将 nums1[2] 变为 2 。 nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2] 。
#
#
# 示例 2：
#
# 输入：nums1 = [1,1,1,1,1,1,1], nums2 = [6]
# 输出：-1
# 解释：没有办法减少 nums1 的和或者增加 nums2 的和使二者相等。
#
#
# 示例 3：
#
# 输入：nums1 = [6,6], nums2 = [1]
# 输出：3
# 解释：你可以通过 3 次操作使 nums1 中所有数的和与 nums2 中所有数的和相等。以下数组下标都从 0 开始。
# - 将 nums1[0] 变为 2 。 nums1 = [2,6], nums2 = [1] 。
# - 将 nums1[1] 变为 2 。 nums1 = [2,2], nums2 = [1] 。
# - 将 nums2[0] 变为 4 。 nums1 = [2,2], nums2 = [4] 。
#
#
#
#
# 提示：
#
#
# 1 <= nums1.length, nums2.length <= 10^5
# 1 <= nums1[i], nums2[i] <= 6
#
#
#
from typing import List


# @lc code=start
class Solution:

    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.minOperations(nums2, nums1)

        if m * 6 < n:
            return -1

        s1, s2 = sum(nums1), sum(nums2)
        if s1 > s2:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        ans, gap = 0, abs(s1 - s2)
        nums1.sort()
        nums2.sort(reverse=True)
        i = j = 0
        while gap and (i < m or j < n):
            d1 = 6 - nums1[i] if i < m else 0
            d2 = nums2[j] - 1 if j < n else 0
            if d1 >= d2:
                gap -= min(d1, gap)
                i += 1
            else:
                gap -= min(d2, gap)
                j += 1
            ans += 1

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    nums1 = [1, 2, 3, 4, 5, 6]
    nums2 = [1, 1, 2, 2, 2, 2]
    print(solu.minOperations(nums1, nums2))

    nums1 = [1, 1, 1, 1, 1, 1, 1]
    nums2 = [6]
    print(solu.minOperations(nums1, nums2))

    nums1 = [6, 6]
    nums2 = [1]
    print(solu.minOperations(nums1, nums2))
