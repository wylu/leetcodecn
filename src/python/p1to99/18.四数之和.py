#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   18.四数之和.py
@Time    :   2020/09/24 19:53:17
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# https://leetcode-cn.com/problems/4sum/description/
#
# algorithms
# Medium (38.43%)
# Likes:    571
# Dislikes: 0
# Total Accepted:    109.1K
# Total Submissions: 283.9K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c
# + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
# 注意：
#
# 答案中不可以包含重复的四元组。
#
# 示例：
#
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
#
# 满足要求的四元组集合为：
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
#
#
#
from typing import List
"""
双指针

详见 [15] 三数之和 https://leetcode-cn.com/problems/3sum/
"""


# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans, n = [], len(nums)
        nums.sort()

        # 枚举 a
        for a in range(n - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            # 枚举 b
            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                # d 对应的指针初始指向数组的最右端
                d = n - 1

                # 枚举 c
                for c in range(b + 1, n - 1):
                    if c > b + 1 and nums[c] == nums[c - 1]:
                        continue

                    while (c < d
                           and nums[a] + nums[b] + nums[c] + nums[d] > target):
                        d -= 1

                    if c == d:
                        break

                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        ans.append([nums[a], nums[b], nums[c], nums[d]])

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.fourSum([1, 0, -1, 0, -2, 2], 0))
