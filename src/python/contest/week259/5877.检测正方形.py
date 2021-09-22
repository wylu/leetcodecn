#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5877.检测正方形.py
@Time    :   2021/09/19 10:44:25
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class DetectSquares:
    def __init__(self):
        self.x2ys = defaultdict(set)
        self.grid = [[0] * 2010 for _ in range(2010)]

    def add(self, point: List[int]) -> None:
        x, y = point
        self.x2ys[x].add(y)
        self.grid[x][y] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        px, py = point
        for y in self.x2ys[px]:
            if py == y:
                continue

            cnt = 0
            if py > y:
                e = py - y
                cnt += self.grid[px][y] * self.grid[px - e][py] * self.grid[
                    px - e][py - e]
                cnt += self.grid[px][y] * self.grid[px + e][py] * self.grid[
                    px + e][py - e]
            else:
                e = y - py
                cnt += self.grid[px][y] * self.grid[px - e][py] * self.grid[
                    px - e][py + e]
                cnt += self.grid[px][y] * self.grid[px + e][py] * self.grid[
                    px + e][py + e]

            ans += cnt

        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

if __name__ == '__main__':
    obj = DetectSquares()

    operations = [
        "add", "add", "add", "count", "add", "add", "add", "count", "add",
        "add", "add", "count", "add", "add", "add", "count", "add", "add",
        "add", "count", "add", "add", "add", "count", "add", "add", "add",
        "count", "add", "add", "add", "count", "add", "add", "add", "count",
        "add", "add", "add", "count", "add", "add", "add", "count"
    ]
    args = [[[419, 351]], [[798, 351]], [[798, 730]], [[419, 730]], [[998, 1]],
            [[0, 999]], [[998, 999]], [[0, 1]], [[226, 561]], [[269, 561]],
            [[226, 604]], [[269, 604]], [[200, 274]], [[200,
                                                        793]], [[719, 793]],
            [[719, 274]], [[995, 99]], [[146, 948]], [[146, 99]], [[995, 948]],
            [[420, 16]], [[962, 558]], [[420, 558]], [[962, 16]], [[217, 833]],
            [[945, 105]], [[217, 105]], [[945, 833]], [[26, 977]], [[26, 7]],
            [[996, 7]], [[996, 977]], [[96, 38]], [[96, 483]], [[541, 483]],
            [[541, 38]], [[38, 924]], [[961, 1]], [[961, 924]], [[38, 1]],
            [[438, 609]], [[818, 609]], [[818, 229]], [[438, 229]]]
    for oper, arg in zip(operations, args):
        getattr(obj, oper)(arg[0])
