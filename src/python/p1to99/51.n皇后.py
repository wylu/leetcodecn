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
from typing import List
"""
两个有用的细节。

（1）一行只可能有一个皇后且一列也只可能有一个皇后。这意味着没有必要
在棋盘上考虑所有的方格。只需要按列循环即可。
（2）对于所有的主对角线有 行号 + 列号 = 常数，对于所有的次对角线有
行号 - 列号 = 常数。

这可以让我们标记已经在攻击范围下的对角线并且检查一个方格 (行号, 列号) 
是否处在攻击位置。
"""


# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n <= 0:
            return []

        def ok(x: int, y: int) -> bool:
            return not bool(cols[y] + hills[x - y] + dales[x + y])

        def dfs(x: int) -> None:
            if x == n:
                ans.append([''.join(r) for r in cur])
                return

            for y in range(n):
                if ok(x, y):
                    cur[x][y] = 'Q'
                    cols[y], hills[x - y], dales[x + y] = 1, 1, 1
                    dfs(x + 1)
                    cur[x][y] = '.'
                    cols[y], hills[x - y], dales[x + y] = 0, 0, 0

        cols, hills, dales = [0] * n, [0] * (2 * n - 1), [0] * (2 * n - 1)
        ans, cur = [], [['.'] * n for _ in range(n)]
        dfs(0)
        return ans


# @lc code=end

# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         if n <= 0:
#             return []

#         def ok(x: int, y: int) -> bool:
#             for i in range(x - 1, -1, -1):
#                 if cur[i][y] == 'Q':
#                     return False
#             l, r = y - 1, y + 1
#             for i in range(x - 1, -1, -1):
#                 if ((l >= 0 and cur[i][l] == 'Q')
#                         or (r < n and cur[i][r] == 'Q')):
#                     return False
#                 l -= 1  # noqa E741
#                 r += 1
#             return True

#         def dfs(i: int) -> None:
#             if i == n:
#                 ans.append([''.join(r) for r in cur])
#                 return

#             for j in range(n):
#                 cur[i][j] = 'Q'
#                 if ok(i, j):
#                     dfs(i + 1)
#                 cur[i][j] = '.'

#         ans = []
#         cur = [['.'] * n for _ in range(n)]
#         dfs(0)
#         return ans

if __name__ == '__main__':
    from pprint import pprint

    solu = Solution()
    pprint(solu.solveNQueens(4))
    # pprint(solu.solveNQueens(5))
    # pprint(solu.solveNQueens(8))
