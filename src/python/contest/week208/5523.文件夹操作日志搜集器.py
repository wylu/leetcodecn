#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5523.文件夹操作日志搜集器.py
@Time    :   2020/09/27 10:31:52
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for log in logs:
            if log == './':
                continue
            if log == '../':
                if ans > 0:
                    ans -= 1
            else:
                ans += 1
        return ans
