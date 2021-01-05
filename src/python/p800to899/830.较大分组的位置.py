#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   830.较大分组的位置.py
@Time    :   2021/01/05 09:36:35
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=830 lang=python3
#
# [830] 较大分组的位置
#
# https://leetcode-cn.com/problems/positions-of-large-groups/description/
#
# algorithms
# Easy (50.37%)
# Likes:    72
# Dislikes: 0
# Total Accepted:    18.3K
# Total Submissions: 35.9K
# Testcase Example:  '"abbxxxxzzy"'
#
# 在一个由小写字母构成的字符串 s 中，包含由一些连续的相同字符所构成的分组。
#
# 例如，在字符串 s = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。
#
# 分组可以用区间 [start, end] 表示，其中 start 和 end 分别表示该分组的起始和终止位置的下标。上例中的 "xxxx"
# 分组用区间表示为 [3,6] 。
#
# 我们称所有包含大于或等于三个连续字符的分组为 较大分组 。
#
# 找到每一个 较大分组 的区间，按起始位置下标递增顺序排序后，返回结果。
#
#
#
# 示例 1：
#
#
# 输入：s = "abbxxxxzzy"
# 输出：[[3,6]]
# 解释："xxxx" 是一个起始于 3 且终止于 6 的较大分组。
#
#
# 示例 2：
#
#
# 输入：s = "abc"
# 输出：[]
# 解释："a","b" 和 "c" 均不是符合要求的较大分组。
#
#
# 示例 3：
#
#
# 输入：s = "abcdddeeeeaabbbcd"
# 输出：[[3,5],[6,9],[12,14]]
# 解释：较大分组为 "ddd", "eeee" 和 "bbb"
#
# 示例 4：
#
#
# 输入：s = "aba"
# 输出：[]
#
#
#
# 提示：
#
#
# 1 <= s.length <= 1000
# s 仅含小写英文字母
#
#
#
from typing import List


# @lc code=start
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        cnt, n = 1, len(s)
        for i in range(n):
            if i == n - 1 or s[i] != s[i + 1]:
                if cnt >= 3:
                    ans.append([i - cnt + 1, i])
                cnt = 1
            else:
                cnt += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.largeGroupPositions("abbxxxxzzy"))
    print(solu.largeGroupPositions("abc"))
    print(solu.largeGroupPositions("abcdddeeeeaabbbcd"))
    print(solu.largeGroupPositions("aba"))
    print(solu.largeGroupPositions("aaa"))
