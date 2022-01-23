#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5989.元素计数.py
@Time    :   2022/01/23 10:30:19
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class Solution:

    def countElements(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1

        arr = [(key, value) for key, value in cnt.items()]
        arr.sort()

        ans = 0
        for _, value in arr[1:-1]:
            ans += value

        return ans
