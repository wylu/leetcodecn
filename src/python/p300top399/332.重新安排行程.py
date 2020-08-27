#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   332.重新安排行程.py
@Time    :   2020/08/27 09:45:41
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#
# https://leetcode-cn.com/problems/reconstruct-itinerary/description/
#
# algorithms
# Medium (40.47%)
# Likes:    178
# Dislikes: 0
# Total Accepted:    12.2K
# Total Submissions: 30K
# Testcase Example: '[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]'
#
# 给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。所有这些机票都属于一个从
# JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。
#
# 说明:
#
#
# 如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"]
# 相比就更小，排序更靠前
# 所有的机场都用三个大写字母表示（机场代码）。
# 假定所有机票至少存在一种合理的行程。
#
#
# 示例 1:
#
# 输入: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# 输出: ["JFK", "MUC", "LHR", "SFO", "SJC"]
#
#
# 示例 2:
#
# 输入: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# 输出: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# 解释: 另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后。
#
#
from typing import List


# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return []

        edges = {}
        for u, v in tickets:
            if u not in edges:
                edges[u] = []
            edges[u].append(v)

        for vs in edges.values():
            # 每个邻接城市列表按照字母表顺序排列
            vs.sort()

        # city: 当前访问的城市，used: 已用掉的机票数
        def dfs(city: str, used: int) -> bool:
            if used == len(tickets):
                # 遍历完所有"边"，返回True
                return True

            if city not in edges or not edges[city]:
                # 机票未用完的情况下，没有邻接城市了
                return False

            next_cities = edges[city]
            n = len(next_cities)
            for i in range(n):
                # 下一个城市
                nc = next_cities[i]

                # 从当前城市的邻接表中删除选择的下一个城市
                # 一张机票不能使用两次（一条边只能访问一次）
                next_cities.remove(nc)
                ans.append(nc)

                if dfs(nc, used + 1):
                    return True

                # 回溯
                next_cities.insert(i, nc)
                ans.pop()

            return False

        ans = ['JFK']
        dfs('JFK', 0)
        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(
        solu.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"],
                            ["ATL", "JFK"], ["ATL", "SFO"]]))
