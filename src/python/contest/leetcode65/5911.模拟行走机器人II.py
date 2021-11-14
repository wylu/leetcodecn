#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5911.模拟行走机器人II.py
@Time    :   2021/11/13 22:34:24
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.d = 'East'

    def _change_direction(self):
        idx2dir = ['East', 'North', 'West', 'South']
        dir2idx = {'East': 0, 'North': 1, 'West': 2, 'South': 3}
        if ((self.x == 0 and self.y == 0)
                or (self.x == 0 and self.y == self.height - 1)
                or (self.x == self.width - 1 and self.y == 0)
                or (self.x == self.width - 1 and self.y == self.height - 1)):
            idx = (dir2idx[self.d] + 1) % 4
            self.d = idx2dir[idx]

    def move(self, num: int) -> None:
        circle = (self.width + self.height) * 2 - 4
        remain = num % circle
        if not remain:
            remain = circle

        while remain:
            if self.d == 'East':
                step = min(remain, self.width - self.x - 1)
                self.x += step
            elif self.d == 'North':
                step = min(remain, self.height - self.y - 1)
                self.y += step
            elif self.d == 'West':
                step = min(remain, abs(0 - self.x))
                self.x -= step
            else:
                step = min(remain, abs(0 - self.y))
                self.y -= step

            remain -= step
            if remain:
                self._change_direction()

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.d


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.move(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
