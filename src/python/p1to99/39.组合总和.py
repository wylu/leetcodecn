#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   39.组合总和.py
@Time    :   2020/08/28 23:37:34
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (69.56%)
# Likes:    842
# Dislikes: 0
# Total Accepted:    128.2K
# Total Submissions: 184.3K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。
#
#
# 示例 1：
#
# 输入：candidates = [2,3,6,7], target = 7,
# 所求解集为：
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
#
#
# 示例 2：
#
# 输入：candidates = [2,3,5], target = 8,
# 所求解集为：
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
#
#
#
# 提示：
#
#
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# candidate 中的每个元素都是独一无二的。
# 1 <= target <= 500
#
#
#
from typing import List
"""
对 candidates 升序排序，以方便根据 target 的大小进行剪枝以减小搜索空间；
递归求可能的组合，每次递归时对所有 candidates 做一次遍历，情况有 3 种：
  1.满足条件，则加入答案；
  2.不足，继续递归；
  3.超出，则直接返回；

注意每层递归都对全体 candidates 做遍历会导致如 [2,2,3], [3,2,2] 这样重复
的答案的产生。这是因为发生了“往前选择”的情况，可以每次更深层的递归都往后
缩小一个 candidates，强制函数只能“往后选择”，这将不会出现重复答案。
"""


# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        def dfs(s: int, target: int) -> None:
            for i in range(s, len(candidates)):
                c = candidates[i]
                if c == target:
                    stack.append(c)
                    ans.append(stack[:])
                    stack.pop()
                elif c < target:
                    stack.append(c)
                    dfs(i, target - c)
                    stack.pop()
                else:
                    break

        candidates.sort()
        ans, stack = [], []
        dfs(0, target)
        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.combinationSum([2, 3, 6, 7], 7))
