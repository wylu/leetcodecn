#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   10.02.变位词组.py
@Time    :   2021/07/18 09:46:10
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            cnt = [0] * 26
            for ch in s:
                cnt[ord(ch) - ord('a')] += 1
            groups[tuple(cnt)].append(s)
        return list(groups.values())


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         groups = defaultdict(list)
#         for s in strs:
#             key = ''.join(sorted(s))
#             groups[key].append(s)
#         return list(groups.values())

if __name__ == '__main__':
    solu = Solution()
    print(solu.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
