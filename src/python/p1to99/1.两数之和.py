#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1.两数之和.py
@Time    :   2020/09/24 11:32:08
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# https://leetcode-cn.com/problems/two-sum/description/
#
# algorithms
# Easy (49.42%)
# Likes:    9201
# Dislikes: 0
# Total Accepted:    1.4M
# Total Submissions: 2.8M
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#
#
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#
#
#
from typing import List


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in indices:
                return [indices[need], i]
            indices[num] = i
        return [-1, -1]


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.twoSum([2, 7, 11, 15], 9))
