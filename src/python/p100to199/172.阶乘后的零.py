#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   172.阶乘后的零.py
@Time    :   2020/09/26 19:28:32
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#
# https://leetcode-cn.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Easy (39.99%)
# Likes:    356
# Dislikes: 0
# Total Accepted:    49.5K
# Total Submissions: 123.6K
# Testcase Example:  '3'
#
# 给定一个整数 n，返回 n! 结果尾数中零的数量。
#
# 示例 1:
#
# 输入: 3
# 输出: 0
# 解释: 3! = 6, 尾数中没有零。
#
# 示例 2:
#
# 输入: 5
# 输出: 1
# 解释: 5! = 120, 尾数中有 1 个零.
#
# 说明: 你算法的时间复杂度应为 O(log n) 。
#
#
"""
首先末尾有多少个 0，只需要给当前数乘以一个 10 就可以加一个 0。

具体地，对于 5!，也就是 5 * 4 * 3 * 2 * 1 = 120，我们发现结果会有一个 0，
原因就是 2 和 5 相乘构成了一个 10。而对于 10 的话，其实也只有 2 * 5 可以
构成，所以我们只需要找有多少对 2/5。

我们把每个乘数再稍微分解下，看一个例子。

11! = 11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
    = 11 * (2 * 5) * 9 * (4 * 2) * 7 * (3 * 2) * (1 * 5) * (2 * 2)
         * 3 * (1 * 2) * 1

对于含有 2 的因子的话是 1 * 2, 2 * 2, 3 * 2, 4 * 2 ...

对于含有 5 的因子的话是 1 * 5, 2 * 5...

含有 2 的因子每两个出现一次，含有 5 的因子每 5 个出现一次，所有 2 出现的
个数远远多于 5，换言之找到一个 5，一定能找到一个 2 与之配对。所以我们只需
找有多少个 5。

对于一个数的阶乘，就如之前分析的，5 的因子一定是每隔 5 个数出现一次，也就是
下边的样子。

n! = 1 * 2 * 3 * 4 * (1 * 5) * ... * (2 * 5) * ... * (3 * 5) *... * n

因为每隔 5 个数出现一个 5，所以计算出现了多少个 5，我们只需要用 n/5 就可以
算出来。但还没有结束，继续分析。

1 * ... * (1 * 5) * ... * (1 * 5 * 5) * ... * (2 * 5 * 5) * ...
  * (3 * 5 * 5) * ... * n

每隔 25 个数字，出现的是两个 5，所以除了每隔 5 个数算作一个 5，每隔 25 个数，
还需要多算一个 5。也就是我们需要再加上 n / 25 个 5。

同理我们还会发现每隔 5 * 5 * 5 = 125 个数字，会出现 3 个 5，所以我们还需要
再加上 n / 125 。

综上，规律就是每隔 5 个数，出现一个 5，每隔 25 个数，出现 2 个 5，每隔 125
个数，出现 3 个 5 ... 以此类推。

最终 5 的个数就是 n / 5 + n / 25 + n / 125 ...

写程序的话，如果直接按照上边的式子计算，分母可能会造成溢出。所以算 n / 25
的时候，我们先把 n 更新，n = n / 5，然后再计算 n / 5 即可。后边的同理。
"""


# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n > 0:
            n //= 5
            ans += n
        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.trailingZeroes(3))
    print(solu.trailingZeroes(5))
    print(solu.trailingZeroes(8))
