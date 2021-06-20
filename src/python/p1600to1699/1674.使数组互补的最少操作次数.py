#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1674.使数组互补的最少操作次数.py
@Time    :   2021/06/20 09:46:24
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1674 lang=python3
#
# [1674] 使数组互补的最少操作次数
#
# https://leetcode-cn.com/problems/minimum-moves-to-make-array-complementary/description/
#
# algorithms
# Medium (35.14%)
# Likes:    47
# Dislikes: 0
# Total Accepted:    2.2K
# Total Submissions: 6.3K
# Testcase Example:  '[1,2,4,3]\n4'
#
# 给你一个长度为 偶数 n 的整数数组 nums 和一个整数 limit 。每一次操作，你可以将 nums 中的任何整数替换为 1 到 limit
# 之间的另一个整数。
#
# 如果对于所有下标 i（下标从 0 开始），nums[i] + nums[n - 1 - i] 都等于同一个数，则数组 nums 是 互补的 。例如，数组
# [1,2,3,4] 是互补的，因为对于所有下标 i ，nums[i] + nums[n - 1 - i] = 5 。
#
# 返回使数组 互补 的 最少 操作次数。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,4,3], limit = 4
# 输出：1
# 解释：经过 1 次操作，你可以将数组 nums 变成 [1,2,2,3]（加粗元素是变更的数字）：
# nums[0] + nums[3] = 1 + 3 = 4.
# nums[1] + nums[2] = 2 + 2 = 4.
# nums[2] + nums[1] = 2 + 2 = 4.
# nums[3] + nums[0] = 3 + 1 = 4.
# 对于每个 i ，nums[i] + nums[n-1-i] = 4 ，所以 nums 是互补的。
#
#
# 示例 2：
#
#
# 输入：nums = [1,2,2,1], limit = 2
# 输出：2
# 解释：经过 2 次操作，你可以将数组 nums 变成 [2,2,2,2] 。你不能将任何数字变更为 3 ，因为 3 > limit 。
#
#
# 示例 3：
#
#
# 输入：nums = [1,2,1,2], limit = 2
# 输出：0
# 解释：nums 已经是互补的。
#
#
#
#
# 提示：
#
#
# n == nums.length
# 2 <= n <= 10^5
# 1 <= nums[i] <= limit <= 10^5
# n 是偶数。
#
#
#
from typing import List
"""
方法一：差分数组
我们考虑任意一个数对 (a,b)，不妨假设 a <= b。假设最终选定的和值为 target，
则我们可以发现，对于 (a,b) 这个数对：

- 当 target < 1+a 时，需要操作两次；
- 当 1+a <= target < a+b 时，需要操作一次；
- 当 target = a+b 时，不需要操作；
- 当 a+b < target <= b+l 时，需要操作一次；
- 当 target > b+limit 时，需要操作两次。

我们设初始操作次数为两次。令 target 从数轴最左端开始向右移动，我们会发现：

- 在 1+a 处，操作次数减少一次；
- 在 a+b 处，操作次数减少一次；
- 在 a+b+1 处，操作次数增加一次；
- 在 b+limit+1 处，操作次数增加一次。

因此，我们可以遍历数组中的所有数对，求出每个数对的这四个关键位置，然后更新
差分数组。最后，我们遍历（扫描）差分数组，就可以找到令总操作次数最小的
target，同时可以得到最少的操作次数。

时间复杂度O(N+L)。
空间复杂度O(L)。
"""


# @lc code=start
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        delta = [0] * (2 * limit + 2)
        for i in range(n // 2):
            lo = 1 + min(nums[i], nums[n - i - 1])
            hi = limit + max(nums[i], nums[n - i - 1])
            tot = nums[i] + nums[n - i - 1]
            delta[lo] -= 1
            delta[tot] -= 1
            delta[tot + 1] += 1
            delta[hi + 1] += 1

        ans = now = n
        for i in range(2, len(delta)):
            now += delta[i]
            ans = min(ans, now)

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.minMoves(nums=[1, 2, 4, 3], limit=4))
    print(solu.minMoves(nums=[1, 2, 2, 1], limit=2))
    print(solu.minMoves(nums=[1, 2, 1, 2], limit=2))
