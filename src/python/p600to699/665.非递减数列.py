#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   665.非递减数列.py
@Time    :   2021/02/07 14:38:26
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#
# https://leetcode-cn.com/problems/non-decreasing-array/description/
#
# algorithms
# Easy (25.04%)
# Likes:    473
# Dislikes: 0
# Total Accepted:    47K
# Total Submissions: 187.7K
# Testcase Example:  '[4,2,3]'
#
# 给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
#
# 我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。
#
#
#
# 示例 1:
#
# 输入: nums = [4,2,3]
# 输出: true
# 解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
#
#
# 示例 2:
#
# 输入: nums = [4,2,1]
# 输出: false
# 解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
#
#
#
#
# 说明：
#
#
# 1 <= n <= 10 ^ 4
# - 10 ^ 5 <= nums[i] <= 10 ^ 5
#
#
#
from typing import List


# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt = 0
        for i in range(1, len(nums)):
            x, y = nums[i - 1], nums[i]
            if x > y:
                cnt += 1
                if cnt > 1:
                    return False
                if i > 1 and y < nums[i - 2]:
                    nums[i] = x
        return True


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.checkPossibility([4, 2, 3]))
    print(solu.checkPossibility([4, 2, 1]))
    print(solu.checkPossibility([3, 4, 2, 3]))
