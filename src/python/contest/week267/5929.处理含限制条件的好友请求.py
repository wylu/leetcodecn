#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5929.处理含限制条件的好友请求.py
@Time    :   2021/11/14 11:37:38
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> None:
        self.par[self.find(x)] = self.find(y)


class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]],
                       requests: List[List[int]]) -> List[bool]:
        ans = []
        uf = UnionFind(n)
        for u, v in requests:
            if uf.find(u) == uf.find(v):
                ans.append(True)
                continue

            su, sv = set(), set()
            pu, pv = uf.find(u), uf.find(v)
            for i in range(n):
                p = uf.find(i)
                if p == pu:
                    su.add(i)
                if p == pv:
                    sv.add(i)

            flag = True
            for eu, ev in restrictions:
                if (eu in su and ev in sv) or (eu in sv and ev in su):
                    flag = False
                    break

            ans.append(flag)
            if flag:
                uf.union(u, v)

        return ans


if __name__ == '__main__':
    solu = Solution()
    n = 5
    restrictions = [[0, 1], [1, 2], [2, 3]]
    requests = [[0, 4], [1, 2], [3, 1], [3, 4]]
    print(solu.friendRequests(n, restrictions, requests))
