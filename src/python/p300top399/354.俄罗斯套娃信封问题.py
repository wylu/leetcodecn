#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   354.俄罗斯套娃信封问题.py
@Time    :   2021/03/04 22:42:42
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#
# https://leetcode-cn.com/problems/russian-doll-envelopes/description/
#
# algorithms
# Hard (42.17%)
# Likes:    437
# Dislikes: 0
# Total Accepted:    45.3K
# Total Submissions: 107.4K
# Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
#
# 给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。
#
# 当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
#
# 请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
#
# 注意：不允许旋转信封。
#
#
# 示例 1：
#
#
# 输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
# 输出：3
# 解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
#
# 示例 2：
#
#
# 输入：envelopes = [[1,1],[1,1],[1,1]]
# 输出：1
#
#
#
#
# 提示：
#
#
# 1 <= envelopes.length <= 5000
# envelopes[i].length == 2
# 1 <= wi, hi <= 10^4
#
#
#
import bisect
from typing import List
"""
前言
根据题目的要求，如果我们选择了 k 个信封，它们的的宽度依次为 w[0],w[1],...,w[k-1]，
高度依次为 h[0],h[1],...,h[k-1]，那么需要满足：

  w[0] < w[1] < ... < w[k-1]
  h[0] < h[1] < ... < h[k-1]

同时控制 w 和 h 两个维度并不是那么容易，因此我们考虑固定一个维度，再在另一个维度上
进行选择。例如，我们固定 w 维度，那么我们将数组 envelopes 中的所有信封按照 w 升序
排序。这样一来，我们只要按照信封在数组中的出现顺序依次进行选取，就一定保证满足：

  w[0] <= w[1] <= ... <= w[k-1]

了。然而小于等于 <= 和小于 < 还是有区别的，但我们不妨首先考虑一个简化版本的问题：

如果我们保证所有信封的 w 值互不相同，那么我们可以设计出一种得到答案的方法吗？

在 w 值互不相同的前提下，小于等于 <= 和小于 < 是等价的，那么我们在排序后，就可以
完全忽略 w 维度，只需要考虑 h 维度了。此时，我们需要解决的问题即为：

给定一个序列，我们需要找到一个最长的子序列，使得这个子序列中的元素严格单调递增，
即上面要求的：

  h[0] < h[1] < ... < h[k-1]

那么这个问题就是经典的「最长严格递增子序列」问题了，读者可以参考力扣平台的 300.
最长递增子序列 及其 官方题解。最长严格递增子序列的详细解决方法属于解决本题的前置
知识点，不是本文分析的重点，因此这里不再赘述，会在方法一和方法二中简单提及。

当我们解决了简化版本的问题之后，我们来想一想使用上面的方法解决原问题，会产生什么
错误。当 w 值相同时，如果我们不规定 h 值的排序顺序，那么可能会有如下的情况：

排完序的结果为 [(w, h)] = [(1, 1), (1, 2), (1, 3), (1, 4)]，由于这些信封的
w 值都相同，不存在一个信封可以装下另一个信封，那么我们只能在其中选择 1 个信封。
然而如果我们完全忽略 w 维度，剩下的 h 维度为 [1, 2, 3, 4]，这是一个严格递增
的序列，那么我们就可以选择所有的 4 个信封了，这就产生了错误。

因此，我们必须要保证对于每一种 w 值，我们最多只能选择 1 个信封。

我们可以将 h 值作为排序的第二关键字进行降序排序，这样一来，对于每一种 w 值，
其对应的信封在排序后的数组中是按照 h 值递减的顺序出现的，那么这些 h 值不可能组成
长度超过 1 的严格递增的序列，这就从根本上杜绝了错误的出现。

因此我们就可以得到解决本题需要的方法：

首先我们将所有的信封按照 w 值第一关键字升序、h 值第二关键字降序进行排序；
随后我们就可以忽略 w 维度，求出 h 维度的最长严格递增子序列，其长度即为答案。

下面简单提及两种计算最长严格递增子序列的方法，更详细的请参考上文提到的题目以及
对应的官方题解。


方法一：动态规划
思路与算法

设 f[i] 表示 h 的前 i 个元素可以组成的最长严格递增子序列的长度，并且我们必须
选择第 i 个元素 hi。在进行状态转移时，我们可以考虑倒数第二个选择的元素 hj，
必须满足 hj < hi 且 j < i，因此可以写出状态转移方程：

  f[i] = max{f[j]} + 1, j < i && hj < hi

如果不存在比 hi 小的元素 hj，那么 f[i] 的值为 1，即只选择了唯一的第 i 个元素。

在计算完所有的 f 值之后，其中的最大值即为最长严格递增子序列的长度。


方法二：基于二分查找的动态规划
思路与算法

设 f[j] 表示 h 的前 i 个元素可以组成的长度为 j 的最长严格递增子序列的末尾元素
的最小值，如果不存在长度为 j 的最长严格递增子序列，对应的 f 值无定义。在定义
范围内，可以看出 f 值是严格单调递增的，因为越长的子序列的末尾元素显然越大。

在进行状态转移时，我们考虑当前的元素 hi：

  如果 hi 大于 f 中的最大值，那么 hi 就可以接在 f 中的最大值之后，形成一个长度
  更长的严格递增子序列；

  否则我们找出 f 中比 hi 严格小的最大的元素 f[j0]，即 f[j0] < hi <= f[j0+1]，
  那么 hi 可以接在 f[j0] 之后，形成一个长度为 j0+1 的严格递增子序列，因此需要
  对 f[j_0+1] 进行更新： f[j0+1] = hi。我们可以在 f 上进行二分查找，找出满足
  要求的 j0。

在遍历所有的 hi 之后，f 中最后一个有定义的元素的下标增加 1（下标从 0 开始）
即为最长严格递增子序列的长度。
"""


# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0

        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        f = [envelopes[0][1]]
        for i in range(1, n):
            if envelopes[i][1] > f[-1]:
                f.append(envelopes[i][1])
            else:
                idx = bisect.bisect_left(f, envelopes[i][1])
                f[idx] = envelopes[i][1]

        return len(f)


# @lc code=end

# class Solution:
#     def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
#         if not envelopes:
#             return 0

#         n = len(envelopes)
#         envelopes.sort(key=lambda x: (x[0], -x[1]))

#         f = [1] * n
#         for i in range(n):
#             for j in range(i):
#                 if envelopes[j][1] < envelopes[i][1]:
#                     f[i] = max(f[i], f[j] + 1)

#         return max(f)

if __name__ == "__main__":
    solu = Solution()
    envelopes = [[5, 4], [6, 5], [6, 7], [2, 3]]
    print(solu.maxEnvelopes(envelopes))

    envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    print(solu.maxEnvelopes(envelopes))

    envelopes = [[1, 1], [1, 1], [1, 1]]
    print(solu.maxEnvelopes(envelopes))

    envelopes = []
    print(solu.maxEnvelopes(envelopes))
