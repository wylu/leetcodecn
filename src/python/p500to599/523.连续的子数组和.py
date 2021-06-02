#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   523.连续的子数组和.py
@Time    :   2021/06/02 09:27:17
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=523 lang=python3
#
# [523] 连续的子数组和
#
# https://leetcode-cn.com/problems/continuous-subarray-sum/description/
#
# algorithms
# Medium (23.35%)
# Likes:    258
# Dislikes: 0
# Total Accepted:    35.1K
# Total Submissions: 149.3K
# Testcase Example:  '[23,2,4,6,7]\n6'
#
# 给你一个整数数组 nums 和一个整数 k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：
#
#
# 子数组大小 至少为 2 ，且
# 子数组元素总和为 k 的倍数。
#
#
# 如果存在，返回 true ；否则，返回 false 。
#
# 如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。
#
#
#
# 示例 1：
#
#
# 输入：nums = [23,2,4,6,7], k = 6
# 输出：true
# 解释：[2,4] 是一个大小为 2 的子数组，并且和为 6 。
#
# 示例 2：
#
#
# 输入：nums = [23,2,6,4,7], k = 6
# 输出：true
# 解释：[23, 2, 6, 4, 7] 是大小为 5 的子数组，并且和为 42 。
# 42 是 6 的倍数，因为 42 = 7 * 6 且 7 是一个整数。
#
#
# 示例 3：
#
#
# 输入：nums = [23,2,6,4,7], k = 13
# 输出：false
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
# 0 <= sum(nums[i]) <= 2^31 - 1
# 1 <= k <= 2^31 - 1
#
#
#
from typing import List
"""
基本分析
这是一道很经典的前缀和题目，类似的原题也在蓝桥杯出现过，坐标在 K 倍区间。

http://lx.lanqiao.cn/problem.page?gpid=T444

本题与那道题不同在于：
  - [K 倍区间] 需要求得所有符合条件的区间数量；本题需要判断是否存在。
  - [K 倍区间] 序列全是正整数，不需要考虑 0 值问题；本题需要考虑 0 值问题。

数据范围为 10^5，因此无论是纯朴素的做法 O(n^3) 还是简单使用前缀和
优化的做法 O(n^2) 都不能满足要求。

我们需要从 k 的倍数作为切入点来做。

预处理前缀和数组 sum，方便快速求得某一段区间的和。然后假定 [i, j]
是我们的目标区间，那么有：

    sum[j] - sum[i - 1] = n * k

经过简单的变形可得：

    (sum[j] / k) - (sum[i - 1] / k) = n

要使得两者除 k 相减为整数，需要满足 sum[j] 和 sum[i - 1] 除 k 余数相同。

也就是说，我们只需要枚举右端点 j，然后在枚举右端点 j 的时候检查之前是否
出现过左端点 i，使得 sum[j] 和 sum[i - 1] 对 k 取余相同。

前缀和 + HashSet
具体的，使用 HashSet 来保存出现过的值。

让循环从 2 开始枚举右端点（根据题目要求，子数组长度至少为 2），每次将
符合长度要求的位置的取余结果存入 HashSet。

如果枚举某个右端点 j 时发现存在某个左端点 i 符合要求，则返回 True。
"""


# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        ps = [0] * (n + 1)
        for i in range(n):
            ps[i + 1] = ps[i] + nums[i]

        seen = set()
        for i in range(2, n + 1):
            seen.add(ps[i - 2] % k)
            if ps[i] % k in seen:
                return True

        return False


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.checkSubarraySum(nums=[23, 2, 4, 6, 7], k=6))
    print(solu.checkSubarraySum(nums=[23, 2, 6, 4, 7], k=6))
    print(solu.checkSubarraySum(nums=[23, 2, 6, 4, 7], k=13))
