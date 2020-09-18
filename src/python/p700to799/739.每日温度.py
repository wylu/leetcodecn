#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   739.每日温度.py
@Time    :   2020/09/18 23:07:48
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#
# https://leetcode-cn.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (64.68%)
# Likes:    505
# Dislikes: 0
# Total Accepted:    103.8K
# Total Submissions: 160.6K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# 请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0
# 来代替。
#
# 例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4,
# 2, 1, 1, 0, 0]。
#
# 提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
#
#
from typing import List


# @lc code=start
class Solution:
    def dailyTemperatures(self, ts: List[int]) -> List[int]:
        ans, stack = [0] * len(ts), []
        for i, t in enumerate(ts):
            while stack and t > ts[stack[-1]]:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans


# @lc code=end
if __name__ == '__main__':
    solu = Solution()
    print(solu.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
