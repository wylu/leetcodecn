#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   79.单词搜索.py
@Time    :   2020/09/13 08:31:27
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (42.69%)
# Likes:    561
# Dislikes: 0
# Total Accepted:    87.6K
# Total Submissions: 205.3K
# Testcase Example:
# '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#
#
# 示例:
#
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false
#
#
#
# 提示：
#
#
# board 和 word 中只包含大写和小写英文字母。
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
#
#
#
from typing import List


# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        d = (0, 1, 0, -1, 0)
        n, m = len(board), len(board[0])

        def dfs(x: int, y: int, c: int) -> bool:
            if x < 0 or x >= n or y < 0 or y >= m or board[x][y] != word[c]:
                return False
            if c == len(word) - 1:
                return True

            tmp, board[x][y] = board[x][y], '#'
            for i in range(4):
                if dfs(x + d[i], y + d[i + 1], c + 1):
                    return True
            board[x][y] = tmp
            return False

        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
        return False


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    print(solu.exist(board, 'ABCCED'))
    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    print(solu.exist(board, 'SEE'))
    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    print(solu.exist(board, 'ABCB'))
