#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   547.朋友圈.py
@Time    :   2020/08/28 13:06:52
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#
# https://leetcode-cn.com/problems/friend-circles/description/
#
# algorithms
# Medium (57.88%)
# Likes:    304
# Dislikes: 0
# Total Accepted:    60.3K
# Total Submissions: 104.2K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
#
# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C
# 的朋友。所谓的朋友圈，是指所有朋友的集合。
#
# 给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j
# 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。
#
#
#
# 示例 1：
#
# 输入：
# [[1,1,0],
# ⁠[1,1,0],
# ⁠[0,0,1]]
# 输出：2
# 解释：已知学生 0 和学生 1 互为朋友，他们在一个朋友圈。
# 第2个学生自己在一个朋友圈。所以返回 2 。
#
#
# 示例 2：
#
# 输入：
# [[1,1,0],
# ⁠[1,1,1],
# ⁠[0,1,1]]
# 输出：1
# 解释：已知学生 0 和学生 1 互为朋友，学生 1 和学生 2 互为朋友，所以学生 0 和学生 2 也是朋友，所以他们三个在一个朋友圈，返回 1
# 。
#
#
#
#
# 提示：
#
#
# 1 <= N <= 200
# M[i][i] == 1
# M[i][j] == M[j][i]
#
#
#
from typing import List


# @lc code=start
class Solution:
    def findCircleNum(self, matrix: List[List[int]]) -> int:
        def dfs(x: int) -> bool:
            flag = False
            friends = []
            for y in range(n):
                if matrix[x][y] == 1:
                    flag = True
                    friends.append(y)
                    matrix[x][y] = matrix[y][x] = 0
            for z in friends:
                dfs(z)
            return flag

        ans = 0
        n = len(matrix)
        for i in range(n):
            if dfs(i):
                ans += 1

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    friends = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
    print(solu.findCircleNum(friends))
