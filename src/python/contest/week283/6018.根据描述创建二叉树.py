#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6018.根据描述创建二叉树.py
@Time    :   2022/03/06 10:58:47
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import Counter
from collections import defaultdict
from collections import deque
from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def createBinaryTree(self,
                         descriptions: List[List[int]]) -> Optional[TreeNode]:
        ins = Counter()
        graph = defaultdict(list)
        for u, v, p in descriptions:
            graph[u].append((v, p))
            ins[v] += 1

        root = None
        for u, _, _ in descriptions:
            if ins[u] == 0:
                root = TreeNode(val=u)
                break

        if not root:
            return

        que = deque([root])
        while que:
            node = que.popleft()
            u = node.val
            for v, p in graph[u]:
                child = TreeNode(val=v)
                if p:
                    node.left = child
                else:
                    node.right = child
                ins[v] -= 1
                if ins[v] == 0:
                    que.append(child)

        return root


if __name__ == '__main__':
    solu = Solution()
    descriptions = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0],
                    [80, 19, 1]]
    print(solu.createBinaryTree(descriptions))
