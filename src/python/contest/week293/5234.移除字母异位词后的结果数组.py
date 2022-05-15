#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5234.移除字母异位词后的结果数组.py
@Time    :   2022/05/15 10:31:31
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = [words[0]]
        for word in words[1:]:
            last = ans[-1]
            cnt = [0] * 26
            for ch in last:
                cnt[ord(ch) - ord('a')] += 1

            for ch in word:
                cnt[ord(ch) - ord('a')] -= 1

            if any(cnt):
                ans.append(word)

        return ans


if __name__ == '__main__':
    solu = Solution()
    words = ["abba", "baba", "bbaa", "cd", "cd"]
    print(solu.removeAnagrams(words))
