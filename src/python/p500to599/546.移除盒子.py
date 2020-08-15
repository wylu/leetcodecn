#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   546.移除盒子.py
@Time    :   2020/08/15 09:49:05
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=546 lang=python3
#
# [546] 移除盒子
#
# https://leetcode-cn.com/problems/remove-boxes/description/
#
# algorithms
# Hard (51.23%)
# Likes:    144
# Dislikes: 0
# Total Accepted:    4.9K
# Total Submissions: 8.9K
# Testcase Example:  '[1,3,2,2,2,3,4,3,1]\r'
#
# 给出一些不同颜色的盒子，盒子的颜色由数字表示，即不同的数字表示不同的颜色。
# 你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止。每一轮你可以移除具有相同颜色的连续 k 个盒子（k >= 1），这样一轮之后你将得到 k*k
# 个积分。
# 当你将所有盒子都去掉之后，求你能获得的最大积分和。
#
#
#
# 示例：
#
# 输入：boxes = [1,3,2,2,2,3,4,3,1]
# 输出：23
# 解释：
# [1, 3, 2, 2, 2, 3, 4, 3, 1]
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 分)
# ----> [1, 3, 3, 3, 1] (1*1=1 分)
# ----> [1, 1] (3*3=9 分)
# ----> [] (2*2=4 分)
#
#
#
#
# 提示：
#
#
# 1 <= boxes.length <= 100
# 1 <= boxes[i] <= 100
#
#
#
from typing import List
"""
Dynamic Programming

State:
  dp[l][r][k]: 起始下标 l (以0开始)，结束下标 r，k 表示在下标 r 后面紧接着
  有 k 个元素值和 boxes[r] 相同，的最大积分和

  比如 [l, l+1, ···, r-1, r, 值同r, 值同r, 值同r]，这里有 3 个元素和
  boxes[r] 相同，即 k==3，那么 dp[l][r][3] = dp[l][r-1][0] + 4*4，
  因为有 3 个和 boxes[r] 相同，即可以消除 4 个所以加上 4*4

Initial State:
  得到初始化条件dp[l][r][k] = dp[l][r-1][0] + (k+1)*(k+1)

State Transition:
  但是有可能在 boxes[l]~boxes[r-1] 中也存在和 boxes[r]相同值的元素，有可能
  获得更大的积分和。

  比如 [l, l+1, ···, i, ···, r-1, r, 值同r, 值同r, 值同r]，
  假设 boxes[i] == boxes[r]，那么先移除 boxes[i+1]~boxes[r-1]，将使原来的
  dp[l][r][3] 的 k=3 变的更大，r变得更小，但是积分和可能变得更大。

  因此就需要在 boxes[l]~boxes[r-1] 中找到 boxes[i] == boxes[r]，
  这样子先移除 boxes[i+1]~boxes[r-1]，这一部分的最大积分和是 dp[i+1][r-1][0]，
  移除之后是 [l, l+1, ···, i, 值同i(原来是r), 值同i(原来是r+1),
  值同i(原来是r+2), 值同i(原来是r+3)]，也即 dp[l][i][k+1]

  所以只需枚举可能的 i 就能得到 dp[l][r][k] 的最优结果：
  dp[l][r][k] = max(dp[l][r][k], dp[i+1][r-1][0] + dp[l][i][k+1])

  最后的答案就是 dp[0][len(boxes)-1][0]
"""


# @lc code=start
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        dp = [[[0] * n for _ in range(n)] for _ in range(n)]

        def dfs(l: int, r: int, k: int) -> int:  # noqa: E741
            if l > r:
                return 0

            # 记忆化
            if dp[l][r][k] != 0:
                return dp[l][r][k]

            # 尽可能的缩小 r 可让递归剪枝
            while l < r and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1

            # 初始值
            dp[l][r][k] = dfs(l, r - 1, 0) + (k + 1) * (k + 1)
            # 枚举可能的消除策略
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    dp[l][r][k] = max(dp[l][r][k],
                                      dfs(i + 1, r - 1, 0) + dfs(l, i, k + 1))

            return dp[l][r][k]

        return dfs(0, n - 1, 0)


# @lc code=end
