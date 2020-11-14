#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1122.数组的相对排序.py
@Time    :   2020/11/14 10:57:42
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#
# https://leetcode-cn.com/problems/relative-sort-array/description/
#
# algorithms
# Easy (67.10%)
# Likes:    110
# Dislikes: 0
# Total Accepted:    32.3K
# Total Submissions: 47K
# Testcase Example:  '[2,3,1,3,2,4,6,7,9,2,19]\n[2,1,4,3,9,6]'
#
# 给你两个数组，arr1 和 arr2，
#
#
# arr2 中的元素各不相同
# arr2 中的每个元素都出现在 arr1 中
#
#
# 对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1
# 的末尾。
#
#
#
# 示例：
#
# 输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# 输出：[2,2,2,1,4,3,3,9,6,7,19]
#
#
#
#
# 提示：
#
#
# arr1.length, arr2.length <= 1000
# 0 <= arr1[i], arr2[i] <= 1000
# arr2 中的元素 arr2[i] 各不相同
# arr2 中的每个元素 arr2[i] 都出现在 arr1 中
#
#
#
from functools import cmp_to_key
from typing import List


# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        pos = {num: i for i, num in enumerate(arr2)}

        def cmp(x: int, y: int) -> bool:
            if x in pos:
                return pos[x] - pos[y] if y in pos else -1
            else:
                return 1 if y in pos else x - y

        arr1.sort(key=cmp_to_key(cmp))
        return arr1


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    print(solu.relativeSortArray(arr1, arr2))
