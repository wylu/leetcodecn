#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   134.加油站.py
@Time    :   2020/11/18 22:08:55
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#
# https://leetcode-cn.com/problems/gas-station/description/
#
# algorithms
# Medium (56.49%)
# Likes:    519
# Dislikes: 0
# Total Accepted:    75.7K
# Total Submissions: 134K
# Testcase Example:  '[1,2,3,4,5]\n[3,4,5,1,2]'
#
# 在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
#
# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
#
# 如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。
#
# 说明:
#
#
# 如果题目有解，该答案即为唯一答案。
# 输入数组均为非空数组，且长度相同。
# 输入数组中的元素均为非负数。
#
#
# 示例 1:
#
# 输入:
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]
#
# 输出: 3
#
# 解释:
# 从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
# 开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
# 开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
# 开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
# 开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
# 开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
# 因此，3 可为起始索引。
#
# 示例 2:
#
# 输入:
# gas  = [2,3,4]
# cost = [3,4,3]
#
# 输出: -1
#
# 解释:
# 你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
# 我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
# 开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
# 开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
# 你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
# 因此，无论怎样，你都不可能绕环路行驶一周。
#
#
from typing import List
"""
1.首先判断总 gas 能不能大于等于总 cost，如果总 gas 不够，一切都白搭；
2.然后找总（gas-cost）的最低点，不管正负（如果最低点都是正的，则一定满足）；
3.找到最低点后，如果有解，那么解就是最低点的下一个点，因为总（gas-cost）
  是要大于等于 0 的，所以前面损失的 gas 总能从最低点下一个点开始都会拿回来！
"""


# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        tot, least, idx = 0, 0x7FFFFFFF, 0
        for i in range(n):
            tot += gas[i] - cost[i]
            if tot < least:
                least, idx = tot, i
        return -1 if tot < 0 else (idx + 1) % n


# @lc code=end
