#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   Q53.同数包夹.py
@Time    :   2020/12/30 23:14:02
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
https://leetcode-cn.com/leetbook/read/interesting-algorithm-puzzles-for-programmers/9umkfd/


方法一：回溯
https://leetcode-cn.com/circle/discuss/FxkmqT/
思路与算法

我们可以想到一种简单的搜索方法：

我们使用一个长度为 2n 的数组 cards 表示每一个位置的牌，如果当前位置
还没有放牌，那么对应的数字为 0；

我们用递归 + 回溯的方法枚举所有可能的情况。具体地，我们用 dfs(num)
表示当前正在尝试放入两张数字为 num 的牌，即在 cards 中找出所有间隔为
num 的两个位置，放入数字为 num 的牌。随后我们调用 dfs(num+1) 递归地
进行搜索，当搜索到 dfs(n+1) 时，表示搜索完成，找到了一种满足要求的
排列方法，并将答案增加 1。

我们调用 dfs(1) 即可得到答案。


方法二：状态压缩 + 记忆化搜索
思路与算法

方法一中的代码在可以接受的时间内能够得到答案，然而我们是可以对它继续
进行优化的。

一种可行的优化是使用「记忆化搜索」，这是因为 dfs(num) 其实只收到两个
变量的影响，一是 num 本身，二是我们用来存储牌放入位置的数组 cards。
换句话说，如果我们在搜索的过程中，当前的 (num,cards) 二元组在之前
被搜索过，那么我们就不必进行重复的搜索，而是使用一个记忆数组 memo
来存储之前搜索过的结果，通过 memo 直接返回答案。

memo 一般使用哈希映射进行实现，这就带来了一个问题：大部分语言没有计算
「数组」哈希值的默认方法，因此我们可以想到使用「状态压缩」的方法表示
整个数组 cards：

在数组 cards 中，我们只关心每个位置当前是否被放入了牌，而不用关系具体
的牌的数字是多少，因此我们可以用一个长度为 2n 的二进制数 mask 表示
cards，其中 mask 从低到高的第 i 位为 1，当且仅当第 i 个位置没有被
放入牌。

这样我们就可以用 (num,mask) 二元组唯一表示搜索过程中的一种状态，
memo[num,mask] 表示在已经放入的牌的位置的状态压缩为 mask，当前正在
放入数为 num 的牌的前提下，满足要求的方案数。注意到 num 和 mask
二者本身也是存在关联的：mask 的二进制表示中包含的 1 的个数，一定是
2(num−1)，即包含数字为 [1,num) 的牌各两张。因此我们可以使用
memo[mask] 表示方案数。

在使用 mask 枚举放入两张数字为 num 的牌时，我们可以使用位运算来进行
枚举的判断，即

    mask & (1 << i)

表示 mask 从低到高的第 i 个二进制位是否为 1。
"""


class Solution:
    def cardPermutation(self, n: int) -> int:
        def dfs(mask: int, num: int) -> int:
            if num == 0:
                return 1

            if memo[mask] != -1:
                return memo[mask]

            memo[mask] = 0
            # 枚举两张数字为 num 的牌的放入空位，它们的间隔为 num
            for i in range(n * 2 - num - 1):
                if (mask & (1 << i)) and (mask & (1 << (i + num + 1))):
                    memo[mask] += dfs(mask - (1 << i) - (1 << (i + num + 1)),
                                      num - 1)

            return memo[mask]

        memo = [-1] * (1 << (n * 2))
        return dfs((1 << (n * 2)) - 1, n)


# class Solution:
#     def cardPermutation(self, n: int) -> int:
#         ans = 0
#         cards = [0] * (n * 2)

#         def dfs(num: int) -> None:
#             nonlocal ans
#             if num == n + 1:
#                 ans += 1
#                 return

#             # 枚举两张数字为 num 的牌的放入空位，它们的间隔为 num
#             for i in range(n * 2 - num - 1):
#                 if cards[i] == 0 and cards[i + num + 1] == 0:
#                     cards[i] = cards[i + num + 1] = num
#                     dfs(num + 1)
#                     cards[i] = cards[i + num + 1] = 0

#         dfs(1)
#         return ans

if __name__ == "__main__":
    solu = Solution()
    print(solu.cardPermutation(3))
    print(solu.cardPermutation(11))
