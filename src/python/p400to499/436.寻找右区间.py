#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   436.寻找右区间.py
@Time    :   2022/05/20 22:53:31
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=436 lang=python3
#
# [436] 寻找右区间
#
# https://leetcode.cn/problems/find-right-interval/description/
#
# algorithms
# Medium (56.34%)
# Likes:    169
# Dislikes: 0
# Total Accepted:    31.9K
# Total Submissions: 56.8K
# Testcase Example:  '[[1,2]]'
#
# 给你一个区间数组 intervals ，其中 intervals[i] = [starti, endi] ，且每个 starti 都 不同 。
#
# 区间 i 的 右侧区间 可以记作区间 j ，并满足 startj >= endi ，且 startj 最小化 。
#
# 返回一个由每个区间 i 的 右侧区间 在 intervals 中对应下标组成的数组。如果某个区间 i 不存在对应的 右侧区间 ，则下标 i 处的值设为
# -1 。
#
#
# 示例 1：
#
#
# 输入：intervals = [[1,2]]
# 输出：[-1]
# 解释：集合中只有一个区间，所以输出-1。
#
#
# 示例 2：
#
#
# 输入：intervals = [[3,4],[2,3],[1,2]]
# 输出：[-1,0,1]
# 解释：对于 [3,4] ，没有满足条件的“右侧”区间。
# 对于 [2,3] ，区间[3,4]具有最小的“右”起点;
# 对于 [1,2] ，区间[2,3]具有最小的“右”起点。
#
#
# 示例 3：
#
#
# 输入：intervals = [[1,4],[2,3],[3,4]]
# 输出：[-1,2,-1]
# 解释：对于区间 [1,4] 和 [3,4] ，没有满足条件的“右侧”区间。
# 对于 [2,3] ，区间 [3,4] 有最小的“右”起点。
#
#
#
#
# 提示：
#
#
# 1 <= intervals.length <= 2 * 10^4
# intervals[i].length == 2
# -10^6 <= starti <= endi <= 10^6
# 每个间隔的起点都 不相同
#
#
#
from bisect import bisect_left
from typing import List


# @lc code=start
class Solution:

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for i, interval in enumerate(intervals):
            interval.append(i)

        intervals.sort()

        n = len(intervals)
        ans = [-1] * n
        for _, end, i in intervals:
            j = bisect_left(intervals, [end])
            if j < n:
                ans[i] = intervals[j][2]

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()

    intervals = [[1, 2]]
    print(solu.findRightInterval(intervals))

    intervals = [[3, 4], [2, 3], [1, 2]]
    print(solu.findRightInterval(intervals))

    intervals = [[1, 4], [2, 3], [3, 4]]
    print(solu.findRightInterval(intervals))
