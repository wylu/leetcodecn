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
import heapq

from typing import List
"""
方法一：堆

思路与算法

首先遍历整个数组，并使用哈希表记录每个数字出现的次数，并形成一个「出现次数数组」。
找出原数组的前 k 个高频元素，就相当于找出「出现次数数组」的前 k 大的值。

最简单的做法是给「出现次数数组」排序。但由于可能有 O(N) 个不同的出现次数
（其中 N 为原数组长度），故总的算法复杂度会达到 O(NlogN)，不满足题目的要求。

在这里，我们可以利用堆的思想：建立一个小顶堆，然后遍历「出现次数数组」：
  - 如果堆的元素个数小于 k，就可以直接插入堆中。
  - 如果堆的元素个数等于 k，则检查堆顶与当前出现次数的大小。
    - 如果堆顶更大，说明至少有 k 个数字的出现次数比当前值大，故舍弃当前值；
    - 否则，就弹出堆顶，并将当前值插入堆中。

遍历完成后，堆中的元素就代表了「出现次数数组」中前 k 大的值。

方法二：快速选择
"""


# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num2cnt = {}
        for num in nums:
            num2cnt[num] = num2cnt.get(num, 0) + 1

        pq = []
        heapq.heapify(pq)

        for num, cnt in num2cnt.items():
            if len(pq) < k:
                heapq.heappush(pq, (cnt, num))
            elif cnt > pq[0][0]:
                heapq.heappop(pq)
                heapq.heappush(pq, (cnt, num))

        return [num for _, num in pq]


# @lc code=end

# 方法二：快速选择
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         cnts = {}
#         for num in nums:
#             cnts[num] = cnts.get(num, 0) + 1

#         nums = [(key, val) for key, val in cnts.items()]

#         def partition(s: int, e: int) -> int:
#             j = s - 1
#             for i in range(s, e):
#                 if nums[i][1] > nums[e][1]:
#                     j += 1
#                     nums[i], nums[j] = nums[j], nums[i]
#             j += 1
#             nums[j], nums[e] = nums[e], nums[j]
#             return j

#         left, right = 0, len(nums) - 1
#         while left <= right:
#             idx = partition(left, right)
#             if idx + 1 == k:
#                 return [key for key, _ in nums[:k]]
#             elif idx + 1 < k:
#                 left = idx + 1
#             else:
#                 right = idx - 1

#         return []

if __name__ == '__main__':
    solu = Solution()
    print(solu.topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(solu.topKFrequent([1], 1))
