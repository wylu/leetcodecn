#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   773.滑动谜题.py
@Time    :   2021/06/26 09:59:56
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=773 lang=python3
#
# [773] 滑动谜题
#
# https://leetcode-cn.com/problems/sliding-puzzle/description/
#
# algorithms
# Hard (66.80%)
# Likes:    152
# Dislikes: 0
# Total Accepted:    10.8K
# Total Submissions: 16.2K
# Testcase Example:  '[[1,2,3],[4,0,5]]'
#
# 在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示.
#
# 一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换.
#
# 最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。
#
# 给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。
#
# 示例：
#
#
# 输入：board = [[1,2,3],[4,0,5]]
# 输出：1
# 解释：交换 0 和 5 ，1 步完成
#
#
#
# 输入：board = [[1,2,3],[5,4,0]]
# 输出：-1
# 解释：没有办法完成谜板
#
#
#
# 输入：board = [[4,1,2],[5,0,3]]
# 输出：5
# 解释：
# 最少完成谜板的最少移动次数是 5 ，
# 一种移动路径:
# 尚未移动: [[4,1,2],[5,0,3]]
# 移动 1 次: [[4,1,2],[0,5,3]]
# 移动 2 次: [[0,1,2],[4,5,3]]
# 移动 3 次: [[1,0,2],[4,5,3]]
# 移动 4 次: [[1,2,0],[4,5,3]]
# 移动 5 次: [[1,2,3],[4,5,0]]
#
#
#
# 输入：board = [[3,2,4],[1,5,0]]
# 输出：14
#
#
# 提示：
#
#
# board 是一个如上所述的 2 x 3 的数组.
# board[i][j] 是一个 [0, 1, 2, 3, 4, 5] 的排列.
#
#
#
from collections import deque
from typing import List
"""
方法一：广度优先搜索
思路与算法

我们可以使用广度优先搜索，找出从初始状态 board 到目标状态
[[1,2,3],[4,5,0]] 的最小交换次数。

具体地，我们在一开始将 (board, 0) 加入队列，并使用该队列进行
广度优先搜索。在搜索的过程中，设当前搜索到的状态为 status，
操作的次数为 step，我们可以枚举 status 通过一次操作得到的状态。
设其中的某个状态为 next_status，如果其没有被搜索过，我们就将
(next_status, step + 1) 加入队列。如果搜索到了 target，我们就返回
其对应的操作次数。

在搜索的过程中，我们需要一个哈希表存储所有搜索到的状态，避免重复搜索。

如果搜索完成后，我们仍没有搜索到 [[1,2,3],[4,5,0]]，说明我们无法解开
谜板，返回 -1。

细节

本题中，搜索的状态 status 是一个 2 * 3 的二维数组，在很多语言中，
我们无法将数组直接放入哈希表中，可行的解决方案有两种：

- 自行实现数组的哈希函数；
- 数组转换成语言中可以直接进行哈希的类型。

在问题中，我们使用第二种解决方案，将 status 按照行优先的顺序拼接成
一个长度为 2 * 3 = 6 的字符串。例如目标状态 [[1,2,3],[4,5,0]]
可以表示为 123450。

在确定了解决方案后，我们还需要考虑如何有效地找出 status 通过一次操作
得到的所有状态。根据题目中的规定，每一次操作可以将 status 中的 0 与
相邻位置的数字进行交换，因此我们同样可以按照行优先的顺序给 2 * 3 的
谜板进行编号：

    +---+---+---+
    | 0 | 1 | 2 |
    +---+---+---+
    | 3 | 4 | 5 |
    +---+---+---+

这样一来，我们可以预处理出每一个位置的所有相邻位置，即：

- 0 的相邻位置是 1, 3；
- 1 的相邻位置是 0, 2, 4；
- 2 的相邻位置是 1, 5；
- 3 的相邻位置是 0, 4；
- 4 的相邻位置是 1, 3, 5；
- 5 的相邻位置是 2, 4。

因此，我们在 status 中找出 0 所在的位置 x，对于每一个与 x 相邻的位置
y，我们将 status[x] 与 status[y] 进行交换，即等同于进行了一次操作。
注意：这里的 status 是已经拼接完成的字符串。

最后我们还需要注意一个细节：如果 board 就是目标状态 [[1,2,3],[4,5,0]]，
那么直接返回答案 0。
"""


# @lc code=start
class Solution:
    TARGET = '123450'
    NEIGHBORS = ((1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4))

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # 枚举 status 通过一次交换操作得到的状态
        def get(status):
            status = list(status)
            x = status.index('0')
            for y in Solution.NEIGHBORS[x]:
                status[x], status[y] = status[y], status[x]
                yield ''.join(status)
                status[x], status[y] = status[y], status[x]

        initial = ''.join(str(num) for row in board for num in row)
        if initial == Solution.TARGET:
            return 0

        seen = {initial}
        que = deque([(initial, 0)])
        while que:
            status, step = que.popleft()
            for next_status in get(status):
                if next_status in seen:
                    continue

                if next_status == Solution.TARGET:
                    return step + 1

                seen.add(next_status)
                que.append((next_status, step + 1))

        return -1


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.slidingPuzzle(board=[[1, 2, 3], [4, 0, 5]]))
    print(solu.slidingPuzzle(board=[[1, 2, 3], [5, 4, 0]]))
    print(solu.slidingPuzzle(board=[[4, 1, 2], [5, 0, 3]]))
    print(solu.slidingPuzzle(board=[[3, 2, 4], [1, 5, 0]]))
