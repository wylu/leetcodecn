#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5505.使数组和能被P整除.py
@Time    :   2020/09/19 22:47:16
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List
"""
前缀和 + 哈希表优化

假设 nums 的和除以 P，余数是 mod，

如果 mod == 0，答案就是 0。
如果 mod != 0，答案变成了找原数组中的最短连续子数组，使得其数字和除以 P，
余数也是 mod。

由于是求解连续子数组和的问题，很容易想到使用前缀和。我们可以扫描一遍整个
数组，计算到每个元素的前缀和。

假设当前前缀和除以 P 的余数是 curmod，为了找到一段连续子数组对 P 的余数
是 mod，我们需要找到一段前缀和，对 P 的余数是 targetmod。其中 targetmod
的求法是：

如果 curmod >= mod，很简单：targetmod = curmod - mod；
如果 curmod < mod，我们需要加上一个 P：targetmod = curmod - mod + P；

这样，我们可以保证，当前前缀和减去目标前缀和，剩余的数组对 P 的余数是
mod。我们只需要找最短的这样的数组就好。

最后，为了快速找到一段对 P 的余数为 targetmod 的前缀和，我们使用一个
哈希表 table，来存储之前前缀和对 P 的余数和所在的索引。
（key 为余数；value 为索引）。

table 在遍历过程中更新，以保证每次在 table 中查找到的，是离当前元素最近
的索引，从而保证找到的是“最短”的连续子数组。
"""


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        mod = sum(nums) % p
        if mod == 0:
            return 0

        n, mp, tot = len(nums), {0: -1}, 0
        ans = n
        for i in range(n):
            tot += nums[i]
            curmod = tot % p
            targetmod = (curmod - mod + p) % p
            mp[curmod] = i
            if targetmod in mp:
                ans = min(ans, i - mp[targetmod])

        return -1 if ans == n else ans


# 超时
# class Solution:
#     def minSubarray(self, nums: List[int], p: int) -> int:
#         n = len(nums)
#         ps = [0]
#         for i in range(1, n + 1):
#             ps.append(ps[-1] + nums[i - 1])

#         if ps[-1] % p == 0:
#             return 0

#         for i in range(1, n):
#             j = 0
#             while j + i <= n:
#                 rm = ps[j + i] - ps[j]
#                 if (ps[n] - rm) % p == 0:
#                     return i
#                 j += 1

#         return -1

if __name__ == '__main__':
    solu = Solution()
    print(solu.minSubarray([3, 1, 4, 2], 6))
    print(solu.minSubarray([6, 3, 5, 2], 9))
    print(solu.minSubarray([1, 2, 3], 3))
