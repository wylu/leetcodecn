#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   60.第k个排列.py
@Time    :   2020/09/05 18:29:24
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#
# https://leetcode-cn.com/problems/permutation-sequence/description/
#
# algorithms
# Medium (50.56%)
# Likes:    359
# Dislikes: 0
# Total Accepted:    55.7K
# Total Submissions: 110.2K
# Testcase Example:  '3\n3'
#
# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
#
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
#
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
#
#
# 给定 n 和 k，返回第 k 个排列。
#
# 说明：
#
#
# 给定 n 的范围是 [1, 9]。
# 给定 k 的范围是[1,  n!]。
#
#
# 示例 1:
#
# 输入: n = 3, k = 3
# 输出: "213"
#
#
# 示例 2:
#
# 输入: n = 4, k = 9
# 输出: "2314"
#
#
#
"""
方法一：数学 + 缩小问题规模
思路

要想解决本题，首先需要了解一个简单的结论：
对于 n 个不同的元素（例如数 1, 2, ⋯, n），它们可以组成的排列总数目为 n!。

对于给定的 n 和 k，我们不妨从左往右确定第 k 个排列中的每一个位置上的元素
到底是什么。

我们首先确定排列中的首个元素 a1。根据上述的结论，我们可以知道：
  - 以 1 为 a1 的排列一共有 (n−1)! 个；
  - 以 2 为 a1 的排列一共有 (n−1)! 个；
  ...
  - 以 n 为 a1 的排列一共有 (n−1)! 个。

由于我们需要求出从小到大的第 k 个排列，因此：
  - 如果 k <= (n−1)!，我们就可以确定排列的首个元素为 1；
  - 如果 (n−1)! < k <= 2⋅(n−1)!，我们就可以确定排列的首个元素为 2；
  ...
  - 如果 (n−1)⋅(n−1)! < k <= n⋅(n−1)!，我们就可以确定排列的首个元素为 n。

因此，第 k 个排列的首个元素就是：
  a1 =  ⌊(k-1) / (n-1)!⌋ + 1

其中 ⌊x⌋ 表示将 x 向下取整。

当我们确定了 a1 后，如何使用相似的思路，确定下一个元素 a2 呢？实际上，
我们考虑以 a1 为首个元素的所有排列：
  - 以 [1,n]\a1 最小的元素为 a2 的排列一共有 (n−2)! 个；
  - 以 [1,n]\a1 次小的元素为 a2 的排列一共有 (n−2)! 个；
  ...
  - 以 [1,n]\a1 最大的元素为 a2 的排列一共有 (n−2)! 个；

其中 [1,n]\a1 表示包含 1, 2, ⋯, n 中除去 a1 以外元素的集合。这些排列
从编号 (a1−1)⋅(n−1)! 开始，到 a1⋅(n−1)! 结束，总计 (n−1)! 个，因此
第 k 个排列实际上就对应着这其中的第

  k' = (k−1) mod (n−1)! + 1

个排列。这样一来，我们就把原问题转化成了一个完全相同但规模减少 1 的子问题：

求 [1,n]\a1 这 n−1 个元素组成的排列中，第 k' 小的排列。

算法

设第 k 个排列为 a1, a2, ..., an，我们从左往右地确定每一个元素 ai。我们
用数组 valid 记录每一个元素是否被使用过。

我们从小到大枚举 i：
  - 我们已经使用过了 i−1 个元素，剩余 n−i+1 个元素未使用过，每一个元素
  作为 ai 都对应着 (n−i)! 个排列，总计 (n−i+1)! 个排列；
  - 因此在第 k 个排列中，ai 即为剩余未使用过的元素中第
  ⌊(k-1) / (n-i)!⌋ + 1 小的元素；
  - 在确定了 ai 后，这 n−i+1 个元素的第 k 个排列，就等于 ai 之后跟着剩余
  n−i 个元素的第 (k−1) mod (n−i)! + 1 个排列。

在实际的代码中，我们可以首先将 k 的值减少 1，这样可以减少运算，降低代码
出错的概率。对应上述的后两步，即为：
  - 因此在第 k 个排列中，ai 即为剩余未使用过的元素中第
  ⌊(k) / (n-i)!⌋ + 1 小的元素；
  - 在确定了 ai 后，这 n−i+1 个元素的第 k 个排列，就等于 ai 之后跟着剩余
  n−i 个元素的第 k mod (n−i)! 个排列。

实际上，这相当于我们将所有的排列从 0 开始进行编号。
"""


# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = [1]
        for i in range(1, n):
            fact.append(fact[-1] * i)

        k -= 1
        ans, valid = [], [1] * (n + 1)
        for i in range(1, n + 1):
            order = k // fact[n - i] + 1
            for j in range(1, n + 1):
                order -= valid[j]
                if order == 0:
                    ans.append(str(j))
                    valid[j] = 0
                    break
            k %= fact[n - i]

        return ''.join(ans)


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    # print(solu.getPermutation(3, 3))
    print(solu.getPermutation(3, 5))
    # print(solu.getPermutation(4, 9))
