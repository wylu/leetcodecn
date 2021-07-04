#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1909.删除一个元素使数组严格递增.py
@Time    :   2021/07/03 19:20:28
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1909 lang=python3
#
# [1909] 删除一个元素使数组严格递增
#
# https://leetcode-cn.com/problems/remove-one-element-to-make-the-array-strictly-increasing/description/
#
# algorithms
# Easy (33.38%)
# Likes:    9
# Dislikes: 0
# Total Accepted:    3.2K
# Total Submissions: 9.4K
# Testcase Example:  '[1,2,10,5,7]'
#
# 给你一个下标从 0 开始的整数数组 nums ，如果 恰好 删除 一个 元素后，数组 严格递增 ，那么请你返回 true ，否则返回 false
# 。如果数组本身已经是严格递增的，请你也返回 true 。
#
# 数组 nums 是 严格递增 的定义为：对于任意下标的 1 <= i < nums.length 都满足 nums[i - 1] < nums[i]
# 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,10,5,7]
# 输出：true
# 解释：从 nums 中删除下标 2 处的 10 ，得到 [1,2,5,7] 。
# [1,2,5,7] 是严格递增的，所以返回 true 。
#
#
# 示例 2：
#
# 输入：nums = [2,3,1,2]
# 输出：false
# 解释：
# [3,1,2] 是删除下标 0 处元素后得到的结果。
# [2,1,2] 是删除下标 1 处元素后得到的结果。
# [2,3,2] 是删除下标 2 处元素后得到的结果。
# [2,3,1] 是删除下标 3 处元素后得到的结果。
# 没有任何结果数组是严格递增的，所以返回 false 。
#
# 示例 3：
#
# 输入：nums = [1,1,1]
# 输出：false
# 解释：删除任意元素后的结果都是 [1,1] 。
# [1,1] 不是严格递增的，所以返回 false 。
#
#
# 示例 4：
#
# 输入：nums = [1,2,3]
# 输出：true
# 解释：[1,2,3] 已经是严格递增的，所以返回 true 。
#
#
#
#
# 提示：
#
#
# 2 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
#
#
#
from typing import List
"""
方法一：寻找非递增相邻下标对
思路与算法

数组 nums 严格递增的充分必要条件是对于任意两个相邻下标对 (i-1, i) 均有
nums[i] > nums[i-1]。换言之，如果存在下标 i 有 nums[i] <= nums[i-1]
，那么 nums 并非严格递增。

因此，我们可以从左至右遍历寻找非递增的相邻下标对。假设对于某个下标对
(i-1, i) 有 nums[i] <= nums[i-1]，如果我们想使得 nums 在删除一个
元素后严格递增，那么必须至少删除下标对 (i-1, i) 对应的元素之一。

我们可以用 check(idx) 函数来检查数组 nums 删去下标为 idx 的元素后是否
严格递增。具体地，我们对 nums 进行一次遍历，在遍历的过程中记录上一个元素
的下标，并与当前遍历到的元素进行比较。需要注意的是，下标为 idx 的元素
需要被跳过。
"""


# @lc code=start
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def check(idx: int) -> bool:
            cur_max = 0
            for i in range(len(nums)):
                if i == idx:
                    continue
                if nums[i] <= cur_max:
                    return False
                cur_max = nums[i]
            return True

        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                return check(i) or check(i + 1)

        return True


# @lc code=end

# class Solution:
#     def canBeIncreasing(self, nums: List[int]) -> bool:
#         ans = 0
#         cur_max, pre_max = nums[0], 0
#         for i in range(1, len(nums)):
#             if nums[i] > cur_max:
#                 cur_max, pre_max = nums[i], cur_max
#                 continue

#             ans += 1
#             if ans > 1:
#                 return False

#             if nums[i] > pre_max:
#                 cur_max = nums[i]

#         return True

if __name__ == '__main__':
    solu = Solution()
    print(solu.canBeIncreasing(nums=[1, 2, 10, 5, 7]))
    print(solu.canBeIncreasing(nums=[2, 3, 1, 2]))
    print(solu.canBeIncreasing(nums=[1, 1, 1]))
    print(solu.canBeIncreasing(nums=[1, 2, 3]))
    print(solu.canBeIncreasing(nums=[4, 1, 2, 3]))
    print(solu.canBeIncreasing(nums=[2, 3, 1, 4]))
    print(solu.canBeIncreasing(nums=[105, 924, 32, 968]))
