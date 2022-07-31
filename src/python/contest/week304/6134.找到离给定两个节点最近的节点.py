#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6134.找到离给定两个节点最近的节点.py
@Time    :   2022/07/31 10:47:11
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import deque
from typing import List


class Solution:

    def closestMeetingNode(self, edges: List[int], node1: int,
                           node2: int) -> int:
        graph = {u: v for u, v in enumerate(edges) if v != -1}

        def bfs(node: int) -> dict:
            que = deque([node])
            dist, depth = {}, 0
            while que:
                next_level = set()
                for _ in range(len(que)):
                    u = que.popleft()
                    if u not in dist:
                        dist[u] = depth

                    if u in graph and graph[u] not in dist:
                        next_level.add(graph[u])

                for v in next_level:
                    que.append(v)

                depth += 1

            return dist

        min_label, min_dist = -1, 0x7FFFFFFF
        dist1, dist2 = bfs(node1), bfs(node2)
        for node in range(len(edges)):
            if node in dist1 and node in dist2:
                d = max(dist1[node], dist2[node])
                if d < min_dist:
                    min_label, min_dist = node, d

        return min_label


if __name__ == '__main__':
    solu = Solution()
    print(solu.closestMeetingNode(edges=[2, 2, 3, -1], node1=0, node2=1))
    print(solu.closestMeetingNode(edges=[1, 2, -1], node1=0, node2=2))
    print(solu.closestMeetingNode(edges=[-1, 2, 3, -1], node1=0, node2=1))
