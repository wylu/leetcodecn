#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   992.k-个不同整数的子数组.py
@Time    :   2021/02/09 21:32:31
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=992 lang=python3
#
# [992] K 个不同整数的子数组
#
# https://leetcode-cn.com/problems/subarrays-with-k-different-integers/description/
#
# algorithms
# Hard (41.83%)
# Likes:    242
# Dislikes: 0
# Total Accepted:    16K
# Total Submissions: 38.4K
# Testcase Example:  '[1,2,1,2,3]\n2'
#
# 给定一个正整数数组 A，如果 A 的某个子数组中不同整数的个数恰好为 K，则称 A 的这个连续、不一定独立的子数组为好子数组。
#
# （例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。）
#
# 返回 A 中好子数组的数目。
#
#
#
# 示例 1：
#
# 输入：A = [1,2,1,2,3], K = 2
# 输出：7
# 解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2],
# [1,2,1,2].
#
#
# 示例 2：
#
# 输入：A = [1,2,1,3,4], K = 3
# 输出：3
# 解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].
#
#
#
#
# 提示：
#
#
# 1 <= A.length <= 20000
# 1 <= A[i] <= A.length
# 1 <= K <= A.length
#
#
#
from collections import defaultdict
from typing import List
"""
方法：双指针（滑动窗口）

把「恰好」改成「最多」就可以使用双指针一前一后交替向右的方法完成，这是因为
对于每一个确定的左边界，最多包含 K 种不同整数的右边界是唯一确定的，并且
在左边界向右移动的过程中，右边界或者在原来的地方，或者在原来地方的右边。

而「最多存在 K 个不同整数的子区间的个数」与「恰好存在 K 个不同整数的子区间
的个数」的差恰好等于「最多存在 K - 1 个不同整数的子区间的个数」。

因为原问题就转换成为求解「最多存在 K 个不同整数的子区间的个数」与 「最多
存在 K - 1 个不同整数的子区间的个数」，它们其实是一个问题。
"""


# @lc code=start
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def kMostDiff(k):
            n = len(A)
            freq = defaultdict(int)
            ans = left = right = cnt = 0

            while right < n:
                if freq[A[right]] == 0:
                    cnt += 1
                freq[A[right]] += 1
                right += 1

                while cnt > k:
                    freq[A[left]] -= 1
                    if freq[A[left]] == 0:
                        cnt -= 1
                    left += 1

                ans += right - left

            return ans

        return kMostDiff(K) - kMostDiff(K - 1)


# @lc code=end
