#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   687.最长同值路径.py
@Time    :   2020/09/26 12:05:57
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=687 lang=python3
#
# [687] 最长同值路径
#
# https://leetcode-cn.com/problems/longest-univalue-path/description/
#
# algorithms
# Easy (41.81%)
# Likes:    358
# Dislikes: 0
# Total Accepted:    23.9K
# Total Submissions: 57.2K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# 给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
#
# 注意：两个节点之间的路径长度由它们之间的边数表示。
#
# 示例 1:
#
# 输入:
#
#
# ⁠             5
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         1   1   5
#
#
# 输出:
#
#
# 2
#
#
# 示例 2:
#
# 输入:
#
#
# ⁠             1
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         4   4   5
#
#
# 输出:
#
#
# 2
#
#
# 注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。
#
#
"""
方法：递归

思路

我们可以将任何路径（具有相同值的节点）看作是最多两个从其根延伸出的箭头。

具体地说，路径的根将是唯一节点，因此该节点的父节点不会出现在该路径中，
而箭头将是根在该路径中只有一个子节点的路径。

然后，对于每个节点，我们想知道向左延伸的最长箭头和向右延伸的最长箭头
是什么？我们可以用递归来解决这个问题。

算法

令 dfs(node) 为从节点 node 延伸出的最长箭头的长度。如果 node.Left
存在且与节点 node 具有相同的值，则该值就会是 1 + dfs(node.left)。
在 node.right 存在的情况下也是一样。

当我们计算箭头长度时，候选答案将是该节点在两个方向上的箭头之和。我们
将这些候选答案记录下来，并返回最佳答案。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @lc code=start
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        ans = 0

        def dfs(root: TreeNode) -> int:
            nonlocal ans
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            path_left, path_right = 0, 0
            if root.left and root.left.val == root.val:
                path_left = left + 1
            if root.right and root.right.val == root.val:
                path_right = right + 1

            ans = max(ans, path_left + path_right)
            return max(path_left, path_right)

        dfs(root)
        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    tree = TreeNode(5)
    tree.left, tree.right = TreeNode(4), TreeNode(5)
    tree.left.left, tree.left.right = TreeNode(1), TreeNode(1)
    tree.right.right = TreeNode(5)
    print(solu.longestUnivaluePath(tree))

    tree = TreeNode(1)
    tree.right = TreeNode(1)
    tree.right.left, tree.right.right = TreeNode(1), TreeNode(1)
    trl = tree.right.left
    trl.left, trl.right = TreeNode(1), TreeNode(1)
    tree.right.right.left = TreeNode(1)
    print(solu.longestUnivaluePath(tree))
