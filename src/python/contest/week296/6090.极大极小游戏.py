#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6090.极大极小游戏.py
@Time    :   2022/06/05 10:30:37
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def minMaxGame(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        ans = []
        for i in range(0, len(nums), 2):
            if (i // 2) % 2 == 0:
                ans.append(min(nums[i], nums[i + 1]))
            else:
                ans.append(max(nums[i], nums[i + 1]))

        return self.minMaxGame(ans)


if __name__ == '__main__':
    solu = Solution()
    print(solu.minMaxGame([70, 38, 21, 22]))
