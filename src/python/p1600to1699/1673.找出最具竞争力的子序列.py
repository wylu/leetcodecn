#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1673.找出最具竞争力的子序列.py
@Time    :   2020/11/30 23:09:06
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1673 lang=python3
#
# [1673] 找出最具竞争力的子序列
#
# https://leetcode-cn.com/problems/find-the-most-competitive-subsequence/description/
#
# algorithms
# Medium (25.79%)
# Likes:    20
# Dislikes: 0
# Total Accepted:    2.8K
# Total Submissions: 10.9K
# Testcase Example:  '[3,5,2,6]\n2'
#
# 给你一个整数数组 nums 和一个正整数 k ，返回长度为 k 且最具 竞争力 的 nums 子序列。
#
# 数组的子序列是从数组中删除一些元素（可能不删除元素）得到的序列。
#
# 在子序列 a 和子序列 b 第一个不相同的位置上，如果 a 中的数字小于 b 中对应的数字，那么我们称子序列 a 比子序列 b（相同长度下）更具 竞争力
# 。 例如，[1,3,4] 比 [1,3,5] 更具竞争力，在第一个不相同的位置，也就是最后一个位置上， 4 小于 5 。
#
#
#
# 示例 1：
#
#
# 输入：nums = [3,5,2,6], k = 2
# 输出：[2,6]
# 解释：在所有可能的子序列集合 {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]} 中，[2,6] 最具竞争力。
#
#
# 示例 2：
#
#
# 输入：nums = [2,4,3,3,5,4,9,6], k = 4
# 输出：[2,3,3,4]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
# 1 <= k <= nums.length
#
#
#
from typing import List


# @lc code=start
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack, n = [], len(nums)
        for i in range(n):
            while (stack and nums[i] < stack[-1]
                   and len(stack) + (n - i - 1) >= k):
                stack.pop()
            stack.append(nums[i])
        return stack[:k]


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.mostCompetitive([3, 5, 2, 6], 2))
    print(solu.mostCompetitive([2, 4, 3, 3, 5, 4, 9, 6], 4))
