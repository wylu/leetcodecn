#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   40.组合总和-ii.py
@Time    :   2020/09/10 09:32:39
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode-cn.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (62.72%)
# Likes:    360
# Dislikes: 0
# Total Accepted:    86.3K
# Total Submissions: 136.3K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用一次。
#
# 说明：
#
#
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。
#
#
# 示例 1:
#
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
#
#
# 示例 2:
#
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
# [1,2,2],
# [5]
# ]
#
#
from typing import List


# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int],
                        target: int) -> List[List[int]]:
        def dfs(c: int, target: int) -> None:
            for i in range(c, len(cds)):
                num, cnt = cds[i]
                if cnt == 0:
                    continue
                if num == target:
                    ans.append(stack[:] + [num])
                elif num < target:
                    stack.append(num)
                    cds[i][1] -= 1
                    dfs(i, target - num)
                    cds[i][1] += 1
                    stack.pop()
                else:
                    break

        cnts = {}
        for num in candidates:
            cnts[num] = cnts.get(num, 0) + 1
        cds = [[k, v] for k, v in cnts.items()]
        cds.sort()

        ans, stack = [], []
        dfs(0, target)
        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(solu.combinationSum2([2, 5, 2, 1, 2], 5))
