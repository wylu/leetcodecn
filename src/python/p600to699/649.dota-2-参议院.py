#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   649.dota-2-参议院.py
@Time    :   2020/12/11 22:31:51
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=649 lang=python3
#
# [649] Dota2 参议院
#
# https://leetcode-cn.com/problems/dota2-senate/description/
#
# algorithms
# Medium (39.23%)
# Likes:    177
# Dislikes: 0
# Total Accepted:    22.1K
# Total Submissions: 47.2K
# Testcase Example:  '"RD"'
#
# Dota2 的世界里有两个阵营：Radiant(天辉)和 Dire(夜魇)
#
# Dota2 参议院由来自两派的参议员组成。现在参议院希望对一个 Dota2
# 游戏里的改变作出决定。他们以一个基于轮为过程的投票进行。在每一轮中，每一位参议员都可以行使两项权利中的一项：
#
#
#
# 禁止一名参议员的权利：
#
# 参议员可以让另一位参议员在这一轮和随后的几轮中丧失所有的权利。
#
#
# 宣布胜利：
#
#
#
# 如果参议员发现有权利投票的参议员都是同一个阵营的，他可以宣布胜利并决定在游戏中的有关变化。
#
#
#
# 给定一个字符串代表每个参议员的阵营。字母 “R” 和 “D” 分别代表了 Radiant（天辉）和 Dire（夜魇）。然后，如果有 n
# 个参议员，给定字符串的大小将是 n。
#
# 以轮为基础的过程从给定顺序的第一个参议员开始到最后一个参议员结束。这一过程将持续到投票结束。所有失去权利的参议员将在过程中被跳过。
#
# 假设每一位参议员都足够聪明，会为自己的政党做出最好的策略，你需要预测哪一方最终会宣布胜利并在 Dota2 游戏中决定改变。输出应该是 Radiant 或
# Dire。
#
#
#
# 示例 1：
#
#
# 输入："RD"
# 输出："Radiant"
# 解释：第一个参议员来自 Radiant
# 阵营并且他可以使用第一项权利让第二个参议员失去权力，因此第二个参议员将被跳过因为他没有任何权利。然后在第二轮的时候，第一个参议员可以宣布胜利，因为他是唯一一个有投票权的人
#
#
# 示例 2：
#
#
# 输入："RDD"
# 输出："Dire"
# 解释：
# 第一轮中,第一个来自 Radiant 阵营的参议员可以使用第一项权利禁止第二个参议员的权利
# 第二个来自 Dire 阵营的参议员会被跳过因为他的权利被禁止
# 第三个来自 Dire 阵营的参议员可以使用他的第一项权利禁止第一个参议员的权利
# 因此在第二轮只剩下第三个参议员拥有投票的权利,于是他可以宣布胜利
#
#
#
#
# 提示：
#
#
# 给定字符串的长度在 [1, 10,000] 之间.
#
#
#
#
#
from collections import deque
"""
方法一：「循环」队列
思路与算法

我们以天辉方的议员为例。当一名天辉方的议员行使权利时：
  - 如果目前所有的议员都为天辉方，那么该议员可以直接宣布天辉方取得胜利；
  - 如果目前仍然有夜魇方的议员，那么这名天辉方的议员只能行使「禁止一名参议员
    的权利」这一项权利。显然，该议员不会令一名同为天辉方的议员丧失权利，所以
    他一定会挑选一名夜魇方的议员。那么应该挑选哪一名议员呢？容易想到的是，
    应该贪心地挑选按照投票顺序的下一名夜魇方的议员。这也是很容易形象化地证明的：
    既然只能挑选一名夜魇方的议员，那么就应该挑最早可以进行投票的那一名议员；
    如果挑选了其它较晚投票的议员，那么等到最早可以进行投票的那一名议员行使
    权利时，一名天辉方议员就会丧失权利，这样就得不偿失了。

由于我们总要挑选投票顺序最早的议员，因此我们可以使用两个队列 radiant 和
dire 分别按照投票顺序存储天辉方和夜魇方每一名议员的投票时间。随后我们就可以
开始模拟整个投票的过程：
  - 如果此时 radiant 或者 dire 为空，那么就可以宣布另一方获得胜利；
  - 如果均不为空，那么比较这两个队列的首元素，就可以确定当前行使权利的是
    哪一名议员。如果 radiant 的首元素较小，那说明轮到天辉方的议员行使权利，
    其会挑选 dire 的首元素对应的那一名议员。因此，我们会将 dire 的首元素
    永久地弹出，并将 radiant 的首元素弹出，增加 n 之后再重新放回队列，
    这里 n 是给定的字符串 senate 的长度，即表示该议员会参与下一轮的投票。

为什么这里是固定地增加 n，而不是增加与当前剩余议员数量相关的一个数？
读者可以思考一下这里的正确性。

同理，如果 dire 的首元素较小，那么会永久弹出 radiant 的首元素，剩余的
处理方法也是类似的。

这样一来，我们就模拟了整个投票的过程，也就可以得到最终的答案了。
"""


# @lc code=start
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant, dire = deque(), deque()

        for i, ch in enumerate(senate):
            if ch == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            if radiant[0] < dire[0]:
                dire.popleft()
                radiant.append(radiant[0] + n)
                radiant.popleft()
            else:
                radiant.popleft()
                dire.append(dire[0] + n)
                dire.popleft()

        return 'Radiant' if radiant else 'Dire'


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.predictPartyVictory("RD"))
    print(solu.predictPartyVictory("RDD"))
    print(solu.predictPartyVictory("R"))
    print(solu.predictPartyVictory("RDRD"))
    print(solu.predictPartyVictory("DRDR"))
    print(solu.predictPartyVictory("RDDR"))
    print(solu.predictPartyVictory("DDRRR"))
