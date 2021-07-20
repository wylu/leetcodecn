#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1877.数组中最大数对和的最小值.py
@Time    :   2021/07/20 09:43:36
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1877 lang=python3
#
# [1877] 数组中最大数对和的最小值
#
# https://leetcode-cn.com/problems/minimize-maximum-pair-sum-in-array/description/
#
# algorithms
# Medium (84.07%)
# Likes:    23
# Dislikes: 0
# Total Accepted:    10.2K
# Total Submissions: 12.2K
# Testcase Example:  '[3,5,2,3]'
#
# 一个数对 (a,b) 的 数对和 等于 a + b 。最大数对和 是一个数对数组中最大的 数对和 。
#
#
# 比方说，如果我们有数对 (1,5) ，(2,3) 和 (4,4)，最大数对和 为 max(1+5, 2+3, 4+4) = max(6, 5, 8) =
# 8 。
#
#
# 给你一个长度为 偶数 n 的数组 nums ，请你将 nums 中的元素分成 n / 2 个数对，使得：
#
#
# nums 中每个元素 恰好 在 一个 数对中，且
# 最大数对和 的值 最小 。
#
#
# 请你在最优数对划分的方案下，返回最小的 最大数对和 。
#
#
#
# 示例 1：
#
# 输入：nums = [3,5,2,3]
# 输出：7
# 解释：数组中的元素可以分为数对 (3,3) 和 (5,2) 。
# 最大数对和为 max(3+3, 5+2) = max(6, 7) = 7 。
#
#
# 示例 2：
#
# 输入：nums = [3,5,4,2,4,6]
# 输出：8
# 解释：数组中的元素可以分为数对 (3,5)，(4,4) 和 (6,2) 。
# 最大数对和为 max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8 。
#
#
#
#
# 提示：
#
#
# n == nums.length
# 2 <= n <= 10^5
# n 是 偶数 。
# 1 <= nums[i] <= 10^5
#
#
#
from typing import List
"""
方法一：排序 + 贪心
提示 1

数组内只有两个数的情况是平凡的。我们可以考虑数组中只有四个数
x_1 \le x_2 \le x_3 \le x_4 的情况。此时 (x_1, x_4), (x_2, x_3)
的拆分方法对应的最大数对和一定是最小的。

提示 1 解释

我们可以枚举所有的拆分方法。除了上文的拆分方法外还有两种拆分方法：

    (x_1, x_3), (x_2, x_4)

此时 x_2 + x_4 \ge x_1 + x_4 且 x_2 + x_4 \ge x_2 + x_3。
那么 \max(x_1+x_3,x_2+x_4) \ge x_2 + x_4 \ge \max(x_1+x_4,x_2+x_3)。

    (x_1, x_2), (x_3, x_4)

同样地，\max(x_1+x_2,x_3+x_4) \ge x_3 + x_4 \ge \max(x_1+x_4,x_2+x_3)。

提示 2

对于 n 个数（n 为偶数）的情况，上述的条件对应的拆分方法，即第 k 大与
第 k 小组成的 n / 2 个数对，同样可以使得最大数对和最小。

提示 2 解释

我们可以类似 提示 1 对所有数建立全序关系，即 x_1 \le \cdots \le x_n。
我们需要证明，任意的拆分方法得到的最大数对和一定大于等于给定的拆分方法
得到的最大数对和。

我们可以考虑上述命题的充分条件：假设给定拆分方法中的数对和 x_k + x_{n+1-k}
在 k = k' 时最大，那么对于任意的拆分方法，都存在一组 u, v 使得
x_u + x_v \ge x_{k'} + x_{n+1-k'}。

我们可以用反证法证明。

同样，我们假设 u < v，那么使得 x_v \ge x_{n+1-k'} 的 v 的取值一共有 k'种。
即闭区间 [n+1-k',n] 中的所有整数。对于这些 v 组成的数对，如果想使得
x_u + x_v < x_{k'} + x_{n+1-k'} 恒成立，必须要 x_u < x_{k'}。此时需要有
k' 个不同的 u 的取值，但只有闭区间 [1,k'-1] 中的 k'-1 个整数满足 x_u < x_{k'}
的条件，这就产生了矛盾。

因此，一定存在一组 u, v 使得 x_u + x_v \ge x_{k'} + x_{n+1-k'}。

思路与算法

根据 提示 2，我们需要将 nums 排序。排序后，我们遍历每一个第 k 大与第 k 小
组成的数对，计算它们的和，并维护这些和的最大值。同样根据 提示 2，遍历完成后
求得的最大数对和就是满足要求的最小值。
"""


# @lc code=start
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n // 2):
            ans = max(ans, nums[i] + nums[n - i - 1])
        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.minPairSum(nums=[3, 5, 2, 3]))
    print(solu.minPairSum(nums=[3, 5, 4, 2, 4, 6]))
