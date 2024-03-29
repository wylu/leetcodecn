#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1743.从相邻元素对还原数组.py
@Time    :   2021/07/25 15:26:15
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1743 lang=python3
#
# [1743] 从相邻元素对还原数组
#
# https://leetcode-cn.com/problems/restore-the-array-from-adjacent-pairs/description/
#
# algorithms
# Medium (63.48%)
# Likes:    42
# Dislikes: 0
# Total Accepted:    6K
# Total Submissions: 9.7K
# Testcase Example:  '[[2,1],[3,4],[3,2]]'
#
# 存在一个由 n 个不同元素组成的整数数组 nums ，但你已经记不清具体内容。好在你还记得 nums 中的每一对相邻元素。
#
# 给你一个二维整数数组 adjacentPairs ，大小为 n - 1 ，其中每个 adjacentPairs[i] = [ui, vi] 表示元素 ui
# 和 vi 在 nums 中相邻。
#
# 题目数据保证所有由元素 nums[i] 和 nums[i+1] 组成的相邻元素对都存在于 adjacentPairs 中，存在形式可能是
# [nums[i], nums[i+1]] ，也可能是 [nums[i+1], nums[i]] 。这些相邻元素对可以 按任意顺序 出现。
#
# 返回 原始数组 nums 。如果存在多种解答，返回 其中任意一个 即可。
#
#
#
# 示例 1：
#
#
# 输入：adjacentPairs = [[2,1],[3,4],[3,2]]
# 输出：[1,2,3,4]
# 解释：数组的所有相邻元素对都在 adjacentPairs 中。
# 特别要注意的是，adjacentPairs[i] 只表示两个元素相邻，并不保证其 左-右 顺序。
#
#
# 示例 2：
#
#
# 输入：adjacentPairs = [[4,-2],[1,4],[-3,1]]
# 输出：[-2,4,1,-3]
# 解释：数组中可能存在负数。
# 另一种解答是 [-3,1,4,-2] ，也会被视作正确答案。
#
#
# 示例 3：
#
#
# 输入：adjacentPairs = [[100000,-100000]]
# 输出：[100000,-100000]
#
#
#
#
# 提示：
#
#
# nums.length == n
# adjacentPairs.length == n - 1
# adjacentPairs[i].length == 2
# 2 <= n <= 10^5
# -10^5 <= nums[i], ui, vi <= 10^5
# 题目数据保证存在一些以 adjacentPairs 作为元素对的数组 nums
#
#
#
# from collections import deque
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)

        ans = []
        for k, v in graph.items():
            if len(v) == 1:
                ans.append(k)
                break

        ans.append(graph[ans[-1]][0])
        for i in range(2, len(adjacentPairs) + 1):
            vs = graph[ans[i - 1]]
            ans.append(vs[1] if vs[0] == ans[i - 2] else vs[0])

        return ans


# @lc code=end

# class Solution:
#     def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
#         graph = defaultdict(list)
#         for u, v in adjacentPairs:
#             graph[u].append(v)
#             graph[v].append(u)

#         ans = deque([adjacentPairs[0][0]])
#         seen = {ans[0]}
#         n = len(adjacentPairs) + 1
#         while len(ans) < n:
#             u = ans[0]
#             for v in graph[u]:
#                 if v not in seen:
#                     ans.appendleft(v)
#                     seen.add(v)
#                     break

#             u = ans[-1]
#             for v in graph[u]:
#                 if v not in seen:
#                     ans.append(v)
#                     seen.add(v)
#                     break

#         return list(ans)

if __name__ == '__main__':
    solu = Solution()
    print(solu.restoreArray(adjacentPairs=[[2, 1], [3, 4], [3, 2]]))
    print(solu.restoreArray(adjacentPairs=[[4, -2], [1, 4], [-3, 1]]))
    print(solu.restoreArray(adjacentPairs=[[100000, -100000]]))
