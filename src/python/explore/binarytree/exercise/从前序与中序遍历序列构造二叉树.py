#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   从前序与中序遍历序列构造二叉树.py
@Time    :   2020/08/15 18:37:13
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import os
import sys

from typing import List

cur_dir = os.path.dirname(os.path.abspath(__file__))
py_dir = os.path.abspath(os.path.join(cur_dir, *(['..'] * 3)))
sys.path.append(py_dir)
common_dir = os.path.abspath(os.path.join(py_dir, 'common'))
sys.path.append(common_dir)

from common.treenode import TreeNode  # noqa: E402
from common.treeprinter import TreePrinter  # noqa: E402


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder or len(preorder) != len(inorder):
            return

        indices = {v: i for i, v in enumerate(inorder)}
        return self.build(preorder, 0, len(preorder) - 1, 0, indices)

    def build(self, pre: List[int], sp: int, ep: int, si: int,
              indices: dict) -> TreeNode:
        if sp > ep:
            return

        root = TreeNode(pre[sp])
        idx = indices[root.val]
        llen = idx - si

        root.left = self.build(pre, sp + 1, sp + llen, si, indices)
        root.right = self.build(pre, sp + llen + 1, ep, idx + 1, indices)

        return root


if __name__ == '__main__':
    solu = Solution()
    tree = solu.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    TreePrinter.prtHorizontalStyle(tree)
