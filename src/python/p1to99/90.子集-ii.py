#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   90.子集-ii.py
@Time    :   2021/03/31 13:46:15
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (62.93%)
# Likes:    484
# Dislikes: 0
# Total Accepted:    86.2K
# Total Submissions: 136.9K
# Testcase Example:  '[1,2,2]'
#
# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
#
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
#
#
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
#
#
# 示例 2：
#
#
# 输入：nums = [0]
# 输出：[[],[0]]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
#
#
#
#
#
from typing import List
"""
方法一：迭代法实现子集枚举
思路

考虑数组 [1,2,2]，选择前两个数，或者第一、三个数，都会得到相同的子集。

也就是说，对于当前选择的数 x，若前面有与其相同的数 y，且没有选择 y，
此时包含 x 的子集，必然会出现在包含 y 的所有子集中。

我们可以通过判断这种情况，来避免生成重复的子集。代码实现时，可以先将
数组排序；迭代时，若发现没有选择上一个数，且当前数字与上一个数相同，
则可以跳过当前生成的子集。

方法二：递归法实现子集枚举
思路

与方法一类似，在递归时，若发现没有选择上一个数，且当前数字与上一个数相同，
则可以跳过当前生成的子集。
"""


# @lc code=start
# 方法二
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans, stack = [], []

        def dfs(cur: int, choosePre: bool) -> None:
            if cur == n:
                ans.append(stack[:])
                return

            dfs(cur + 1, False)
            if not choosePre and cur > 0 and nums[cur - 1] == nums[cur]:
                return
            stack.append(nums[cur])
            dfs(cur + 1, True)
            stack.pop()

        nums.sort()
        dfs(0, False)

        return ans


# @lc code=end

# 方法一
# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         ans, n = [], len(nums)
#         nums.sort()

#         for mask in range(1 << n):
#             flag, stack = True, []
#             for i in range(n):
#                 if mask & (1 << i):
#                     if (i > 0 and ((mask >> (i - 1)) & 1) == 0
#                             and nums[i] == nums[i - 1]):
#                         flag = False
#                         break
#                     stack.append(nums[i])
#             if flag:
#                 ans.append(stack)

#         return ans

if __name__ == '__main__':
    solu = Solution()
    print(solu.subsetsWithDup([1, 2, 2]))
    print(solu.subsetsWithDup([0]))
