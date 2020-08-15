#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   297.二叉树的序列化与反序列化.py
@Time    :   2020/08/15 22:56:25
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#
# https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (51.66%)
# Likes:    334
# Dislikes: 0
# Total Accepted:    45.9K
# Total Submissions: 88.8K
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
#
# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
#
# 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 /
# 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
#
# 示例:
#
# 你可以将以下二叉树：
#
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠    / \
# ⁠   4   5
#
# 序列化为 "[1,2,3,null,null,4,5]"
#
# 提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode
# 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
#
# 说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。
#
#
from typing import List


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @lc code=start
class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.

        Args:
            root (TreeNode): the root of tree

        Returns:
            str: a serial str of binary tree
        """
        res = []
        self._serial(root, res)
        return ','.join(res)

    def _serial(self, root: TreeNode, res: List[str]) -> None:
        if not root:
            res.append('#')
            return

        res.append(str(root.val))
        self._serial(root.left, res)
        self._serial(root.right, res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.

        Args:
            data (str): a serial str of binary tree

        Returns:
            TreeNode: the root of tree
        """
        data = data.split(',')
        data.reverse()
        return self._deserial(data)

    def _deserial(self, data: List[str]) -> TreeNode:
        val = data.pop()
        if val == '#':
            return

        root = TreeNode(int(val))
        root.left = self._deserial(data)
        root.right = self._deserial(data)

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end
