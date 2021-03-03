#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   338.比特位计数.py
@Time    :   2021/03/03 09:14:36
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#
# https://leetcode-cn.com/problems/counting-bits/description/
#
# algorithms
# Medium (77.29%)
# Likes:    542
# Dislikes: 0
# Total Accepted:    77.8K
# Total Submissions: 100.7K
# Testcase Example:  '2'
#
# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
#
# 示例 1:
#
# 输入: 2
# 输出: [0,1,1]
#
# 示例 2:
#
# 输入: 5
# 输出: [0,1,1,2,1,2]
#
# 进阶:
#
#
# 给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
# 要求算法的空间复杂度为O(n)。
# 你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。
#
#
#
from typing import List
"""
方法四：动态规划——最低设置位
定义正整数 x 的「最低设置位」为 x 的二进制表示中的最低的 1 所在位。
例如，10 的二进制表示是 1010，其最低设置位为 2，对应的二进制表示是 10。

令 y = x & (x−1)，则 y 为将 x 的最低设置位从 1 变成 0 之后的数，显然
0 ≤ y < x，bits[x] = bits[y] + 1。因此对任意正整数 x，都有
bits[x] = bits[x & (x−1)] + 1。

遍历从 1 到 num 的每个正整数 i，计算 bits 的值。最终得到的数组 bits
即为答案。
"""


# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        bits = [0] * (num + 1)
        for i in range(1, num + 1):
            bits[i] = bits[i & (i - 1)] + 1
        return bits


# @lc code=end

# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         ans = [0, 1]
#         power = 1
#         cur = 2**power
#         while cur <= num:
#             for i in range(cur, cur * 2):
#                 ans.append(1 + ans[i - cur])
#             power += 1
#             cur *= 2
#         return ans[:num + 1]

if __name__ == "__main__":
    solu = Solution()
    print(solu.countBits(0))
    print(solu.countBits(1))
    print(solu.countBits(2))
    print(solu.countBits(3))
    print(solu.countBits(4))
    print(solu.countBits(7))
    print(solu.countBits(8))
