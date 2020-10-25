#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5547.等差子数组.py
@Time    :   2020/10/25 10:38:54
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], lt: List[int],
                                 rt: List[int]) -> List[bool]:
        ans = [True] * len(lt)
        for i in range(len(lt)):
            if rt[i] == lt[i]:
                ans[i] = False
                continue

            tmp = nums[lt[i]:rt[i] + 1]
            tmp.sort()

            d = tmp[1] - tmp[0]
            for j in range(2, len(tmp)):
                if tmp[j] - tmp[j - 1] != d:
                    ans[i] = False
                    break

        return ans


if __name__ == "__main__":
    solu = Solution()
    nums = [4, 6, 5, 9, 3, 7]
    lt = [0, 0, 2]
    rt = [2, 3, 5]
    print(solu.checkArithmeticSubarrays(nums, lt, rt))
