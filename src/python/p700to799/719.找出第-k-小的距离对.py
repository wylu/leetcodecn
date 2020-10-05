#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   719.找出第-k-小的距离对.py
@Time    :   2020/10/05 20:03:10
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=719 lang=python3
#
# [719] 找出第 k 小的距离对
#
# https://leetcode-cn.com/problems/find-k-th-smallest-pair-distance/description/
#
# algorithms
# Hard (33.94%)
# Likes:    120
# Dislikes: 0
# Total Accepted:    5.3K
# Total Submissions: 15.6K
# Testcase Example:  '[1,3,1]\n1'
#
# 给定一个整数数组，返回所有数对之间的第 k 个最小距离。一对 (A, B) 的距离被定义为 A 和 B 之间的绝对差值。
#
# 示例 1:
#
#
# 输入：
# nums = [1,3,1]
# k = 1
# 输出：0
# 解释：
# 所有数对如下：
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# 因此第 1 个最小距离的数对是 (1,1)，它们之间的距离为 0。
#
#
# 提示:
#
#
# 2 <= len(nums) <= 10000.
# 0 <= nums[i] < 1000000.
# 1 <= k <= len(nums) * (len(nums) - 1) / 2.
#
#
#
from typing import List
"""
二分查找 + 双指针

我们可以使用双指针来计算出所有小于等于 guess 的距离对数目。我们维护 left
和 right，其中 right 通过循环逐渐递增，left 在每次循环中被维护，使得它
满足 nums[right] - nums[left] <= guess 且最小。这样对于 nums[right]，
以它为右端的满足距离小于等于 guess 的距离对数目即为 right - left。我们
在循环中对这些 right - left 进行累加，就得到了所有小于等于 guess 的
距离对数目。
"""


# @lc code=start
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        def ok(guess: int) -> bool:
            cnt = i = 0
            for j in range(n):
                while nums[j] - nums[i] > guess:
                    i += 1
                cnt += j - i
            return cnt < k

        # def ok(guess: int) -> bool:
        #     cnt = j = 0
        #     for i in range(n):
        #         while j < n and nums[j] - nums[i] <= guess:
        #             j += 1
        #         cnt += j - i - 1
        #     return cnt < k

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if ok(mid):
                left = mid + 1
            else:
                right = mid

        return left


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.smallestDistancePair([1, 3, 1], 1))
    print(solu.smallestDistancePair([1, 6, 1], 3))
