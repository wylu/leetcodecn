#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5869.两个回文子序列长度的最大乘积.py
@Time    :   2021/09/12 10:43:04
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def maxProduct(self, s: str) -> int:
        ans = 0
        n = len(s)
        options = []
        opt2size = {}

        def check(num: int) -> bool:
            seq = []
            for i in range(n - 1, -1, -1):
                if num & (1 << i):
                    seq.append(s[n - i - 1])

            if not seq:
                return False

            left, right = 0, len(seq) - 1
            while left < right:
                if seq[left] != seq[right]:
                    return False
                left += 1
                right -= 1

            # print(f'seq: {"".join(seq)}')
            opt2size[num] = len(seq)
            return True

        for i in range(1, 1 << n):
            if check(i):
                options.append(i)

        m = len(options)
        for i in range(m):
            for j in range(i + 1, m):
                if options[i] & options[j] == 0:
                    ans = max(ans, opt2size[options[i]] * opt2size[options[j]])

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.maxProduct(s="leetcodecom"))
    print(solu.maxProduct(s="bb"))
    print(solu.maxProduct(s="accbcaxxcxx"))
