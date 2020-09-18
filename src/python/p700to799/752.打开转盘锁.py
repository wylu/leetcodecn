#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   752.打开转盘锁.py
@Time    :   2020/09/18 14:26:08
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#
# https://leetcode-cn.com/problems/open-the-lock/description/
#
# algorithms
# Medium (49.05%)
# Likes:    166
# Dislikes: 0
# Total Accepted:    23.6K
# Total Submissions: 48.2K
# Testcase Example:  '["0201","0101","0102","1212","2002"]\n"0202"'
#
# 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8',
# '9' 。每个拨轮可以自由旋转：例如把 '9' 变为  '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
#
# 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
#
# 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
#
# 字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。
#
#
#
# 示例 1:
#
#
# 输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# 输出：6
# 解释：
# 可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
# 注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
# 因为当拨动到 "0102" 时这个锁就会被锁定。
#
#
# 示例 2:
#
#
# 输入: deadends = ["8888"], target = "0009"
# 输出：1
# 解释：
# 把最后一位反向旋转一次即可 "0000" -> "0009"。
#
#
# 示例 3:
#
#
# 输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"],
# target = "8888"
# 输出：-1
# 解释：
# 无法旋转到目标数字且不被锁定。
#
#
# 示例 4:
#
#
# 输入: deadends = ["0000"], target = "8888"
# 输出：-1
#
#
#
#
# 提示：
#
#
# 死亡列表 deadends 的长度范围为 [1, 500]。
# 目标数字 target 不会在 deadends 之中。
# 每个 deadends 和 target 中的字符串的数字会在 10,000 个可能的情况 '0000' 到 '9999' 中产生。
#
#
#
from collections import deque
from typing import List
"""
方法一：广度优先搜索

我们可以将 0000 到 9999 这 10000 状态看成图上的 10000 个节点，两个节点
之间存在一条边，当且仅当这两个节点对应的状态只有 1 位不同，且不同的那位
相差 1（包括 0 和 9 也相差 1 的情况），并且这两个节点均不在数组 deadends
中。那么最终的答案即为 0000 到 target 的最短路径。

我们用广度优先搜索来找到最短路径，从 0000 开始搜索。对于每一个状态，它可以
扩展到最多 8 个状态，即将它的第 i = 0, 1, 2, 3 位增加 1 或减少 1，将这些
状态中没有搜索过并且不在 deadends 中的状态全部加入到队列中，并继续进行搜索。
注意 0000 本身有可能也在 deadends 中。
"""


# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def bfs(x: str) -> int:
            dist = 0
            q = deque()
            q.append(x)
            while q:
                size = len(q)
                for _ in range(size):
                    x = q.popleft()
                    if x in deadends:
                        continue
                    if x == target:
                        return dist
                    x = list(x)
                    for i in range(4):
                        for j in (-1, 1):
                            tmp = x[i]
                            x[i] = str((int(tmp) + j + 10) % 10)
                            y = ''.join(x)
                            if y not in visit:
                                visit.add(y)
                                q.append(y)
                            x[i] = tmp
                dist += 1
            return -1

        start = '0000'
        visit = {start}
        deadends = set(deadends)
        return bfs(start)


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    print(solu.openLock(deadends, target))

    deadends = ["8888"]
    target = "0009"
    print(solu.openLock(deadends, target))

    deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    target = "8888"
    print(solu.openLock(deadends, target))

    deadends = ["0000"]
    target = "8888"
    print(solu.openLock(deadends, target))
