#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   87.扰乱字符串.py
@Time    :   2021/04/16 22:32:14
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=87 lang=python3
#
# [87] 扰乱字符串
#
# https://leetcode-cn.com/problems/scramble-string/description/
#
# algorithms
# Hard (48.77%)
# Likes:    349
# Dislikes: 0
# Total Accepted:    32.7K
# Total Submissions: 67.1K
# Testcase Example:  '"great"\n"rgeat"'
#
# 使用下面描述的算法可以扰乱字符串 s 得到字符串 t ：
#
# 如果字符串的长度为 1 ，算法停止
# 如果字符串的长度 > 1 ，执行下述步骤：
#
# 在一个随机下标处将字符串分割成两个非空的子字符串。即，如果已知字符串 s ，则可以将其分成两个子字符串 x 和 y ，且满足 s = x + y
# 。
# 随机 决定是要「交换两个子字符串」还是要「保持这两个子字符串的顺序不变」。即，在执行这一步骤之后，s 可能是 s = x + y 或者 s = y + x
# 。
# 在 x 和 y 这两个子字符串上继续从步骤 1 开始递归执行此算法。
#
#
#
#
# 给你两个 长度相等 的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。如果是，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
#
# 输入：s1 = "great", s2 = "rgeat"
# 输出：true
# 解释：s1 上可能发生的一种情形是：
# "great" --> "gr/eat" // 在一个随机下标处分割得到两个子字符串
# "gr/eat" --> "gr/eat" // 随机决定：「保持这两个子字符串的顺序不变」
# "gr/eat" --> "g/r / e/at" // 在子字符串上递归执行此算法。两个子字符串分别在随机下标处进行一轮分割
# "g/r / e/at" --> "r/g / e/at" // 随机决定：第一组「交换两个子字符串」，第二组「保持这两个子字符串的顺序不变」
# "r/g / e/at" --> "r/g / e/ a/t" // 继续递归执行此算法，将 "at" 分割得到 "a/t"
# "r/g / e/ a/t" --> "r/g / e/ a/t" // 随机决定：「保持这两个子字符串的顺序不变」
# 算法终止，结果字符串和 s2 相同，都是 "rgeat"
# 这是一种能够扰乱 s1 得到 s2 的情形，可以认为 s2 是 s1 的扰乱字符串，返回 true
#
#
# 示例 2：
#
#
# 输入：s1 = "abcde", s2 = "caebd"
# 输出：false
#
#
# 示例 3：
#
#
# 输入：s1 = "a", s2 = "a"
# 输出：true
#
#
#
#
# 提示：
#
#
# s1.length == s2.length
# 1 <= s1.length <= 30
# s1 和 s2 由小写英文字母组成
#
#
#

# from collections import Counter
# from functools import lru_cache
"""
方法一：记忆化搜索
思路与算法

显然「扰乱字符串」的关系是具有对称性的，即如果 s1 是 s2 的扰乱字符串，
那么 s2 也是 s1 的扰乱字符串。为了叙述方便，我们称这种情况下，s1 和 s2
是「和谐」的。

那么如何判断 s1 和 s2 是否「和谐」呢？我们首先可以想到几个简单的判断方法：

- 如果 s1 = s2，那么它们是「和谐」的；
- 如果 s1 和 s2 的长度不同，那么它们一定不是「和谐」的；
- 如果 s1 中某个字符 c 出现了 x1 次，而 c 在 s2 中出现了 x2 次，且
  x1 != x2 ，那么它们一定不是「和谐」的。这是因为任意操作都不会改变一个
  字符串中的字符种类以及数量。

那么对于剩下的情况，我们该如何判断呢？我们可以从 s1 的分割方法入手。假设
s1 作为根节点时被分割成了 l(s1) 以及 r(s1) 两个子串，那么：

- 如果 l(s1) 和 r(s1) 没有被交换，那么 s2 需要存在一种分割方法
  s2 = l(s2) + r(s2)，使得 l(s1) 和 l(s2) 是「和谐」的，并且 r(s1)
  和 r(s2) 也是「和谐」的；
- 如果 l(s1) 和 r(s1) 被交换了，那么 s2 需要存在一种分割方法
  s2 = l(s2) + r(s2)，使得 l(s1) 和 r(s2) 是「和谐」的，并且 r(s1)
  和 l(s2) 也是「和谐」的。

这样一来，我们就把原本需要解决的问题划分成了两个本质相同，但规模更小的
子问题，因此可以考虑使用动态规划解决。

设 f(s1,s2) 表示 s1 和 s2 是否「和谐」，那么我们可以写出状态转移方程：

  f(s1,s2) = True,   s1 = s2
  f(s1,s2) = False,  存在某个字符 c，它在 s1 和 s2 中的出现次数不同

因为题目保证给定的原始字符串的长度相同，因此我们只需要判断上面的两种情况。
如果 s1 和 s2 不符合这两种情况，那么我们需要枚举分割点。

设 s1 和 s2 的长度为 n，我们用 s1(x,y) 表示从 s1 从第 x 个字符（从 0
开始编号）开始，长度为 y 的子串。由于分割出的两个字符串不能为空串，那么
其中一个字符串就是 s1(0,i)，另一个字符串是 s1(i,n-i)。

对于 l(s1) 和 r(s1) 没有被交换的情况，s2 同样需要被分为 s2(0,i) 以及
s2(i,n-i)，否则长度不同的字符串是不可能「和谐」的。因此我们可以写出状态
转移方程：

  f(s1,s2) = False
  0 < i < n
  f(s1,s2) ||= (f(s1(0,i), s2(0,i)) && f(s1(i,n-i), s2(i,n-i)))

其中 && 表示与运算，即 s1 和 s2 分割出的两对字符串都要是「和谐」的；
|| 表示或运算，即只要有一种满足要求的分割方法，s1 和 s2 就是和谐的。

对于 l(s1) 和 r(s1) 被交换的情况，s2 需要被分为 s2(0,n-i) 以及 s2(n-i,i)，
这样对应的长度才会相同。因此我们可以写出状态转移方程：

  f(s1,s2) = False
  0 < i < n
  f(s1,s2) = (f(s1(0,i), s2(n-i,i)) && f(s1(i,n-i), s2(0,n-i)))

我们将上面两种状态转移方程用 || 或运算拼在一起，即可得到最终的状态转移方程。

细节

在进行状态转移时，我们需要先计算出较短的字符串对应的 f 值，再去转移计算出
较长的字符串对应的 f 值，这是因为我们需要保证在计算 f(s1,s2) 时，所有它们
的子串对应的状态都需要被计算过。因此，如果我们使用常规的动态规划方法编写代码，
可能会受到计算顺序的困扰，使得代码冗长。

而我们可以考虑使用「记忆化搜索」自顶向下地进行动态规划，这样我们只需要用题目
中给定的两个原始字符串开始，递归地计算所有的 f 值，而无需考虑计算顺序。

由于我们使用记忆化搜索，因此我们需要把 s1 和 s2 作为参数传入记忆化搜索使用
的递归函数。这样一来，在递归传递参数的过程中，会使用到大量字符串的切片、拷贝
等操作，使得时空复杂度不那么优。本题中，由于给定原始字符串的长度不超过 30，
因此不会产生太大的影响，但我们还是要尽可能对代码进行优化。

一种通用的优化方法是，我们将状态变更为 f(i1, i2, length)，表示第一个字符串
是原始字符串从第 i1 个字符开始，长度为 length 的子串，第二个字符串是原始
字符串从第 i2 个字符开始，长度为 length 的子串。可以发现，我们只是改变了
表达 s1 和 s2 的方式，但此时我们只需要在递归时传递三个整数类型的变量，省去
了字符串的操作；


方法二：动态规划
关于区间dp

背景：给定一个序列或字符串要进行一些操作，从最后一步出发，要将序列或字符串
去头、去尾，如果做过最长回文子串，你就就可以想一下这样子的操作。区间型 dp
一般用 dp[i][j] ，i 代表左端点，j 代表右端点，若有其他维度可再添加，若两个
端点之间存在联系，则可再压缩空间。力扣上还有一些题也属于区间 dp：

5. 最长回文子串
516. 最长回文子序列
312. 戳气球
1246. 删除回文子数组

初步分析
给定两个字符串 T 和 S，假设 T 是由 S 变换而来

- 如果 T 和 S 长度不一样，必定不能变来
- 如果长度一样，字符串 S 能够划分为 S1 和 S2，同样字符串 T 也能够划分为
  T1 和 T2
  - 情况一：没交换，S1 ==> T1，S2 ==> T2
  - 情况二：交换了，S1 ==> T2，S2 ==> T1

子问题就是分别讨论两种情况，T1 是否由 S1 变来，T2 是否由 S2 变来，
或 T1 是否由 S2 变来，T2 是否由 S1 变来。

得到状态
dp[i][j][k][h] 表示 T[k..h] 是否由 S[i..j] 变来。由于变换必须长度是
一样的，因此这边有个关系 j-i = h-k，可以把四维数组降成三维。dp[i][j][len]
表示从字符串 S 中 i 开始长度为 len 的字符串是否能变换为从字符串 T 中 j
开始长度为 len 的字符串

转移方程
dp[i][j][k]==
  OR{1 <= w <= k-1} { dp[i][j][w] && dp[i+w][j+w][k-w] } 或
  OR{1 <= w <= k-1} { dp[i][j+k-w][w] && dp[i+w][j][k-w] }

解释下：枚举 S1 长度 w（从 1～k-1，因为要划分），f[i][j][w] 表示 S1
能变成 T1，f[i+w][j+w][k-w] 表示 S2 能变成 T2，或者是 S1 能变成 T2，
S2 能变成 T1。

初始条件
对于长度是 1 的子串，只有相等才能变过去，相等为 true，不相等为 false。

得到答案
还记得我们的定义吗？dp[i][j][len] 表示从字符串 S 中 i 开始长度为 len
的字符串是否能变换为从字符串 T 中 j 开始长度为 len 的字符串，所以答案是
dp[0][0][n]。

时间复杂度 O(N^4)，空间复杂度 O(N^3)
"""


# @lc code=start
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]
        # 初始化单个字符的情况
        for i in range(n):
            for j in range(n):
                dp[i][j][1] = s1[i] == s2[j]

        # 枚举区间长度
        for length in range(2, n + 1):
            # 枚举 S 中的起点位置
            for i in range(n - length + 1):
                # 枚举 T 中的起点位置
                for j in range(n - length + 1):
                    # 枚举划分位置
                    for k in range(1, length):
                        # 第一种情况：S1->T1, S2->T2
                        if dp[i][j][k] and dp[i + k][j + k][length - k]:
                            dp[i][j][length] = True
                            break

                        # 第二种情况：S1->T2, S2->T1
                        if (dp[i][j + length - k][k]
                                and dp[i + k][j][length - k]):
                            dp[i][j][length] = True
                            break

        return dp[0][0][n]


# @lc code=end

# class Solution:
#     def isScramble(self, s1: str, s2: str) -> bool:
#         @lru_cache(None)
#         def dfs(i1: int, i2: int, length: int) -> bool:
#             """判断两个字符串是否和谐

#             Args:
#                 i1 (int): 第一个字符串从 i1 开始
#                 i2 (int): 第二个字符串从 i2 开始
#                 length (int): 子串的长度

#             Returns:
#                 bool: 是否和谐
#             """
#             # 判断两个子串是否相等
#             if s1[i1:i1 + length] == s2[i2:i2 + length]:
#                 return True

#             # 统计字符频次是否一致
#             if Counter(s1[i1:i1 + length]) != Counter(s2[i2:i2 + length]):
#                 return False

#             # 枚举分割点
#             for i in range(1, length):
#                 # 不交换顺序
#                 if dfs(i1, i2, i) and dfs(i1 + i, i2 + i, length - i):
#                     return True

#                 # 交换顺序
#                 if dfs(i1, i2 + length - i, i) and dfs(i1 + i, i2, length - i):  # noqa E501
#                     return True

#             return False

#         return dfs(0, 0, len(s1))

if __name__ == '__main__':
    solu = Solution()
    print(solu.isScramble(s1="great", s2="rgeat"))
    print(solu.isScramble(s1="abcde", s2="caebd"))
    print(solu.isScramble(s1="a", s2="a"))
