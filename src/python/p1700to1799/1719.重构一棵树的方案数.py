#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1719.重构一棵树的方案数.py
@Time    :   2022/02/16 20:09:01
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1719 lang=python3
#
# [1719] 重构一棵树的方案数
#
# https://leetcode-cn.com/problems/number-of-ways-to-reconstruct-a-tree/description/
#
# algorithms
# Hard (68.55%)
# Likes:    107
# Dislikes: 0
# Total Accepted:    8.3K
# Total Submissions: 12.1K
# Testcase Example:  '[[1,2],[2,3]]'
#
# 给你一个数组 pairs ，其中 pairs[i] = [xi, yi] ，并且满足：
#
#
# pairs 中没有重复元素
# xi < yi
#
#
# 令 ways 为满足下面条件的有根树的方案数：
#
#
# 树所包含的所有节点值都在 pairs 中。
# 一个数对 [xi, yi] 出现在 pairs 中 当且仅当 xi 是 yi 的祖先或者 yi 是 xi 的祖先。
# 注意：构造出来的树不一定是二叉树。
#
#
# 两棵树被视为不同的方案当存在至少一个节点在两棵树中有不同的父节点。
#
# 请你返回：
#
#
# 如果 ways == 0 ，返回 0 。
# 如果 ways == 1 ，返回 1 。
# 如果 ways > 1 ，返回 2 。
#
#
# 一棵 有根树 指的是只有一个根节点的树，所有边都是从根往外的方向。
#
# 我们称从根到一个节点路径上的任意一个节点（除去节点本身）都是该节点的 祖先 。根节点没有祖先。
#
#
#
# 示例 1：
#
#
# 输入：pairs = [[1,2],[2,3]]
# 输出：1
# 解释：如上图所示，有且只有一个符合规定的有根树。
#
#
# 示例 2：
#
#
# 输入：pairs = [[1,2],[2,3],[1,3]]
# 输出：2
# 解释：有多个符合规定的有根树，其中三个如上图所示。
#
#
# 示例 3：
#
#
# 输入：pairs = [[1,2],[2,3],[2,4],[1,5]]
# 输出：0
# 解释：没有符合规定的有根树。
#
#
#
# 提示：
#
#
# 1 <= pairs.length <= 10^5
# 1 <= xi < yi <= 500
# pairs 中的元素互不相同。
#
#
#
from collections import defaultdict
from sys import maxsize
from typing import List


# @lc code=start
class Solution:

    def checkWays(self, pairs: List[List[int]]) -> int:
        adj = defaultdict(set)
        for x, y in pairs:
            adj[x].add(y)
            adj[y].add(x)

        # 检测是否存在根节点
        root = next((node for node, neighbours in adj.items()
                     if len(neighbours) == len(adj) - 1), -1)
        if root == -1:
            return 0

        ans = 1
        for node, neighbours in adj.items():
            if node == root:
                continue

            current_degree = len(neighbours)
            parent, parent_degree = -1, maxsize

            # 根据 degree 的大小找到 node 的父节点 parent
            for neighbour in neighbours:
                if current_degree <= len(adj[neighbour]) < parent_degree:
                    parent = neighbour
                    parent_degree = len(adj[neighbour])

            # 检测 neighbours 是否为 adj[parent] 的子集
            if (parent == -1
                    or any(neighbour != parent and neighbour not in adj[parent]
                           for neighbour in neighbours)):
                return 0

            if parent_degree == current_degree:
                ans = 2

        return ans


# @lc code=end
