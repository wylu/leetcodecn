#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1449.数位成本和为目标值的最大数字.py
@Time    :   2021/06/12 21:38:19
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1449 lang=python3
#
# [1449] 数位成本和为目标值的最大数字
#
# https://leetcode-cn.com/problems/form-largest-integer-with-digits-that-add-up-to-target/description/
#
# algorithms
# Hard (59.63%)
# Likes:    97
# Dislikes: 0
# Total Accepted:    11K
# Total Submissions: 18.4K
# Testcase Example:  '[4,3,2,5,6,7,2,5,5]\n9'
#
# 给你一个整数数组 cost 和一个整数 target 。请你返回满足如下规则可以得到的 最大 整数：
#
#
# 给当前结果添加一个数位（i + 1）的成本为 cost[i] （cost 数组下标从 0 开始）。
# 总成本必须恰好等于 target 。
# 添加的数位中没有数字 0 。
#
#
# 由于答案可能会很大，请你以字符串形式返回。
#
# 如果按照上述要求无法得到任何整数，请你返回 "0" 。
#
#
#
# 示例 1：
#
#
# 输入：cost = [4,3,2,5,6,7,2,5,5], target = 9
# 输出："7772"
# 解释：添加数位 '7' 的成本为 2 ，添加数位 '2' 的成本为 3 。所以 "7772" 的代价为 2*3+ 3*1 = 9 。 "977"
# 也是满足要求的数字，但 "7772" 是较大的数字。
# ⁠数字     成本
# ⁠ 1  ->   4
# ⁠ 2  ->   3
# ⁠ 3  ->   2
# ⁠ 4  ->   5
# ⁠ 5  ->   6
# ⁠ 6  ->   7
# ⁠ 7  ->   2
# ⁠ 8  ->   5
# ⁠ 9  ->   5
#
#
# 示例 2：
#
#
# 输入：cost = [7,6,5,5,5,6,8,7,8], target = 12
# 输出："85"
# 解释：添加数位 '8' 的成本是 7 ，添加数位 '5' 的成本是 5 。"85" 的成本为 7 + 5 = 12 。
#
#
# 示例 3：
#
#
# 输入：cost = [2,4,6,2,4,6,4,4,4], target = 5
# 输出："0"
# 解释：总成本是 target 的条件下，无法生成任何整数。
#
#
# 示例 4：
#
#
# 输入：cost = [6,10,15,40,40,40,40,40,40], target = 47
# 输出："32211"
#
#
#
#
# 提示：
#
#
# cost.length == 9
# 1 <= cost[i] <= 5000
# 1 <= target <= 5000
#
#
#
from typing import List
"""
https://leetcode-cn.com/problems/form-largest-integer-with-digits-that-add-up-to-target/solution/gong-shui-san-xie-fen-liang-bu-kao-lu-we-uy4y/

基本分析
根据题意：给定 1~9 几个数字，每个数字都有选择成本，求给定费用情况下，凑成的最
大数字是多少。

通常我们会如何比较两数大小关系？

首先我们 根据长度进行比较，长度较长数字较大；再者，对于长度相等的数值，从高度
往低位进行比较，找到第一位不同，不同位值大的数值较大。

其中规则一的比较优先级要高于规则二。

基于此，我们可以将构造分两步进行。

动态规划 + 贪心
具体的，先考虑「数值长度」问题，每个数字有相应选择成本，所能提供的长度均为 1。

问题转换为：有若干物品，求给定费用的前提下，花光所有费用所能选择的最大价值
（物品个数）为多少。

每个数字可以被选择多次，属于完全背包模型。

当求得最大「数值长度」后，考虑如何构造答案。

根据规则二，应该尽可能让高位的数值越大越好，因此我们可以从数值 9 开始往数值
1 遍历，如果状态能够由该数值转移而来，则选择该数值。
"""


# @lc code=start
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        n = len(cost)
        f = [float('-inf')] * (target + 1)
        f[0] = 0

        for i in range(n):
            for j in range(cost[i], target + 1):
                f[j] = max(f[j], f[j - cost[i]] + 1)

        if f[target] == float('-inf'):
            return '0'

        ans = []
        for i in range(9, 0, -1):
            u = cost[i - 1]
            while target >= u and f[target] == f[target - u] + 1:
                ans.append(str(i))
                target -= u

        return ''.join(ans)


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.largestNumber(cost=[4, 3, 2, 5, 6, 7, 2, 5, 5], target=9))
    print(solu.largestNumber(cost=[7, 6, 5, 5, 5, 6, 8, 7, 8], target=12))
    print(solu.largestNumber(cost=[2, 4, 6, 2, 4, 6, 4, 4, 4], target=5))

    cost = [6, 10, 15, 40, 40, 40, 40, 40, 40]
    target = 47
    print(solu.largestNumber(cost, target))
