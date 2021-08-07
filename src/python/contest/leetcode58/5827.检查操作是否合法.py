#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5827.检查操作是否合法.py
@Time    :   2021/08/07 23:58:50
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int,
                  color: str) -> bool:
        n = len(board)

        middle = 'W' if color == 'B' else 'B'

        # up
        if rMove >= 2:
            for i in range(rMove - 1, -1, -1):
                if board[i][cMove] != middle:
                    if board[i][cMove] == color and rMove - i >= 2:
                        return True
                    break

        # down
        if rMove <= n - 3:
            for i in range(rMove + 1, n):
                if board[i][cMove] != middle:
                    if board[i][cMove] == color and i - rMove >= 2:
                        return True
                    break

        # left
        if cMove >= 2:
            for i in range(cMove - 1, -1, -1):
                if board[rMove][i] != middle:
                    if board[rMove][i] == color and cMove - i >= 2:
                        return True
                    break

        # right
        if cMove <= n - 3:
            for i in range(cMove + 1, n):
                if board[rMove][i] != middle:
                    if board[rMove][i] == color and i - cMove >= 2:
                        return True
                    break

        # left-up
        if rMove >= 2 and cMove >= 2:
            for i in range(1, min(rMove, cMove) + 1):
                if board[rMove - i][cMove - i] != middle:
                    if board[rMove - i][cMove - i] == color and i >= 2:
                        return True
                    break

        # right-up
        if rMove >= 2 and cMove <= n - 3:
            for i in range(1, min(rMove, n - cMove - 1) + 1):
                if board[rMove - i][cMove + i] != middle:
                    if board[rMove - i][cMove + i] == color and i >= 2:
                        return True
                    break

        # left-down
        if rMove <= n - 3 and cMove >= 2:
            for i in range(1, min(n - rMove - 1, cMove) + 1):
                if board[rMove + i][cMove - i] != middle:
                    if board[rMove + i][cMove - i] == color and i >= 2:
                        return True
                    break

        # right-down
        if rMove <= n - 3 and cMove <= n - 3:
            for i in range(1, min(n - rMove - 1, n - cMove - 1) + 1):
                if board[rMove + i][cMove + i] != middle:
                    if board[rMove + i][cMove + i] == color and i >= 2:
                        return True
                    break

        return False
