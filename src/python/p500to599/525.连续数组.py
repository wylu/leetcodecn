#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   525.连续数组.py
@Time    :   2021/06/03 09:50:44
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=525 lang=python3
#
# [525] 连续数组
#
# https://leetcode-cn.com/problems/contiguous-array/description/
#
# algorithms
# Medium (49.55%)
# Likes:    306
# Dislikes: 0
# Total Accepted:    16.9K
# Total Submissions: 34.2K
# Testcase Example:  '[0,1]'
#
# 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。
#
#
#
# 示例 1:
#
#
# 输入: nums = [0,1]
# 输出: 2
# 说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
#
# 示例 2:
#
#
# 输入: nums = [0,1,0]
# 输出: 2
# 说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# nums[i] 不是 0 就是 1
#
#
#
from typing import List
"""
https://leetcode-cn.com/problems/contiguous-array/solution/gong-shui-san-xie-qian-zhui-he-ha-xi-bia-q400/

基本分析
根据题意，我们可以轻易发现如下性质：

如果答案非 0，那么子数组长度必然为偶数，且长度至少为 2。

前缀和 + 哈希表
具体的，我们在预处理前缀和时，将 nums[i] 为 0 的值当做 −1 处理。

从而将问题转化为：如何求得最长一段区间和为 0 的子数组。

同时使用「哈希表」来记录「某个前缀和出现的最小下标」是多少。

再结合「如果答案非 0，子数组长度至少为 2」的特性，我们让循环从 2 开始，
并在循环开始前往「哈希表」存入哨兵，从而实现不需要处理边界问题。

PS. 哈希表常数还是比较大的，用数组模拟哈希表的卡常代码见 P2。
"""


# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ps = [0] * (n + 1)
        for i in range(n):
            ps[i + 1] = ps[i] + (1 if nums[i] else -1)

        ans, seen = 0, {}
        for i in range(n + 1):
            if ps[i] in seen:
                ans = max(ans, i - seen[ps[i]])
            else:
                seen[ps[i]] = i

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.findMaxLength(nums=[0, 1]))
    print(solu.findMaxLength(nums=[0, 1, 0]))
    print(solu.findMaxLength(nums=[0, 1, 1, 0]))
    print(solu.findMaxLength(nums=[0, 1, 1, 1, 0]))
    print(solu.findMaxLength(nums=[0, 1, 1, 1, 0, 0]))
    print(solu.findMaxLength(nums=[1, 1, 1, 1, 0, 0]))
    print(solu.findMaxLength(nums=[0, 0, 1]))
