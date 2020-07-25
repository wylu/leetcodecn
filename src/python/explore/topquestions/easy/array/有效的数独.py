#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   有效的数独.py
@Time    :   2020/07/25 17:42:22
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False for _ in range(9)] for _ in range(9)]
        cols = [[False for _ in range(9)] for _ in range(9)]
        boxes = [[False for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                num = int(board[i][j])
                idx = i // 3 * 3 + j // 3
                if rows[i][num - 1] or cols[j][num - 1] or boxes[idx][num - 1]:
                    return False

                rows[i][num - 1] = True
                cols[j][num - 1] = True
                boxes[idx][num - 1] = True

        return True
