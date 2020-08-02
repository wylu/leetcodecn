#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   打乱数组.py
@Time    :   2020/08/02 16:50:06
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
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
