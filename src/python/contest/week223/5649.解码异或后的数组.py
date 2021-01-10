#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5649.解码异或后的数组.py
@Time    :   2021/01/10 10:37:53
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        for i in range(len(encoded)):
            ans.append(encoded[i] ^ ans[i])
        return ans
