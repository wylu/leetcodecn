#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1723.完成所有工作的最短时间.py
@Time    :   2021/05/08 21:44:43
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1723 lang=python3
#
# [1723] 完成所有工作的最短时间
#
# https://leetcode-cn.com/problems/find-minimum-time-to-finish-all-jobs/description/
#
# algorithms
# Hard (49.16%)
# Likes:    183
# Dislikes: 0
# Total Accepted:    15.8K
# Total Submissions: 32.1K
# Testcase Example:  '[3,2,3]\n3'
#
# 给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。
#
# 请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。工人的 工作时间
# 是完成分配给他们的所有工作花费时间的总和。请你设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。
#
# 返回分配方案中尽可能 最小 的 最大工作时间 。
#
#
#
# 示例 1：
#
#
# 输入：jobs = [3,2,3], k = 3
# 输出：3
# 解释：给每位工人分配一项工作，最大工作时间是 3 。
#
#
# 示例 2：
#
#
# 输入：jobs = [1,2,4,7,8], k = 2
# 输出：11
# 解释：按下述方式分配工作：
# 1 号工人：1、2、8（工作时间 = 1 + 2 + 8 = 11）
# 2 号工人：4、7（工作时间 = 4 + 7 = 11）S
# 最大工作时间是 11 。
#
#
#
# 提示：
#
#
# 1 <= k <= jobs.length <= 12
# 1 <= jobs[i] <= 10^7
#
#
#
from typing import List
"""
方法一：二分查找 + 回溯 + 剪枝
思路及算法

在本题中，我们很难直接计算出完成所有工作的最短时间。而注意到，当完成所有
工作的最短时间已经确定为 limit 时，如果存在可行的方案，那么对于任意长于
limit 的最短时间，都一定也存在可行的方案。因此我们可以考虑使用二分查找的
方法寻找最小的存在可行方案的 limit 值。

当完成所有工作的最短时间已经确定为 limit 时，我们可以利用回溯的方式来寻找
方案。

一个朴素的方案是，开辟一个大小为 k 的数组 workloads，workloads[i] 表示
第 i 个工人的当前已经被分配的工作量，然后我们利用一个递归函数 backtrack(i)
递归地枚举第 i 个任务的分配方案，过程中实时地更新 workloads 数组。具体地，
函数中我们检查每一个工人 j 当前已经被分配的工作量，如果被分配的工作量
workloads[j] 与当前工作的工作量 jobs[i] 之和不超过 limit 的限制，我们
即可以将该工作分配给工人 j，然后计算下一个工作 jobs[i+1] 的分配方案。过程
中一旦我们找到了一个可行方案，我们即可以返回 true，而无需枚举完所有的方案。

朴素的方案中，backtrack 函数的效率可能十分低下，有可能需要枚举完所有的
分配方案才能得到答案，因此我们提出几个优化措施：

1.缩小二分查找的上下限，下限为所有工作中的最大工作量，上限为所有工作的
工作量之和。
  1.1.每一个工作都必须被分配，因此必然有一个工人承接了工作量最大的工作；
  1.2.在最坏情况下，只有一个工人，他必须承接所有工作。

2.优先分配工作量大的工作。
  2.1.感性地理解，如果要求将小石子和大石块放入玻璃瓶中，优先放入大石块
  更容易使得工作变得简单。
  2.2.在搜索过程中，优先分配工作量小的工作会使得工作量大的工作更有可能
  最后无法被分配。

3.当工人 i 还没被分配工作时，我们不给工人 i+1 分配工作。
  3.1.如果当前工人 i 和 i+1 都没有被分配工作，那么我们将工作先分配给任何
  一个人都没有区别，如果分配给工人 i 不能成功完成分配任务，那么分配给工人
  i+1 也一样无法完成。

4.当我们将工作 i 分配给工人 j，使得工人 j 的工作量恰好达到 limit，且计算
分配下一个工作的递归函数返回了 false，此时即无需尝试将工作 i 分配给其他
工人，直接返回 false 即可。
  4.1.常规逻辑下，递归函数返回了 false，那么我们需要尝试将工作 i 分配给
  其他工人，假设分配给了工人 j'，那么此时工人 j' 的工作量必定不多于工人
  j 的工作量；
  4.2.如果存在一个方案使得分配给工人 j' 能够成功完成分配任务，那么此时
  必然有一个或一组工作 i' 取代了工作 i 被分配给工人 j，否则我们可以直接
  将工作 i 移交给工人 j，仍然能成功完成分配任务。而我们知道工作 i' 的总
  工作量不会超过工作 i，因此我们可以直接交换工作 i 与工作 i'，仍然能成功
  完成分配任务。这与假设不符，可知不存在这样一个满足条件的工人 j'。

方法二：动态规划 + 状态压缩
思路及算法

按照朴素的思路，我们按顺序给每一个工人安排工作，注意到当我们给第 i 个工人
分配工作的时候，能够选择的分配方案仅和前 i-1 个人被分配的工作有关。因此
我们考虑使用动态规划解决本题，只需要记录已经被分配了工作的工人数量，以及
已经被分配的工作是哪些即可。

因为工作数量较少，我们可以使用状态压缩的方式来表示已经被分配的工作是哪些。
具体地，假设有 n 个工作需要被分配，我们就使用一个 n 位的二进制整数来表示
哪些工作已经被分配，哪些工作尚未被分配，如果该二进制整数的第 i 位为 1，
那么第 i 个工作已经被分配，否则第 i 个工作尚未被分配。如有 3 个工作需要
被分配，那么 5=(101) 即代表 第 0 和第 2 个工作已经被分配，第 1 个工作
还未被分配。

这样我们可以写出状态方程：f[i][j] 表示给前 i 个人分配工作，工作的分配情况
为 j 时，完成所有工作的最短时间。注意这里的 j 是一个二进制整数，表示了工作
的分配情况。实际上我们也可以将 j 看作一个集合，包含了已经被分配的工作。

那么我们可以写出状态转移方程：

  f[i][j] = min{j'∈j} max(f[i-1][C{j}j'], sum[j'])}

式中 sum[j'] 表示集合 j' 中的工作的总工作量，C{j}j' 表示集合 j 中子集 j'
的补集。状态转移方程的含义为，我们枚举 j 的每一个子集 j'，让其作为分配给
工人 i 的工作，这样我们需要给前 i-1 个人分配 C{j}j' 的工作。

在实际代码中，我们首先预处理出 sum 数组，然后初始化 f[0][j] = sum[j]，
最终答案即为 f[k-1][2^n-1]（表示给全部 k 个工人分配全部 n 个工作，完成
所有工作的最短时间）。
"""


# @lc code=start
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)

        def dfs(workloads: List[int], idx: int, limit: int) -> bool:
            if idx == n:
                return True

            cur = jobs[idx]
            for i in range(k):
                if workloads[i] + cur <= limit:
                    workloads[i] += cur
                    if dfs(workloads, idx + 1, limit):
                        return True
                    workloads[i] -= cur

                # 如果当前工人未被分配工作，那么下一个工人也必然未被分配工作
                # 或者当前工作恰能使该工人的工作量达到了上限
                # 这两种情况下我们无需尝试继续分配工作
                if workloads[i] == 0 or workloads[i] + cur == limit:
                    break

            return False

        def check(limit: int) -> bool:
            return dfs([0] * k, 0, limit)

        jobs.sort()
        left, right = jobs[0], sum(jobs)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.minimumTimeRequired(jobs=[3, 2, 3], k=3))
    print(solu.minimumTimeRequired(jobs=[1, 2, 4, 7, 8], k=2))

    jobs = [
        20010, 20006, 20014, 20004, 20008, 20006, 20005, 20012, 19999, 20014,
        20003, 20012
    ]
    print(solu.minimumTimeRequired(jobs, k=8))
