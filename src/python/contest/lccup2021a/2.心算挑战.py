#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2.心算挑战.py
@Time    :   2021/09/11 15:06:12
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort()
        part1, part2 = cards[:-cnt], cards[-cnt:]

        tot = sum(part2)
        if tot % 2 == 0:
            return tot

        p2_odd, p2_even = None, None
        for num in part2:
            r = num % 2
            if r == 0 and not p2_even:
                p2_even = num
            if r == 1 and not p2_odd:
                p2_odd = num
            if p2_odd and p2_even:
                break

        # print(f'p2_odd: {p2_odd}, p2_even: {p2_even}, tot: {tot}')

        p1_odd, p1_even = None, None
        for num in reversed(part1):
            r = num % 2
            if r == 0 and not p1_even:
                p1_even = num
            if r == 1 and not p1_odd:
                p1_odd = num
            if p1_odd and p1_even:
                break

        # print(f'p1_odd: {p1_odd}, p1_even: {p1_even}, tot: {tot}')

        ans = 0
        if p2_odd and p1_even:
            ans = tot - p2_odd + p1_even
        if p2_even and p1_odd:
            ans = max(ans, tot - p2_even + p1_odd)

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.maxmiumScore(cards=[1, 2, 8, 9], cnt=3))
    print(solu.maxmiumScore(cards=[3, 3, 1], cnt=1))
