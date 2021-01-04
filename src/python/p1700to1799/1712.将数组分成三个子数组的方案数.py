#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1712.将数组分成三个子数组的方案数.py
@Time    :   2021/01/04 23:22:50
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1712 lang=python3
#
# [1712] 将数组分成三个子数组的方案数
#
# https://leetcode-cn.com/problems/ways-to-split-array-into-three-subarrays/description/
#
# algorithms
# Medium (25.60%)
# Likes:    23
# Dislikes: 0
# Total Accepted:    1.9K
# Total Submissions: 7.3K
# Testcase Example:  '[1,1,1]'
#
# 我们称一个分割整数数组的方案是 好的 ，当它满足：
#
#
# 数组被分成三个 非空 连续子数组，从左至右分别命名为 left ， mid ， right 。
# left 中元素和小于等于 mid 中元素和，mid 中元素和小于等于 right 中元素和。
#
#
# 给你一个 非负 整数数组 nums ，请你返回 好的 分割 nums 方案数目。由于答案可能会很大，请你将结果对 10^9 + 7 取余后返回。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,1,1]
# 输出：1
# 解释：唯一一种好的分割方案是将 nums 分成 [1] [1] [1] 。
#
# 示例 2：
#
#
# 输入：nums = [1,2,2,2,5,0]
# 输出：3
# 解释：nums 总共有 3 种好的分割方案：
# [1] [2] [2,2,5,0]
# [1] [2,2] [2,5,0]
# [1,2] [2,2] [5,0]
#
#
# 示例 3：
#
#
# 输入：nums = [3,2,1]
# 输出：0
# 解释：没有好的分割方案。
#
#
#
# 提示：
#
#
# 3 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^4
#
#
#
from typing import List


# @lc code=start
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        ps = [0] * (n + 1)

        for i in range(n):
            ps[i + 1] = ps[i] + nums[i]

        def search_left(i: int) -> int:
            lo, hi = i + 1, n - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if ps[mid] - ps[i] < ps[i]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return lo

        def search_right(i: int) -> int:
            lo, hi = i + 1, n - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if ps[n] - ps[mid] >= ps[mid] - ps[i]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return hi

        ans, i = 0, 1
        while i < n - 1 and ps[i] * 3 <= ps[n]:
            lo = search_left(i)
            hi = search_right(i)
            ans += hi - lo + 1
            i += 1

        return ans % 1000000007


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.waysToSplit([1, 1, 1]))
    print(solu.waysToSplit([1, 2, 2, 2, 5, 0]))
    print(solu.waysToSplit([3, 2, 1]))
    print(solu.waysToSplit([2, 3, 2, 7, 7, 1, 9, 4]))
