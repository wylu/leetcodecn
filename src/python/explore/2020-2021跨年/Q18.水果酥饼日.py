#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   Q18.水果酥饼日.py
@Time    :   2020/12/25 22:23:02
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
https://leetcode-cn.com/leetbook/read/interesting-algorithm-puzzles-for-programmers/97r135/

日本每月的 22 日是水果酥饼日。因为看日历的时候，22 日的上方刚好是 15 日，
也就是“‘22’ 这个数字上面点缀着草莓”[1]

切分酥饼的时候，要求切分后每一块上面的草莓个数都不相同。假设切分出来的 N 块
酥饼上要各有“1~N 个（共 N(N + 1)÷2 个草莓）”。

但这里要追加一个条件，那就是“一定要使相邻的两块酥饼上的数字之和是平方数”。

举个例子，假设 N ＝ 4 时采用如 图 4 的切法。这时，虽然 1 + 3 ＝ 4 得到
的是平方数，但“1 和 4” “2 和 3” “2 和 4”的部分都不满足条件（图 4）。


思路：

这个问题关键在于如何验证平方数。为验证相邻两数之和是否是平方数，只要预先准备
好平方数就相对简单了。因为相邻两块酥饼上的草莓个数最多也不会超过 N 的 2 倍，
所以可以事先计算好。

准确地说，相邻两个酥饼上的草莓个数之和应该是 N+(N-1) = 2N-1 个。

切分后的酥饼是围成圆形的，首先固定最开始的一块酥饼，并假设这块酥饼上的草莓
个数为 1。因为其他切法都可以通过旋转酥饼得到，所以这个假设的前提是成立的。

然后顺时针分配放置的草莓个数，保证每次放置的草莓个数都符合条件，直到最后一块
上的数字和最初的 1 相加也得到平方数。
"""


class Solution:
    def solve(self, n: int) -> bool:
        squares = set(i * i for i in range(2, n * 2))
        used = [False] * n
        used[0] = True
        stack = [1]

        def check() -> bool:
            if len(stack) == n:
                return stack[-1] + stack[0] in squares

            for i in range(n):
                if used[i] or (i + 1 + stack[-1] not in squares):
                    continue

                used[i] = True
                stack.append(i + 1)
                if check():
                    return True
                stack.pop()
                used[i] = False

            return False

        ans = check()
        if ans:
            print(stack)
        return ans

    def split_pie(self) -> int:
        n = 2
        while not self.solve(n):
            n += 1
        return n


if __name__ == "__main__":
    solu = Solution()
    print(solu.split_pie())
