#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   二叉树的中序遍历.py
@Time    :   2020/08/14 21:42:21
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
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

        # 遍历左子树
        cls.recursive(root.left, res)
        # 访问当前树的根结点
        res.append(root.val)
        # 遍历右子树
        cls.recursive(root.right, res)

    def iterateTraversal(self, root: TreeNode) -> List[int]:
        return self.iterate(root)

    @classmethod
    def iterate(cls, root: TreeNode) -> List[int]:
        """迭代地进行中序遍历

        创建一个辅助栈：
        1.当前结点置为根结点
        2.如果当前结点不为空，则将最左路径的所有结点压入栈中
        3.弹出栈顶结点作为当前结点，将结点值追加到结果序列的尾部
        4.然后将当前结点置为当前结点的右子结点
        5.重复步骤2、3、4，直至当前结点为空且栈空

        Args:
            root (TreeNode): 树的根结点

        Returns:
            List[int]: 中序遍历结果
        """
        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            res.append(root.val)
            root = root.right

        return res
