#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   861.翻转矩阵后的得分.py
@Time    :   2020/12/07 22:22:21
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=861 lang=python3
#
# [861] 翻转矩阵后的得分
#
# https://leetcode-cn.com/problems/score-after-flipping-matrix/description/
#
# algorithms
# Medium (81.10%)
# Likes:    166
# Dislikes: 0
# Total Accepted:    24.3K
# Total Submissions: 30K
# Testcase Example:  '[[0,0,1,1],[1,0,1,0],[1,1,0,0]]'
#
# 有一个二维矩阵 A 其中每个元素的值为 0 或 1 。
#
# 移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。
#
# 在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。
#
# 返回尽可能高的分数。
#
#
#
#
#
#
# 示例：
#
# 输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# 输出：39
# 解释：
# 转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
#
#
#
# 提示：
#
#
# 1 <= A.length <= 20
# 1 <= A[0].length <= 20
# A[i][j] 是 0 或 1
#
#
#
from typing import List
"""
方法一：贪心
根据题意，能够知道一个重要的事实：给定一个翻转方案，则它们之间任意交换
顺序后，得到的结果保持不变。因此，我们总可以先考虑所有的行翻转，再考虑
所有的列翻转。

不难发现一点：为了得到最高的分数，矩阵的每一行的最左边的数都必须为 1。
为了做到这一点，我们可以翻转那些最左边的数不为 1 的那些行，而其他的行
则保持不动。

当将每一行的最左边的数都变为 1 之后，就只能进行列翻转了。为了使得总
得分最大，我们要让每个列中 1 的数目尽可能多。因此，我们扫描除了最左边
的列以外的每一列，如果该列 0 的数目多于 1 的数目，就翻转该列，其他
的列则保持不变。

实际编写代码时，我们无需修改原矩阵，而是可以计算每一列对总分数的
「贡献」，从而直接计算出最高的分数。假设矩阵共有 m 行 n 列，计算方法
如下：

对于最左边的列而言，由于最优情况下，它们的取值都为 1，因此每个元素
对分数的贡献都为 2^(n-1)，总贡献为 m * 2^(n-1)。

对于第 j 列（j>0，此处规定最左边的列是第 0 列）而言，我们统计这一列
0,1 的数量，令其中的最大值为 k，则 k 是列翻转后的 1 的数量，该列的
总贡献为 k * 2^(n-j-1)。需要注意的是，在统计 0,1 的数量的时候，
要考虑最初进行的行反转。
"""


# @lc code=start
class Solution:
    def matrixScore(self, a: List[List[int]]) -> int:
        m, n = len(a), len(a[0])
        ans = m * (1 << n - 1)

        for j in range(1, n):
            k = 0
            for i in range(m):
                if a[i][0] == 1:
                    k += a[i][j]
                else:
                    k += 1 - a[i][j]
            k = max(k, m - k)
            ans += k * pow(2, n - j - 1)

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))
