#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5761.找出和为指定值的下标对.py
@Time    :   2021/05/16 11:17:09
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.val2idx = defaultdict(set)
        for idx, num in enumerate(nums2):
            self.val2idx[num].add(idx)

    def add(self, index: int, val: int) -> None:
        self.val2idx[self.nums2[index]].discard(index)
        self.nums2[index] += val
        self.val2idx[self.nums2[index]].add(index)

    def count(self, tot: int) -> int:
        ans = 0
        for num in self.nums1:
            ans += len(self.val2idx[tot - num])
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
