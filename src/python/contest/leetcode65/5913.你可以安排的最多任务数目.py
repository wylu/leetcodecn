#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5913.你可以安排的最多任务数目.py
@Time    :   2021/11/14 09:47:07
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :

方法一：二分答案+贪心

本题显然具有决策单调性：如果能安排 K 个任务，一定能安排 K-1 个任务；
如果不能安排 K 个任务，一定不能安排 K+1 个任务，因此可以二分答案。

现在考虑安排 K 个任务。显然，我们应该选择最容易的 K 个任务，同时选择
最强的 K 个人。

我们从难到易来考虑这 K 个任务。

一种贪心策略是：

- 如果有人能完成当前任务，我们就安排其中能力值最小的那个人去做这一任务。
- 如果没有人能完成当前任务，但当前有药，并且有人能在服药后完成这一任务，
  我们就安排其中能力值最小的那个人去做这一任务。
- 否则说明无法完成 K 个任务。

另一种贪心策略是：

- 如果当前有药，我们就安排服药后能够完成任务的人中能力值最小的那个人去做这一任务。
- 如果当前没有药，我们就安排能完成任务的人中能力值最小的那个人去做这一任务。
- 否则说明无法完成 K 个任务。

这两种贪心策略都是正确的。我们可以这样考虑：在有药丸的情况下，可能会存在
A 服药能完成任务，B 不服药也能完成任务这样的情形。此时我们应该选择谁呢？
实际上，因为后面的任务只会更简单，所以 A+药 或 B 都一定能完成后面的任务，
因此此时使用 A+药 或使用 B 其实对后面的任务没有影响。

时间复杂度 O(N*(logN)^2)。
空间复杂度 O(N)。
"""
from typing import List

from sortedcontainers import SortedList


class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int,
                      strength: int) -> int:
        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()

        def check(k: int) -> bool:
            if k > m:
                return False

            rem = pills
            sl = SortedList(workers[-k:])  # type: SortedList
            for i in range(k - 1, -1, -1):
                idx = sl.bisect_left(tasks[i])
                if idx == len(sl):
                    if rem == 0:
                        return False
                    idx = sl.bisect_left(tasks[i] - strength)
                    if idx == k:
                        return False
                    rem -= 1
                    sl.discard(sl[idx])
                else:
                    sl.discard(sl[idx])

            return True

        left, right = 0, n
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1

        return left


if __name__ == '__main__':
    solu = Solution()
    tasks = [3, 2, 1]
    workers = [0, 3, 3]
    pills = 1
    strength = 1
    print(solu.maxTaskAssign(tasks, workers, pills, strength))

    tasks = [5, 4]
    workers = [0, 0, 0]
    pills = 1
    strength = 5
    print(solu.maxTaskAssign(tasks, workers, pills, strength))

    tasks = [10, 15, 30]
    workers = [0, 10, 10, 10, 10]
    pills = 3
    strength = 10
    print(solu.maxTaskAssign(tasks, workers, pills, strength))

    tasks = [5, 9, 8, 5, 9]
    workers = [1, 6, 4, 2, 6]
    pills = 1
    strength = 5
    print(solu.maxTaskAssign(tasks, workers, pills, strength))
