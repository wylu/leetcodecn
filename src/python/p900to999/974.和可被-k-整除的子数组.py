#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   974.和可被-k-整除的子数组.py
@Time    :   2020/09/21 20:10:30
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=974 lang=python3
#
# [974] 和可被 K 整除的子数组
#
# https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/description/
#
# algorithms
# Medium (45.60%)
# Likes:    201
# Dislikes: 0
# Total Accepted:    24.6K
# Total Submissions: 53.9K
# Testcase Example:  '[4,5,0,-2,-3,1]\n5'
#
# 给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。
#
#
#
# 示例：
#
# 输入：A = [4,5,0,-2,-3,1], K = 5
# 输出：7
# 解释：
# 有 7 个子数组满足其元素之和可被 K = 5 整除：
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2,
# -3]
#
#
#
#
# 提示：
#
#
# 1 <= A.length <= 30000
# -10000 <= A[i] <= 10000
# 2 <= K <= 10000
#
#
#
from typing import List
"""
方法一：哈希表 + 逐一统计

思路和算法

通常，涉及连续子数组问题的时候，我们使用前缀和来解决。

我们令 P[i] = A[0] + A[1] + ... + A[i]。那么每个连续子数组的和 sum(i,j)
就可以写成 P[j] - P[i-1]（其中 0 < i < j）的形式。此时，判断子数组的和
能否被 K 整除就等价于判断 (P[j] − P[i−1]) mod K == 0，根据 同余定理，
只要 P[j] mod K == P[i-1] mod K，就可以保证上面的等式成立。

因此我们可以考虑对数组进行遍历，在遍历同时统计答案。当我们遍历到第 i 个
元素时，我们统计以 i 结尾的符合条件的子数组个数。我们可以维护一个以前缀和
模 K 的值为键，出现次数为值的哈希表 record，在遍历的同时进行更新。这样在
计算以 i 结尾的符合条件的子数组个数时，根据上面的分析，答案即为 [0..i-1]
中前缀和模 K 也为 P[i] mod K 的位置个数，即 record[P[i] mod K]。

最后的答案即为以每一个位置为数尾的符合条件的子数组个数之和。需要注意的
一个边界条件是，我们需要对哈希表初始化，记录 record[0] = 1，这样就考虑
了前缀和本身被 K 整除的情况。

注意：不同的语言负数取模的值不一定相同，有的语言为负数，对于这种情况需要
特殊处理。
"""


# @lc code=start
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        ans = 0
        cnts, tot = {0: 1}, 0
        for num in A:
            tot += num
            mod = tot % K
            ans += cnts.get(mod, 0)
            cnts[mod] = cnts.get(mod, 0) + 1
        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))
    print(solu.subarraysDivByK([5], 5))
