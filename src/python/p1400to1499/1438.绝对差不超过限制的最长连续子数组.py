#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1438.绝对差不超过限制的最长连续子数组.py
@Time    :   2021/02/21 15:25:52
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1438 lang=python3
#
# [1438] 绝对差不超过限制的最长连续子数组
#
# https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/
#
# algorithms
# Medium (45.51%)
# Likes:    128
# Dislikes: 0
# Total Accepted:    16.6K
# Total Submissions: 36.5K
# Testcase Example:  '[8,2,4,7]\n4'
#
# 给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于
# limit 。
#
# 如果不存在满足条件的子数组，则返回 0 。
#
#
#
# 示例 1：
#
# 输入：nums = [8,2,4,7], limit = 4
# 输出：2
# 解释：所有子数组如下：
# [8] 最大绝对差 |8-8| = 0 <= 4.
# [8,2] 最大绝对差 |8-2| = 6 > 4.
# [8,2,4] 最大绝对差 |8-2| = 6 > 4.
# [8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
# [2] 最大绝对差 |2-2| = 0 <= 4.
# [2,4] 最大绝对差 |2-4| = 2 <= 4.
# [2,4,7] 最大绝对差 |2-7| = 5 > 4.
# [4] 最大绝对差 |4-4| = 0 <= 4.
# [4,7] 最大绝对差 |4-7| = 3 <= 4.
# [7] 最大绝对差 |7-7| = 0 <= 4.
# 因此，满足题意的最长子数组的长度为 2 。
#
#
# 示例 2：
#
# 输入：nums = [10,1,2,4,7,2], limit = 5
# 输出：4
# 解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。
#
#
# 示例 3：
#
# 输入：nums = [4,2,2,2,4,4,2,2], limit = 0
# 输出：3
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 0 <= limit <= 10^9
#
#
#
from collections import deque
from typing import List
# from sortedcontainers import SortedList
"""
方法一：滑动窗口 + 有序集合
思路和解法

我们可以枚举每一个位置作为右端点，找到其对应的最靠左的左端点，满足区间中
最大值与最小值的差不超过 limit。

注意到随着右端点向右移动，左端点也将向右移动，于是我们可以使用滑动窗口
解决本题。

为了方便统计当前窗口内的最大值与最小值，我们可以使用平衡树来维护窗口内
元素构成的有序集合。

语言自带的红黑树，例如 C++ 中的 std::multiset，Java 中的 TreeMap；

第三方的平衡树库，例如 Python 中的 sortedcontainers（事实上，这个库的
底层实现并不是平衡树，但各种操作的时间复杂度仍然很优秀）；

方法二：滑动窗口 + 单调队列
思路和解法

在方法一中，我们仅需要统计当前窗口内的最大值与最小值，因此我们也可以
分别使用两个单调队列解决本题。

在实际代码中，我们使用一个单调递增的队列 queMin 维护最小值，一个单调
递减的队列 queMax 维护最大值。这样我们只需要计算两个队列的队首的差值，
即可知道当前窗口是否满足条件。
"""


# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans, n = 0, len(nums)
        left = right = 0
        queMin, queMax = deque(), deque()

        while right < n:
            while queMin and queMin[-1] > nums[right]:
                queMin.pop()
            while queMax and queMax[-1] < nums[right]:
                queMax.pop()

            queMin.append(nums[right])
            queMax.append(nums[right])

            while queMax and queMin and queMax[0] - queMin[0] > limit:
                if nums[left] == queMin[0]:
                    queMin.popleft()
                if nums[left] == queMax[0]:
                    queMax.popleft()
                left += 1

            ans = max(ans, right - left + 1)
            right += 1

        return ans


# @lc code=end

# class Solution:
#     def longestSubarray(self, nums: List[int], limit: int) -> int:
#         s = SortedList()
#         n = len(nums)
#         ans = left = right = 0

#         while right < n:
#             s.add(nums[right])
#             while s[-1] - s[0] > limit:
#                 s.remove(nums[left])
#                 left += 1
#             ans = max(ans, right - left + 1)
#             right += 1

#         return ans

if __name__ == "__main__":
    solu = Solution()
    print(solu.longestSubarray(nums=[8, 2, 4, 7], limit=4))
    print(solu.longestSubarray(nums=[10, 1, 2, 4, 7, 2], limit=5))
    print(solu.longestSubarray(nums=[4, 2, 2, 2, 4, 4, 2, 2], limit=0))
