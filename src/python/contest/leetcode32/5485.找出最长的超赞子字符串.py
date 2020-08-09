#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5485.找出最长的超赞子字符串.py
@Time    :   2020/08/08 23:50:56
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
这道题中， 每个子串我们只关心每个数字出现的次数是奇数次还是偶数次。
这里我们设一个字符的 hash 值为 (count(i) % 2) ∗ 2, 0 <= i <= 9
题中给出的“超赞子字符串”只有 2 种可能：
  1. 所有字符都出现偶数次；
  2. 除一个字符出现奇数次， 其余所有字符都出现偶数次；

我们从左往右扫描字符串， 记录其每个前缀对应的hash值。
若一个字符串 s[i...j] 为第 1 类回文串， 则存在 i 使得 s[0...i] xor s[0...j] = 0;
若一个字符串 s[i...j] 为第 2 类回文串， 则存在 i 使得 s[0...i] xor s[0...j]
的二进制表示中仅有 1 为 1（共10种可能）;

以上两种共计 11 种情况， 我们只需判断每种可能是否存在即可。
时间复杂度 O(nC)，C 为字符集大小。
"""


class Solution:
    def longestAwesome(self, s: str) -> int:
        if not s:
            return 0

        first = [-1] * (1 << 10)
        good = [0]
        for i in range(10):
            good.append(1 << i)

        ans = 0
        state = 0
        first[0] = 0
        for i in range(1, len(s) + 1):
            c = int(s[i - 1])
            state ^= (1 << c)

            if first[state] == -1:
                first[state] = i

            for g in good:
                need = g ^ state
                if first[need] != -1:
                    ans = max(ans, i - first[need])

        return ans
