#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   二叉树的前序遍历.py
@Time    :   2020/08/14 12:44:20
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # return self.recursiveTraversal(root)
        return self.iterateTraversal(root)

    def recursiveTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.recursive(root, res)
        return res

    @classmethod
    def recursive(cls, root: TreeNode, res: List[int]) -> None:
        if not root:
            return

        res.append(root.val)
        cls.recursive(root.left, res)
        cls.recursive(root.right, res)

    def iterateTraversal(self, root: TreeNode) -> List[int]:
        return self.iterate(root)

    @classmethod
    def iterate(cls, root: TreeNode) -> List[int]:
        """迭代地前序遍历

        创建一个辅助栈：
        1.将根结点压入栈
        2.弹出栈顶结点，将结点值追加到结果序列的尾部
        3.然后先将右子结点压入栈中（如果有）
        4.再将左子结点压入栈中（如果有）
        5.重复步骤2、3、4，直至栈空

        Args:
            root (TreeNode): 树的根结点

        Returns:
            List[int]: 前序遍历结果
        """
        res = []
        if not root:
            return res

        stack = [root]
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

        return res
