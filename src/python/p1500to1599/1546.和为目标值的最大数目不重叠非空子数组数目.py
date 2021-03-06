#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1546.和为目标值的最大数目不重叠非空子数组数目.py
@Time    :   2020/08/12 22:28:19
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1546 lang=python3
#
# [1546] 和为目标值的最大数目不重叠非空子数组数目
#
# https://leetcode-cn.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/description/
#
# algorithms
# Medium (36.05%)
# Likes:    18
# Dislikes: 0
# Total Accepted:    2.7K
# Total Submissions: 7.5K
# Testcase Example:  '[1,1,1,1,1]\n2'
#
# 给你一个数组 nums 和一个整数 target 。
#
# 请你返回 非空不重叠 子数组的最大数目，且每个子数组中数字和都为 target 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,1,1,1,1], target = 2
# 输出：2
# 解释：总共有 2 个不重叠子数组（加粗数字表示） [1,1,1,1,1] ，它们的和为目标值 2 。
#
#
# 示例 2：
#
# 输入：nums = [-1,3,5,1,4,2,-9], target = 6
# 输出：2
# 解释：总共有 3 个子数组和为 6 。
# ([5,1], [4,2], [3,5,1,4,2,-9]) 但只有前 2 个是不重叠的。
#
# 示例 3：
#
# 输入：nums = [-2,6,6,3,5,4,1,2,8], target = 10
# 输出：3
#
#
# 示例 4：
#
# 输入：nums = [0,0,0], target = 0
# 输出：3
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 0 <= target <= 10^6
#
#
#
from typing import List
"""
方法一：贪心
思路与算法

由于题目要求所有的子数组互不重叠，因此对于某个满足条件的子数组，如果其右端点
是所有满足条件的子数组的右端点中最小的那一个，则该子数组一定会被选择。

故可以使用贪心算法：从左到右遍历数组，一旦发现有某个以当前下标 i 为右端点的
子数组和为 target，就给计数器的值加 1，并从数组 nums 的下标 i+1 开始，进行
下一次寻找。

为了判断是否存在和为 target 的子数组，我们在遍历的过程中记录数组的前缀和，
并将它们保存在哈希表中。如果位置 i 对应的前缀和为 sum[i]，而 sum[i] − target
已经存在于哈希表中，就说明找到了一个和为 target 的子数组。

如果找到了一个符合条件的子数组，则接下来遍历时需要用一个新的哈希表，而不是
使用原有的哈希表，因为要确保每次找到的子数组都与此前找到的不重合。
"""


# @lc code=start
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        seen = {0}
        ans, cur = 0, 0

        for num in nums:
            cur += num
            if cur - target in seen:
                ans += 1
                seen = {0}
                cur = 0
            else:
                seen.add(cur)

        return ans


# @lc code=end
