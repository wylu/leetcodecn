#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   treenode.py
@Time    :   2020/08/03 21:44:50
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


def buildFromPreAndIn(pre: List[int], ino: List[int]) -> TreeNode:
    """利用前序遍历序列和中序遍历序列构建一颗二叉树

    Args:
        pre (List[int]): 前序遍历序列
        ino (List[int]): 中序遍历序列

    Returns:
        TreeNode: 树的根结点
    """
    if not pre or not ino or len(pre) != len(ino):
        return

    return _buildFromPreAndIn(pre, 0, len(pre) - 1, ino, 0, len(ino) - 1)


def _buildFromPreAndIn(pre: List[int], sp: int, ep: int, ino: List[int],
                       si: int, ei: int) -> TreeNode:
    if sp > ep:
        return

    root = TreeNode(pre[sp])
    # 中序遍历序列根结点索引
    idx = si
    while idx <= ei and ino[idx] != root.val:
        idx += 1

    # 左子树序列长度
    llen = idx - si
    # 左右子树序列中点（右子树序列起始点）
    mpre = sp + 1 + llen
    root.left = _buildFromPreAndIn(pre, sp + 1, mpre - 1, ino, si, idx - 1)
    root.right = _buildFromPreAndIn(pre, mpre, ep, ino, idx + 1, ei)

    return root


def mkTreeFromInAndPost(ino: List[int], post: List[int]) -> TreeNode:
    """利用中序遍历序列和后序遍历序列构建一颗二叉树

    前提：所有结点的值唯一

    Args:
        ino (List[int]): 中序遍历序列
        post (List[int]): 后序遍历序列

    Returns:
        TreeNode: 树的根结点
    """
    if not ino or not post or len(ino) != len(post):
        return

    map = {ino[i]: i for i in range(len(ino))}

    return _mkTreeFromInAndPost(0, post, 0, len(post) - 1, map)


def _mkTreeFromInAndPost(si: int, post: List[int], sp: int, ep: int,
                         map: Dict) -> TreeNode:
    if sp > ep:
        return

    root = TreeNode(post[ep])
    idx = map[root.val]
    llen = idx - si

    root.left = _mkTreeFromInAndPost(si, post, sp, sp + llen - 1, map)
    root.right = _mkTreeFromInAndPost(idx + 1, post, sp + llen, ep - 1, map)

    return root


def buildFromInAndPost(ino: List[int], post: List[int]) -> TreeNode:
    """利用中序遍历序列和后序遍历序列构建一颗二叉树

    Args:
        ino (List[int]): 中序遍历序列
        post (List[int]): 后序遍历序列

    Returns:
        TreeNode: 树的根结点
    """
    if not ino or not post or len(ino) != len(post):
        return

    return _buildFromInAndPost(ino, 0, len(ino) - 1, post, 0, len(post) - 1)


def _buildFromInAndPost(ino: List[int], si, ei, post: List[int], sp,
                        ep) -> TreeNode:
    if sp > ep:
        return

    root = TreeNode(post[ep])
    # 中序遍历序列根结点索引
    idx = si
    while idx <= ei and ino[idx] != root.val:
        idx += 1

    # 左子树序列长度
    llen = idx - si
    # 左右子树序列中点（右子树序列起始点）
    mpost = sp + llen

    root.left = _buildFromInAndPost(ino, si, idx - 1, post, sp, mpost - 1)
    root.right = _buildFromInAndPost(ino, idx + 1, ei, post, mpost, ep - 1)

    return root
