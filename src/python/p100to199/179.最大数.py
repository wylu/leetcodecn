#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   179.最大数.py
@Time    :   2021/04/12 22:24:37
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#
# https://leetcode-cn.com/problems/largest-number/description/
#
# algorithms
# Medium (40.07%)
# Likes:    654
# Dislikes: 0
# Total Accepted:    87.8K
# Total Submissions: 219.2K
# Testcase Example:  '[10,2]'
#
# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
#
# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
#
#
#
# 示例 1：
#
#
# 输入：nums = [10,2]
# 输出："210"
#
# 示例 2：
#
#
# 输入：nums = [3,30,34,5,9]
# 输出："9534330"
#
#
# 示例 3：
#
#
# 输入：nums = [1]
# 输出："1"
#
#
# 示例 4：
#
#
# 输入：nums = [10]
# 输出："10"
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 10^9
#
#
#
from functools import cmp_to_key
from typing import List


# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(num1: str, num2: str) -> int:
            return int(num2 + num1) - int(num1 + num2)

        ans = sorted(map(str, nums), key=cmp_to_key(cmp))
        return '0' if ans[0] == '0' else ''.join(ans)


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.largestNumber([10, 2]))
    print(solu.largestNumber([3, 30, 34, 5, 9]))
    print(solu.largestNumber([1]))
    print(solu.largestNumber([10]))
    print(solu.largestNumber([0, 0]))
