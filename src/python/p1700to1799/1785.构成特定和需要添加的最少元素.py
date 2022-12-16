#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1785.构成特定和需要添加的最少元素.py
@Time    :   2022/12/16 17:22:28
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
#
# @lc app=leetcode.cn id=1785 lang=python3
#
# [1785] 构成特定和需要添加的最少元素
#
# https://leetcode.cn/problems/minimum-elements-to-add-to-form-a-given-sum/description/
#
# algorithms
# Medium (36.51%)
# Likes:    40
# Dislikes: 0
# Total Accepted:    20.5K
# Total Submissions: 48.8K
# Testcase Example:  '[1,-1,1]\n3\n-4'
#
# 给你一个整数数组 nums ，和两个整数 limit 与 goal 。数组 nums 有一条重要属性：abs(nums[i])  。
#
# 返回使数组元素总和等于 goal 所需要向数组中添加的 最少元素数量 ，添加元素 不应改变 数组中 abs(nums[i])  这一属性。
#
# 注意，如果 x >= 0 ，那么 abs(x) 等于 x ；否则，等于 -x 。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,-1,1], limit = 3, goal = -4
# 输出：2
# 解释：可以将 -2 和 -3 添加到数组中，数组的元素总和变为 1 - 1 + 1 - 2 - 3 = -4 。
#
#
# 示例 2：
#
#
# 输入：nums = [1,-10,9,1], limit = 100, goal = 0
# 输出：1
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# 1 <= limit <= 10^6
# -limit <= nums[i] <= limit
# -10^9 <= goal <= 10^9
#
#
#
from typing import List


# @lc code=start
class Solution:

    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        return (abs(sum(nums) - goal) + limit - 1) // limit


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    nums = [1, -1, 1]
    limit = 3
    goal = -4
    print(solu.minElements(nums, limit, goal))

    nums = [1, -10, 9, 1]
    limit = 100
    goal = 0
    print(solu.minElements(nums, limit, goal))
