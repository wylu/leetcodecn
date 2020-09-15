#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   37.解数独.py
@Time    :   2020/09/15 13:23:58
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#
# https://leetcode-cn.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (64.75%)
# Likes:    577
# Dislikes: 0
# Total Accepted:    46.5K
# Total Submissions: 71.8K
# Testcase Example:
# '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# 编写一个程序，通过已填充的空格来解决数独问题。
#
# 一个数独的解法需遵循如下规则：
#
#
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
#
#
# 空白格用 '.' 表示。
#
#
#
# 一个数独。
#
#
#
# 答案被标成红色。
#
# Note:
#
#
# 给定的数独序列只包含数字 1-9 和字符 '.' 。
# 你可以假设给定的数独只有唯一解。
# 给定数独永远是 9x9 形式的。
#
#
#
from typing import List


# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def ok(x: int, y: int, num: str) -> bool:
            for i in range(9):
                cx = (x // 3) * 3 + i // 3
                cy = (y // 3) * 3 + i % 3
                if (board[x][i] == num or board[i][y] == num
                        or board[cx][cy] == num):
                    return False
            return True

        def dfs(x: int, y: int) -> bool:
            for i in range(x, 9):
                for j in range(y, 9):
                    if board[i][j] != '.':
                        continue
                    for num in opts:
                        if ok(i, j, num):
                            board[i][j] = num
                            if dfs(i, j + 1):
                                return True
                            board[i][j] = '.'
                    return False
                y = 0
            return True

        opts = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
        dfs(0, 0)


# @lc code=end

if __name__ == '__main__':
    from pprint import pprint

    solu = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    solu.solveSudoku(board)
    pprint(board)
