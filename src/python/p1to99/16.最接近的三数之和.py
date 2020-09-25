#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   16.最接近的三数之和.py
@Time    :   2020/09/25 13:34:30
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.83%)
# Likes:    580
# Dislikes: 0
# Total Accepted:    155.8K
# Total Submissions: 340.1K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
#
#
# 示例：
#
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#
#
#
#
# 提示：
#
#
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4
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
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans, n = sum(nums[:3]), len(nums)

        for a in range(n - 2):
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            c = n - 1

            for b in range(a + 1, n - 1):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                while b < c and nums[a] + nums[b] + nums[c] > target:
                    if (nums[a] + nums[b] + nums[c] - target <
                            abs(ans - target)):
                        ans = nums[a] + nums[b] + nums[c]
                    c -= 1

                if b == c:
                    break

                if (abs(nums[a] + nums[b] + nums[c] - target) <
                        abs(ans - target)):
                    ans = nums[a] + nums[b] + nums[c]

                if ans == target:
                    return ans

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.threeSumClosest([-1, 2, 1, -4], 1))
