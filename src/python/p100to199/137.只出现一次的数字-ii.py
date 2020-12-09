#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   137.只出现一次的数字-ii.py
@Time    :   2020/12/09 22:02:59
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#
# https://leetcode-cn.com/problems/single-number-ii/description/
#
# algorithms
# Medium (68.22%)
# Likes:    468
# Dislikes: 0
# Total Accepted:    46.5K
# Total Submissions: 68.2K
# Testcase Example:  '[2,2,3,2]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
#
# 说明：
#
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 示例 1:
#
# 输入: [2,2,3,2]
# 输出: 3
#
#
# 示例 2:
#
# 输入: [0,1,0,1,0,1,99]
# 输出: 99
#
#
from typing import List
"""
方法三：位运算符：NOT，AND 和 XOR
思路

为了区分出现一次的数字和出现三次的数字，使用两个位掩码：
seen_once 和 seen_twice。思路是：
  - 仅当 seen_twice 未变时，改变 seen_once。
  - 仅当 seen_once 未变时，改变seen_twice。

位掩码 seen_once 仅保留出现一次的数字，不保留出现三次的数字。
"""


# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        for num in nums:
            # first appearance:
            # add num to seen_once
            # don't add to seen_twice because of presence in seen_once

            # second appearance:
            # remove num from seen_once
            # add num to seen_twice

            # third appearance:
            # don't add to seen_once because of presence in seen_twice
            # remove num from seen_twice
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)
        return seen_once


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.singleNumber([2, 2, 3, 2]))
    print(solu.singleNumber([0, 1, 0, 1, 0, 1, 99]))
