#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   637.二叉树的层平均值.py
@Time    :   2020/09/12 09:31:57
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#
# https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/description/
#
# algorithms
# Easy (66.61%)
# Likes:    165
# Dislikes: 0
# Total Accepted:    28.7K
# Total Submissions: 43.2K
# Testcase Example:  '[3,9,20,15,7]'
#
# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。
#
#
#
# 示例 1：
#
# 输入：
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 输出：[3, 14.5, 11]
# 解释：
# 第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
#
#
#
#
# 提示：
#
#
# 节点值的范围在32位有符号整数范围内。
#
#
#
from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @lc code=start
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []

        q = deque()
        q.append(root)
        ans = []
        level, cnt = 0, 0
        cur_last, next_last = root, None

        while q:
            root = q.popleft()
            level += root.val
            cnt += 1

            if root.left:
                q.append(root.left)
                next_last = root.left
            if root.right:
                q.append(root.right)
                next_last = root.right

            if root == cur_last:
                ans.append(level / cnt)
                level, cnt = 0, 0
                cur_last = next_last

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    tree = TreeNode(3)
    tree.left, tree.right = TreeNode(9), TreeNode(20)
    tree.right.left, tree.right.right = TreeNode(15), TreeNode(7)
    print(solu.averageOfLevels(tree))
