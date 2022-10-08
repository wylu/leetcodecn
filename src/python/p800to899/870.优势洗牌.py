#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   870.优势洗牌.py
@Time    :   2022/10/08 21:37:38
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
#
# @lc app=leetcode.cn id=870 lang=python3
#
# [870] 优势洗牌
#
# https://leetcode.cn/problems/advantage-shuffle/description/
#
# algorithms
# Medium (47.60%)
# Likes:    316
# Dislikes: 0
# Total Accepted:    50.2K
# Total Submissions: 102.5K
# Testcase Example:  '[2,7,11,15]\n[1,10,4,11]'
#
# 给定两个大小相等的数组 nums1 和 nums2，nums1 相对于 nums2 的优势可以用满足 nums1[i] > nums2[i] 的索引 i
# 的数目来描述。
#
# 返回 nums1 的任意排列，使其相对于 nums2 的优势最大化。
#
#
#
# 示例 1：
#
#
# 输入：nums1 = [2,7,11,15], nums2 = [1,10,4,11]
# 输出：[2,11,7,15]
#
#
# 示例 2：
#
#
# 输入：nums1 = [12,24,8,32], nums2 = [13,25,32,11]
# 输出：[24,32,8,12]
#
#
#
#
# 提示：
#
#
# 1 <= nums1.length <= 10^5
# nums2.length == nums1.length
# 0 <= nums1[i], nums2[i] <= 10^9
#
#
#
from typing import List


# @lc code=start
class Solution:

    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        idx1 = sorted(range(n), key=lambda x: nums1[x])
        idx2 = sorted(range(n), key=lambda x: nums2[x])

        ans = [0] * n
        left, right = 0, n - 1
        for i in range(n):
            if nums1[idx1[i]] > nums2[idx2[left]]:
                ans[idx2[left]] = nums1[idx1[i]]
                left += 1
            else:
                ans[idx2[right]] = nums1[idx1[i]]
                right -= 1

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    nums1 = [2, 7, 11, 15]
    nums2 = [1, 10, 4, 11]
    print(solu.advantageCount(nums1, nums2))

    nums1 = [12, 24, 8, 32]
    nums2 = [13, 25, 32, 11]
    print(solu.advantageCount(nums1, nums2))
