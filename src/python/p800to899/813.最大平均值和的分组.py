#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   813.最大平均值和的分组.py
@Time    :   2022/11/28 09:24:42
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
#
# @lc app=leetcode.cn id=813 lang=python3
#
# [813] 最大平均值和的分组
#
# https://leetcode.cn/problems/largest-sum-of-averages/description/
#
# algorithms
# Medium (56.36%)
# Likes:    259
# Dislikes: 0
# Total Accepted:    12.6K
# Total Submissions: 21.8K
# Testcase Example:  '[9,1,2,3,9]\n3'
#
# 给定数组 nums 和一个整数 k 。我们将给定的数组 nums 分成 最多 k 个相邻的非空子数组 。 分数 由每个子数组内的平均值的总和构成。
#
# 注意我们必须使用 nums 数组中的每一个数进行分组，并且分数不一定需要是整数。
#
# 返回我们所能得到的最大 分数 是多少。答案误差在 10^-6 内被视为是正确的。
#
#
#
# 示例 1:
#
#
# 输入: nums = [9,1,2,3,9], k = 3
# 输出: 20.00000
# 解释:
# nums 的最优分组是[9], [1, 2, 3], [9]. 得到的分数是 9 + (1 + 2 + 3) / 3 + 9 = 20.
# 我们也可以把 nums 分成[9, 1], [2], [3, 9].
# 这样的分组得到的分数为 5 + 2 + 6 = 13, 但不是最大值.
#
#
# 示例 2:
#
#
# 输入: nums = [1,2,3,4,5,6,7], k = 4
# 输出: 20.50000
#
#
#
#
# 提示:
#
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 10^4
# 1 <= k <= nums.length
#
#
#
from typing import List


# @lc code=start
class Solution:

    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        ps = [0] * (n + 1)
        for i in range(n):
            ps[i + 1] = ps[i] + nums[i]

        f = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            f[i][1] = ps[i] / i

        for j in range(2, k + 1):
            for i in range(j, n + 1):
                for x in range(j - 1, i):
                    cur = (ps[i] - ps[x]) / (i - x)
                    f[i][j] = max(f[i][j], f[x][j - 1] + cur)

        return f[n][k]


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    nums = [4, 1, 7, 5, 6, 2, 3]
    k = 4
    print(solu.largestSumOfAverages(nums, k))
