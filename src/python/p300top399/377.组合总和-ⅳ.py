#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   377.组合总和-ⅳ.py
@Time    :   2021/04/24 10:27:23
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#
# https://leetcode-cn.com/problems/combination-sum-iv/description/
#
# algorithms
# Medium (45.53%)
# Likes:    343
# Dislikes: 0
# Total Accepted:    30.7K
# Total Submissions: 67.2K
# Testcase Example:  '[1,2,3]\n4'
#
# 给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。
#
# 题目数据保证答案符合 32 位整数范围。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,3], target = 4
# 输出：7
# 解释：
# 所有可能的组合为：
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# 请注意，顺序不同的序列被视作不同的组合。
#
#
# 示例 2：
#
#
# 输入：nums = [9], target = 3
# 输出：0
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# nums 中的所有元素 互不相同
# 1 <= target <= 1000
#
#
#
#
# 进阶：如果给定的数组中含有负数会发生什么？问题会产生何种变化？如果允许负数出现，需要向题目中添加哪些限制条件？
#
#
from typing import List
"""
动态规划
本题与「完全背包求方案数」问题的差别在于：选择方案中的不同的物品顺序代表
不同方案。

举个例子，在「完全背包」问题中，凑成总价值为 6 的方案 [1,2,3] 算是 1 种
方案，但在本题算是 3 * 2 * 1 = 6 种方案（[1,2,3],[2,1,3],[3,1,2]...）

因此我们不能直接代入「完全背包」的思路（状态定义）来求解。

这时候可以从「构成答案的组合」入手：利用 1 <= nums[i] <= 1000 和
1 <= target <= 1000 条件可以确定，组合长度必然在 [1, 1000]。

定义 f[i][j] 为组合长度为 i，凑成总和为 j 的方案数是多少。由于对组合
方案的长度没有限制，因此我们最终答案为所有的 f[x][target] 的总和。

同时有显而易见的初始条件（有效值）：f[0][0] = 1。

那么对任意的 f[len][target] 而言，组合中的最后一个数字可以选择 nums 中的
任意数值，因此 f[len][target] 应该为以下所有方案总和：

最后一个数选择 nums[0]，方案数为 f[len - 1][target - nums[0]]
最后一个数选择 nums[1]，方案数为 f[len - 1][target - nums[1]]
最后一个数选择 nums[2]，方案数为 f[len - 1][target - nums[2]]
...
即转移方程为：

  0 <= i < n
  f[len][target] = f[len - 1][target - nums[i]], target >= nums[i]

降维优化
我们知道「完全背包」可以通过取消物品维度来实现降维优化。

本题也可以使用相同手段：定义 f[i] 为凑成总和为 i 的方案数是多少。由于
nums 的数都是正整数，因此我们有显然的初始化条件 f[0] = 1（代表什么都
不选，凑成总和为 0 的方案数为 1），同时最终答案为 f[target]。

不失一般性的考虑 f[i] 该如何转移，由于每个数值可以被选择无限次，因此在
计算任意总和时，我们保证 nums 中的每一位都会被考虑到即可（即确保对组合
总和 target 的遍历在外，对数组 nums 的遍历在内）。

即转移方程为：

  0 <= i < n
  f[j] = f[target - nums[i]], target >= nums[i]
"""


# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        f = [1] + [0] * (target)

        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    f[i] += f[i - num]

        return f[target]


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.combinationSum4(nums=[1, 2, 3], target=4))
    print(solu.combinationSum4(nums=[9], target=3))
