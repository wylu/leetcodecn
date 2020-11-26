#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   164.最大间距.py
@Time    :   2020/11/26 22:50:18
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=164 lang=python3
#
# [164] 最大间距
#
# https://leetcode-cn.com/problems/maximum-gap/description/
#
# algorithms
# Hard (55.18%)
# Likes:    314
# Dislikes: 0
# Total Accepted:    42.7K
# Total Submissions: 69.9K
# Testcase Example:  '[3,6,9,1]'
#
# 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
#
# 如果数组元素个数小于 2，则返回 0。
#
# 示例 1:
#
# 输入: [3,6,9,1]
# 输出: 3
# 解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
#
# 示例 2:
#
# 输入: [10]
# 输出: 0
# 解释: 数组元素个数小于 2，因此返回 0。
#
# 说明:
#
#
# 你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
# 请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。
#
#
#
from typing import List
"""
方法一：基数排序

基数排序可以在 O(N) 的时间内完成整数之间的排序。
"""


# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        exp, buf, maxVal = 1, [0] * n, max(nums)

        while exp <= maxVal:
            cnt = [0] * 10

            for num in nums:
                digit = num // exp % 10
                cnt[digit] += 1

            for i in range(1, 10):
                cnt[i] += cnt[i - 1]

            for i in range(n - 1, -1, -1):
                digit = nums[i] // exp % 10
                buf[cnt[digit] - 1] = nums[i]
                cnt[digit] -= 1

            nums = buf[:]
            exp *= 10

        ans = 0
        for i in range(1, n):
            ans = max(ans, nums[i] - nums[i - 1])

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.maximumGap([10, 321, 1, 743, 60, 127]))
