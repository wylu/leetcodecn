#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   946.验证栈序列.py
@Time    :   2020/09/01 23:38:05
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=946 lang=python3
#
# [946] 验证栈序列
#
# https://leetcode-cn.com/problems/validate-stack-sequences/description/
#
# algorithms
# Medium (59.42%)
# Likes:    116
# Dislikes: 0
# Total Accepted:    13.6K
# Total Submissions: 22.9K
# Testcase Example:  '[1,2,3,4,5]\n[4,5,3,2,1]'
#
# 给定 pushed 和 popped 两个序列，每个序列中的 值都不重复，只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop
# 操作序列的结果时，返回 true；否则，返回 false 。
#
#
#
# 示例 1：
#
# 输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# 输出：true
# 解释：我们可以按以下顺序执行：
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
#
#
# 示例 2：
#
# 输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# 输出：false
# 解释：1 不能在 2 之前弹出。
#
#
#
#
# 提示：
#
#
# 0 <= pushed.length == popped.length <= 1000
# 0 <= pushed[i], popped[i] < 1000
# pushed 是 popped 的排列。
#
#
#
from typing import List


# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int],
                               popped: List[int]) -> bool:
        i, stack = 0, []
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return not stack


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    print(solu.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
