#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   628.三个数的最大乘积.py
@Time    :   2020/09/23 21:10:36
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#
# https://leetcode-cn.com/problems/maximum-product-of-three-numbers/description/
#
# algorithms
# Easy (50.36%)
# Likes:    174
# Dislikes: 0
# Total Accepted:    27.8K
# Total Submissions: 55.2K
# Testcase Example:  '[1,2,3]'
#
# 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
#
# 示例 1:
#
#
# 输入: [1,2,3]
# 输出: 6
#
#
# 示例 2:
#
#
# 输入: [1,2,3,4]
# 输出: 24
#
#
# 注意:
#
#
# 给定的整型数组长度范围是[3,10^4]，数组中所有的元素范围是[-1000, 1000]。
# 输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
#
#
#
from typing import List
"""
方法一：排序

我们将数组进行升序排序，如果数组中所有的元素都是非负数，那么答案即为最后
三个元素的乘积。

如果数组中出现了负数，那么我们还需要考虑乘积中包含负数的情况，显然选择最小
的两个负数和最大的一个正数是最优的，即为前两个元素与最后一个元素的乘积。

上述两个结果中的较大值就是答案。注意我们可以不用判断数组中到底有没有正数，
0 或者负数，因为上述两个结果实际上已经包含了所有情况，最大值一定在其中。
"""


# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1],
                   nums[-3] * nums[-2] * nums[-1])


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.maximumProduct([1, 2, 3]))
    print(solu.maximumProduct([-3, -2, -1]))
    print(solu.maximumProduct([-2, -1, 3]))
    print(solu.maximumProduct([-1, 2, 3]))
    print(solu.maximumProduct([-1, 2, 3, 4]))
    print(solu.maximumProduct([-1, -2, 3, 4]))
    print(solu.maximumProduct([-3, -2, -1, 4]))
    print(solu.maximumProduct([-4, -3, -2, -1]))
