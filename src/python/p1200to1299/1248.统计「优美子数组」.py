#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1248.统计「优美子数组」.py
@Time    :   2020/09/21 19:30:15
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1248 lang=python3
#
# [1248] 统计「优美子数组」
#
# https://leetcode-cn.com/problems/count-number-of-nice-subarrays/description/
#
# algorithms
# Medium (54.37%)
# Likes:    128
# Dislikes: 0
# Total Accepted:    25.3K
# Total Submissions: 46.6K
# Testcase Example:  '[1,1,2,1,1]\n3'
#
# 给你一个整数数组 nums 和一个整数 k。
#
# 如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
#
# 请返回这个数组中「优美子数组」的数目。
#
#
#
# 示例 1：
#
# 输入：nums = [1,1,2,1,1], k = 3
# 输出：2
# 解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
#
#
# 示例 2：
#
# 输入：nums = [2,4,6], k = 1
# 输出：0
# 解释：数列中不包含任何奇数，所以不存在优美子数组。
#
#
# 示例 3：
#
# 输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# 输出：16
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10^5
# 1 <= k <= nums.length
#
#
#
from typing import List


# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        cnts, tot = {0: 1}, 0
        for num in nums:
            tot += num % 2 == 1
            ans += cnts.get(tot - k, 0)
            cnts[tot] = cnts.get(tot, 0) + 1
        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.numberOfSubarrays([1, 1, 2, 1, 1], 3))
    print(solu.numberOfSubarrays([2, 4, 6], 1))
    print(solu.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
