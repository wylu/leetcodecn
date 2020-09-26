#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   898.子数组按位或操作.py
@Time    :   2020/09/26 22:10:51
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=898 lang=python3
#
# [898] 子数组按位或操作
#
# https://leetcode-cn.com/problems/bitwise-ors-of-subarrays/description/
#
# algorithms
# Medium (29.66%)
# Likes:    67
# Dislikes: 0
# Total Accepted:    3.5K
# Total Submissions: 11.7K
# Testcase Example:  '[0]'
#
# 我们有一个非负整数数组 A。
#
# 对于每个（连续的）子数组 B = [A[i], A[i+1], ..., A[j]] （ i <= j），我们对 B 中的每个元素进行按位或操作，获得结果
# A[i] | A[i+1] | ... | A[j]。
#
# 返回可能结果的数量。 （多次出现的结果在最终答案中仅计算一次。）
#
#
#
# 示例 1：
#
# 输入：[0]
# 输出：1
# 解释：
# 只有一个可能的结果 0 。
#
#
# 示例 2：
#
# 输入：[1,1,2]
# 输出：3
# 解释：
# 可能的子数组为 [1]，[1]，[2]，[1, 1]，[1, 2]，[1, 1, 2]。
# 产生的结果为 1，1，2，1，3，3 。
# 有三个唯一值，所以答案是 3 。
#
#
# 示例 3：
#
# 输入：[1,2,4]
# 输出：6
# 解释：
# 可能的结果是 1，2，3，4，6，以及 7 。
#
#
#
#
# 提示：
#
#
# 1 <= A.length <= 50000
# 0 <= A[i] <= 10^9
#
#
#
from typing import List
"""
方法一：集合

分析

显然，最简单的方法就是枚举所有满足 i <= j 的 (i, j)，并计算出不同的
result(i, j) = A[i] | A[i + 1] | ... | A[j] 的数量。
由于 result(i, j + 1) = result(i, j) | A[j + 1]，因此我们可以在
O(N^2) 的时间复杂度计算出所有的 result(i, j)，其中 N 是数组 A 的长度。

我们尝试优化一下这种最简单的枚举方法。可以发现，对于固定的 j，
result(j, j), result(j - 1, j), result(j - 2), j, ..., result(1, j)
的值是单调不降的，因为将 result(k, j) 对 A[k - 1] 做按位或操作，得到的
结果 result(k - 1, j) 一定不会变小。并且，根据按位或操作的性质，如果把
result(k, j) 和 result(k - 1, j) 都用二进制表示，那么后者将前者二进制
表示中的若干个 0 变成了 1。

由于数组 A 中都是小于 10^9 的正整数，它们的二进制表示最多只有 32 位。
因此从 result(j, j) 开始到 result(1, j) 结束，最多只会有 32 个 0
变成了 1，也就是说，result(j, j), result(j - 1, j), result(j - 2),
j, ..., result(1, j) 中最多只有 32 个不同的数。这样我们就可以维护一个
集合，存储所有以 j 为结尾的 result 值。当结尾从 j 枚举到 j + 1 时，
我们将集合中的每个数对 A[j + 1] 做按位或操作，得到的新的 result 值也
不会超过 32 个。

算法

我们用一个集合 cur 存储以 j 为结尾的 result 值，即所有满足 i <= j 的
A[i] | ... | A[j] 的值。集合的大小不会超过 32。
"""


# @lc code=start
class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        ans = set()
        cur = {0}
        for x in A:
            cur = {x | y for y in cur} | {x}
            ans |= cur
        return len(ans)


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.subarrayBitwiseORs([0]))
    print(solu.subarrayBitwiseORs([1, 1, 2]))
    print(solu.subarrayBitwiseORs([1, 2, 4]))
