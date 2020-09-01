#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   31.栈的压入弹出序列.py
@Time    :   2020/09/02 00:07:30
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int],
                               popped: List[int]) -> bool:
        i, stack = 0, []
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack


if __name__ == '__main__':
    solu = Solution()
    print(solu.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    print(solu.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
