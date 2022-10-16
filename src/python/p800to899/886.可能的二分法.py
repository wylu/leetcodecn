#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   886.可能的二分法.py
@Time    :   2022/10/16 19:19:20
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
#
# @lc app=leetcode.cn id=886 lang=python3
#
# [886] 可能的二分法
#
# https://leetcode.cn/problems/possible-bipartition/description/
#
# algorithms
# Medium (49.69%)
# Likes:    297
# Dislikes: 0
# Total Accepted:    33.7K
# Total Submissions: 66.9K
# Testcase Example:  '4\n[[1,2],[1,3],[2,4]]'
#
# 给定一组 n 人（编号为 1, 2, ..., n）， 我们想把每个人分进任意大小的两组。每个人都可能不喜欢其他人，那么他们不应该属于同一组。
#
# 给定整数 n 和数组 dislikes ，其中 dislikes[i] = [ai, bi] ，表示不允许将编号为 ai 和
# bi的人归入同一组。当可以用这种方法将所有人分进两组时，返回 true；否则返回 false。
#
#
#
#
#
#
# 示例 1：
#
#
# 输入：n = 4, dislikes = [[1,2],[1,3],[2,4]]
# 输出：true
# 解释：group1 [1,4], group2 [2,3]
#
#
# 示例 2：
#
#
# 输入：n = 3, dislikes = [[1,2],[1,3],[2,3]]
# 输出：false
#
#
# 示例 3：
#
#
# 输入：n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# 输出：false
#
#
#
#
# 提示：
#
#
# 1 <= n <= 2000
# 0 <= dislikes.length <= 10^4
# dislikes[i].length == 2
# 1 <= dislikes[i][j] <= n
# ai < bi
# dislikes 中每一组都 不同
#
#
#
#
#
from typing import List


# @lc code=start
class Solution:

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = [[] for _ in range(n)]
        for x, y in dislikes:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)

        # color[x] = 0 表示未访问节点 x
        color = [0] * n

        def dfs(x: int, c: int) -> bool:
            color[x] = c
            return all(color[y] != c and (color[y] or dfs(y, -c))
                       for y in g[x])

        return all(c or dfs(i, 1) for i, c in enumerate(color))


# @lc code=end
