#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   437.路径总和-iii.py
@Time    :   2020/09/26 10:46:47
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#
# https://leetcode-cn.com/problems/path-sum-iii/description/
#
# algorithms
# Medium (55.97%)
# Likes:    584
# Dislikes: 0
# Total Accepted:    53K
# Total Submissions: 94.6K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# 给定一个二叉树，它的每个结点都存放着一个整数值。
#
# 找出路径和等于给定数值的路径总数。
#
# 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
#
# 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
#
# 示例：
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
# ⁠     10
# ⁠    /  \
# ⁠   5   -3
# ⁠  / \    \
# ⁠ 3   2   11
# ⁠/ \   \
# 3  -2   1
#
# 返回 3。和等于 8 的路径有:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3.  -3 -> 11
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
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        ans, ps = 0, {0: 1}

        def dfs(root: TreeNode, tot: int) -> None:
            nonlocal ans
            if not root:
                return

            tot += root.val
            need = tot - target
            ans += ps.get(need, 0)

            ps[tot] = ps.get(tot, 0) + 1
            dfs(root.left, tot)
            dfs(root.right, tot)
            ps[tot] -= 1

        dfs(root, 0)
        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    tree = TreeNode(0)
    tree.left, tree.right = TreeNode(1), TreeNode(1)
    print(solu.pathSum(tree, 1))
