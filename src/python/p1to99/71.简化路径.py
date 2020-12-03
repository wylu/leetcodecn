#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   71.简化路径.py
@Time    :   2020/12/03 22:17:34
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#
# https://leetcode-cn.com/problems/simplify-path/description/
#
# algorithms
# Medium (41.04%)
# Likes:    226
# Dislikes: 0
# Total Accepted:    62.3K
# Total Submissions: 151.7K
# Testcase Example:  '"/home/"'
#
# 以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。
#
# 在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..）
# 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。更多信息请参阅：Linux / Unix中的绝对路径 vs 相对路径
#
# 请注意，返回的规范路径必须始终以斜杠 / 开头，并且两个目录名之间必须只有一个斜杠 /。最后一个目录名（如果存在）不能以 /
# 结尾。此外，规范路径必须是表示绝对路径的最短字符串。
#
#
#
# 示例 1：
#
# 输入："/home/"
# 输出："/home"
# 解释：注意，最后一个目录名后面没有斜杠。
#
#
# 示例 2：
#
# 输入："/../"
# 输出："/"
# 解释：从根目录向上一级是不可行的，因为根是你可以到达的最高级。
#
#
# 示例 3：
#
# 输入："/home//foo/"
# 输出："/home/foo"
# 解释：在规范路径中，多个连续斜杠需要用一个斜杠替换。
#
#
# 示例 4：
#
# 输入："/a/./b/../../c/"
# 输出："/c"
#
#
# 示例 5：
#
# 输入："/a/../../b/../c//.//"
# 输出："/c"
#
#
# 示例 6：
#
# 输入："/a//b////c/d//././/.."
# 输出："/a/b/c"
#
#


# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i, n = 1, len(path)
        while i < n:
            j = i
            while j < n and path[j] != '/':
                j += 1

            cur = path[i:j]
            if not cur or cur == '.':
                # double '/' or '.'
                pass
            elif cur == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(cur)
            i = j + 1

        return '/' + '/'.join(stack)


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.simplifyPath("/home/"))
    print(solu.simplifyPath("/../"))
    print(solu.simplifyPath("/home//foo/"))
    print(solu.simplifyPath("/a/./b/../../c/"))
    print(solu.simplifyPath("/a/../../b/../c//.//"))
    print(solu.simplifyPath("/a//b////c/d//././/.."))
