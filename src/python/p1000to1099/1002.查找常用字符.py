#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1002.查找常用字符.py
@Time    :   2020/10/14 11:16:09
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找常用字符
#
# https://leetcode-cn.com/problems/find-common-characters/description/
#
# algorithms
# Easy (72.73%)
# Likes:    137
# Dislikes: 0
# Total Accepted:    25.8K
# Total Submissions: 35.5K
# Testcase Example:  '["bella","label","roller"]'
#
# 给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3
# 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
#
# 你可以按任意顺序返回答案。
#
#
#
# 示例 1：
#
# 输入：["bella","label","roller"]
# 输出：["e","l","l"]
#
#
# 示例 2：
#
# 输入：["cool","lock","cook"]
# 输出：["c","o"]
#
#
#
#
# 提示：
#
#
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] 是小写字母
#
#
#
from typing import List


# @lc code=start
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        n = len(A)
        freq = [110] * 26
        for i in range(n):
            tmp = [0] * 26
            for ch in A[i]:
                tmp[ord(ch) - ord('a')] += 1
            for j in range(26):
                freq[j] = min(freq[j], tmp[j])

        ans = []
        for i in range(26):
            for j in range(freq[i]):
                ans.append(chr(i + ord('a')))

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.commonChars(["bella", "label", "roller"]))
    print(solu.commonChars(["cool", "lock", "cook"]))
