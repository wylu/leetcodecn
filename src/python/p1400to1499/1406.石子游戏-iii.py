#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1406.石子游戏-iii.py
@Time    :   2020/09/02 22:14:26
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1406 lang=python3
#
# [1406] 石子游戏 III
#
# https://leetcode-cn.com/problems/stone-game-iii/description/
#
# algorithms
# Hard (55.97%)
# Likes:    53
# Dislikes: 0
# Total Accepted:    2.7K
# Total Submissions: 4.8K
# Testcase Example:  '[1,2,3,7]'
#
# Alice 和 Bob 用几堆石子在做游戏。几堆石子排成一行，每堆石子都对应一个得分，由数组 stoneValue 给出。
#
# Alice 和 Bob 轮流取石子，Alice 总是先开始。在每个玩家的回合中，该玩家可以拿走剩下石子中的的前 1、2 或 3 堆石子
# 。比赛一直持续到所有石头都被拿走。
#
# 每个玩家的最终得分为他所拿到的每堆石子的对应得分之和。每个玩家的初始分数都是 0
# 。比赛的目标是决出最高分，得分最高的选手将会赢得比赛，比赛也可能会出现平局。
#
# 假设 Alice 和 Bob 都采取 最优策略 。如果 Alice 赢了就返回 "Alice" ，Bob 赢了就返回 "Bob"，平局（分数相同）返回
# "Tie" 。
#
#
#
# 示例 1：
#
# 输入：values = [1,2,3,7]
# 输出："Bob"
# 解释：Alice 总是会输，她的最佳选择是拿走前三堆，得分变成 6 。但是 Bob 的得分为 7，Bob 获胜。
#
#
# 示例 2：
#
# 输入：values = [1,2,3,-9]
# 输出："Alice"
# 解释：Alice 要想获胜就必须在第一个回合拿走前三堆石子，给 Bob 留下负分。
# 如果 Alice 只拿走第一堆，那么她的得分为 1，接下来 Bob 拿走第二、三堆，得分为 5 。之后 Alice 只能拿到分数 -9
# 的石子堆，输掉比赛。
# 如果 Alice 拿走前两堆，那么她的得分为 3，接下来 Bob 拿走第三堆，得分为 3 。之后 Alice 只能拿到分数 -9
# 的石子堆，同样会输掉比赛。
# 注意，他们都应该采取 最优策略 ，所以在这里 Alice 将选择能够使她获胜的方案。
#
# 示例 3：
#
# 输入：values = [1,2,3,6]
# 输出："Tie"
# 解释：Alice 无法赢得比赛。如果她决定选择前三堆，她可以以平局结束比赛，否则她就会输。
#
#
# 示例 4：
#
# 输入：values = [1,2,3,-1,-2,-3,7]
# 输出："Alice"
#
#
# 示例 5：
#
# 输入：values = [-1,-2,-3]
# 输出："Tie"
#
#
#
#
# 提示：
#
#
# 1 <= values.length <= 50000
# -1000 <= values[i] <= 1000
#
#
#
from typing import List
"""
方法一：动态规划

对于这种两个玩家、分先后手、博弈类型的题目，一般可以使用动态规划来解决。

由于玩家只能拿走前面的石子，因此我们考虑使用状态 f[i] 表示还剩下第
i, i+1, ⋯, n−1 堆石子时，当前玩家（也就是当前准备拿石子的那一名玩家）
的某一个状态。这个「某一个状态」具体是什么状态，我们暂且不表，这里带着
大家一步一步来分析这个状态。

根据题目描述，当前玩家有三种策略可以选择，即取走前 1、2 或 3 堆石子，
那么留给 下一位玩家（也就是下一个准备拿石子的那一名玩家） 的状态为
f[i+1]、f[i+2] 或 f[i+3]。设想一下，假如你是当前玩家，你希望 f[i]
表示什么，才可以帮助你选择自己的 最优策略 呢？

一个聪明的读者会说：我希望 f[i] 表示还剩下第 i, i+1, ⋯, n−1 堆石子时，
当前玩家最多能从剩下的石子中拿到的石子数目（这个「剩下」的意义是，如果
i, i+1, ⋯, n−1 堆石子的总数是 t，Alice 拿走了 x，Bob 就拿走了 t - x，
也就是我们只讨论 i, i+1, ⋯, n−1 堆石子，而不讨论对 0, 1, ⋯, i−1 堆
石子 Alice 和 Bob 作出了怎样的决策）。这样一来：

如果当前玩家选择了一堆石子，那么留给下一位玩家的状态为 f[i+1]，表示他
可以最多拿到 f[i+1] 数量的石子。

咦？我们之前的定义中，f[i+1] 是表示当前玩家最多能拿到的石子数目，为什么
这里变成了下一位玩家呢？仔细想想，「当前玩家」和「下一位玩家」的概念其实
是相对的。在「当前玩家」拿完石子后，「下一位玩家」就成了此时的「当前玩家」）。
由于下一位玩家可以拿 f[i+1] 数量的石子，如果我们用 sum(l,r) 表示第
l, l+1, ⋯, r 堆石子的的数量之和，那么当前玩家就可以拿到
sum(i+1,n−1) − f[i+1] 数量的石子。加上当前玩家选择了一堆石子，它一共
可以拿到 sum(i,i) + sum(i+1,n−1) − f[i+1] 数量的石子。可以发现，
它可以化简为 sum(i,n−1) − f[i+1]；

同理，如果当前玩家选择了两堆石子，那么留给下一位玩家的状态为 f[i+2]，
当前玩家一共可以拿到 sum(i,n−1) − f[i+2] 数量的石子；

同理，如果当前玩家选择了三堆石子，那么留给下一位玩家的状态为 f[i+3]，
当前玩家一共可以拿到 sum(i,n−1) − f[i+3] 数量的石子。

故当前玩家只要选择上面三种情况中能拿到最多数量的石子的方案，就是他的最优策略。

因此，我们就可以用动态规划来解决这个问题了。我们首先处理出表示石子数量
的数组 stones 的后缀和，方便我们快速地求出 sum(l,r)。随后，我们就可以
倒序地进行动态规划（因为在计算 f[i] 的值的时候，需要已经求出 f[i+1]，
f[i+2] 和 f[i+3] 的值），状态转移方程为：

    f[i] = max(sum(i,n−1) − f[j])
         = sum(i,n−1) − min(f[j]), j ∈ [i+1,i+3]
​
最后的 f[0] 就表示 Alice 最多可以获得的石子数量。我们根据 f[0] 与
sum(0,n−1) 的关系，就可以得到最终的获胜者。
"""


# @lc code=start
class Solution:
    def stoneGameIII(self, stones: List[int]) -> str:
        n = len(stones)
        ss = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            ss[i] = ss[i + 1] + stones[i]

        # 边界情况，当没有石子时，分数为 0
        f = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            f[i] = ss[i] - min(f[i + 1:i + 4])

        alice, bob = f[0], ss[0] - f[0]
        if alice > bob:
            return 'Alice'
        elif alice < bob:
            return 'Bob'
        else:
            return 'Tie'


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.stoneGameIII([1, 2, 3, 7]))
    print(solu.stoneGameIII([1, 2, 3, -9]))
    print(solu.stoneGameIII([1, 2, 3, 6]))
    print(solu.stoneGameIII([1, 2, 3, -1, -2, -3, 7]))
    print(solu.stoneGameIII([-1, -2, -3]))
