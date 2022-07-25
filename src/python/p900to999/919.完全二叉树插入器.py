#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   919.完全二叉树插入器.py
@Time    :   2022/07/25 18:54:08
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=919 lang=python3
#
# [919] 完全二叉树插入器
#
# https://leetcode.cn/problems/complete-binary-tree-inserter/description/
#
# algorithms
# Medium (66.94%)
# Likes:    128
# Dislikes: 0
# Total Accepted:    22K
# Total Submissions: 32.9K
# Testcase Example:  '["CBTInserter","insert","get_root"]\n[[[1]],[2],[]]'
#
# 完全二叉树 是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。
#
# 设计一种算法，将一个新节点插入到一个完整的二叉树中，并在插入后保持其完整。
#
# 实现 CBTInserter 类:
#
#
# CBTInserter(TreeNode root) 使用头节点为 root 的给定树初始化该数据结构；
# CBTInserter.insert(int v)  向树中插入一个值为 Node.val == val的新节点
# TreeNode。使树保持完全二叉树的状态，并返回插入节点 TreeNode 的父节点的值；
# CBTInserter.get_root() 将返回树的头节点。
#
#
#
#
#
#
#
# 示例 1：
#
#
#
#
# 输入
# ["CBTInserter", "insert", "insert", "get_root"]
# [[[1, 2]], [3], [4], []]
# 输出
# [null, 1, 2, [1, 2, 3, 4]]
#
# 解释
# CBTInserter cBTInserter = new CBTInserter([1, 2]);
# cBTInserter.insert(3);  // 返回 1
# cBTInserter.insert(4);  // 返回 2
# cBTInserter.get_root(); // 返回 [1, 2, 3, 4]
#
#
#
# 提示：
#
#
# 树中节点数量范围为 [1, 1000]
# 0 <= Node.val <= 5000
# root 是完全二叉树
# 0 <= val <= 5000
# 每个测试用例最多调用 insert 和 get_root 操作 10^4 次
#
#
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class CBTInserter:
    def __init__(self, root: TreeNode):
        self.tree = []

        que = deque([root])
        while que:
            for _ in range(len(que)):
                root = que.popleft()
                self.tree.append(root)
                if root.left:
                    que.append(root.left)
                if root.right:
                    que.append(root.right)

    def insert(self, val: int) -> int:
        d, r = divmod(len(self.tree) - 1, 2)
        node = TreeNode(val)
        if r:
            self.tree[d].right = node
        else:
            self.tree[d].left = node
        self.tree.append(node)
        return self.tree[d].val

    def get_root(self) -> TreeNode:
        return self.tree[0]


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
# @lc code=end
