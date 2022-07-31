#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6133.分组的最大数量.py
@Time    :   2022/07/31 10:35:52
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def maximumGroups(self, grades: List[int]) -> int:
        grades.sort()
        ans = 1
        pre_sum, pre_cnt = grades[0], 1
        i, n = 1, len(grades)

        while i < n:
            cur_sum, cur_cnt = 0, 0
            while i < n and (cur_sum <= pre_sum or cur_cnt <= pre_cnt):
                cur_sum += grades[i]
                cur_cnt += 1
                i += 1

            if cur_sum > pre_sum and cur_cnt > pre_cnt:
                ans += 1
                pre_sum, pre_cnt = cur_sum, cur_cnt

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.maximumGroups(grades=[10, 6, 12, 7, 3, 5]))
    print(solu.maximumGroups(grades=[8, 8]))

    print(solu.maximumGroups(grades=[47, 2, 16, 17, 41, 4, 38, 23, 47]))
