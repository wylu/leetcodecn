#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1838.最高频元素的频数.py
@Time    :   2021/07/19 17:14:57
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1838 lang=python3
#
# [1838] 最高频元素的频数
#
# https://leetcode-cn.com/problems/frequency-of-the-most-frequent-element/description/
#
# algorithms
# Medium (42.17%)
# Likes:    117
# Dislikes: 0
# Total Accepted:    17K
# Total Submissions: 40.3K
# Testcase Example:  '[1,2,4]\n5'
#
# 元素的 频数 是该元素在一个数组中出现的次数。
#
# 给你一个整数数组 nums 和一个整数 k 。在一步操作中，你可以选择 nums 的一个下标，并将该下标对应元素的值增加 1 。
#
# 执行最多 k 次操作后，返回数组中最高频元素的 最大可能频数 。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,4], k = 5
# 输出：3
# 解释：对第一个元素执行 3 次递增操作，对第二个元素执 2 次递增操作，此时 nums = [4,4,4] 。
# 4 是数组中最高频元素，频数是 3 。
#
# 示例 2：
#
#
# 输入：nums = [1,4,8,13], k = 5
# 输出：2
# 解释：存在多种最优解决方案：
# - 对第一个元素执行 3 次递增操作，此时 nums = [4,4,8,13] 。4 是数组中最高频元素，频数是 2 。
# - 对第二个元素执行 4 次递增操作，此时 nums = [1,8,8,13] 。8 是数组中最高频元素，频数是 2 。
# - 对第三个元素执行 5 次递增操作，此时 nums = [1,4,13,13] 。13 是数组中最高频元素，频数是 2 。
#
#
# 示例 3：
#
#
# 输入：nums = [3,9,6], k = 2
# 输出：1
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
# 1 <= k <= 10^5
#
#
#
from typing import List
"""
方法一：排序 + 滑动窗口
提示 1

操作后的最高频元素必定可以是数组中已有的某一个元素。

提示 1 解释

我们用 x_i 来表示 nums 数组中下标为 i 的元素。
如果可以将数组内的一系列元素 {x_i}_1,\dots,{x_i}_k 全部变为 y，假设这些元素中的
最大值为 x，那么我们一定可以将这些数全部变成 x，此时频数不变且操作次数更少。

提示 2

优先操作距离目标值最近的（小于目标值的）元素。

提示 2 解释

假设目标值为 y，对于数组内任意两个小于 y 的元素 x_i < x_j ，将较大者（x_j）变为
y 所需要的操作数为 y - x_j，而对应改变较小者（x_i）做需要的操作数为 y - x_i，
显然有 y - x_j < y - x_i。

提示 3

遍历数组中的每个元素作为目标值并进行尝试。此处是否存在一些可以用于优化算法的性质？

思路与算法

我们可以按照提示 1 与提示 2 的贪心策略进行操作。

将数组排序，遍历排序后数组每个元素 x_r 作为目标值，并求出此时按贪心策略可以改变
至目标值的元素左边界。

此时考虑到数据范围为 10^5，朴素的线性查找显然会超时，因此需要寻找可以优化的性质。

我们可以枚举 x_r 作为目标值。假设 x_r 对应的答案左边界为 x_l，定义 \Delta(l, r)
为将 x_l,\dots,x_r 全部变为 x_r 所需要的操作次数：

\Delta(l, r) = \sum_{i = l}^{r} (x_r - x_i) = (r - l)x_r - \sum_{i = l}^{r-1} x_i

考虑右边界 r 右移至 r + 1 的过程，此时：

\Delta(l, r + 1) - \Delta(l, r) = (x_{r + 1} - x_{r})\cdot(r - l + 1) \ge 0

操作数有可能超过限制 k，因此在超过限制的情况下，我们需要移动左边界 l。同样考虑左边界
l 右移至 l + 1 的过程，此时:

\Delta(l + 1, r + 1) - \Delta(l, r + 1) = -(x_{r + 1} - x_{l}) \le 0

这说明右移左边界会使得答案减小，因此我们需要移动左边界直至对应的 \Delta(l', r + 1) 不大于 k。

我们使用 l 与 r 作为执行操作的左右边界（闭区间），同时用 total 来维护将 [l, r]
区间全部变为末尾元素的操作次数。在顺序枚举目标值（右边界）的同时，我们更新对应的
左边界，并用 res 来维护满足限制的最大区间元素数量即可。

另外要注意，此处 total 有可能会超过 32 位整数的范围，因此在 C++ 等语言中需要使用
更高位数的整型变量（long long 等）。
"""


# @lc code=start
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        L, R = 0, 1
        ans, tot = 1, 0

        while R < n:
            tot += (nums[R] - nums[R - 1]) * (R - L)
            while tot > k:
                tot -= nums[R] - nums[L]
                L += 1
            ans = max(ans, R - L + 1)
            R += 1

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.maxFrequency(nums=[1, 2, 4], k=5))
    print(solu.maxFrequency(nums=[1, 4, 8, 13], k=5))
    print(solu.maxFrequency(nums=[3, 9, 6], k=2))
