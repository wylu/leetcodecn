#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1190.反转每对括号间的子串.py
@Time    :   2021/05/26 21:11:35
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1190 lang=python3
#
# [1190] 反转每对括号间的子串
#
# https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/
#
# algorithms
# Medium (64.35%)
# Likes:    157
# Dislikes: 0
# Total Accepted:    31.1K
# Total Submissions: 48.3K
# Testcase Example:  '"(abcd)"'
#
# 给出一个字符串 s（仅含有小写英文字母和括号）。
#
# 请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
#
# 注意，您的结果中 不应 包含任何括号。
#
#
#
# 示例 1：
#
# 输入：s = "(abcd)"
# 输出："dcba"
#
#
# 示例 2：
#
# 输入：s = "(u(love)i)"
# 输出："iloveu"
#
#
# 示例 3：
#
# 输入：s = "(ed(et(oc))el)"
# 输出："leetcode"
#
#
# 示例 4：
#
# 输入：s = "a(bcdefghijkl(mno)p)q"
# 输出："apmnolkjihgfedcbq"
#
#
#
#
# 提示：
#
#
# 0 <= s.length <= 2000
# s 中只有小写英文字母和括号
# 我们确保所有括号都是成对出现的
#
#
#
"""
方法二：预处理括号
思路及算法

我们可以将括号的反转理解为逆序地遍历括号，如下图：

    +---+  1   +---+   4  +---+   3  +---+   2  +---+  5   +---+
    | a | ---> | ( | <--- | b | <--- | c | <--- | ) | ---> | d |
    +---+      +---+      +---+      +---+      +---+      +---+

1.第一步我们向右移动到左括号，此时我们跳跃到该左括号对应的右括号（进入了更深一层）；
2.第二到第三步我们在括号内部向左移动（完成了更深层的遍历）；
3.第四步我们向左移动到左括号，此时我们跳跃到该左括号对应的右括号（返回到上一层）；
4.第五步我们在括号外向右移动（继续遍历）。

读者们可以自行尝试模拟两层乃至多层括号嵌套的移动方案，规律可以从当前的单层括号中
总结出来。

假设我们沿着某个方向移动，此时遇到了括号，那么我们只需要首先跳跃到该括号对应的
另一个括号所在处，然后改变我们的移动方向即可。这个方案同时适用于遍历时进入更深
一层，以及完成当前层的遍历后返回到上一层的方案。

在实际代码中，我们需要预处理出每一个括号对应的另一个括号所在的位置，这一部分
我们可以使用栈解决。当我们预处理完成后，即可在线性时间内完成遍历，遍历的字符串
顺序即为反转后的字符串。
"""


# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pos, stk = {}, []
        for i in range(n):
            if s[i] == '(':
                stk.append(i)
            elif s[i] == ')':
                j = stk.pop()
                pos[i], pos[j] = j, i

        ans = []
        idx, step = 0, 1
        while idx < n:
            if s[idx] == '(' or s[idx] == ')':
                idx = pos[idx]
                step = -step
            else:
                ans.append(s[idx])
            idx += step

        return ''.join(ans)


# @lc code=end

# class Solution:
#     def reverseParentheses(self, s: str) -> str:
#         stk = []
#         for ch in s:
#             if ch != ')':
#                 stk.append(ch)
#                 continue

#             tmp = []
#             while stk[-1] != '(':
#                 tmp.append(stk.pop())
#             stk.pop()

#             for t in tmp:
#                 stk.append(t)

#         return ''.join(stk)

if __name__ == '__main__':
    solu = Solution()
    print(solu.reverseParentheses(s="(abcd)"))
    print(solu.reverseParentheses(s="(u(love)i)"))
    print(solu.reverseParentheses(s="(ed(et(oc))el)"))
    print(solu.reverseParentheses(s="a(bcdefghijkl(mno)p)q"))
    print(solu.reverseParentheses(s="a((ef)d(bc))g"))
