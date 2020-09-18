#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   克隆图.py
@Time    :   2020/09/18 23:35:18
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node: 'Node') -> 'Node':
            if not node:
                return None
            if node in visit:
                return visit[node]

            copyNode = Node(node.val)
            visit[node] = copyNode
            for neighbor in node.neighbors:
                copyNode.neighbors.append(dfs(neighbor))

            return copyNode

        visit = {}
        return dfs(node)
