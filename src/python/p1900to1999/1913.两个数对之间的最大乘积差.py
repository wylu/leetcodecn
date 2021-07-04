#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1913.两个数对之间的最大乘积差.py
@Time    :   2021/07/04 16:30:13
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1913 lang=python3
#
# [1913] 两个数对之间的最大乘积差
#
# https://leetcode-cn.com/problems/maximum-product-difference-between-two-pairs/description/
#
# algorithms
# Easy (86.09%)
# Likes:    4
# Dislikes: 0
# Total Accepted:    5.2K
# Total Submissions: 6.1K
# Testcase Example:  '[5,6,2,7,4]'
#
# 两个数对 (a, b) 和 (c, d) 之间的 乘积差 定义为 (a * b) - (c * d) 。
#
#
# 例如，(5, 6) 和 (2, 7) 之间的乘积差是 (5 * 6) - (2 * 7) = 16 。
#
#
# 给你一个整数数组 nums ，选出四个 不同的 下标 w、x、y 和 z ，使数对 (nums[w], nums[x]) 和 (nums[y],
# nums[z]) 之间的 乘积差 取到 最大值 。
#
# 返回以这种方式取得的乘积差中的 最大值 。
#
#
#
# 示例 1：
#
# 输入：nums = [5,6,2,7,4]
# 输出：34
# 解释：可以选出下标为 1 和 3 的元素构成第一个数对 (6, 7) 以及下标 2 和 4 构成第二个数对 (2, 4)
# 乘积差是 (6 * 7) - (2 * 4) = 34
#
#
# 示例 2：
#
# 输入：nums = [4,2,5,9,7,4,8]
# 输出：64
# 解释：可以选出下标为 3 和 6 的元素构成第一个数对 (9, 8) 以及下标 1 和 5 构成第二个数对 (2, 4)
# 乘积差是 (9 * 8) - (2 * 4) = 64
#
#
#
#
# 提示：
#
#
# 4 <= nums.length <= 10^4
# 1 <= nums[i] <= 10^4
#
#
#
from typing import List


# @lc code=start
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]


# @lc code=end
