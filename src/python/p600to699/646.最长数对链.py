#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   646.最长数对链.py
@Time    :   2020/08/25 11:08:57
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=646 lang=python3
#
# [646] 最长数对链
#
# https://leetcode-cn.com/problems/maximum-length-of-pair-chain/description/
#
# algorithms
# Medium (55.79%)
# Likes:    108
# Dislikes: 0
# Total Accepted:    10.6K
# Total Submissions: 19K
# Testcase Example:  '[[1,2], [2,3], [3,4]]'
#
# 给出 n 个数对。 在每一个数对中，第一个数字总是比第二个数字小。
#
# 现在，我们定义一种跟随关系，当且仅当 b < c 时，数对(c, d) 才可以跟在 (a, b) 后面。我们用这种形式来构造一个数对链。
#
# 给定一个对数集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。
#
# 示例 :
#
#
# 输入: [[1,2], [2,3], [3,4]]
# 输出: 2
# 解释: 最长的数对链是 [1,2] -> [3,4]
#
#
# 注意：
#
#
# 给出数对的个数在 [1, 1000] 范围内。
#
#
#
from typing import List


# @lc code=start
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda e: e[1])
        ans, last = 0, pairs[0][0] - 1
        for i in range(len(pairs)):
            if pairs[i][0] > last:
                ans += 1
                last = pairs[i][1]
        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.findLongestChain([[1, 2], [2, 3], [3, 4]]))
