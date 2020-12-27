#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   Q30.用插线板制作章鱼脚状线路.py
@Time    :   2020/12/27 18:52:33
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
https://leetcode-cn.com/leetbook/read/interesting-algorithm-puzzles-for-programmers/9l2pjv/

方法一：记忆化搜索
https://leetcode-cn.com/circle/discuss/SCX9Iu/

思路与算法

我们首先考虑接在插座上的那个插线板，显然它有两种情况：接双插口
或者接三插口。

如果我们接的是双插口，那么其中一个插口如果最终通过继续外接插线板
贡献了 i 个插口，那么另一个插口必须最终恰好贡献 n-i 个插口。可以
发现，我们将原问题 n 分解成了两个规模更小的子问题 i 和 n-i。

如果我们接的是三插口，同理可得，如果这三个插口最终通过继续外接插线板
分别贡献了 i,j,k 个插口，那么必须满足 i+j+k = n。我们将原问题 n
分解成了三个规模更小的子问题 i，j 和 n-i-j。

边界条件
然后我们来考虑边界条件，明显，当 n = 1 时，dp[n] = 1，即直接插在
第一块插线板上。

状态转移方程
最后来考虑状态转移方程。需要注意的有：

需要考虑双插口与三插口的情况
题目中要求：使用同一个插线板时，不考虑插口位置，只考虑插线板的连接方法。
因此我们要注意避免重复计数。
这里「重复」的含义具体到公式表示中就是：例如，对于双插口情况，(i,j)
和 (j,i) 是同一种方法；对于三插口情况，(i,j,k) 和 (i,k,j), (k,i,j)
是同一种方法。

那么对于双插口，规定 1≤i≤j， n = i+j ，插线方法 p(i,j) 的计算公式如下：

p(i,j) = (dp[i]+1)*dp[i]/2, i = j
p(i,j) = ​dp[i]*dp[i], i < j
​
对于三插口，规定 1≤i≤j≤k， n = i+j+k，插线方法 q(i,j,k) 的计算公式如下：

q(i,j,k) = (dp[i]+2)*(dp[i]+1)*dp[i]/6, i=j=k
q(i,j,k) = (dp[i]+1)*dp[i]*dp[k]/2, i=j<k
q(i,j,k) = dp[i]*(dp[j]+1)*dp[j]/2, i<j=k
q(i,j,k) = dp[i]*dp[j]*dp[k], i<j<k

总的状态转移方程为：

dp[n] = ∑(1≤i≤j,i+j=n) p(i,j) + ∑(1≤i≤j≤k,i+j+k=n) q(i,j,k)
"""


class Solution:
    def plugBoard(self, n: int) -> int:
        def dfs(n: int) -> int:
            if n == 1:
                return 1

            if f[n] != 0:
                return f[n]

            for i in range(1, n // 2 + 1):
                j = n - i
                if i == j:
                    f[n] += (dfs(i) + 1) * dfs(i) // 2
                else:
                    f[n] += dfs(i) * dfs(j)

            for i in range(1, n // 3 + 1):
                for j in range(i, (n - i) // 2 + 1):
                    k = n - i - j
                    if i == j and j == k:
                        f[n] += (dfs(i) + 2) * (dfs(i) + 1) * dfs(i) // 6
                    elif i == j:
                        f[n] += (dfs(i) + 1) * dfs(i) // 2 * dfs(k)
                    elif j == k:
                        f[n] += dfs(i) * (dfs(j) + 1) * dfs(j) // 2
                    else:
                        f[n] += dfs(i) * dfs(j) * dfs(k)

            return f[n]

        f = [0] * (n + 1)
        return dfs(n)


if __name__ == "__main__":
    solu = Solution()
    print(solu.plugBoard(20))
