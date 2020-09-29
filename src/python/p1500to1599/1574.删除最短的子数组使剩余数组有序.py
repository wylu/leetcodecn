#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1574.删除最短的子数组使剩余数组有序.py
@Time    :   2020/09/29 08:58:11
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1574 lang=python3
#
# [1574] 删除最短的子数组使剩余数组有序
#
# https://leetcode-cn.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/description/
#
# algorithms
# Medium (29.01%)
# Likes:    15
# Dislikes: 0
# Total Accepted:    2K
# Total Submissions: 6.9K
# Testcase Example:  '[1,2,3,10,4,2,3,5]'
#
# 给你一个整数数组 arr ，请你删除一个子数组（可以为空），使得 arr 中剩下的元素是 非递减 的。
#
# 一个子数组指的是原数组中连续的一个子序列。
#
# 请你返回满足题目要求的最短子数组的长度。
#
#
#
# 示例 1：
#
#
# 输入：arr = [1,2,3,10,4,2,3,5]
# 输出：3
# 解释：我们需要删除的最短子数组是 [10,4,2] ，长度为 3 。剩余元素形成非递减数组 [1,2,3,3,5] 。
# 另一个正确的解为删除子数组 [3,10,4] 。
#
# 示例 2：
#
#
# 输入：arr = [5,4,3,2,1]
# 输出：4
# 解释：由于数组是严格递减的，我们只能保留一个元素。所以我们需要删除长度为 4 的子数组，要么删除 [5,4,3,2]，要么删除 [4,3,2,1]。
#
#
# 示例 3：
#
#
# 输入：arr = [1,2,3]
# 输出：0
# 解释：数组已经是非递减的了，我们不需要删除任何元素。
#
#
# 示例 4：
#
#
# 输入：arr = [1]
# 输出：0
#
#
#
#
# 提示：
#
#
# 1 <= arr.length <= 10^5
# 0 <= arr[i] <= 10^9
#
#
#
from typing import List
"""
双指针
"""


# @lc code=start
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n - 1

        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1

        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        ans = min(n - left - 1, right)
        if ans == 0:
            return 0

        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                ans = min(ans, j - i - 1)
                i += 1
            else:
                j += 1

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.findLengthOfShortestSubarray([1, 2, 3, 10, 4, 2, 3, 5]))
    print(solu.findLengthOfShortestSubarray([5, 4, 3, 2, 1]))
    print(solu.findLengthOfShortestSubarray([1, 2, 3]))
    print(solu.findLengthOfShortestSubarray([1]))
