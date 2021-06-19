#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   483.最小好进制.py
@Time    :   2021/06/18 15:05:36
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=483 lang=python3
#
# [483] 最小好进制
#
# https://leetcode-cn.com/problems/smallest-good-base/description/
#
# algorithms
# Hard (56.10%)
# Likes:    95
# Dislikes: 0
# Total Accepted:    8.5K
# Total Submissions: 15.1K
# Testcase Example:  '"13"'
#
# 对于给定的整数 n, 如果n的k（k>=2）进制数的所有数位全为1，则称 k（k>=2）是 n 的一个好进制。
#
# 以字符串的形式给出 n, 以字符串的形式返回 n 的最小好进制。
#
#
#
# 示例 1：
#
#
# 输入："13"
# 输出："3"
# 解释：13 的 3 进制是 111。
#
#
# 示例 2：
#
#
# 输入："4681"
# 输出："8"
# 解释：4681 的 8 进制是 11111。
#
#
# 示例 3：
#
#
# 输入："1000000000000000000"
# 输出："999999999999999999"
# 解释：1000000000000000000 的 999999999999999999 进制是 11。
#
#
#
#
# 提示：
#
#
# n的取值范围是 [3, 10^18]。
# 输入总是有效且没有前导 0。
#
#
#
#
#
import math
"""
方法一：数学
思路及解法

假设正整数 n 在 k (k >= 2) 进制下的所有数位都为 1，且位数为 m + 1，那么有：

    n = k^0 + k^1 + k^2 + ... + k^m    (1)

我们首先讨论两种特殊情况：

    m=0，此时 n=1，而题目保证 n >= 3，所以本题中 m > 0。
    m=1，此时 n=(11)k，即 k = n-1 >= 2，这保证了本题有解。

然后我们分别证明一般情况下的两个结论，以帮助解决本题。

结论一：m < logk(n)

注意到 (1) 式右侧是一个首项为 1、公比为 k 的等比数列，利用等比数列求和公式，
我们可以得到：

    n = (1 - k^{m+1}) / (1 - k)

对公式进行变换可得：

    k^{m+1} = kn - n + 1 < kn

移项并化简可得：

    m < logk(n)

这个结论帮助我们限制了 m 的范围，本题中 3 <= n <= 10^{18} 且 k >= 2，
所以 m < log2(10^{18}) < 60。

结论二：k = floor(sqrt[m]{n})

依据 (1) 式，可知：

    n = k^0 + k^1 + k^2 + ... + k^m > k^m    (2)

依据二项式定理可知：

    (k+1)^m = {m,0}k^0 + {m,1}k^1 + {m,2}k^2 + ... + {m,m}k^m

因为当 m>1 时，∀i ∈ [1,m-1], {m,i} > 1，所以有：

    (k+1)^m = {m,0}k^0 + {m,1}k^1 + {m,2}k^2 + ... + {m,m}k^m
            > k^0 + k^1 + k^2 + ... + k^m = n    (3)

结合 (2)(3) 两式可知，当 m>1 时，有 k^m < n < (k+1)^m。两边同时开方得：

    k < sqrt[m]{n} < k+1

依据这个公式我们知道，sqrt[m]{n} 必然为一个小数，且 k 为 sqrt[m]{n}
的整数部分，即 k = floor(sqrt[m]{n})。

这个结论帮助我们在 n 和 m 已知的情况下快速确定 k 的值。

综合上述两个结论，依据结论一，我们知道 m 的取值范围为 [1,logk(n))，
且 m = 1 时必然有解。因为随着 m 的增大，k 不断减小，所以我们只需要
从大到小检查每一个 m 可能的取值，利用结论二快速算出对应的 k 值，
然后校验计算出的 k 值是否有效即可。如果 k 值有效，我们即可返回结果。

在实际代码中，我们首先算出 m 取值的上界 mMax，然后从上界开始向下枚举
m 值，如果当前 m 值对应的 k 合法，那么我们即可返回当前的 k 值。如果
我们一直检查到 m=2 都没能找到答案，那么此时即可直接返回 m=1 对应的
k 值：n-1。
"""


# @lc code=start
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        mMax = math.floor(math.log2(n))
        for m in range(mMax, 1, -1):
            k = int(pow(n, 1.0 / m))
            tot = base = 1
            for i in range(m):
                base *= k
                tot += base
            if tot == n:
                return str(k)
        return str(n - 1)


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.smallestGoodBase("13"))
    print(solu.smallestGoodBase("4681"))
    print(solu.smallestGoodBase("1000000000000000000"))
