#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   213.打家劫舍-ii.py
@Time    :   2020/08/21 13:51:33
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#
# https://leetcode-cn.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (39.31%)
# Likes:    354
# Dislikes: 0
# Total Accepted:    51.8K
# Total Submissions: 131.9K
# Testcase Example:  '[2,3,2]'
#
#
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
#
# 示例 1:
#
# 输入: [2,3,2]
# 输出: 3
# 解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
#
#
# 示例 2:
#
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
# 偷窃到的最高金额 = 1 + 3 = 4 。
#
#
from typing import List
"""
此题是 198. 打家劫舍 的拓展版：唯一的区别是此题中的房间是环状排列的
（即首尾相接），而 198. 题中的房间是单排排列的；而这也是此题的难点。

环状排列意味着第一个房子和最后一个房子中只能选择一个偷窃，因此可以把
此环状排列房间问题约化为两个单排排列房间子问题：

  - 在不偷窃第一个房子的情况下（即 nums[1:]），最大金额是 p1；
  - 在不偷窃最后一个房子的情况下（即 nums[:n−1]），最大金额是 p2。

综合偷窃最大金额：为以上两种情况的较大值，即 max(p1,p2) 。
"""


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        pass


# @lc code=end
