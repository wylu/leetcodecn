#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   801.使序列递增的最小交换次数.py
@Time    :   2022/10/10 19:32:52
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
#
# @lc app=leetcode.cn id=801 lang=python3
#
# [801] 使序列递增的最小交换次数
#
# https://leetcode.cn/problems/minimum-swaps-to-make-sequences-increasing/description/
#
# algorithms
# Hard (48.23%)
# Likes:    375
# Dislikes: 0
# Total Accepted:    22.2K
# Total Submissions: 46K
# Testcase Example:  '[1,3,5,4]\n[1,2,3,7]'
#
# 我们有两个长度相等且不为空的整型数组 nums1 和 nums2 。在一次操作中，我们可以交换 nums1[i] 和 nums2[i]的元素。
#
#
# 例如，如果 nums1 = [1,2,3,8] ， nums2 =[5,6,7,4] ，你可以交换 i = 3 处的元素，得到 nums1
# =[1,2,3,4] 和 nums2 =[5,6,7,8] 。
#
#
# 返回 使 nums1 和 nums2 严格递增 所需操作的最小次数 。
#
# 数组 arr 严格递增 且  arr[0] < arr[1] < arr[2] < ... < arr[arr.length - 1] 。
#
# 注意：
#
#
# 用例保证可以实现操作。
#
#
#
#
# 示例 1:
#
#
# 输入: nums1 = [1,3,5,4], nums2 = [1,2,3,7]
# 输出: 1
# 解释:
# 交换 A[3] 和 B[3] 后，两个数组如下:
# A = [1, 3, 5, 7] ， B = [1, 2, 3, 4]
# 两个数组均为严格递增的。
#
# 示例 2:
#
#
# 输入: nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]
# 输出: 1
#
#
#
#
# 提示:
#
#
# 2 <= nums1.length <= 10^5
# nums2.length == nums1.length
# 0 <= nums1[i], nums2[i] <= 2 * 10^5
#
#
#
from typing import List


# @lc code=start
class Solution:

    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        a, b = 0, 1

        for i in range(1, len(nums1)):
            pa, pb = a, b

            flag1 = nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]
            flag2 = nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]

            if flag1 and flag2:
                a, b = min(pa, pb), min(pa, pb) + 1
            elif flag1 and not flag2:
                a, b = pa, pb + 1
            elif not flag1 and flag2:
                a, b = pb, pa + 1

        return min(a, b)


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    nums1 = [1, 3, 5, 4]
    nums2 = [1, 2, 3, 7]
    print(solu.minSwap(nums1, nums2))

    nums1 = [0, 3, 5, 8, 9]
    nums2 = [2, 1, 4, 6, 9]
    print(solu.minSwap(nums1, nums2))
