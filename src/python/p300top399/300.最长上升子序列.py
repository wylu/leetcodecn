#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   300.最长上升子序列.py
@Time    :   2020/08/25 13:05:07
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#
# https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (45.16%)
# Likes:    927
# Dislikes: 0
# Total Accepted:    134.9K
# Total Submissions: 298.8K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
#
# 示例:
#
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
#
# 说明:
#
#
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n^2) 。
#
#
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
#
#
from typing import List
"""
方法一：Dynamic Programming

State:
  dp[i]: 表示以 nums[i] 为结尾的最长上升子序列的长度

State Transition:
  i > j
  if nums[i] >= nums[j]:
      dp[i] = max(dp[i], dp[j] + 1)

Initial State:
  dp[i] = 1 (0 <= i < len(nums))


方法二：贪心 + 二分查找
思路与算法

考虑一个简单的贪心，如果我们要使上升子序列尽可能的长，则我们需要让序列
上升得尽可能慢，因此我们希望每次在上升子序列最后加上的那个数尽可能的小。

基于上面的贪心思路，我们维护一个数组 d[i]，表示长度为 i 的最长上升
子序列的末尾元素的最小值，用 last 记录目前最长上升子序列的长度，起始时
last 为 1，d[1] = nums[0]。

同时我们可以注意到 d[i] 是关于 i 单调递增的。因为如果 d[j] >= d[i]
且 j < i，我们考虑从长度为 i 的最长上升子序列的末尾删除 i−j 个元素，
那么这个序列长度变为 j ，且第 j 个元素 x（末尾元素）必然小于 d[i]，
也就小于 d[j]。那么我们就找到了一个长度为 j 的最长上升子序列，并且
末尾元素比 d[j] 小，从而产生了矛盾。因此数组 d 的单调性得证。

我们依次遍历数组 nums 中的每个元素，并更新数组 d 和 last 的值。如果
nums[i] > d[last] 则更新 last = last + 1，否则在 d[1...last] 中找
满足 d[i - 1] < nums[j] < d[i] 的下标 i，并更新 d[i] = nums[j]。

根据 d 数组的单调性，我们可以使用二分查找寻找下标 i，优化时间复杂度。

最后整个算法流程为：

设当前已求出的最长上升子序列的长度为 last（初始时为 1），从前往后遍历
数组 nums，在遍历到 nums[i] 时：
  - 如果 nums[i] > d[last]，则直接加入到 d 数组末尾，并更新 last += 1；
  - 否则，在 d 数组中二分查找，找到第一个比 nums[i] 小的数 d[k]，
    并更新 d[k+1] = nums[i]。如果找不到，则更新 d[0] = nums[i]。

以输入序列 [0, 8, 4, 12, 2] 为例：
  - 第一步插入 0，d = [0]；
  - 第二步插入 8，d = [0, 8]；
  - 第三步插入 4，d = [0, 4]；
  - 第四步插入 12，d = [0, 4, 12]；
  - 第五步插入 2，d = [0, 2, 12]。
最终得到最大递增子序列长度为 3。
"""


# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        d, n = [nums[0]], len(nums)

        for i in range(1, n):
            if nums[i] > d[-1]:
                d.append(nums[i])
                continue

            lo, hi = 0, len(d) - 1
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if d[mid] < nums[i]:
                    lo = mid
                else:
                    hi = mid - 1

            if d[lo] >= nums[i]:
                d[0] = nums[i]
            else:
                d[lo + 1] = nums[i]

        return len(d)


# @lc code=end

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if not nums:
#             return 0

#         n = len(nums)
#         dp = [1] * n

#         for i in range(n):
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[i], dp[j] + 1)

#         return max(dp)

if __name__ == '__main__':
    solu = Solution()
    print(solu.lengthOfLIS([10, 9, 2, 5, 3, 4]))
    print(solu.lengthOfLIS([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]))
