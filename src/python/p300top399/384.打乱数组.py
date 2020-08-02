#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   384.打乱数组.py
@Time    :   2020/08/02 19:49:03
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=384 lang=python3
#
# [384] 打乱数组
#
# https://leetcode-cn.com/problems/shuffle-an-array/description/
#
# algorithms
# Medium (52.39%)
# Likes:    83
# Dislikes: 0
# Total Accepted:    23.3K
# Total Submissions: 44.3K
# Testcase Example:
# '["Solution","shuffle","reset","shuffle"]\n[[[1,2,3]],[],[],[]]'
#
# 打乱一个没有重复元素的数组。
#
#
#
# 示例:
#
# // 以数字集合 1, 2 和 3 初始化数组。
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);
#
# // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
# solution.shuffle();
#
# // 重设数组到它的初始状态[1,2,3]。
# solution.reset();
#
# // 随机返回数组[1,2,3]打乱后的结果。
# solution.shuffle();
#
#
#

# @lc code=start
from random import randrange
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.origin = nums if nums else []
        self.nums = self.origin[:]
        self.size = len(self.nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.origin[:]
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(self.size):
            j = randrange(i, self.size)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end
