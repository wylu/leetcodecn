#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5918.统计字符串中的元音子字符串.py
@Time    :   2021/11/07 10:30:27
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        n = len(word)
        ans = 0
        for i in range(n - 4):
            cnt = {ch: 0 for ch in 'aeiou'}
            j = i
            while j < n and word[j] in 'aeiou':
                cnt[word[j]] += 1
                if all(cnt.values()):
                    ans += 1
                j += 1
        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.countVowelSubstrings(word="aeiouu"))
    print(solu.countVowelSubstrings(word="unicornarihan"))
    print(solu.countVowelSubstrings(word="cuaieuouac"))
    print(solu.countVowelSubstrings(word="bbaeixoubb"))
    print(solu.countVowelSubstrings(word="duuebuaeeeeeeuaoeiueaoui"))
