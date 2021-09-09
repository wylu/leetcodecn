#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   68.文本左右对齐.py
@Time    :   2021/09/09 12:48:27
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#
# https://leetcode-cn.com/problems/text-justification/description/
#
# algorithms
# Hard (50.34%)
# Likes:    185
# Dislikes: 0
# Total Accepted:    26.1K
# Total Submissions: 51.9K
# Testcase Example:
# '["This", "is", "an", "example", "of", "text", "justification."]\n16'
#
# 给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
#
# 你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。
#
# 要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
#
# 文本的最后一行应为左对齐，且单词之间不插入额外的空格。
#
# 说明:
#
#
# 单词是指由非空格字符组成的字符序列。
# 每个单词的长度大于 0，小于等于 maxWidth。
# 输入单词数组 words 至少包含一个单词。
#
#
# 示例:
#
# 输入:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# 输出:
# [
# "This    is    an",
# "example  of text",
# "justification.  "
# ]
#
#
# 示例 2:
#
# 输入:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# 输出:
# [
# "What   must   be",
# "acknowledgment  ",
# "shall be        "
# ]
# 解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
# 因为最后一行应为左对齐，而不是左右两端对齐。
# ⁠    第二行同样为左对齐，这是因为这行只包含一个单词。
#
#
# 示例 3:
#
# 输入:
# words =
# ["Science","is","what","we","understand","well","enough","to","explain",
# "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# 输出:
# [
# "Science  is  what we",
# ⁠ "understand      well",
# "enough to explain to",
# "a  computer.  Art is",
# "everything  else  we",
# "do                  "
# ]
#
#
#
from collections import deque
from typing import List


# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        cur, size = deque(), 0

        def fill_blank() -> str:
            gaps = len(cur) - 1
            blanks = maxWidth - size

            line = []
            while cur:
                line.append(cur.popleft())
                d, r = divmod(blanks, gaps) if gaps else (blanks, 0)
                c = d + (1 if r else 0)
                line.append(' ' * c)
                blanks -= c
                gaps -= 1

            return ''.join(line)

        for word in words:
            if size + len(word) + len(cur) > maxWidth:
                lines.append(fill_blank())
                cur, size = deque(), 0

            size += len(word)
            cur.append(word)

        last_line = ' '.join(cur)
        lines.append(last_line + ' ' * (maxWidth - len(last_line)))

        return lines


# @lc code=end

if __name__ == '__main__':
    solu = Solution()

    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    print(solu.fullJustify(words, maxWidth))

    words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    maxWidth = 16
    print(solu.fullJustify(words, maxWidth))

    words = [
        "Science", "is", "what", "we", "understand", "well", "enough", "to",
        "explain", "to", "a", "computer.", "Art", "is", "everything", "else",
        "we", "do"
    ]
    maxWidth = 20
    print(solu.fullJustify(words, maxWidth))

# class Solution:
#     def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
#         lines = []
#         cur, size = deque(), 0

#         def fill_blank() -> str:
#             gaps = len(cur) - 1
#             blanks = maxWidth - (size - gaps)
#             # print(f'blanks: {blanks}, size: {size}, gaps: {gaps}')

#             line = []
#             while cur:
#                 line.append(cur.popleft())
#                 d, r = divmod(blanks, gaps) if gaps else (blanks, 0)
#                 c = d + (1 if r else 0)
#                 line.append(' ' * c)
#                 blanks -= c
#                 gaps -= 1

#             return ''.join(line)

#         for word in words:
#             need = len(word)
#             if size:
#                 need += 1

#             if size + need > maxWidth:
#                 lines.append(fill_blank())
#                 cur, size = deque(), len(word)
#             else:
#                 size += need

#             cur.append(word)

#         if cur:
#             line = ' '.join(cur)
#             line += ' ' * (maxWidth - len(line))
#             lines.append(line)

#         return lines
