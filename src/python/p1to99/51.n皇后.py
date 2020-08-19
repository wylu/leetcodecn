#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   51.n皇后.py
@Time    :   2020/08/18 22:41:51
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#
# https://leetcode-cn.com/problems/n-queens/description/
#
# algorithms
# Hard (70.70%)
# Likes:    507
# Dislikes: 0
# Total Accepted:    56.4K
# Total Submissions: 79.7K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
#
#
# 上图为 8 皇后问题的一种解法。
#
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
#
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
# 示例:
#
# 输入: 4
# 输出: [
# ⁠[".Q..",  // 解法 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
#
# ⁠["..Q.",  // 解法 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
#
#
#
#
# 提示：
#
#
#
# 皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一到七步，可进可退。（引用自
# 百度百科 - 皇后 ）
#
#
#
from copy import deepcopy
from typing import List


# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n <= 0:
            return []

        def ok(cur: List[List[str]], x: int, y: int) -> bool:
            for i in range(n):
                if ((cur[x][i] == 'Q' and i != y)
                        or (cur[i][y] == 'Q' and i != x)):
                    return False
            l, r = y - 1, y + 1
            for i in range(x - 1, -1, -1):
                if ((l >= 0 and cur[x][l] == 'Q')
                        or (r < n and cur[x][r] == 'Q')):
                    return False
            return True

        def dfs(cur: List[List[str]], i: int, cnt: int) -> None:
            if i >= n:
                if cnt == n:
                    ans.append(deepcopy(cur))
                return

            for j in range(n):
                cur[i][j] = 'Q'
                if ok(cur, i, j):
                    dfs(cur, i + 1, cnt + 1)
                cur[i][j] = '.'

        ans = []
        dfs([['.'] * n for _ in range(n)], 0, 0)
        return ans


# @lc code=end

if __name__ == '__main__':
    from pprint import pprint

    solu = Solution()
    pprint(solu.solveNQueens(4))
