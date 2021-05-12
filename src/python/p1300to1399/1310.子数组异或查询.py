#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1310.子数组异或查询.py
@Time    :   2021/05/12 09:31:02
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1310 lang=python3
#
# [1310] 子数组异或查询
#
# https://leetcode-cn.com/problems/xor-queries-of-a-subarray/description/
#
# algorithms
# Medium (70.22%)
# Likes:    70
# Dislikes: 0
# Total Accepted:    11K
# Total Submissions: 15.7K
# Testcase Example:  '[1,3,4,8]\n[[0,1],[1,2],[0,3],[3,3]]'
#
# 有一个正整数数组 arr，现给你一个对应的查询数组 queries，其中 queries[i] = [Li, Ri]。
#
# 对于每个查询 i，请你计算从 Li 到 Ri 的 XOR 值（即 arr[Li] xor arr[Li+1] xor ... xor
# arr[Ri]）作为本次查询的结果。
#
# 并返回一个包含给定查询 queries 所有结果的数组。
#
#
#
# 示例 1：
#
# 输入：arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
# 输出：[2,7,14,8]
# 解释：
# 数组中元素的二进制表示形式是：
# 1 = 0001
# 3 = 0011
# 4 = 0100
# 8 = 1000
# 查询的 XOR 值为：
# [0,1] = 1 xor 3 = 2
# [1,2] = 3 xor 4 = 7
# [0,3] = 1 xor 3 xor 4 xor 8 = 14
# [3,3] = 8
#
#
# 示例 2：
#
# 输入：arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
# 输出：[8,0,4,4]
#
#
#
#
# 提示：
#
#
# 1 <= arr.length <= 3 * 10^4
# 1 <= arr[i] <= 10^9
# 1 <= queries.length <= 3 * 10^4
# queries[i].length == 2
# 0 <= queries[i][0] <= queries[i][1] < arr.length
#
#
#
from typing import List


# @lc code=start
class Solution:
    def xorQueries(self, arr: List[int],
                   queries: List[List[int]]) -> List[int]:
        n = len(arr)
        xors = [0] * (n + 1)
        for i in range(n):
            xors[i + 1] = arr[i] ^ xors[i]

        return [xors[rt + 1] ^ xors[lt] for lt, rt in queries]


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    arr = [1, 3, 4, 8]
    queries = [[0, 1], [1, 2], [0, 3], [3, 3]]
    print(solu.xorQueries(arr, queries))

    arr = [4, 8, 2, 10]
    queries = [[2, 3], [1, 3], [0, 0], [0, 3]]
    print(solu.xorQueries(arr, queries))
