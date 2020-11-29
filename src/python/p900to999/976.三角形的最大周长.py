#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   976.三角形的最大周长.py
@Time    :   2020/11/29 17:22:53
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=976 lang=python3
#
# [976] 三角形的最大周长
#
# https://leetcode-cn.com/problems/largest-perimeter-triangle/description/
#
# algorithms
# Easy (56.00%)
# Likes:    116
# Dislikes: 0
# Total Accepted:    36K
# Total Submissions: 60.7K
# Testcase Example:  '[2,1,2]'
#
# 给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
#
# 如果不能形成任何面积不为零的三角形，返回 0。
#
#
#
#
#
#
# 示例 1：
#
# 输入：[2,1,2]
# 输出：5
#
#
# 示例 2：
#
# 输入：[1,2,1]
# 输出：0
#
#
# 示例 3：
#
# 输入：[3,2,3,4]
# 输出：10
#
#
# 示例 4：
#
# 输入：[3,6,2,3]
# 输出：8
#
#
#
#
# 提示：
#
#
# 3 <= A.length <= 10000
# 1 <= A[i] <= 10^6
#
#
#
from typing import List


# @lc code=start
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 3, -1, -1):
            a, b, c = nums[i:i + 3]
            if a + b > c:
                return a + b + c
        return 0


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.largestPerimeter([2, 1, 2]))
    print(solu.largestPerimeter([1, 2, 1]))
    print(solu.largestPerimeter([3, 2, 3, 4]))
    print(solu.largestPerimeter([3, 6, 2, 3]))
