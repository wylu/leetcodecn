#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   173.二叉搜索树迭代器.py
@Time    :   2020/12/07 22:48:54
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
#
# https://leetcode-cn.com/problems/binary-search-tree-iterator/description/
#
# algorithms
# Medium (75.11%)
# Likes:    291
# Dislikes: 0
# Total Accepted:    33.8K
# Total Submissions: 45K
# Testcase Example:
# '["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]\n'
# + '[[[7,3,15,null,null,9,20]],[],[],[],[],[],[],[],[],[]]'
#
# 实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。
#
# 调用 next() 将返回二叉搜索树中的下一个最小的数。
#
#
#
# 示例：
#
#
#
# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // 返回 3
# iterator.next();    // 返回 7
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 9
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 15
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 20
# iterator.hasNext(); // 返回 false
#
#
#
# 提示：
#
#
# next() 和 hasNext() 操作的时间复杂度是 O(1)，并使用 O(h) 内存，其中 h 是树的高度。
# 你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 中至少存在一个下一个最小的数。
#
#
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self._to_leftmost(root)

    def next(self) -> int:
        root = self.stack.pop()
        if root.right:
            self._to_leftmost(root.right)
        return root.val

    def hasNext(self) -> bool:
        return bool(self.stack)

    def _to_leftmost(self, root: TreeNode) -> None:
        while root:
            self.stack.append(root)
            root = root.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
