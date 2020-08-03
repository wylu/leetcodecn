#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   treeprinter.py
@Time    :   2020/08/03 22:32:25
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List

from treenode import buildFromInAndPost
from treenode import buildFromPreAndIn
from treenode import mkTreeFromInAndPost
from treenode import mkTreeFromPreAndIn
from treenode import TreeNode


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


if __name__ == '__main__':
    # Case 1
    #
    # 1
    # ├── 3
    # │   ├── 6
    # │   │   └── 8
    # │   └── 5
    # └── 2
    #     └── 4
    #         ├── 7
    #
    #          /----- 6
    #          |       \----- 8
    #  /----- 3
    #  |       \----- 5
    # 1
    #  \----- 2
    #          |       /----- 7
    #          \----- 4
    print('Case 1: -------------------------------------------')
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    ino = [4, 7, 2, 1, 5, 3, 8, 6]
    root = mkTreeFromPreAndIn(pre, ino)
    TreePrinter.prtLinuxStyle(root)
    TreePrinter.prtHorizontalStyle(root)

    # Case 2
    print('Case 2: -------------------------------------------')
    root = buildFromPreAndIn(pre, ino)
    TreePrinter.prtLinuxStyle(root)
    TreePrinter.prtHorizontalStyle(root)

    # Case 3
    print('Case 3: -------------------------------------------')
    pre = [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 20, 15]
    ino = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20]
    root = mkTreeFromPreAndIn(pre, ino)
    TreePrinter.prtLinuxStyle(root)
    TreePrinter.prtHorizontalStyle(root)

    # Case 4
    print('Case 4: -------------------------------------------')
    root = buildFromPreAndIn(pre, ino)
    TreePrinter.prtLinuxStyle(root)
    TreePrinter.prtHorizontalStyle(root)

    # Case 5
    print('Case 5: -------------------------------------------')
    post = [1, 3, 2, 5, 7, 6, 4, 9, 11, 10, 13, 15, 20, 14, 12, 8]
    root = mkTreeFromInAndPost(ino, post)
    TreePrinter.prtLinuxStyle(root)
    TreePrinter.prtHorizontalStyle(root)

    # Case 6
    print('Case 6: -------------------------------------------')
    root = buildFromInAndPost(ino, post)
    TreePrinter.prtLinuxStyle(root)
    TreePrinter.prtHorizontalStyle(root)
