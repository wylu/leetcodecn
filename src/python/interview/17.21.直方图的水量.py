#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   17.21.直方图的水量.py
@Time    :   2021/04/02 22:00:48
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :

找到数组中从下标 i 到最左端最高的条形块高度 left_max。
找到数组中从下标 i 到最右端最高的条形块高度 right_max。
扫描数组 height 并更新答案：
  累加 min(max_left[i],max_right[i])−height[i] 到 ans 上
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        lefts, rights = [0] * n, [0] * n
        lefts[0], rights[-1] = height[0], height[-1]
        for i in range(1, n):
            lefts[i] = max(height[i], lefts[i - 1])
            rights[n - 1 - i] = max(height[n - 1 - i], rights[n - i])

        ans = 0
        for i in range(1, n - 1):
            ans += min(lefts[i], rights[i]) - height[i]

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
