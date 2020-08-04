#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   preorder.py
@Time    :   2020/08/04 12:35:43
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import os
import sys
import unittest

from typing import List

cur_dir = os.path.dirname(os.path.abspath(__file__))
py_dir = os.path.abspath(os.path.join(cur_dir, *(['..'] * 3)))
sys.path.append(py_dir)

from common.treenode import mkTreeFromPreAndIn  # noqa: E402
from common.treenode import TreeNode  # noqa: E402


class PreorderTraversal(object):
    @classmethod
    def recursiveTraversal(cls, root: TreeNode) -> List[int]:
        ans = []
        cls.recursive(root, ans)
        return ans

    @classmethod
    def recursive(cls, root: TreeNode, ans: List[int]) -> None:
        if not root:
            return

        # 访问当前树的根结点
        ans.append(root.val)
        # 遍历左子树
        cls.recursive(root.left, ans)
        # 遍历右子树
        cls.recursive(root.right, ans)

    @classmethod
    def iterateTraversal(cls, root: TreeNode) -> List[int]:
        return cls.iterate(root)

    @classmethod
    def iterate(cls, root: TreeNode) -> List[int]:
        """迭代地进行前序遍历

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
        if not root:
            return

        ans = []
        stack = [root]
        while stack:
            root = stack.pop()
            ans.append(root.val)

            if root.right:
                stack.append(root.right)

            if root.left:
                stack.append(root.left)

        return ans


class TestPreorder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pre = [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 16, 15]
        cls.ino = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        cls.root = mkTreeFromPreAndIn(cls.pre, cls.ino)

    def test_recursive_traversal(self):
        ans = PreorderTraversal.recursiveTraversal(self.root)
        self.assertListEqual(ans, self.pre)

    def test_iterate_traversal(self):
        ans = PreorderTraversal.iterateTraversal(self.root)
        self.assertListEqual(ans, self.pre)


if __name__ == '__main__':
    unittest.main()
