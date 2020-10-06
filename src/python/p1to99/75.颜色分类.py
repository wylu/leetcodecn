#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   75.颜色分类.py
@Time    :   2020/10/06 19:12:04
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
# https://leetcode-cn.com/problems/sort-colors/description/
#
# algorithms
# Medium (55.42%)
# Likes:    604
# Dislikes: 0
# Total Accepted:    118.5K
# Total Submissions: 213.9K
# Testcase Example:  '[2,0,2,1,1,0]'
#
# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
#
# 注意:
# 不能使用代码库中的排序函数来解决这道题。
#
# 示例:
#
# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]
#
# 进阶：
#
#
# 一个直观的解决方案是使用计数排序的两趟扫描算法。
# 首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
# 你能想出一个仅使用常数空间的一趟扫描算法吗？
#
#
#
from typing import List
"""
荷兰国旗问题

https://leetcode-cn.com/problems/sort-colors/solution/yan-se-fen-lei-by-leetcode/

我们用三个指针（p0, p2 和 curr）来分别追踪0的最右边界，2的最左边界和当前考虑的元素。

本解法的思路是沿着数组移动 curr 指针，若 nums[curr] = 0，则将其与 nums[p0]互换；
若 nums[curr] = 2 ，则与 nums[p2]互换。

算法

初始化 0 的最右边界：p0 = 0。在整个算法执行过程中 nums[idx < p0] = 0.
初始化 2 的最左边界：p2 = n - 1。在整个算法执行过程中 nums[idx > p2] = 2.
初始化当前考虑的元素序号：curr = 0.
While curr <= p2 :
  若 nums[curr] = 0：交换第 curr 个和第 p0个元素，并将指针都向右移。
  若 nums[curr] = 2：交换第 curr 个和第 p2个元素，并将 p2 指针左移。
  若 nums[curr] = 1：将指针 curr 右移。
"""


# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 对于所有 idx < p0 : nums[idx < p0] = 0
        # curr是当前考虑元素的下标
        p0 = curr = 0
        # 对于所有 idx > p2 : nums[idx > p2] = 2
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    solu.sortColors(nums)
    print(nums)
