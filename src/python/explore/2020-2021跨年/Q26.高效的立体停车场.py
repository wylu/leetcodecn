#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   Q26.高效的立体停车场.py
@Time    :   2020/12/26 21:59:57
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
https://leetcode-cn.com/leetbook/read/interesting-algorithm-puzzles-for-programmers/97g5sc/

方法一：广度优先搜索
思路与算法

对于找出「最少步数」的题目，我们一般可以使用广度优先搜索的方法解决。

对于本题中 m = n = 10 的停车场，如果我们把整个停车场看成一个二维数组，
表示广度优先搜索中的每一个状态，那么将会在搜索中使用大量的空间，并且
使得编码变得较为困难。但如果我们把初始时位于左上角的车成为「目标车」，
那么在任意时刻我们其实只会关心目标车和空位所在的格子，而其余所有的格子
都是其它的车，我们不必真正的将它们存储在状态中。

因此，我们可以使用一个二元组 (car,space) 表示一个状态，其中 car 表示
目标车所在的格子，space 表示空位所在的格子。由于停车场是二维的，对于
第 i 行第 j 列的格子，我们可以使用 i * n + j 将二维「压缩」成一维进行
存储在一个变量中。这样每一个在 [0, mn) 中的数都恰好对应了二维停车场中
的一个格子。

在广度优先搜索的过程中，我们每一步只能将一辆车移动至相邻的空位中，那么
我们可以将这个过程看作「将空位与相邻的一辆车进行交换」，那么 space
左右上下分别对应着 space−1，space+1，space−n 和 space+n。需要注意
的是，如果相邻的位置是目标车，那么也需要对 car 进行修改，实际上在这种
情况中，我们只需要将 space 和 car 直接交换即可。

此外，对于每一个状态，我们还需要使用变量 step 记录移动的步数，以便最终
返回答案。为了防止重复搜索，我们需要使用哈希表存储所有已搜索和待搜索的
状态，防止重复搜索同一个状态。
"""
from collections import deque
from typing import List


class Status(object):
    m = 10
    n = 10

    def __init__(self, car: int = 0, space: int = m * n - 1, step: int = 0):
        self.car = car
        self.space = space
        self.step = step

    def __hash__(self):
        return hash(f'{self.car}{self.space}')

    def __eq__(self, other: 'Status') -> bool:
        return (self.car == other.car) and (self.space == other.space)

    # 空位左移
    def go_left(self):
        # 在最左列
        if self.space % self.n == 0:
            return
        if self.car == self.space - 1:
            return Status(self.space, self.car, self.step + 1)
        return Status(self.car, self.space - 1, self.step + 1)

    # 空位右移
    def go_right(self):
        # 在最右列
        if self.space % self.n == self.n - 1:
            return
        if self.car == self.space + 1:
            return Status(self.space, self.car, self.step + 1)
        return Status(self.car, self.space + 1, self.step + 1)

    # 空位上移
    def go_up(self):
        # 在最上行
        if self.space // self.n == 0:
            return
        if self.car == self.space - self.n:
            return Status(self.space, self.car, self.step + 1)
        return Status(self.car, self.space - self.n, self.step + 1)

    # 空位下移
    def go_down(self):
        # 在最下行
        if self.space // self.n == self.m - 1:
            return
        if self.car == self.space + self.n:
            return Status(self.space, self.car, self.step + 1)
        return Status(self.car, self.space + self.n, self.step + 1)

    def get_adjacent(self) -> List['Status']:
        neighbors = [
            self.go_left(),
            self.go_right(),
            self.go_up(),
            self.go_down()
        ]
        return [neighbor for neighbor in neighbors if neighbor]

    def finished(self) -> bool:
        return self.car == self.m * self.n - 1


class Solution:
    def effectiveParkingArea(self, m: int, n: int) -> int:
        Status.m, Status.n = m, n
        seen = set()
        q = deque([Status()])

        while q:
            cur = q.popleft()
            for neighbor in cur.get_adjacent():
                if neighbor.finished():
                    return neighbor.step

                if neighbor not in seen:
                    seen.add(neighbor)
                    q.append(neighbor)

        return -1


if __name__ == "__main__":
    solu = Solution()
    print(solu.effectiveParkingArea(10, 10))
