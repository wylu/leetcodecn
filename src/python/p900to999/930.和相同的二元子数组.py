#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   930.和相同的二元子数组.py
@Time    :   2020/09/23 08:57:30
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=930 lang=python3
#
# [930] 和相同的二元子数组
#
# https://leetcode-cn.com/problems/binary-subarrays-with-sum/description/
#
# algorithms
# Medium (37.74%)
# Likes:    60
# Dislikes: 0
# Total Accepted:    4.3K
# Total Submissions: 11.4K
# Testcase Example:  '[1,0,1,0,1]\n2'
#
# 在由若干 0 和 1  组成的数组 A 中，有多少个和为 S 的非空子数组。
#
#
#
# 示例：
#
# 输入：A = [1,0,1,0,1], S = 2
# 输出：4
# 解释：
# 如下面黑体所示，有 4 个满足题目要求的子数组：
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
#
#
#
#
# 提示：
#
#
# A.length <= 30000
# 0 <= S <= A.length
# A[i] 为 0 或 1
#
#
#
from typing import List
"""
前缀和 + 哈希表优化
"""


# @lc code=start
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        n = len(A)
        ps = [0] * (n + 1)
        for i in range(n):
            ps[i + 1] = ps[i] + A[i]

        ans, mp = 0, {0: 1}
        for i in range(n):
            ans += mp.get(ps[i + 1] - S, 0)
            mp[ps[i + 1]] = mp.get(ps[i + 1], 0) + 1

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.numSubarraysWithSum([1, 0, 1, 0, 1], 2))
