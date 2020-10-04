#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   寻找比目标字母大的最小字母.py
@Time    :   2020/10/05 00:23:55
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return letters[0] if left == n else letters[left]


if __name__ == "__main__":
    solu = Solution()
    print(solu.nextGreatestLetter(["c", "f", "j"], "a"))
    print(solu.nextGreatestLetter(["c", "f", "j"], "c"))
    print(solu.nextGreatestLetter(["c", "f", "j"], "d"))
    print(solu.nextGreatestLetter(["c", "f", "j"], "g"))
    print(solu.nextGreatestLetter(["c", "f", "j"], "j"))
    print(solu.nextGreatestLetter(["c", "f", "j"], "k"))
