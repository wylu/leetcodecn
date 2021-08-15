#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5832.构造元素不等于两相邻元素平均值的数组.py
@Time    :   2021/08/15 10:31:53
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import deque
from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums = deque(nums)

        ans = deque([nums.popleft(), nums.popleft()])
        while nums:
            if ans[-1] == (nums[0] + ans[-2]) / 2:
                if len(nums) == 1:
                    ans.appendleft(nums.pop())
                else:
                    ans.append(nums.pop())
            else:
                ans.append(nums.popleft())

        return list(ans)


if __name__ == '__main__':
    solu = Solution()
    print(solu.rearrangeArray(nums=[1, 2, 3, 4, 5]))
    print(solu.rearrangeArray(nums=[6, 2, 0, 9, 7]))
    print(solu.rearrangeArray(nums=[1, 3, 5, 7, 9]))
    print(solu.rearrangeArray(nums=[2, 4, 6, 8, 10]))
    print(solu.rearrangeArray(nums=[2, 4, 6, 8, 12]))
    print(solu.rearrangeArray(nums=[2, 4, 6, 8]))
    print(solu.rearrangeArray(nums=[1, 5, 2, 6, 3, 7, 4, 8]))
    print(solu.rearrangeArray(nums=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]))
    print(solu.rearrangeArray(nums=[5, 1, 7, 3]))
    print(solu.rearrangeArray(nums=[9, 17, 4, 6, 13, 12, 5, 19, 18, 0]))
