#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   26.树的子结构.py
@Time    :   2020/08/29 23:25:19
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
要查找树A中是否存在和树B结构一样的子树，我们可以分成两步：
第一步，在树A中找到和树B的根结点的值一样的结点R;
第二步，判断树A中以R为根结点的子树是不是包含和树B一样的结构；
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, a: TreeNode, b: TreeNode) -> bool:
        def ok(r1: TreeNode, r2: TreeNode) -> bool:
            if not r2:
                return True
            if not r1 or r1.val != r2.val:
                return False
            return ok(r1.left, r2.left) and ok(r1.right, r2.right)

        def dfs(r1: TreeNode, r2: TreeNode) -> bool:
            if not r1 or not r2:
                return False
            if (r1.val == r2.val and ok(r1.left, r2.left)
                    and ok(r1.right, r2.right)):
                return True
            return dfs(r1.left, r2) or dfs(r1.right, r2)

        return dfs(a, b)


if __name__ == '__main__':
    solu = Solution()
    ta = TreeNode(1)
    ta.left, ta.right = TreeNode(0), TreeNode(1)
    ta.left.left, ta.left.right = TreeNode(-4), TreeNode(-3)
    tb = TreeNode(1)
    tb.left = TreeNode(-4)
    print(solu.isSubStructure(ta, tb))
