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
"""
requests 最大只有 16，这意味着我们枚举所有请求的组合，也不过有
1 << 16 = 65536 种可能。对于每种请求的组合，我们只需要检查一下这个组合
是否可以满足。一旦可以满足，记录最大的请求数量即可。

枚举所有请求的组合，可以直接使用状态压缩。用一个数字 state 表示一组请求
的组合，state 的二进制表示中，1 代表采用这个请求，0 代表忽略这个请求。
这样，遍历所有的请求的组合，只需要 state 从 0 检查到 1 << (请求总数)
（最大是 65536）即可。

对于某一个 state，检查的方法也非常简单。我们用 out[k] 表示有多少人想从
k 号楼出来；用 in[k] 表示有多少人想搬入 k 号楼。对于每一个我们需要考虑
的请求 (from, to)，out[from]++，in[to]--。最后，out 和 in 数组中的
对应元素都相等，说明这样一组请求可以被满足。
"""


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans = 0
        m = len(requests)
        for state in range(1 << m):
            ins, outs = [0] * n, [0] * n
            cnt = 0
            for i in range(m):
                if state & (1 << i):
                    ins[requests[i][1]] += 1
                    outs[requests[i][0]] += 1
                    cnt += 1

            flag = True
            for i in range(n):
                if ins[i] != outs[i]:
                    flag = False
                    break

            if flag:
                ans = max(ans, cnt)

        return ans


if __name__ == "__main__":
    solu = Solution()
    requests = [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]
    print(solu.maximumRequests(5, requests))
    requests = [[1, 2], [1, 2], [2, 2], [0, 2], [2, 1], [1, 1], [1, 2]]
    print(solu.maximumRequests(3, requests))
