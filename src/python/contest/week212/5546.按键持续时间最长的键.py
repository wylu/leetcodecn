#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5546.按键持续时间最长的键.py
@Time    :   2020/10/25 10:30:48
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        ts = [0] * 26

        maxTime = ts[ord(keysPressed[0]) - ord('a')] = releaseTimes[0]
        for i in range(1, len(keysPressed)):
            ch = ord(keysPressed[i]) - ord('a')
            rt = releaseTimes[i] - releaseTimes[i - 1]
            ts[ch] = max(ts[ch], rt)
            maxTime = max(maxTime, ts[ch])

        ans = [i for i, t in enumerate(ts) if t == maxTime]
        ans.sort()

        return chr(ans[-1] + ord('a'))
