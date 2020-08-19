#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   52.n皇后-ii.py
@Time    :   2020/08/19 16:33:47
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#
# https://leetcode-cn.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (79.20%)
# Likes:    140
# Dislikes: 0
# Total Accepted:    29.9K
# Total Submissions: 37.8K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
#
#
# 上图为 8 皇后问题的一种解法。
#
# 给定一个整数 n，返回 n 皇后不同的解决方案的数量。
#
# 示例:
#
# 输入: 4
# 输出: 2
# 解释: 4 皇后问题存在如下两个不同的解法。
# [
# [".Q..",  // 解法 1
# "...Q",
# "Q...",
# "..Q."],
#
# ["..Q.",  // 解法 2
# "Q...",
# "...Q",
# ".Q.."]
# ]
#
#
#
#
# 提示：
#
#
# 皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一或
# N-1 步，可进可退。（引用自 百度百科 - 皇后 ）
#
#
#


# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        if n <= 0:
            return 0

        def ok(x: int, y: int) -> bool:
            return not bool(cols[y] + dales[x - y] + hills[x + y])

        def dfs(x: int) -> None:
            nonlocal ans
            if x == n:
                ans += 1
                return

            for y in range(n):
                if ok(x, y):
                    cols[y], dales[x - y], hills[x + y] = 1, 1, 1
                    dfs(x + 1)
                    cols[y], dales[x - y], hills[x + y] = 0, 0, 0

        cols, dales, hills = [0] * n, [0] * (2 * n - 1), [0] * (2 * n - 1)
        ans = 0
        dfs(0)
        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.totalNQueens(4))
    print(solu.totalNQueens(8))
