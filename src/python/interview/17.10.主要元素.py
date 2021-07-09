#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   17.10.主要元素.py
@Time    :   2021/07/09 12:40:08
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, cnt = -1, 0
        for num in nums:
            if cnt == 0:
                candidate = num
            cnt += 1 if num == candidate else -1

        cnt = sum(1 for num in nums if num == candidate)

        return candidate if cnt > len(nums) / 2 else -1


if __name__ == '__main__':
    solu = Solution()
    print(solu.majorityElement([1, 2, 5, 9, 5, 9, 5, 5, 5]))
    print(solu.majorityElement([3, 2]))
    print(solu.majorityElement([2, 2, 1, 1, 1, 2, 2]))
