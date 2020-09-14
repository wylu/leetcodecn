#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   从中序与后序遍历序列构造二叉树.py
@Time    :   2020/08/15 17:54:05
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder or len(inorder) != len(postorder):
            return

        indices = {v: i for i, v in enumerate(inorder)}
        return self.build(0, postorder, 0, len(postorder) - 1, indices)

    def build(self, si: int, post: List[int], sp: int, ep: int,
              indices: dict) -> TreeNode:
        if sp > ep:
            return

        root = TreeNode(post[ep])
        idx = indices[root.val]
        llen = idx - si

        root.left = self.build(si, post, sp, sp + llen - 1, indices)
        root.right = self.build(idx + 1, post, sp + llen, ep - 1, indices)

        return root


if __name__ == '__main__':
    solu = Solution()
    tree = solu.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    TreePrinter.prtHorizontalStyle(tree)
