#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   33.二叉搜索树的后序遍历序列.py
@Time    :   2020/09/02 23:16:39
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
在后序遍历得到的序列中，最后一个数字是树的根结点的值。数组中前面的数字可以分为两部分：
第一部分是左子树结点的值，它们都比根结点的值小；第二部分是右子树结点的值，它们都比根结
点的值，它们都比根结点的值大。

根据这个规律，我们可以递归地遍历左子树和右子树，以判断所有的子树是否都满足二叉搜索树的
条件。
"""
from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def dfs(s: int, e: int) -> bool:
            if s >= e:
                return True

            root = postorder[e]

            # 在二叉搜索树中左子树结点的值小于根结点的值
            i = s
            while i < e and postorder[i] < root:
                i += 1

            # 在二叉搜索树中右子树结点的值大于根结点的值
            for j in range(i, e):
                if postorder[j] < root:
                    return False

            # 递归判断左子树和右子树是不是二叉搜索树
            return dfs(s, i - 1) and dfs(i, e - 1)

        return dfs(0, len(postorder) - 1)


if __name__ == '__main__':
    solu = Solution()
    print(solu.verifyPostorder([5, 7, 6, 9, 11, 10, 8]))
    print(solu.verifyPostorder([7, 4, 6, 5]))
