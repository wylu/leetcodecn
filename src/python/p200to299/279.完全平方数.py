#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   279.完全平方数.py
@Time    :   2020/09/18 22:32:14
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#
# https://leetcode-cn.com/problems/perfect-squares/description/
#
# algorithms
# Medium (57.84%)
# Likes:    593
# Dislikes: 0
# Total Accepted:    87.1K
# Total Submissions: 150.7K
# Testcase Example:  '12'
#
# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
#
# 示例 1:
#
# 输入: n = 12
# 输出: 3
# 解释: 12 = 4 + 4 + 4.
#
# 示例 2:
#
# 输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9.
#
#
from collections import deque


# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        dist = 0
        q = deque()
        q.append(0)
        while q:
            dist += 1
            nexts = set()
            while q:
                cur = q.popleft()
                i, need = 0, n - cur
                while i * i <= need:
                    if i * i == need:
                        return dist
                    nexts.add(cur + i * i)
                    i += 1
            q = deque(nexts)
        return -1


# @lc code=end
if __name__ == '__main__':
    solu = Solution()
    print(solu.numSquares(12))
    print(solu.numSquares(13))
