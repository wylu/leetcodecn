#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   treepath.py
@Time    :   2022/04/21 21:38:50
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import Dict
from typing import List


class TreeNode(object):

    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class TreePrinter(object):

    @classmethod
    def prtLinuxStyle(cls, root: TreeNode) -> None:
        """print tree in linux style

        z
        ├── c
        │ ├── a
        │ └── b
        └── d

        Args:
            root (TreeNode): 树的根结点
        """
        print(cls.getLinuxStyle(root))

    @classmethod
    def getLinuxStyle(cls, root: TreeNode) -> str:
        sb = []
        cls.linuxStyle(root, sb, '', '')
        return ''.join(sb)

    @classmethod
    def linuxStyle(cls, root: TreeNode, sb: List[str], prefix: str,
                   childPrefix: str) -> None:
        if not root:
            return

        sb.append(prefix)
        sb.append(str(root.val))
        sb.append('\n')

        cls.linuxStyle(root.right, sb, childPrefix + '├── ',
                       childPrefix + '│   ')
        cls.linuxStyle(root.left, sb, childPrefix + '└── ',
                       childPrefix + '    ')

    @classmethod
    def prtHorizontalStyle(cls, root: TreeNode) -> None:
        """print tree in horizontal style

        Args:
            root (TreeNode): 树的根结点
        """
        #                 /----- 20
        #                 |       \----- 15
        #         /----- 14
        #         |       \----- 13
        # /----- 12
        # |       |       /----- 11
        # |       \----- 10
        # |               \----- 9
        # 8
        # |              /----- 7
        # |      /----- 6
        # |      |       \----- 5
        # \----- 4
        #        |       /----- 3
        #        \----- 2
        #                \----- 1
        print(cls.horizontalStyle(root))

    @classmethod
    def horizontalStyle(cls, root: TreeNode) -> str:
        sb = []

        if root.right:
            cls.horizontal(root.right, sb, True, '')

        sb.append(str(root.val))
        sb.append('\n')

        if root.left:
            cls.horizontal(root.left, sb, False, '')

        return ''.join(sb)

    @classmethod
    def horizontal(cls, root: TreeNode, sb: List[str], isRight: bool,
                   indent: str) -> None:
        if root.right:
            cls.horizontal(root.right, sb, True,
                           indent + ('        ' if isRight else ' |      '))

        sb.append(indent)
        sb.append(' /' if isRight else ' \\')
        sb.append('----- ')
        sb.append(str(root.val))
        sb.append('\n')

        if root.left:
            cls.horizontal(root.left, sb, False,
                           indent + (' |      ' if isRight else '        '))


def mkTreeFromPreAndIn(pre: List[int], ino: List[int]) -> TreeNode:
    """利用前序遍历序列和中序遍历序列构建一颗二叉树

    前提：所有结点的值唯一

    Args:
        pre (List[int]): 前序遍历序列
        ino (List[int]): 中序遍历序列

    Returns:
        TreeNode: 树的根结点
    """
    if not pre or not ino or len(pre) != len(ino):
        return

    map = {ino[i]: i for i in range(len(ino))}

    return _mkTreeFromPreAndIn(0, pre, 0, len(pre) - 1, map)


def _mkTreeFromPreAndIn(si: int, pre: List[int], sp: int, ep: int,
                        map: Dict) -> TreeNode:
    if sp > ep:
        return

    root = TreeNode(pre[sp])
    idx = map[root.val]
    llen = idx - si

    root.left = _mkTreeFromPreAndIn(si, pre, sp + 1, sp + llen, map)
    root.right = _mkTreeFromPreAndIn(idx + 1, pre, sp + llen + 1, ep, map)

    return root


class Solution:

    def preorder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ans = []
        stk = [(root, 0)]
        values = []
        while stk:
            node, depth = stk.pop()

            while len(values) > depth:
                values.pop()

            values.append(node.val)
            if not (node.left or node.right):
                ans.append(values[:])
                continue

            if node.right:
                stk.append((node.right, depth + 1))
            if node.left:
                stk.append((node.left, depth + 1))

        return ans


if __name__ == '__main__':
    # Test Case 1
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    ino = [4, 7, 2, 1, 5, 3, 8, 6]
    root = mkTreeFromPreAndIn(pre, ino)
    TreePrinter.prtHorizontalStyle(root)

    solu = Solution()
    paths = solu.preorder(root)
    for path in paths:
        print(path)

    # Test Case 2
    pre = [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 20, 15]
    ino = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20]
    root = mkTreeFromPreAndIn(pre, ino)
    TreePrinter.prtHorizontalStyle(root)

    solu = Solution()
    paths = solu.preorder(root)
    for path in paths:
        print(path)
