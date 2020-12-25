#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   Q04.切分木棒.py
@Time    :   2020/12/25 23:06:24
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
https://leetcode-cn.com/leetbook/read/interesting-algorithm-puzzles-for-programmers/90ach5/

假设要把长度为 n 厘米的木棒切分为 1 厘米长的小段，但是 1 根木棒只能由 1 人切分，
当木棒被切分为 3 段后，可以同时由 3 个人分别切分木棒.

求最多有 m 个人时，最少要切分几次。譬如 n ＝ 8，m＝ 3 时如图所示，
切分 4 次就可以了。


思路：

我们考虑一个逆向的过程：初始时有 n 根长度为 1 厘米的木棒，每一个人在一次「还原」
（而不是「切分」）中可以将两根木棒粘合在一起，最后要恢复 1 根长度为 n 厘米的木棒。
显然，这个逆向的过程与题目中正向的过程是等价的。

设当前木棒的段数为 slices，初始时有 slices = n。在每一次还原的过程中，如果
m⌊slices/2⌋ >= m，说明人数为瓶颈，只有 m 段木棒会被粘合到其它的木棒上；如果
⌊slices/2⌋ < m，说明段数为瓶颈，只有 ⌊slices/2⌋ 段木棒会被粘合到其它的木棒上。
因此每一次还原的木棒数量为 ⌊slices/2⌋ 和 m 中的较小值。

    min(⌊slices/2⌋,m)

因此我们可以从初始时开始模拟，每次将木棒段数减少这个值，直到这个值等于 1 为止。
"""


class Solution:
    def solve(self, n: int, m: int) -> int:
        ans, seg = 0, n

        while seg > 1:
            ans += 1
            seg -= min(seg // 2, m)

        return ans


if __name__ == "__main__":
    solu = Solution()
    print(solu.solve(8, 3))
    print(solu.solve(20, 3))
    print(solu.solve(100, 5))
