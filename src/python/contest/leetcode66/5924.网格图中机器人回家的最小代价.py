#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5924.网格图中机器人回家的最小代价.py
@Time    :   2021/11/27 22:48:51
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def minCost(self, startPos: List[int], homePos: List[int],
                rowCosts: List[int], colCosts: List[int]) -> int:
        robotX, robotY = startPos
        homeX, homeY = homePos

        def countX() -> int:
            res = 0
            if robotX > homeX:
                begin, end = homeX, robotX
            elif robotX < homeX:
                begin, end = robotX + 1, homeX + 1
            else:
                begin, end = robotX, homeX
            # print(f'CountX begin: {begin}, end: {end}')
            for i in range(begin, end):
                res += rowCosts[i]
            return res

        def countY() -> int:
            res = 0
            if robotY > homeY:
                begin, end = homeY, robotY
            elif robotY < homeY:
                begin, end = robotY + 1, homeY + 1
            else:
                begin, end = robotY, homeY
            # print(f'CountY begin: {begin}, end: {end}')
            for i in range(begin, end):
                res += colCosts[i]
            return res

        return countX() + countY()


if __name__ == '__main__':
    solu = Solution()
    startPos = [1, 0]
    homePos = [2, 3]
    rowCosts = [5, 4, 3]
    colCosts = [8, 2, 6, 7]
    print(solu.minCost(startPos, homePos, rowCosts, colCosts))
