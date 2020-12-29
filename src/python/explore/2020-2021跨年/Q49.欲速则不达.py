#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   Q49.欲速则不达.py
@Time    :   2020/12/29 13:52:05
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
https://leetcode-cn.com/leetbook/read/interesting-algorithm-puzzles-for-programmers/9iftw2/

方法一：回溯
https://leetcode-cn.com/circle/discuss/11mBnL/
思路与算法

我们可以从左上角开始进行递归搜索，当我们到达右下角时，就可以根据当前
的移动距离来更新答案。

由于我们不能在同一条直线上移动超过 2 次，因此我们可以考虑在搜索的
过程中，使用数组 rowCount 和 colCount 记录每一行和每一列的移动次数，
其中 rowCount 表示在第 i 行上移动的次数，colCount 表示在第 j 列上
移动的次数。需要注意的是，虽然给定的长方形的长度 m=5，宽度 n=6，
但由于我们是在网格图的边上进行移动的，因此行数和列数实际上分别是
m+1=6 以及 n+1=7。

此时，我们就可以使用函数 dfs(i,j,step) 来帮助我们进行搜索，其中
i 和 j 表示我们当前所在的行列，step 表示当前移动的距离。我们可以
向四个方向进行移动，只需要保证不移动出网格，并且没有在同一条直线上
移动超过 2 次即可。题目中规定了「可以在同一条路径上往返」，因此
我们无需考虑重复经过同一条边的情况。

当我们移动到右下角 (i,j)=(m,n) 时，我们就可以根据 step 来对最长
移动距离进行更新。
"""


class Solution:
    def maximumDistance(self, m: int, n: int) -> int:
        ans, rowCnts, colCnts = 0, [0] * (m + 1), [0] * (n + 1)

        def dfs(i: int, j: int, s: int) -> None:
            nonlocal ans
            if i == m and n == j:
                ans = max(ans, s)

            # UP
            if i > 0 and colCnts[j] < 2:
                colCnts[j] += 1
                dfs(i - 1, j, s + 1)
                colCnts[j] -= 1

            # DOWN
            if i < m and colCnts[j] < 2:
                colCnts[j] += 1
                dfs(i + 1, j, s + 1)
                colCnts[j] -= 1

            # LEFT
            if j > 0 and rowCnts[i] < 2:
                rowCnts[i] += 1
                dfs(i, j - 1, s + 1)
                rowCnts[i] -= 1

            # RIGHT
            if j < n and rowCnts[i] < 2:
                rowCnts[i] += 1
                dfs(i, j + 1, s + 1)
                rowCnts[i] -= 1

        dfs(0, 0, 0)
        return ans


if __name__ == "__main__":
    solu = Solution()
    print(solu.maximumDistance(5, 6))
