#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   274.h-指数.py
@Time    :   2021/07/11 09:42:42
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#
# https://leetcode-cn.com/problems/h-index/description/
#
# algorithms
# Medium (40.85%)
# Likes:    160
# Dislikes: 0
# Total Accepted:    30.6K
# Total Submissions: 75.1K
# Testcase Example:  '[3,0,6,1,5]'
#
# 给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 h 指数。
#
# h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）总共有 h
# 篇论文分别被引用了至少 h 次。且其余的 N - h 篇论文每篇被引用次数 不超过 h 次。
#
# 例如：某人的 h 指数是 20，这表示他已发表的论文中，每篇被引用了至少 20 次的论文总共有 20 篇。
#
#
#
# 示例：
#
#
# 输入：citations = [3,0,6,1,5]
# 输出：3
# 解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
# 由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。
#
#
#
# 提示：如果 h 有多种可能的值，h 指数是其中最大的那个。
#
#
# import bisect
from typing import List
"""
方法一：排序
首先我们可以将初始的 H 指数 h 设为 0，然后将引用次数排序，并且对排序后的数组从大到小遍历。

根据 H 指数的定义，如果当前 H 指数为 h 并且在遍历过程中找到当前值 citations[i] > h，
则说明我们找到了一篇被引用了至少 h+1 次的论文，所以将现有的 h 值加 1。继续遍历直到 h
无法继续增大。最后返回 h 作为最终答案。
"""


# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h = 0
        n = len(citations)
        i = n - 1
        while i >= 0 and citations[i] > h:
            h += 1
            i -= 1

        return h


# @lc code=end

# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         citations.sort()
#         n = len(citations)

#         def check(h: int) -> bool:
#             idx = bisect.bisect_left(citations, h)
#             return n - idx >= h

#         left, right = 0, n
#         while left < right:
#             mid = (left + right + 1) // 2
#             if check(mid):
#                 left = mid
#             else:
#                 right = mid - 1

#         return left

if __name__ == '__main__':
    solu = Solution()
    print(solu.hIndex(citations=[3, 0, 6, 1, 5]))
    print(solu.hIndex(citations=[0]))
    print(solu.hIndex(citations=[0, 0, 0]))
    print(solu.hIndex(citations=[1]))
    print(solu.hIndex(citations=[2, 3]))
    print(solu.hIndex(citations=[1, 3, 1]))
    print(solu.hIndex(citations=[100]))
    print(solu.hIndex(citations=[100, 100, 100]))
