#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   779.第k个语法符号.py
@Time    :   2022/10/20 22:33:06
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=779 lang=python3
#
# [779] 第K个语法符号
#
# https://leetcode.cn/problems/k-th-symbol-in-grammar/description/
#
# algorithms
# Medium (43.94%)
# Likes:    261
# Dislikes: 0
# Total Accepted:    44.9K
# Total Submissions: 91.4K
# Testcase Example:  '1\n1'
#
# 我们构建了一个包含 n 行( 索引从 1  开始 )的表。首先在第一行我们写上一个
# 0。接下来的每一行，将前一行中的0替换为01，1替换为10。
#
#
# 例如，对于 n = 3 ，第 1 行是 0 ，第 2 行是 01 ，第3行是 0110 。
#
#
# 给定行数 n 和序数 k，返回第 n 行中第 k 个字符。（ k 从索引 1 开始）
#
#
# 示例 1:
#
#
# 输入: n = 1, k = 1
# 输出: 0
# 解释: 第一行：0
#
#
# 示例 2:
#
#
# 输入: n = 2, k = 1
# 输出: 0
# 解释:
# 第一行: 0
# 第二行: 01
#
#
# 示例 3:
#
#
# 输入: n = 2, k = 2
# 输出: 1
# 解释:
# 第一行: 0
# 第二行: 01
#
#
#
#
# 提示:
#
#
# 1 <= n <= 30
# 1 <= k <= 2^n - 1
#
#
#


# @lc code=start
class Solution:

    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        parent = self.kthGrammar(n - 1, (k + 1) // 2)
        children = (1, 0) if parent else (0, 1)
        return children[0] if k % 2 else children[1]


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.kthGrammar(n=1, k=1))
    print(solu.kthGrammar(n=2, k=1))
    print(solu.kthGrammar(n=2, k=2))
    print(solu.kthGrammar(n=4, k=4))
    print(solu.kthGrammar(n=4, k=5))
