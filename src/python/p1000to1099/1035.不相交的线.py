#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1035.不相交的线.py
@Time    :   2021/05/21 21:23:59
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1035 lang=python3
#
# [1035] 不相交的线
#
# https://leetcode-cn.com/problems/uncrossed-lines/description/
#
# algorithms
# Medium (60.90%)
# Likes:    191
# Dislikes: 0
# Total Accepted:    24.6K
# Total Submissions: 40.4K
# Testcase Example:  '[1,4,2]\n[1,2,4]'
#
# 在两条独立的水平线上按给定的顺序写下 nums1 和 nums2 中的整数。
#
# 现在，可以绘制一些连接两个数字 nums1[i] 和 nums2[j] 的直线，这些直线需要同时满足满足：
#
#
# nums1[i] == nums2[j]
# 且绘制的直线不与任何其他连线（非水平线）相交。
#
#
# 请注意，连线即使在端点也不能相交：每个数字只能属于一条连线。
#
# 以这种方法绘制线条，并返回可以绘制的最大连线数。
#
#
#
# 示例 1：
#
#
#
# 输入：nums1 = [1,4,2], nums2 = [1,2,4]
# 输出：2
# 解释：可以画出两条不交叉的线，如上图所示。
# 但无法画出第三条不相交的直线，因为从 nums1[1]=4 到 nums2[2]=4 的直线将与从 nums1[2]=2 到 nums2[1]=2
# 的直线相交。
#
#
#
# 示例 2：
#
#
# 输入：nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
# 输出：3
#
#
#
# 示例 3：
#
#
# 输入：nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
# 输出：2
#
#
#
#
#
# 提示：
#
#
# 1 <= nums1.length <= 500
# 1 <= nums2.length <= 500
# 1 <= nums1[i], nums2[i] <= 2000
#
#
#
#
#
from typing import List
"""
方法一：动态规划
给定两个数组 nums1 和 nums2，当 nums1[i] = nums2[j] 时，可以用一条直线
连接 nums1[i] 和 nums2[j]。假设一共绘制了 k 条互不相交的直线，其中第 x
条直线连接 nums1[ix] 和 nums2[jx]，则对于任意 1 <= x <= k 都有
nums1[ix] = nums2[jx]，其中 i1 < i2 < ... < ik, j1 < j2 < ... < jk。

上述 k 条互不相交的直线分别连接了数组 nums1 和 nums2 的 k 对相等的元素，
而且这 k 对相等的元素在两个数组中的相对顺序是一致的，因此，这 k 对相等的
元素组成的序列即为数组 nums1 和 nums2 的公共子序列。要计算可以绘制的最大
连线数，即为计算数组 nums1 和 nums2 的最长公共子序列的长度。最长公共子序列
问题是典型的二维动态规划问题。

假设数组 nums1 和 nums2 的长度分别为 m 和 n，创建 m+1 行 n+1 列的二维
数组 dp，其中 dp[i][j] 表示 nums1[0:i] 和 nums2[0:j] 的最长公共子序列
的长度。

上述表示中，nums1[0:i] 表示数组 nums1 的长度为 i 的前缀，nums2[0:j]
表示数组 nums2 的长度为 j 的前缀。

考虑动态规划的边界情况：

- 当 i=0 时，nums1[0:i] 为空，空数组和任何数组的最长公共子序列的长度都是
  0，因此对任意 0 <= j <= n，有 dp[0][j] = 0；
- 当 j=0 时，nums2[0:j] 为空，同理可得，对任意 0 <= i <= m，有
  dp[i][0] = 0。

因此动态规划的边界情况是：当 i=0 或 j=0 时，dp[i][j] = 0。

当 i>0 且 j>0 时，考虑 dp[i][j] 的计算：
- 当 nums1[i-1] = nums2[j-1] 时，将这两个相同的元素称为公共元素，考虑
  nums1[0:i-1] 和 nums2[0:j-1] 的最长公共子序列，再增加一个元素（即公共
  元素）即可得到 nums1[0:i] 和 nums2[0:j] 的最长公共子序列，因此
  dp[i][j] = dp[i-1][j-1] + 1。
- 当 nums1[i-1] != nums2[j-1] 时，考虑以下两项：
  - nums1[0:i-1] 和 nums2[0:j] 的最长公共子序列；
  - nums1[0:i] 和 nums2[0:j-1] 的最长公共子序列。

要得到 nums1[0:i] 和 nums2[0:j] 的最长公共子序列，应取两项中的长度较大
的一项，因此 dp[i][j] = max(dp[i-1][j], dp[i][j-1])。

由此可以得到如下状态转移方程：

  dp[i][j] = dp[i-1][j-1] + 1,  nums1[i-1] = nums2[j-1]
  dp[i][j] = max(dp[i-1][j], dp[i][j-1]),  nums1[i-1] != nums2[j-1]

最终计算得到 dp[m][n] 即为数组 nums1 和 nums2 的最长公共子序列的长度，
即可以绘制的最大连线数。
"""


# @lc code=start
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        f = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + 1
                else:
                    f[i][j] = max(f[i - 1][j], f[i][j - 1])

        return f[m][n]


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.maxUncrossedLines(nums1=[1, 4, 2], nums2=[1, 2, 4]))

    nums1 = [2, 5, 1, 2, 5]
    nums2 = [10, 5, 2, 1, 5, 2]
    print(solu.maxUncrossedLines(nums1, nums2))

    nums1 = [1, 3, 7, 1, 7, 5]
    nums2 = [1, 9, 2, 5, 1]
    print(solu.maxUncrossedLines(nums1, nums2))
