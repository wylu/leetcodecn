#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2033.获取单值网格的最小操作数.py
@Time    :   2021/10/12 14:54:36
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=2033 lang=python3
#
# [2033] 获取单值网格的最小操作数
#
# https://leetcode-cn.com/problems/minimum-operations-to-make-a-uni-value-grid/description/
#
# algorithms
# Medium (38.27%)
# Likes:    9
# Dislikes: 0
# Total Accepted:    3.3K
# Total Submissions: 8.6K
# Testcase Example:  '[[2,4],[6,8]]\n2'
#
# 给你一个大小为 m x n 的二维整数网格 grid 和一个整数 x 。每一次操作，你可以对 grid 中的任一元素 加 x 或 减 x 。
#
# 单值网格 是全部元素都相等的网格。
#
# 返回使网格化为单值网格所需的 最小 操作数。如果不能，返回 -1 。
#
#
#
# 示例 1：
#
#
#
#
# 输入：grid = [[2,4],[6,8]], x = 2
# 输出：4
# 解释：可以执行下述操作使所有元素都等于 4 ：
# - 2 加 x 一次。
# - 6 减 x 一次。
# - 8 减 x 两次。
# 共计 4 次操作。
#
#
# 示例 2：
#
#
#
#
# 输入：grid = [[1,5],[2,3]], x = 1
# 输出：5
# 解释：可以使所有元素都等于 3 。
#
#
# 示例 3：
#
#
#
#
# 输入：grid = [[1,2],[3,4]], x = 2
# 输出：-1
# 解释：无法使所有元素相等。
#
#
#
#
# 提示：
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10^5
# 1 <= m * n <= 10^5
# 1 <= x, grid[i][j] <= 10^4
#
#
#
from typing import List
"""
首先，所有数如果不是关于 X 同余，则本题显然无解。

在所有数关于 X 同余的情况下，我们可以将所有数除以 X。这时就变成了经典的
数轴集合问题（N个人在数轴上，要集合到一个位置使得所有人移动距离之和最小），
最优的集合位置就是中位数。我们找到这些数的中位数，再计算总距离（也即
总操作数）即可。

寻找中位数可以排序；也可以使用快速选择算法（比如 C++ 中的 nth_element），
以得到更优的时间复杂度。
"""


# @lc code=start
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        mod = grid[0][0] % x
        nums = []
        for row in grid:
            for num in row:
                if num % x != mod:
                    return -1
                nums.append(num // x)

        nums.sort()
        mid = nums[len(nums) // 2]
        ans = 0
        for num in nums:
            ans += abs(num - mid)

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.minOperations(grid=[[2, 4], [6, 8]], x=2))
    print(solu.minOperations(grid=[[1, 5], [2, 3]], x=1))
    print(solu.minOperations(grid=[[1, 2], [3, 4]], x=2))
