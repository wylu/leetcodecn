#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   189.旋转数组.py
@Time    :   2021/01/08 21:47:48
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#
# https://leetcode-cn.com/problems/rotate-array/description/
#
# algorithms
# Medium (45.14%)
# Likes:    841
# Dislikes: 0
# Total Accepted:    213.4K
# Total Submissions: 472.9K
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#
#
# 示例 2:
#
# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释:
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
#
# 说明:
#
#
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的 原地 算法。
#
#
#
from typing import List


# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(i: int, j: int) -> None:
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        if not nums:
            return

        n = len(nums)
        k %= n
        reverse(0, n - k - 1)
        reverse(n - k, n - 1)
        reverse(0, n - 1)


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    nums = []
    solu.rotate(nums, 3)
    print(nums)

    nums = [1, 2, 3]
    solu.rotate(nums, 0)
    print(nums)

    nums = [1, 2, 3, 4, 5, 6, 7]
    solu.rotate(nums, 3)
    print(nums)

    nums = [-1, -100, 3, 99]
    solu.rotate(nums, 2)
    print(nums)
