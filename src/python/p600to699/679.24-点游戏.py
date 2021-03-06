#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   679.24-点游戏.py
@Time    :   2020/08/22 18:00:11
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=679 lang=python3
#
# [679] 24 点游戏
#
# https://leetcode-cn.com/problems/24-game/description/
#
# algorithms
# Hard (44.74%)
# Likes:    184
# Dislikes: 0
# Total Accepted:    13.6K
# Total Submissions: 26K
# Testcase Example:  '[4,1,8,7]'
#
# 你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。
#
# 示例 1:
#
# 输入: [4, 1, 8, 7]
# 输出: True
# 解释: (8-4) * (7-1) = 24
#
#
# 示例 2:
#
# 输入: [1, 2, 1, 2]
# 输出: False
#
#
# 注意:
#
#
# 除法运算符 / 表示实数除法，而不是整数除法。例如 4 / (1 - 2/3) = 12 。
# 每个运算符对两个数进行运算。特别是我们不能用 - 作为一元运算符。例如，[1, 1, 1, 1] 作为输入时，表达式 -1 - 1 - 1 - 1
# 是不允许的。
# 你不能将数字连接在一起。例如，输入为 [1, 2, 1, 2] 时，不能写成 12 + 12 。
#
#
#
from typing import List
"""
递归回溯：

一共有 4 个数和 3 个运算操作，因此可能性非常有限。一共有多少种可能性呢？

首先从 4 个数字中有序地选出 2 个数字，共有 4*3=12 种选法，并选择加、减、
乘、除 4 种运算操作之一，用得到的结果取代选出的 2 个数字，剩下 3 个数字。
然后在剩下的 3 个数字中有序地选出 2 个数字，共有 3*2=6 种选法，并选择 4
种运算操作之一，用得到的结果取代选出的 2 个数字，剩下 2 个数字。最后剩下
2 个数字，有 2 种不同的顺序，并选择 4 种运算操作之一。
因此，一共有 12*4*6*4*2*4=9216 种不同的可能性。

可以通过回溯的方法遍历所有不同的可能性。具体做法是，使用一个列表存储目前
的全部数字，每次从列表中选出 2 个数字，再选择一种运算操作，用计算得到的
结果取代选出的 2 个数字，这样列表中的数字就减少了 1 个。重复上述步骤，
直到列表中只剩下 1 个数字，这个数字就是一种可能性的结果，如果结果等于
24，则说明可以通过运算得到 24。如果所有的可能性的结果都不等于 24，则
说明无法通过运算得到 24。

实现时，有一些细节需要注意:
除法运算为实数除法，因此结果为浮点数，列表中存储的数字也都是浮点数。
在判断结果是否等于 24 时应考虑精度误差，这道题中，误差小于 10^(-6)
可以认为是相等。
进行除法运算时，除数不能为 0，如果遇到除数为 0 的情况，则这种可能性
可以直接排除。由于列表中存储的数字是浮点数，因此判断除数是否为 0 时
应考虑精度误差，这道题中，当一个数字的绝对值小于 10^(-6) 时，可以
认为该数字等于 0。

还有一个可以优化的点:
加法和乘法都满足交换律，因此如果选择的运算操作是加法或乘法，则对于
选出的 2 个数字不需要考虑不同的顺序，在遇到第二种顺序时可以不进行
运算，直接跳过。
"""


# @lc code=start
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        TARGET = 24
        EPSILON = 1e-6
        ADD, MUL, SUB, DIV = 0, 1, 2, 3

        def dfs(nums: List[int]) -> bool:
            if not nums:
                return False
            if len(nums) == 1:
                return abs(nums[0] - TARGET) < EPSILON

            for i, x in enumerate(nums):
                for j, y in enumerate(nums):
                    if i != j:
                        newNums = []
                        for k, z in enumerate(nums):
                            if k != i and k != j:
                                newNums.append(z)

                        for k in range(4):
                            if k < 2 and i > j:
                                continue

                            if k == ADD:
                                newNums.append(x + y)
                            elif k == MUL:
                                newNums.append(x * y)
                            elif k == SUB:
                                newNums.append(x - y)
                            elif k == DIV:
                                if abs(y) < EPSILON:
                                    continue
                                newNums.append(x / y)

                            if dfs(newNums):
                                return True

                            newNums.pop()
            return False

        return dfs(nums)


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.judgePoint24([4, 1, 8, 7]))
    print(solu.judgePoint24([1, 2, 1, 2]))
