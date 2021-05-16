#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   421.数组中两个数的最大异或值.py
@Time    :   2021/05/16 10:14:29
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=421 lang=python3
#
# [421] 数组中两个数的最大异或值
#
# https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
#
# algorithms
# Medium (60.29%)
# Likes:    269
# Dislikes: 0
# Total Accepted:    13.8K
# Total Submissions: 22.9K
# Testcase Example:  '[3,10,5,25,2,8]'
#
# 给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。
#
# 进阶：你可以在 O(n) 的时间解决这个问题吗？
#
#
#
#
#
# 示例 1：
#
#
# 输入：nums = [3,10,5,25,2,8]
# 输出：28
# 解释：最大运算结果是 5 XOR 25 = 28.
#
# 示例 2：
#
#
# 输入：nums = [0]
# 输出：0
#
#
# 示例 3：
#
#
# 输入：nums = [2,4]
# 输出：6
#
#
# 示例 4：
#
#
# 输入：nums = [8,10,2]
# 输出：10
#
#
# 示例 5：
#
#
# 输入：nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# 输出：127
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 2 * 10^4
# 0 <= nums[i] <= 2^31 - 1
#
#
#
#
#
from typing import List
"""
前言
假设我们在数组中选择了元素 ai 和 aj（i != j），使得它们达到最大的按位异或运算
结果 x：

    x = ai ^ aj

其中 ^ 表示按位异或运算。要想求出 x，一种简单的方法是使用二重循环枚举 i 和 j，
但这样做的时间复杂度为 O(n^2)，会超出时间限制。因此，我们需要寻求时间复杂度
更低的做法。

根据按位异或运算的性质，x = ai ^ aj 等价于 aj = x ^ ai。我们可以根据这一变换，
设计一种「从高位到低位依次确定 x 二进制表示的每一位」的方法，以此得到 x 的值。
该方法的精髓在于：

由于数组中的元素都在 [0, 2^31 - 1) 的范围内，那么我们可以将每一个数表示为一个
长度为 31 位的二进制数（如果不满 31 位，在最高位之前补上若干个前导 0 即可）；

这 31 个二进制位从低位到高位依次编号为 0, 1, ..., 30。我们从最高位第 30 个
二进制位开始，依次确定 x 的每一位是 0 还是 1；

由于我们需要找出最大的 x，因此在枚举每一位时，我们先判断 x 的这一位是否能取到
1。如果能，我们取这一位为 1，否则我们取这一位为 0。

「判断 x 的某一位是否能取到 1」这一步骤并不容易。下面介绍两种判断的方法。

方法一：哈希表
思路与算法

假设我们已经确定了 x 最高的若干个二进制位，当前正在确定第 k 个二进制位。根据
「前言」部分的分析，我们希望第 k 个二进制位能够取到 1。

我们用 pre_k(x) 表示 x 从最高位第 30 个二进制位开始，到第 k 个二进制位为止的
数，那么 aj = x ^ ai 蕴含着：

  pre_k(aj) = pre_k(x) ^ pre_k(ai)

由于 pre_k(x) 对于我们来说是已知的，因此我们将所有的 pre_k(aj) 放入哈希表中，
随后枚举 i 并计算 pre_k(x) ^ pre_k(ai)。如果其出现在哈希表中，那么说明第 k
个二进制位能够取到 1，否则第 k 个二进制位只能为 0。
"""


# @lc code=start
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        x = 0
        for k in range(30, -1, -1):
            seen = set()
            # 将所有的 pre_k(aj) 放入集合中
            for num in nums:
                # 如果只想保留从最高位开始到第 k 个二进制位为止的部分
                # 只需将其右移 k 位
                seen.add(num >> k)

            # 目前 x 包含从最高位开始到第 k+1 个二进制位为止的部分
            # 我们将 x 的第 k 个二进制位置为 1，即为 x = (x << 1) + 1
            x = (x << 1) + 1

            found = False
            for num in nums:
                if x ^ (num >> k) in seen:
                    found = True
                    break

            # 如果找不到满足等式的 ai 和 aj，那么 x 的第 k 个二进制位只能为 0
            # 即 x <<= 1
            if not found:
                x -= 1

        return x


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.findMaximumXOR(nums=[3, 10, 5, 25, 2, 8]))
    print(solu.findMaximumXOR(nums=[0]))
    print(solu.findMaximumXOR(nums=[2, 4]))
    print(solu.findMaximumXOR(nums=[8, 10, 2]))
    nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]
    print(solu.findMaximumXOR(nums))
