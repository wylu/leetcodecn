#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1356.根据数字二进制下-1-的数目排序.py
@Time    :   2020/11/06 14:37:23
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1356 lang=python3
#
# [1356] 根据数字二进制下 1 的数目排序
#
# https://leetcode-cn.com/problems/sort-integers-by-the-number-of-1-bits/description/
#
# algorithms
# Easy (73.28%)
# Likes:    65
# Dislikes: 0
# Total Accepted:    24.7K
# Total Submissions: 33.7K
# Testcase Example:  '[0,1,2,3,4,5,6,7,8]'
#
# 给你一个整数数组 arr 。请你将数组中的元素按照其二进制表示中数字 1 的数目升序排序。
#
# 如果存在多个数字二进制中 1 的数目相同，则必须将它们按照数值大小升序排列。
#
# 请你返回排序后的数组。
#
#
#
# 示例 1：
#
# 输入：arr = [0,1,2,3,4,5,6,7,8]
# 输出：[0,1,2,4,8,3,5,6,7]
# 解释：[0] 是唯一一个有 0 个 1 的数。
# [1,2,4,8] 都有 1 个 1 。
# [3,5,6] 有 2 个 1 。
# [7] 有 3 个 1 。
# 按照 1 的个数排序得到的结果数组为 [0,1,2,4,8,3,5,6,7]
#
#
# 示例 2：
#
# 输入：arr = [1024,512,256,128,64,32,16,8,4,2,1]
# 输出：[1,2,4,8,16,32,64,128,256,512,1024]
# 解释：数组中所有整数二进制下都只有 1 个 1 ，所以你需要按照数值大小将它们排序。
#
#
# 示例 3：
#
# 输入：arr = [10000,10000]
# 输出：[10000,10000]
#
#
# 示例 4：
#
# 输入：arr = [2,3,5,7,11,13,17,19]
# 输出：[2,3,5,17,7,11,13,19]
#
#
# 示例 5：
#
# 输入：arr = [10,100,1000,10000]
# 输出：[10,100,10000,1000]
#
#
#
#
# 提示：
#
#
# 1 <= arr.length <= 500
# 0 <= arr[i] <= 10^4
#
#
#
from typing import List


# @lc code=start
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        ones = [(bin(v).count('1'), v) for v in arr]
        ones.sort()
        return [v for _, v in ones]


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]))
    print(solu.sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))
    print(solu.sortByBits([10000, 10000]))
    print(solu.sortByBits([2, 3, 5, 7, 11, 13, 17, 19]))
    print(solu.sortByBits([10, 100, 1000, 10000]))
