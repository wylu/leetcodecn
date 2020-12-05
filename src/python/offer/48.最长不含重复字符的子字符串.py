#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   48.最长不含重复字符的子字符串.py
@Time    :   2020/12/05 22:29:20
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        ans, i, j, n = 0, 0, 0, len(s)
        seen = set()

        while n - i > ans:
            while j < n and s[j] not in seen:
                seen.add(s[j])
                j += 1
            ans = max(ans, j - i)
            seen.remove(s[i])
            i += 1

        return ans


if __name__ == "__main__":
    solu = Solution()
    print(solu.lengthOfLongestSubstring("abcabcbb"))
    print(solu.lengthOfLongestSubstring("bbbbb"))
    print(solu.lengthOfLongestSubstring("pwwkew"))
