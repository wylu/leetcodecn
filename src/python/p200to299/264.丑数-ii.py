#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   264.丑数-ii.py
@Time    :   2021/04/11 12:15:55
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#
# https://leetcode-cn.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (55.60%)
# Likes:    556
# Dislikes: 0
# Total Accepted:    59.5K
# Total Submissions: 105.9K
# Testcase Example:  '10'
#
# 给你一个整数 n ，请你找出并返回第 n 个 丑数 。
#
# 丑数 就是只包含质因数 2、3 和/或 5 的正整数。
#
#
#
# 示例 1：
#
#
# 输入：n = 10
# 输出：12
# 解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
#
#
# 示例 2：
#
#
# 输入：n = 1
# 输出：1
# 解释：1 通常被视为丑数。
#
#
#
#
# 提示：
#
#
# 1 <= n <= 1690
#
#
#
"""
思路：

用空间换时间，创建一个数组，保存排好序的丑数，利用已得到的丑数计算出
下一个丑数，并将新的丑数加到数组尾部。

利用已得有序丑数计算下一个丑数的思路：

每一个丑数都是前面的丑数乘以 2、3 或者 5 得到的（除 1 以外）。

  - 假设已有最大的丑数记为 M
  - T2 代表着数组的某个丑数的下标，这个丑数满足 arr[T2]∗2>M，同时若有
    任意小于 arr[T2] 的丑数 arr[T]，则 T 满足 arr[T]∗2≤M，T3、T5 的
    含义与 T2 类似
  - M2=arr[T2]∗2，M3=arr[T3]∗3，M5=arr[T5]∗5，则下一个丑数为
    M′=min(M2,M3,M5)
  - 每次计算完下一个丑数 M′，及时更新 T2、T3、T5
"""


# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [1]
        t2 = t3 = t5 = 0
        for _ in range(1, n):
            cur = min(ans[t2] * 2, ans[t3] * 3, ans[t5] * 5)
            if cur % 2 == 0:
                t2 += 1
            if cur % 3 == 0:
                t3 += 1
            if cur % 5 == 0:
                t5 += 1
            ans.append(cur)
        return ans[-1]


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.nthUglyNumber(10))
    print(solu.nthUglyNumber(1))
    print(solu.nthUglyNumber(1690))
