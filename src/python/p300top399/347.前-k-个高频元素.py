#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   347.前-k-个高频元素.py
@Time    :   2020/09/07 18:54:50
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
# https://leetcode-cn.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (61.47%)
# Likes:    480
# Dislikes: 0
# Total Accepted:    94.9K
# Total Submissions: 154.4K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
#
#
#
# 示例 1:
#
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#
#
# 示例 2:
#
# 输入: nums = [1], k = 1
# 输出: [1]
#
#
#
# 提示：
#
#
# 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
# 你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
# 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
# 你可以按任意顺序返回答案。
#
#
#
from typing import List


# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = {}
        for num in nums:
            cnts[num] = cnts.get(num, 0) + 1

        nums = [(key, val) for key, val in cnts.items()]

        def partition(s: int, e: int) -> int:
            j = s - 1
            for i in range(s, e):
                if nums[i][1] > nums[e][1]:
                    j += 1
                    nums[i], nums[j] = nums[j], nums[i]
            j += 1
            nums[j], nums[e] = nums[e], nums[j]
            return j

        left, right = 0, len(nums) - 1
        while left <= right:
            idx = partition(left, right)
            if idx + 1 == k:
                return [key for key, _ in nums[:k]]
            elif idx + 1 < k:
                left = idx + 1
            else:
                right = idx - 1

        return []


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(solu.topKFrequent([1], 1))
