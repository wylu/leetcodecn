#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1625.执行操作后字典序最小的字符串.py
@Time    :   2020/10/26 22:55:36
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1625 lang=python3
#
# [1625] 执行操作后字典序最小的字符串
#
# https://leetcode-cn.com/problems/lexicographically-smallest-string-after-applying-operations/description/
#
# algorithms
# Medium (51.57%)
# Likes:    14
# Dislikes: 0
# Total Accepted:    1.9K
# Total Submissions: 3.7K
# Testcase Example:  '"5525"\n9\n2'
#
# 给你一个字符串 s 以及两个整数 a 和 b 。其中，字符串 s 的长度为偶数，且仅由数字 0 到 9 组成。
#
# 你可以在 s 上按任意顺序多次执行下面两个操作之一：
#
#
# 累加：将 a 加到 s 中所有下标为奇数的元素上（下标从 0 开始）。数字一旦超过 9 就会变成 0，如此循环往复。
# 例如，s = "3456" 且 a = 5，则执行此操作后 s 变成 "3951"。
# 轮转：将 s 向右轮转 b 位。例如，s = "3456" 且 b = 1，则执行此操作后 s 变成 "6345"。
#
#
# 请你返回在 s 上执行上述操作任意次后可以得到的 字典序最小 的字符串。
#
# 如果两个字符串长度相同，那么字符串 a 字典序比字符串 b 小可以这样定义：在 a 和 b 出现不同的第一个位置上，字符串 a
# 中的字符出现在字母表中的时间早于 b 中的对应字符。例如，"0158” 字典序比 "0190" 小，因为不同的第一个位置是在第三个字符，显然 '5'
# 出现在 '9' 之前。
#
#
#
# 示例 1：
#
#
# 输入：s = "5525", a = 9, b = 2
# 输出："2050"
# 解释：执行操作如下：
# 初态："5525"
# 轮转："2555"
# 累加："2454"
# 累加："2353"
# 轮转："5323"
# 累加："5222"
# 累加："5121"
# 轮转："2151"
# 累加："2050"​​​​​​​​​​​​
# 无法获得字典序小于 "2050" 的字符串。
#
#
# 示例 2：
#
#
# 输入：s = "74", a = 5, b = 1
# 输出："24"
# 解释：执行操作如下：
# 初态："74"
# 轮转："47"
# 累加："42"
# 轮转："24"​​​​​​​​​​​​
# 无法获得字典序小于 "24" 的字符串。
#
#
# 示例 3：
#
#
# 输入：s = "0011", a = 4, b = 2
# 输出："0011"
# 解释：无法获得字典序小于 "0011" 的字符串。
#
#
# 示例 4：
#
#
# 输入：s = "43987654", a = 7, b = 3
# 输出："00553311"
#
#
#
#
# 提示：
#
#
# 2 <= s.length <= 100
# s.length 是偶数
# s 仅由数字 0 到 9 组成
# 1 <= a <= 9
# 1 <= b <= s.length - 1
#
#
#
"""
https://leetcode-cn.com/problems/lexicographically-smallest-string-after-applying-operations/solution/bao-li-mei-xue-by-lucifer1004/

解题思路

在本题的数据范围内，可以枚举所有可能的操作结果，从中选择最小的那一个。
关键是：如何枚举？

首先考虑轮转操作。对于一个长度为 N 的字符串，每次轮转 b 个位置，等价于
轮转 g = GCD(N,b) 个位置。所以，我们只需要以 g 为步长进行轮转的枚举即可。

接下来考虑增加操作。如果 g 是偶数，那么不管怎么轮转，我们只能对下标为奇数
的位置进行增加操作；否则，我们也可以对下标为偶数的位置进行增加操作。根据
这两种情况，枚举奇数和偶数位置的增加操作的次数即可。因为每一位是 [0,9] 之间
的数，而 1 <= a <= 9，所以我们只需要枚举操作 [0,9] 次的情形。

复杂度

时间复杂度 O(D^2|S|^2)，本题中 D = 10, |S| 为 s 的长度
空间复杂度 O(|S|)
"""


# @lc code=start
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def gcd(x: int, y: int) -> int:
            return x if y == 0 else gcd(y, x % y)

        ans, n = s, len(s)
        s = list(s + s)

        for i in range(0, n, gcd(n, b)):
            for j in range(0, 10):
                # 轮转
                u = s[i:i + n]
                for p in range(1, n, 2):
                    u[p] = str((int(u[p]) + a * j) % 10)

                if b % 2 == 0:
                    ans = min(ans, ''.join(u))
                else:
                    for k in range(0, 10):
                        v = u[:]
                        for q in range(0, n, 2):
                            v[q] = str((int(v[q]) + a * k) % 10)
                        ans = min(ans, ''.join(v))

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.findLexSmallestString("5525", 9, 2))
    print(solu.findLexSmallestString("74", 5, 1))
    print(solu.findLexSmallestString("0011", 4, 2))
    print(solu.findLexSmallestString("43987654", 7, 3))
    print(solu.findLexSmallestString("192804", 8, 5))
