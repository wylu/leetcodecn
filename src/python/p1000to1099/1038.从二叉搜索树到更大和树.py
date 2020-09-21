#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1038.从二叉搜索树到更大和树.py
@Time    :   2020/09/21 10:05:50
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


#
# @lc app=leetcode.cn id=1038 lang=python3
#
# [1038] 从二叉搜索树到更大和树
#
# https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/description/
#
# algorithms
# Medium (76.97%)
# Likes:    77
# Dislikes: 0
# Total Accepted:    12.4K
# Total Submissions: 16.1K
# Testcase Example:  '[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]'
#
# 给出二叉 搜索 树的根节点，该二叉树的节点值各不相同，修改二叉树，使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
#
# 提醒一下，二叉搜索树满足下列约束条件：
#
#
# 节点的左子树仅包含键 小于 节点键的节点。
# 节点的右子树仅包含键 大于 节点键的节点。
# 左右子树也必须是二叉搜索树。
#
#
#
#
# 示例：
#
#
#
# 输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# 输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
#
#
#
#
# 提示：
#
#
# 树中的节点数介于 1 和 100 之间。
# 每个节点的值介于 0 和 100 之间。
# 给定的树为二叉搜索树。
#
#
#
#
# 注意：该题目与 538: https://leetcode-cn.com/problems/convert-bst-to-greater-tree/
# 相同
#
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @lc code=start
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        tot = 0

        def dfs(root: TreeNode) -> None:
            nonlocal tot
            if not root:
                return
            dfs(root.right)
            root.val += tot
            tot = root.val
            dfs(root.left)

        dfs(root)
        return root


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    tree = TreeNode(2)
    tree.left, tree.right = TreeNode(0), TreeNode(3)
    tree.left.left, tree.left.right = TreeNode(-4), TreeNode(1)
    solu.convertBST(tree)
