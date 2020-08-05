#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   337.打家劫舍-iii.py
@Time    :   2020/08/05 12:56:30
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#
# https://leetcode-cn.com/problems/house-robber-iii/description/
#
# algorithms
# Medium (58.90%)
# Likes:    487
# Dislikes: 0
# Total Accepted:    49.1K
# Total Submissions: 83.3K
# Testcase Example:  '[3,2,3,null,3,null,1]'
#
# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。
# 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
# 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
#
# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
#
# 示例 1:
#
# 输入: [3,2,3,null,3,null,1]
#
# ⁠    3
# ⁠   / \
# ⁠  2   3
# ⁠   \   \
# ⁠    3   1
#
# 输出: 7
# 解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
#
# 示例 2:
#
# 输入: [3,4,5,1,3,null,1]
#
# 3
# ⁠   / \
# ⁠  4   5
# ⁠ / \   \
# ⁠1   3   1
#
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
#
#
#
from typing import List
"""
动态规划 DFS

终止条件：什么时候无需任何计算就能知道rob(root)的答案？
当然，当树是空的时，我们没有什么可抢的，所以钱是零。

递归关系：即如何从rob(root.left)，rob(root.right)，...等获取rob(root)。
从树根的角度来看，最后只有两种情况：root是否被抢。
a)如果root被抢，由于“我们不能抢劫任何两个直接链接的房屋”的限制，下一级
  可用的子树将是四个“孙子树”(root.left.left, root.left.right,
   root.right.left, root.right.right)
b)如果未抢走root，则下一级可用子树将只是两个“子树”(root.left, root.right)
  我们只需要选择产生大量资金的方案即可。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @lc code=start
class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self._rob(root))

    def _rob(self, root: TreeNode) -> List[int]:
        if not root:
            return (0, 0)

        left = self._rob(root.left)
        right = self._rob(root.right)

        return (
            # 未抢走当前节点
            max(left) + max(right),
            # 抢走当前节点
            root.val + left[0] + right[0])


# @lc code=end
