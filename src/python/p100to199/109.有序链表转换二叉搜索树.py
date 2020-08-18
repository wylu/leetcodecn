#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   109.有序链表转换二叉搜索树.py
@Time    :   2020/08/18 08:54:37
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#
# https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (74.01%)
# Likes:    290
# Dislikes: 0
# Total Accepted:    39.3K
# Total Submissions: 53.2K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
# 示例:
#
# 给定的有序链表： [-10, -3, 0, 5, 9],
#
# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
#
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
#
#
#
"""
分治 + 中序遍历优化

由于构造出的二叉搜索树的中序遍历结果就是链表本身，因此我们可以将分治和
中序遍历结合起来，减少时间复杂度。
具体地，设当前链表的左端点编号为 left，右端点编号为 right，包含关系为
「双闭」，即 left 和 right 均包含在链表中。链表节点的编号为 [0,n)。
中序遍历的顺序是「左子树 - 根节点 - 右子树」，那么在分治的过程中，我们
不用急着找出链表的中位数节点，而是使用一个占位节点，等到中序遍历到该节
点时，再填充它的值。

我们可以通过计算编号范围来进行中序遍历：
中位数节点对应的编号为 mid = (left+right+1) / 2；
编号为 (left+right) / 2 的节点同样也可以是中位数节点。

左右子树对应的编号范围分别为 [left,mid−1] 和 [mid+1,right]。
如果 left > right，那么遍历到的位置对应着一个空节点，否则对应着二叉
搜索树中的一个节点。

这样一来，我们其实已经知道了这棵二叉搜索树的结构，并且题目给定了它的
中序遍历结果，那么我们只要对其进行中序遍历，就可以还原出整棵二叉搜索树了。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getLength(head: ListNode) -> int:
            res = 0
            while head:
                res += 1
                head = head.next
            return res

        def dfs(left: int, right: int) -> TreeNode:
            if left > right:
                return

            mid = (left + right + 1) // 2
            root = TreeNode()
            root.left = dfs(left, mid - 1)

            nonlocal head
            root.val = head.val
            head = head.next

            root.right = dfs(mid + 1, right)
            return root

        length = getLength(head)
        return dfs(0, length - 1)


# @lc code=end

# class Solution:
#     def sortedListToBST(self, head: ListNode) -> TreeNode:
#         def dfs(left: int, right: int) -> TreeNode:
#             if left > right:
#                 return
#             mid = (left + right + 1) // 2
#             root = TreeNode(nodes[mid])
#             root.left = dfs(left, mid - 1)
#             root.right = dfs(mid + 1, right)
#             return root

#         nodes = []
#         while head:
#             nodes.append(head.val)
#             head = head.next

#         return dfs(0, len(nodes) - 1)
