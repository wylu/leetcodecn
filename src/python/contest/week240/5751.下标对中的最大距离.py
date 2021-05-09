#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5751.下标对中的最大距离.py
@Time    :   2021/05/09 10:56:20
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        m, n = len(nums1), len(nums2)
        for i in range(m - 1):
            if i >= n - 1:
                break

            left, right = i + 1, n - 1
            while left < right:
                mid = (left + right + 1) // 2
                if nums2[mid] >= nums1[i]:
                    left = mid
                else:
                    right = mid - 1

            if nums2[left] >= nums1[i]:
                ans = max(ans, left - i)
        return ans


if __name__ == '__main__':
    solu = Solution()
    nums1 = [
        9819, 9508, 7398, 7347, 6337, 5756, 5493, 5446, 5123, 3215, 1597, 774,
        368, 313
    ]
    nums2 = [
        9933, 9813, 9770, 9697, 9514, 9490, 9441, 9439, 8939, 8754, 8665, 8560
    ]
    print(solu.maxDistance(nums1, nums2))
