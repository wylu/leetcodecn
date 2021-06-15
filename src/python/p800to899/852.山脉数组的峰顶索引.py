#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   852.山脉数组的峰顶索引.py
@Time    :   2021/06/15 13:09:24
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=852 lang=python3
#
# [852] 山脉数组的峰顶索引
#
# https://leetcode-cn.com/problems/peak-index-in-a-mountain-array/description/
#
# algorithms
# Easy (71.47%)
# Likes:    181
# Dislikes: 0
# Total Accepted:    59.2K
# Total Submissions: 82.9K
# Testcase Example:  '[0,1,0]'
#
# 符合下列属性的数组 arr 称为 山脉数组 ：
#
# arr.length >= 3
# 存在 i（0 < i < arr.length - 1）使得：
#
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
#
#
#
#
# 给你由整数组成的山脉数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i +
# 1] > ... > arr[arr.length - 1] 的下标 i 。
#
#
#
# 示例 1：
#
#
# 输入：arr = [0,1,0]
# 输出：1
#
#
# 示例 2：
#
#
# 输入：arr = [0,2,1,0]
# 输出：1
#
#
# 示例 3：
#
#
# 输入：arr = [0,10,5,2]
# 输出：1
#
#
# 示例 4：
#
#
# 输入：arr = [3,4,5,1]
# 输出：2
#
#
# 示例 5：
#
#
# 输入：arr = [24,69,100,99,79,78,67,36,26,19]
# 输出：2
#
#
#
#
# 提示：
#
#
# 3 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^6
# 题目数据保证 arr 是一个山脉数组
#
#
#
#
# 进阶：很容易想到时间复杂度 O(n) 的解决方案，你可以设计一个 O(log(n)) 的解决方案吗？
#
#
from typing import List
"""
方法二：二分查找
思路与算法

记满足题目要求的下标 i 为 i{ans}。我们可以发现：

当 i < i{ans} 时，arr[i] < arr[i+1] 恒成立；
当 i >= i{ans} 时，arr[i] > arr[i+1] 恒成立。

这与方法一的遍历过程也是一致的，因此 i{ans} 即为「最小的满足
arr[i] > arr[i+1] 的下标 i」，我们可以用二分查找的方法来找出
i{ans}。
"""


# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        ans = -1
        left, right = 1, len(arr) - 2
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


# @lc code=end

# class Solution:
#     def peakIndexInMountainArray(self, arr: List[int]) -> int:
#         n = len(arr)
#         for i in range(1, n - 1):
#             if arr[i] > arr[i + 1]:
#                 return i
#         return -1

if __name__ == '__main__':
    solu = Solution()
    arr = [0, 1, 0]
    print(solu.peakIndexInMountainArray(arr))

    arr = [0, 2, 1, 0]
    print(solu.peakIndexInMountainArray(arr))

    arr = [0, 10, 5, 2]
    print(solu.peakIndexInMountainArray(arr))

    arr = [3, 4, 5, 1]
    print(solu.peakIndexInMountainArray(arr))

    arr = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
    print(solu.peakIndexInMountainArray(arr))
