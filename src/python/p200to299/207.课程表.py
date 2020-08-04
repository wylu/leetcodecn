#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   207.课程表.py
@Time    :   2020/08/04 21:46:43
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#
# https://leetcode-cn.com/problems/course-schedule/description/
#
# algorithms
# Medium (52.05%)
# Likes:    496
# Dislikes: 0
# Total Accepted:    62.9K
# Total Submissions: 117.8K
# Testcase Example:  '2\n[[1,0]]'
#
# 你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
#
# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
#
# 给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？
#
#
#
# 示例 1:
#
# 输入: 2, [[1,0]]
# 输出: true
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
#
# 示例 2:
#
# 输入: 2, [[1,0],[0,1]]
# 输出: false
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
#
#
#
# 提示：
#
#
# 输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
# 你可以假定输入的先决条件中没有重复的边。
# 1 <= numCourses <= 10^5
#
#
#
from collections import deque
from typing import List
"""
广度优先搜索

思路:

方法一的深度优先搜索是一种「逆向思维」：最先被放入栈中的节点是在拓扑排序中
最后面的节点。我们也可以使用正向思维，顺序地生成拓扑排序，这种方法也更加直观。

我们考虑拓扑排序中最前面的节点，该节点一定不会有任何入边，也就是它没有任何的
先修课程要求。当我们将一个节点加入答案中后，我们就可以移除它的所有出边，代表
着它的相邻节点少了一门先修课程的要求。如果某个相邻节点变成了「没有任何入边的
节点」，那么就代表着这门课可以开始学习了。按照这样的流程，我们不断地将没有
入边的节点加入答案，直到答案中包含所有的节点（得到了一种拓扑排序）或者不存在
没有入边的节点（图中包含环）。

上面的想法类似于广度优先搜索，因此我们可以将广度优先搜索的流程与拓扑排序的
求解联系起来。

算法：

我们使用一个队列来进行广度优先搜索。初始时，所有入度为 0 的节点都被放入
队列中，它们就是可以作为拓扑排序最前面的节点，并且它们之间的相对顺序是
无关紧要的。

在广度优先搜索的每一步中，我们取出队首的节点 u，将 u 放入答案中；然后移除
u 的所有出边，也就是将 u 的所有相邻节点的入度减少 1。如果某个相邻节点 v
的入度变为 0，那么我们就将 v 放入队列中。

在广度优先搜索的过程结束后。如果答案中包含了这 n 个节点，那么我们就找到了
一种拓扑排序，否则说明图中存在环，也就不存在拓扑排序了。
"""


# @lc code=start
class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        ind = [0] * numCourses
        graph = {}
        # 计算每个节点的入度
        for u, v in prerequisites:
            ind[v] += 1

            # 同时建图
            if u in graph:
                graph[u].append(v)
            else:
                graph[u] = [v]

        ans = 0

        # 初始时，将所有入度为 0 的节点加入队列
        que = deque(i for i in range(numCourses) if ind[i] == 0)
        while que:
            u = que.popleft()
            ans += 1

            # 将 u 指向的所有节点的入度减一
            for v in graph.get(u, []):
                ind[v] -= 1

                # 当有节点入度为 0 时，加入队列
                if ind[v] == 0:
                    que.append(v)

        return ans == numCourses


# @lc code=end
