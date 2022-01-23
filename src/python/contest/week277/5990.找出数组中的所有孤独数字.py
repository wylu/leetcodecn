#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5990.找出数组中的所有孤独数字.py
@Time    :   2022/01/23 10:44:51
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class Solution:

    def findLonely(self, nums: List[int]) -> List[int]:
        cnts = defaultdict(int)
        for num in nums:
            cnts[num] += 1

        ans = []
        for num, cnt in cnts.items():
            if cnt == 1 and num - 1 not in cnts and num + 1 not in cnts:
                ans.append(num)

        return ans
