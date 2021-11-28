#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5941.找出知晓秘密的所有专家.py
@Time    :   2021/11/28 10:57:39
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]],
                      firstPerson: int) -> List[int]:
        known = set([0, firstPerson])
        t2m = defaultdict(set)
        for meet in meetings:
            t2m[meet[2]].add(tuple(meet))

        ts = list(t2m.keys())
        ts.sort()

        for t in ts:
            flag = True
            while flag:
                flag = False
                nxt = set()
                for meet in t2m[t]:
                    if meet[0] in known or meet[1] in known:
                        known.add(meet[0])
                        known.add(meet[1])
                        flag = True
                    else:
                        nxt.add(meet)
                t2m[t] = nxt

        return list(known)


if __name__ == '__main__':
    solu = Solution()
    n = 6
    meetings = [[1, 2, 5], [2, 3, 8], [1, 5, 10]]
    firstPerson = 1
    print(solu.findAllPeople(n, meetings, firstPerson))

    n = 4
    meetings = [[3, 1, 3], [1, 2, 2], [0, 3, 3]]
    firstPerson = 3
    print(solu.findAllPeople(n, meetings, firstPerson))

    n = 5
    meetings = [[3, 4, 2], [1, 2, 1], [2, 3, 1]]
    firstPerson = 1
    print(solu.findAllPeople(n, meetings, firstPerson))

    n = 6
    meetings = [[0, 2, 1], [1, 3, 1], [4, 5, 1]]
    firstPerson = 1
    print(solu.findAllPeople(n, meetings, firstPerson))

    n = 11
    meetings = [[5, 1, 4], [0, 4, 18]]
    firstPerson = 1
    # [0,1,4,5]
    print(solu.findAllPeople(n, meetings, firstPerson))
