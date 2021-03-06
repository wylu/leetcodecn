#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1537.最大得分.py
@Time    :   2020/08/04 17:50:33
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1537 lang=python3
#
# [1537] 最大得分
#
# https://leetcode-cn.com/problems/get-the-maximum-score/description/
#
# algorithms
# Hard (33.46%)
# Likes:    15
# Dislikes: 0
# Total Accepted:    2.5K
# Total Submissions: 7.3K
# Testcase Example:  '[2,4,5,8,10]\n[4,6,8,9]'
#
# 你有两个 有序 且数组内元素互不相同的数组 nums1 和 nums2 。
#
# 一条 合法路径 定义如下：
#
#
# 选择数组 nums1 或者 nums2 开始遍历（从下标 0 处开始）。
# 从左到右遍历当前数组。
# 如果你遇到了 nums1 和 nums2 中都存在的值，那么你可以切换路径到另一个数组对应数字处继续遍历（但在合法路径中重复数字只会被统计一次）。
#
#
# 得分定义为合法路径中不同数字的和。
#
# 请你返回所有可能合法路径中的最大得分。
#
# 由于答案可能很大，请你将它对 10^9 + 7 取余后返回。
#
#
#
# 示例 1：
#
#
#
# 输入：nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]
# 输出：30
# 解释：合法路径包括：
# [2,4,5,8,10], [2,4,5,8,9], [2,4,6,8,9], [2,4,6,8,10],（从 nums1 开始遍历）
# [4,6,8,9], [4,5,8,10], [4,5,8,9], [4,6,8,10]  （从 nums2 开始遍历）
# 最大得分为上图中的绿色路径 [2,4,6,8,10] 。
#
#
# 示例 2：
#
# 输入：nums1 = [1,3,5,7,9], nums2 = [3,5,100]
# 输出：109
# 解释：最大得分由路径 [1,3,5,100] 得到。
#
#
# 示例 3：
#
# 输入：nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10]
# 输出：40
# 解释：nums1 和 nums2 之间无相同数字。
# 最大得分由路径 [6,7,8,9,10] 得到。
#
#
# 示例 4：
#
# 输入：nums1 = [1,4,5,8,9,11,19], nums2 = [2,3,4,11,12]
# 输出：61
#
#
#
#
# 提示：
#
#
# 1 <= nums1.length <= 10^5
# 1 <= nums2.length <= 10^5
# 1 <= nums1[i], nums2[i] <= 10^7
# nums1 和 nums2 都是严格递增的数组。
#
#
#
from typing import List


# @lc code=start
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        s1, s2 = 0, 0
        i, j = 0, 0

        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                s1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                s2 += nums2[j]
                j += 1
            else:
                s1 = s2 = max(s1 + nums1[i], s2 + nums2[j])
                i += 1
                j += 1

        while i < n1:
            s1 += nums1[i]
            i += 1

        while j < n2:
            s2 += nums2[j]
            j += 1

        return max(s1, s2) % (10**9 + 7)


# @lc code=end
