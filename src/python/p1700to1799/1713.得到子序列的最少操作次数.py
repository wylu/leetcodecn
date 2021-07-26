#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1713.得到子序列的最少操作次数.py
@Time    :   2021/07/26 22:28:15
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1713 lang=python3
#
# [1713] 得到子序列的最少操作次数
#
# https://leetcode-cn.com/problems/minimum-operations-to-make-a-subsequence/description/
#
# algorithms
# Hard (48.82%)
# Likes:    121
# Dislikes: 0
# Total Accepted:    11.5K
# Total Submissions: 23.7K
# Testcase Example:  '[5,1,3]\n[9,4,2,3,4]'
#
# 给你一个数组 target ，包含若干 互不相同 的整数，以及另一个整数数组 arr ，arr 可能 包含重复元素。
#
# 每一次操作中，你可以在 arr 的任意位置插入任一整数。比方说，如果 arr = [1,4,1,2] ，那么你可以在中间添加 3 得到
# [1,4,3,1,2] 。你可以在数组最开始或最后面添加整数。
#
# 请你返回 最少 操作次数，使得 target 成为 arr 的一个子序列。
#
# 一个数组的 子序列 指的是删除原数组的某些元素（可能一个元素都不删除），同时不改变其余元素的相对顺序得到的数组。比方说，[2,7,4] 是
# [4,2,3,7,2,1,4] 的子序列（加粗元素），但 [2,4,2] 不是子序列。
#
#
#
# 示例 1：
#
# 输入：target = [5,1,3], arr = [9,4,2,3,4]
# 输出：2
# 解释：你可以添加 5 和 1 ，使得 arr 变为 [5,9,4,1,2,3,4] ，target 为 arr 的子序列。
#
#
# 示例 2：
#
# 输入：target = [6,4,8,1,3,2], arr = [4,7,6,2,3,8,6,1]
# 输出：3
#
#
#
#
# 提示：
#
#
# 1 <= target.length, arr.length <= 10^5
# 1 <= target[i], arr[i] <= 10^9
# target 不包含任何重复元素。
#
#
#
import bisect
from typing import List
"""
方法一：贪心 + 二分查找
记数组 target 的长度为 n，数组 arr 的长度为 m。

根据题意，target 和 arr 这两个数组的公共子序列越长，需要添加的元素个数也就越少。
因此最少添加的元素个数为 n 减去两数组的最长公共子序列的长度。

求最长公共子序列是一个经典问题，读者可参考「1143. 最长公共子序列的官方题解」。
但是，这一做法的时间复杂度是 O(nm) 的，在本题的数据范围下无法承受，我们需要改变思路。

由于 target 的元素互不相同，我们可以用一个哈希表记录 target 的每个元素所处的下标，
并将 arr 中的元素映射到下标上，对于不存在于 target 中的元素，由于其必然不会在
最长公共子序列中，可将其忽略。

我们使用示例 2 来说明，将 arr 中的元素转换成该元素在 target 中的下标（去掉不在
target 中的元素 7），可以得到一个新数组

    arr' = [1,0,5,4,2,0,3]

若将 target 也做上述转换，这相当于将每个元素变为其下标，得

    target' = [0,1,2,3,4,5]

则求原数组的最长公共子序列等价于求上述转换后的两数组的最长公共子序列。

注意到 target' 是严格单调递增的，因此 arr' 在最长公共子序列中的部分也必须是严格
单调递增的，因此问题可进一步地转换成求 arr' 的最长递增子序列的长度。这也是一个
经典问题，读者可以参考「300. 最长递增子序列的官方题解」，使用贪心和二分查找的方法
得到最长递增子序列的长度。
"""


# @lc code=start
class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        n = len(target)
        pos = {num: i for i, num in enumerate(target)}

        d = []
        for num in arr:
            if num in pos:
                idx = pos[num]
                p = bisect.bisect_left(d, idx)
                if p != len(d):
                    d[p] = idx
                else:
                    d.append(idx)

        return n - len(d)


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.minOperations(target=[5, 1, 3], arr=[9, 4, 2, 3, 4]))

    target = [6, 4, 8, 1, 3, 2]
    arr = [4, 7, 6, 2, 3, 8, 6, 1]
    print(solu.minOperations(target, arr))
