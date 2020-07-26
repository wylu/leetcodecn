#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   存在重复元素.py
@Time    :   2020/07/26 09:34:30
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for e in nums:
            if e in s:
                return True
            s.add(e)
        return False
