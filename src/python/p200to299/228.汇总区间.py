#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   228.汇总区间.py
@Time    :   2021/01/10 19:06:01
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#
# https://leetcode-cn.com/problems/summary-ranges/description/
#
# algorithms
# Easy (57.82%)
# Likes:    118
# Dislikes: 0
# Total Accepted:    33.8K
# Total Submissions: 58.5K
# Testcase Example:  '[0,1,2,4,5,7]'
#
# 给定一个无重复元素的有序整数数组 nums 。
#
# 返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于
# nums 的数字 x 。
#
# 列表中的每个区间范围 [a,b] 应该按如下格式输出：
#
#
# "a->b" ，如果 a != b
# "a" ，如果 a == b
#
#
#
#
# 示例 1：
#
#
# 输入：nums = [0,1,2,4,5,7]
# 输出：["0->2","4->5","7"]
# 解释：区间范围是：
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
#
#
# 示例 2：
#
#
# 输入：nums = [0,2,3,4,6,8,9]
# 输出：["0","2->4","6","8->9"]
# 解释：区间范围是：
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
#
#
# 示例 3：
#
#
# 输入：nums = []
# 输出：[]
#
#
# 示例 4：
#
#
# 输入：nums = [-1]
# 输出：["-1"]
#
#
# 示例 5：
#
#
# 输入：nums = [0]
# 输出：["0"]
#
#
#
#
# 提示：
#
#
# 0 <= nums.length <= 20
# -2^31 <= nums[i] <= 2^31 - 1
# nums 中的所有值都 互不相同
# nums 按升序排列
#
#
#
from typing import List


# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)

        ans = []
        i, j = 0, 1
        while i < n:
            while j < n and nums[j] == nums[j - 1] + 1:
                j += 1

            if j - 1 == i:
                ans.append(str(nums[i]))
            else:
                ans.append(str(nums[i]) + '->' + str(nums[j - 1]))
            i, j = j, j + 1

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.summaryRanges([0, 1, 2, 4, 5, 7]))
    print(solu.summaryRanges([0, 2, 3, 4, 6, 8, 9]))
    print(solu.summaryRanges([]))
