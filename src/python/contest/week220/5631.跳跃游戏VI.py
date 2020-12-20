#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5631.跳跃游戏VI.py
@Time    :   2020/12/20 11:04:36
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
动态规划 + 单调队列优化

State:
  f[i]: 表示从 nums[0] 跳到 nums[i] 的最大得分

State Transition:
  f[i] = max(f[i-k], ..., f[i-1]) + nums[i]


对于 j1 < j2，如果 f[j1] <= f[j2]，那么在 i > j 之后，j1 将永远不可能
作为状态转移方程中最优的 j。这是因为 f[j2] 不劣于 f[j1]，并且 j2 的下标
更大，满足限制的最远位置也大于 j1，因此无论什么时候从 j1 转移都不会比从
j2转移要优，因此我们可以将 j1 从候选的 j 值集合中永远的移除。

基于这个思路，我们可以使用一个严格单调递减的队列存储所有的候选 j 值集合，
这里严格单调递减的意思是：从队首到队尾的所有 j 值，它们的下标严格单调递增，
而对应的 f[j] 值严格单调递减。这样一来，当我们枚举到 i 时，队首的 j 就是
我们的最优转移。与优先队列类似，此时队首的 j 可能已经不满足限制，因此我们
需要不断弹出队首元素，直到其满足限制为止。在转移完成之后，i 就是我们未来
的一个候选 j 值，因此我们将 i 加入队尾，并且不断弹出队尾元素，直到队列为
空或者队尾的 j 值满足 f[j] > f[i]。
"""
from collections import deque
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [0] * n
        f[0] = nums[0]
        q = deque([0])

        for i in range(1, n):
            while q[0] + k < i:
                q.popleft()
            f[i] = f[q[0]] + nums[i]
            while q and f[i] >= f[q[-1]]:
                q.pop()
            q.append(i)

        return f[n - 1]


if __name__ == "__main__":
    solu = Solution()
    print(solu.maxResult([1, -1, -2, 4, -7, 3], 2))
    print(solu.maxResult([10, -5, -2, 4, 0, 3], 3))
    print(solu.maxResult([1, -5, -20, 4, -1, 3, -6, -3], 2))
