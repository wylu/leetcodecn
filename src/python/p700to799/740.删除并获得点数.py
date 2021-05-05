#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   740.删除并获得点数.py
@Time    :   2021/05/05 10:28:57
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=740 lang=python3
#
# [740] 删除并获得点数
#
# https://leetcode-cn.com/problems/delete-and-earn/description/
#
# algorithms
# Medium (57.20%)
# Likes:    268
# Dislikes: 0
# Total Accepted:    16K
# Total Submissions: 28K
# Testcase Example:  '[3,4,2]'
#
# 给你一个整数数组 nums ，你可以对它进行一些操作。
#
# 每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] +
# 1 的元素。
#
# 开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。
#
#
#
# 示例 1：
#
#
# 输入：nums = [3,4,2]
# 输出：6
# 解释：
# 删除 4 获得 4 个点数，因此 3 也被删除。
# 之后，删除 2 获得 2 个点数。总共获得 6 个点数。
#
#
# 示例 2：
#
#
# 输入：nums = [2,2,3,3,3,4]
# 输出：9
# 解释：
# 删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
# 之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
# 总共获得 9 个点数。
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 2 * 10^4
# 1 <= nums[i] <= 10^4
#
#
#
from typing import List
"""
方法一：动态规划
思路

根据题意，在选择了元素 x 后，该元素以及所有等于 x-1 或 x+1 的元素会从数组
中删去。若还有多个值为 x 的元素，由于所有等于 x-1 或 x+1 的元素已经被删除，
我们可以直接删除 x 并获得其点数。因此若选择了 x，所有等于 x 的元素也应一同
被选择，以尽可能多地获得点数。

记元素 x 在数组中出现的次数为 cx，我们可以用一个数组 sum 记录数组 nums 中
所有相同元素之和，即 sum[x] = x * c。若选择了 x，则可以获取 sum[x] 的点数，
且无法再选择 x-1 和 x+1。这与「198. 打家劫舍」是一样的，在统计出 sum 数组
后，读者可参考「198. 打家劫舍的官方题解」中的动态规划过程计算出答案。
"""


# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = max(nums) + 1
        tot = [0] * n
        for num in nums:
            tot[num] += num

        def rob(tot: List[int]) -> int:
            f0, f1 = 0, tot[0]
            for i in range(1, n):
                f0, f1 = max(f0, f1), f0 + tot[i]
            return max(f0, f1)

        return rob(tot)


# @lc code=end
"""
Dynamic Programming

State:
  dp[i][0]: nums[0...i] 经过操作后且 nums[i] 不是主动删除时的最大点数
  dp[i][1]: nums[0...i] 经过操作后且 nums[i] 是主动删除时的最大点数

State Transition:
  dp[i][0] = max{j < i} dp[j][1],  nums[j] + 1 == nums[i]
  dp[i][1] = max{j < i} dp[j][0] + nums[i],  nums[j] + 1 == nums[i]
  dp[i][1] = max{j < i} max(dp[j]) + nums[i],  nums[j] + 1 < nums[i]
  dp[i][1] = max{j < i} dp[j][1] + nums[i],  nums[j] == nums[i]

Initial State:
  dp[0][0]: 0
  dp[0][1]: nums[0]
"""

# class Solution:
#     def deleteAndEarn(self, nums: List[int]) -> int:
#         n = len(nums)
#         nums.sort()
#         f = [[0] * 2 for _ in range(n)]
#         f[0][1] = nums[0]

#         for i in range(1, n):
#             for j in range(i):
#                 if nums[j] + 1 == nums[i]:
#                     f[i][0] = max(f[i][0], f[j][1])
#                     f[i][1] = max(f[i][1], f[j][0] + nums[i])
#                 elif nums[j] + 1 < nums[i]:
#                     f[i][1] = max(f[i][1], max(f[j]) + nums[i])
#                 elif nums[j] == nums[i]:
#                     f[i][1] = max(f[i][1], f[j][1] + nums[i])

#         return max(f[n - 1])

if __name__ == '__main__':
    solu = Solution()
    print(solu.deleteAndEarn(nums=[3, 4, 2]))
    print(solu.deleteAndEarn(nums=[2, 2, 3, 3, 3, 4]))
    print(solu.deleteAndEarn(nums=[3, 1]))
