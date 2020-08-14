#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   102.二叉树的层序遍历.py
@Time    :   2020/08/14 23:35:20
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (63.18%)
# Likes:    596
# Dislikes: 0
# Total Accepted:    177.6K
# Total Submissions: 281.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
#
#
#
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
# 返回其层次遍历结果：
#
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
#
#
#

# @lc code=start
from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ans = []
        que = deque()
        que.append(root)

        while que:
            level, size = [], len(que)

            for _ in range(size):
                root = que.popleft()
                level.append(root.val)

                if root.left:
                    que.append(root.left)
                if root.right:
                    que.append(root.right)

            ans.append(level)

        return ans


# @lc code=end
