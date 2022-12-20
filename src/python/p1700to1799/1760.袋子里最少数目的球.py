#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1760.袋子里最少数目的球.py
@Time    :   2022/12/20 17:10:44
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
#
# @lc app=leetcode.cn id=1760 lang=python3
#
# [1760] 袋子里最少数目的球
#
# https://leetcode.cn/problems/minimum-limit-of-balls-in-a-bag/description/
#
# algorithms
# Medium (62.22%)
# Likes:    177
# Dislikes: 0
# Total Accepted:    17.3K
# Total Submissions: 27.8K
# Testcase Example:  '[9]\n2'
#
# 给你一个整数数组 nums ，其中 nums[i] 表示第 i 个袋子里球的数目。同时给你一个整数 maxOperations 。
#
# 你可以进行如下操作至多 maxOperations 次：
#
#
# 选择任意一个袋子，并将袋子里的球分到 2 个新的袋子中，每个袋子里都有 正整数 个球。
#
#
# 比方说，一个袋子里有 5 个球，你可以把它们分到两个新袋子里，分别有 1 个和 4 个球，或者分别有 2 个和 3 个球。
#
#
#
#
# 你的开销是单个袋子里球数目的 最大值 ，你想要 最小化 开销。
#
# 请你返回进行上述操作后的最小开销。
#
#
#
# 示例 1：
#
#
# 输入：nums = [9], maxOperations = 2
# 输出：3
# 解释：
# - 将装有 9 个球的袋子分成装有 6 个和 3 个球的袋子。[9] -> [6,3] 。
# - 将装有 6 个球的袋子分成装有 3 个和 3 个球的袋子。[6,3] -> [3,3,3] 。
# 装有最多球的袋子里装有 3 个球，所以开销为 3 并返回 3 。
#
#
# 示例 2：
#
#
# 输入：nums = [2,4,8,2], maxOperations = 4
# 输出：2
# 解释：
# - 将装有 8 个球的袋子分成装有 4 个和 4 个球的袋子。[2,4,8,2] -> [2,4,4,4,2] 。
# - 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,4,4,4,2] -> [2,2,2,4,4,2] 。
# - 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,2,2,4,4,2] -> [2,2,2,2,2,4,2] 。
# - 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,2,2,2,2,4,2] -> [2,2,2,2,2,2,2,2] 。
# 装有最多球的袋子里装有 2 个球，所以开销为 2 并返回 2 。
#
#
# 示例 3：
#
#
# 输入：nums = [7,17], maxOperations = 2
# 输出：7
#
#
#
#
# 提示：
#
#
# 1
# 1
#
#
#
from typing import List


# @lc code=start
class Solution:

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def ok(threshold: int) -> bool:
            cnt = 0
            for num in nums:
                cnt += (num + threshold - 1) // threshold - 1
                if cnt > maxOperations:
                    return False
            return True

        left, right = 1, max(nums)
        while left < right:
            mid = left + (right - left) // 2
            if ok(mid):
                right = mid
            else:
                left = mid + 1

        return left


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    nums = [9]
    maxOperations = 2
    print(solu.minimumSize(nums, maxOperations))

    nums = [2, 4, 8, 2]
    maxOperations = 4
    print(solu.minimumSize(nums, maxOperations))

    nums = [7, 17]
    maxOperations = 2
    print(solu.minimumSize(nums, maxOperations))
