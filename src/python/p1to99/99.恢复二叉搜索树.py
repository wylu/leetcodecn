#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   99.恢复二叉搜索树.py
@Time    :   2020/08/08 21:25:14
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#
# https://leetcode-cn.com/problems/recover-binary-search-tree/description/
#
# algorithms
# Hard (57.96%)
# Likes:    304
# Dislikes: 0
# Total Accepted:    32.6K
# Total Submissions: 53.4K
# Testcase Example:  '[1,3,null,null,2]'
#
# 二叉搜索树中的两个节点被错误地交换。
#
# 请在不改变其结构的情况下，恢复这棵树。
#
# 示例 1:
#
# 输入: [1,3,null,null,2]
#
#   1
#  /
# 3
#  \
#   2
#
# 输出: [3,1,null,null,2]
#
#   3
#  /
# 1
#  \
#   2
#
#
# 示例 2:
#
# 输入: [3,1,4,null,null,2]
#
# ⁠  3
#  ⁠/ \
# 1   4
#    /
#   2
#
# 输出: [2,1,4,null,null,3]
#
#  ⁠ 2
#  ⁠/ \
# 1   4
#    /
# ⁠  3
#
# 进阶:
#
#
# 使用 O(n) 空间复杂度的解法很容易实现。
# 你能想出一个只使用常数空间的解决方案吗？
#
#
#
"""
思路与算法

我们需要考虑两个节点被错误地交换后对原二叉搜索树造成了什么影响。对于二叉搜索树，
我们知道如果对其进行中序遍历，得到的值序列是递增有序的，而如果我们错误地交换了
两个节点，等价于在这个值序列中交换了两个值，破坏了值序列的递增性。

我们来看下如果在一个递增的序列中交换两个值会造成什么影响。假设有一个递增序列
a = [1,2,3,4,5,6,7]。如果我们交换两个不相邻的数字，例如 2 和 6，原序列变成了
a = [1,6,3,4,5,2,7]，那么显然序列中有两个位置不满足 a[i] < a[i+1]，在这个
序列中体现为 6 > 3，5 > 2，因此只要我们找到这两个位置，即可找到被错误交换的
两个节点。如果我们交换两个相邻的数字，例如 2 和 3，此时交换后的序列只有一个
位置不满足 a[i] < a[i+1]。因此整个值序列中不满足条件的位置或者有两个，或者
有一个。

至此，解题方法已经呼之欲出了：

找到二叉搜索树中序遍历得到值序列的不满足条件的位置。
如果有两个，我们记为 i 和 j (i<j && a[i]>a[i+1] && a[j]>a[j+1])，那么
对应被错误交换的节点即为 a[i] 对应的节点和 a[j+1] 对应的节点，我们分别记为
x 和 y。
如果有一个，我们记为 i，那么对应被错误交换的节点即为 a[i] 对应的节点和 a[i+1]
对应的节点，我们分别记为 x 和 y。

交换 x 和 y 两个节点即可。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        if not root:
            return

        first, second = None, None
        pre = None
        while root:
            if not root.left:
                if pre and root.val < pre.val:
                    second = root
                    if not first:
                        first = pre
                pre = root
                root = root.right
                continue

            precursor = root.left
            while precursor.right and precursor.right != root:
                precursor = precursor.right

            if not precursor.right:
                precursor.right = root
                root = root.left
            else:
                if pre and root.val < pre.val:
                    second = root
                    if not first:
                        first = pre

                precursor.right = None
                pre = root
                root = root.right

        first.val, second.val = second.val, first.val


# @lc code=end
