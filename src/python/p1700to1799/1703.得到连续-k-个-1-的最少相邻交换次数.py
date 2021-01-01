#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1703.得到连续-k-个-1-的最少相邻交换次数.py
@Time    :   2021/01/01 11:13:44
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1703 lang=python3
#
# [1703] 得到连续 K 个 1 的最少相邻交换次数
#
# https://leetcode-cn.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/description/
#
# algorithms
# Hard (36.96%)
# Likes:    8
# Dislikes: 0
# Total Accepted:    567
# Total Submissions: 1.5K
# Testcase Example:  '[1,0,0,1,0,1]\n2'
#
# 给你一个整数数组 nums 和一个整数 k 。 nums 仅包含 0 和 1 。每一次移动，你可以选择 相邻 两个数字并将它们交换。
#
# 请你返回使 nums 中包含 k 个 连续 1 的 最少 交换次数。
#
#
#
# 示例 1：
#
# 输入：nums = [1,0,0,1,0,1], k = 2
# 输出：1
# 解释：在第一次操作时，nums 可以变成 [1,0,0,0,1,1] 得到连续两个 1 。
#
#
# 示例 2：
#
# 输入：nums = [1,0,0,0,0,0,1,1], k = 3
# 输出：5
# 解释：通过 5 次操作，最左边的 1 可以移到右边直到 nums 变为 [0,0,0,0,0,1,1,1] 。
#
#
# 示例 3：
#
# 输入：nums = [1,1,0,1], k = 2
# 输出：0
# 解释：nums 已经有连续 2 个 1 了。
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# nums[i] 要么是 0 ，要么是 1 。
# 1 <= k <= sum(nums)
#
#
#
from typing import List
"""
题目求的是最少的交换次数，如果交换 1 和 1 或者 0 和 0 是没有任何意义的，
只会增加交换次数，所以我们只考虑1和0的交换。

也就是我们只需要交换其它的 1 到某一个位置，构成一段长度为 k 下标连续的 1
即可，这样就说明 1 的相对顺序一定是不变的。我们只需记录下数字 1 的下标，
假设为 a1, a2, a3 ...  an

问题就转换为：需要把连续的 k 个 ai, 交换到一起的最小交换次数？

假设 k 个 a 为：a1, a2 ... ak, 也就是需要把这 k 个 a，交换变成公差为
1 的等差数列。

-->  假设移动到 x, x+1, ... , x+k-1

那么步数就是 |a1-x| + |a2-(x+1)| + ... + |ak-(x+k-1)|       公式1

也就是求 x，使得上述绝对值的和最小，也即求上述点到一个公差为 1 等差数列
的距离的最小值。

可以联系到货仓选址(https://www.acwing.com/problem/content/106/)的
结论，所有点到一个点的绝对值的和的最小值，x 等于中位数。

但是这个是等差数列，所以需要做一下映射，令 ai` = ai - (i - 1)，则：
a1` = a1
a2` = a2 - 1
a3` = a3 - 2
...
ak` = ak - (k - 1)

代入公式 1 也就变成：|a1`-x| + |a2`-x| + ... + |ak`-x|      公式2

公式 2 的最小值就是当 x 取 a1`,a2`, ... ak`的中位数，求出来的和就是
最小值, 就是所求之和。

还有一个问题，我们是每次求连续 k 个 ai 的和的最小值, 需要快速的求
每个数与中位数的差的绝对值的和。假设其它 k 个 a 为：a[l], a[l+1], ... a[r],
中位数是 a[mid]，其中 mid = l + r >> 1;

mid左边的和：a[mid] - a[l] + a[mid] - a[l+1] + ... + a[mid] - a[mid - 1]
              = a[mid] * (mid - l) - (a[l] + a[l + 1] + ... + a[mid - 1])
              = a[mid] * (mid - l) - (sum[mid - 1] - sum[l - 1])  前缀和

mid右边的和：a[r] - a[mid] + a[r - 1] - a[mid] + ... + a[mid + 1] - a[mid]
              = sum[r] - sum[mid]  - (r - mid ) * a[mid]

需要预处理下前缀和
"""


# @lc code=start
class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        n = len(nums)

        a, m = [], 0
        for i in range(n):
            if nums[i] == 1:
                a.append(i - m)
                m += 1

        ps = [0] * (m + 1)
        for i in range(m):
            ps[i + 1] = ps[i] + a[i]

        ans = 0x7FFFFFFF
        for i in range(m - k + 1):
            j = i + k - 1
            mid = (i + j) >> 1
            left = a[mid] * (mid - i) - (ps[mid] - ps[i])
            right = ps[j + 1] - ps[mid + 1] - a[mid] * (j - mid)
            ans = min(ans, left + right)

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.minMoves([1, 0, 0, 1, 0, 1], 2))
    print(solu.minMoves([1, 0, 0, 0, 0, 0, 1, 1], 3))
    print(solu.minMoves([1, 1, 0, 1], 2))
