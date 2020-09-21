#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1590.使数组和能被-p-整除.py
@Time    :   2020/09/21 23:12:22
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1590 lang=python3
#
# [1590] 使数组和能被 P 整除
#
# https://leetcode-cn.com/problems/make-sum-divisible-by-p/description/
#
# algorithms
# Medium (20.85%)
# Likes:    4
# Dislikes: 0
# Total Accepted:    966
# Total Submissions: 4.6K
# Testcase Example:  '[3,1,4,2]\n6'
#
# 给你一个正整数数组 nums，请你移除 最短 子数组（可以为 空），使得剩余元素的 和 能被 p 整除。 不允许 将整个数组都移除。
#
# 请你返回你需要移除的最短子数组的长度，如果无法满足题目要求，返回 -1 。
#
# 子数组 定义为原数组中连续的一组元素。
#
#
#
# 示例 1：
#
# 输入：nums = [3,1,4,2], p = 6
# 输出：1
# 解释：nums 中元素和为 10，不能被 p 整除。我们可以移除子数组 [4] ，剩余元素的和为 6 。
#
#
# 示例 2：
#
# 输入：nums = [6,3,5,2], p = 9
# 输出：2
# 解释：我们无法移除任何一个元素使得和被 9 整除，最优方案是移除子数组 [5,2] ，剩余元素为 [6,3]，和为 9 。
#
#
# 示例 3：
#
# 输入：nums = [1,2,3], p = 3
# 输出：0
# 解释：和恰好为 6 ，已经能被 3 整除了。所以我们不需要移除任何元素。
#
#
# 示例  4：
#
# 输入：nums = [1,2,3], p = 7
# 输出：-1
# 解释：没有任何方案使得移除子数组后剩余元素的和被 7 整除。
#
#
# 示例 5：
#
# 输入：nums = [1000000000,1000000000,1000000000], p = 3
# 输出：0
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 1 <= p <= 10^9
#
#
#
from typing import List
"""
前缀和 + 哈希表优化

假设 nums 的和除以 P，余数是 mod，

如果 mod == 0，答案就是 0。
如果 mod != 0，答案变成了找原数组中的最短连续子数组，使得其数字和除以 P，
余数也是 mod。

由于是求解连续子数组和的问题，很容易想到使用前缀和。我们可以扫描一遍整个
数组，计算到每个元素的前缀和。

假设当前前缀和除以 P 的余数是 curmod，为了找到一段连续子数组对 P 的余数
是 mod，我们需要找到一段前缀和，对 P 的余数是 targetmod。其中 targetmod
的求法是：

如果 curmod >= mod，很简单：targetmod = curmod - mod；
如果 curmod < mod，我们需要加上一个 P：targetmod = curmod - mod + P；

这样，我们可以保证，当前前缀和减去目标前缀和，剩余的数组对 P 的余数是
mod。我们只需要找最短的这样的数组就好。

最后，为了快速找到一段对 P 的余数为 targetmod 的前缀和，我们使用一个
哈希表 table，来存储之前前缀和对 P 的余数和所在的索引。
（key 为余数；value 为索引）。

table 在遍历过程中更新，以保证每次在 table 中查找到的，是离当前元素最近
的索引，从而保证找到的是“最短”的连续子数组。
"""


# @lc code=start
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        mod = sum(nums) % p
        if mod == 0:
            return 0

        n = len(nums)
        ans, mp, tot = n, {0: -1}, 0
        for i in range(n):
            tot += nums[i]
            curmod = tot % p
            targetmod = (curmod - mod + p) % p
            if targetmod in mp:
                ans = min(ans, i - mp[targetmod])
            mp[curmod] = i

        return -1 if ans == n else ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.minSubarray([3, 1, 4, 2], 6))
    print(solu.minSubarray([6, 3, 5, 2], 9))
    print(solu.minSubarray([1, 2, 3], 3))
