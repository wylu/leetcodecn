#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5908.统计最高分的节点数目.py
@Time    :   2021/10/24 10:57:25
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from collections import deque
from typing import List


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        cnt = [0] * n
        indegree = [0] * n
        p2c = defaultdict(list)
        c2p = {}
        for i in range(1, n):
            c, p = i, parents[i]
            p2c[p].append(c)
            c2p[c] = p
            indegree[p] += 1

        nodes = [1] * n
        que = deque()
        for c, val in enumerate(indegree):
            if val == 0:
                que.append(c)
                nodes[c] = 1

        # print(que)

        while que:
            u = que.popleft()
            res = 1
            for c in p2c[u]:
                res *= nodes[c]
                nodes[u] += nodes[c]

            if n - nodes[u]:
                res *= (n - nodes[u])
            cnt[u] = res

            if u == 0:
                continue

            v = c2p[u]
            indegree[v] -= 1
            if indegree[v] == 0:
                que.append(v)

        # print(cnt)
        ans = 0
        max_val = 0
        for val in cnt:
            if val == max_val:
                ans += 1
            elif val > max_val:
                ans, max_val = 1, val

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.countHighestScoreNodes(parents=[-1, 2, 0, 2, 0]))
    print(solu.countHighestScoreNodes(parents=[-1, 2, 0]))
    print(solu.countHighestScoreNodes(parents=[-1]))
