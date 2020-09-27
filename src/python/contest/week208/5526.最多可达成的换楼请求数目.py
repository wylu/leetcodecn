#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5526.最多可达成的换楼请求数目.py
@Time    :   2020/09/27 13:08:54
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    solu = Solution()
    requests = [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]
    print(solu.maximumRequests(5, requests))
    requests = [[1, 2], [1, 2], [2, 2], [0, 2], [2, 1], [1, 1], [1, 2]]
    print(solu.maximumRequests(3, requests))
