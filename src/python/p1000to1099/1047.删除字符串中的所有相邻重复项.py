#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1047.删除字符串中的所有相邻重复项.py
@Time    :   2021/03/09 22:28:15
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#
# https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/description/
#
# algorithms
# Easy (72.25%)
# Likes:    212
# Dislikes: 0
# Total Accepted:    73.3K
# Total Submissions: 101.5K
# Testcase Example:  '"abbaca"'
#
# 给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
#
# 在 S 上反复执行重复项删除操作，直到无法继续删除。
#
# 在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
#
#
#
# 示例：
#
# 输入："abbaca"
# 输出："ca"
# 解释：
# 例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串
# "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
#
#
#
#
# 提示：
#
#
# 1 <= S.length <= 20000
# S 仅由小写英文字母组成。
#
#
#


# @lc code=start
class Solution:
    def removeDuplicates(self, S: str) -> str:
        ans = []
        for ch in S:
            if ans and ch == ans[-1]:
                ans.pop()
            else:
                ans.append(ch)

        return ''.join(ans)


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.removeDuplicates("abbaca"))
    print(solu.removeDuplicates(""))
    print(solu.removeDuplicates("aaa"))
    print(solu.removeDuplicates("aaaa"))
