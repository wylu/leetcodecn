#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   239.滑动窗口最大值.py
@Time    :   2021/01/02 11:23:45
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
# https://leetcode-cn.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (49.13%)
# Likes:    713
# Dislikes: 0
# Total Accepted:    98.9K
# Total Submissions: 201.3K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k
# 个数字。滑动窗口每次只向右移动一位。
#
# 返回滑动窗口中的最大值。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
#
#
# 示例 2：
#
#
# 输入：nums = [1], k = 1
# 输出：[1]
#
#
# 示例 3：
#
#
# 输入：nums = [1,-1], k = 1
# 输出：[1,-1]
#
#
# 示例 4：
#
#
# 输入：nums = [9,11], k = 2
# 输出：[11]
#
#
# 示例 5：
#
#
# 输入：nums = [4,-2], k = 2
# 输出：[4]
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
#
#
#
from collections import deque
from typing import List


# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()

        def push_max(i: int) -> None:
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        for i in range(k):
            push_max(i)

        ans = [nums[q[0]]]
        for i in range(len(nums) - k):
            if i == q[0]:
                q.popleft()
            push_max(i + k)
            ans.append(nums[q[0]])

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
    print(solu.maxSlidingWindow(nums=[1], k=1))
    print(solu.maxSlidingWindow(nums=[1, -1], k=1))
    print(solu.maxSlidingWindow(nums=[9, 11], k=2))
    print(solu.maxSlidingWindow(nums=[4, -2], k=2))
