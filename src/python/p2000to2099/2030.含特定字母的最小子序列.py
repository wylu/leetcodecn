#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2030.含特定字母的最小子序列.py
@Time    :   2021/10/22 22:26:31
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=2030 lang=python3
#
# [2030] 含特定字母的最小子序列
#
# https://leetcode-cn.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/description/
#
# algorithms
# Hard (34.25%)
# Likes:    11
# Dislikes: 0
# Total Accepted:    1.2K
# Total Submissions: 3.4K
# Testcase Example:  '"leet"\n3\n"e"\n1'
#
# 给你一个字符串 s ，一个整数 k ，一个字母 letter 以及另一个整数 repetition 。
#
# 返回 s 中长度为 k 且 字典序最小 的子序列，该子序列同时应满足字母 letter 出现 至少 repetition 次。生成的测试用例满足
# letter 在 s 中出现 至少 repetition 次。
#
# 子序列 是由原字符串删除一些（或不删除）字符且不改变剩余字符顺序得到的剩余字符串。
#
# 字符串 a 字典序比字符串 b 小的定义为：在 a 和 b 出现不同字符的第一个位置上，字符串 a 的字符在字母表中的顺序早于字符串 b 的字符。
#
#
#
# 示例 1：
#
#
# 输入：s = "leet", k = 3, letter = "e", repetition = 1
# 输出："eet"
# 解释：存在 4 个长度为 3 ，且满足字母 'e' 出现至少 1 次的子序列：
# - "lee"（"leet"）
# - "let"（"leet"）
# - "let"（"leet"）
# - "eet"（"leet"）
# 其中字典序最小的子序列是 "eet" 。
#
#
# 示例 2：
#
#
#
#
# 输入：s = "leetcode", k = 4, letter = "e", repetition = 2
# 输出："ecde"
# 解释："ecde" 是长度为 4 且满足字母 "e" 出现至少 2 次的字典序最小的子序列。
#
#
# 示例 3：
#
#
# 输入：s = "bb", k = 2, letter = "b", repetition = 2
# 输出："bb"
# 解释："bb" 是唯一一个长度为 2 且满足字母 "b" 出现至少 2 次的子序列。
#
#
#
#
# 提示：
#
#
# 1 <= repetition <= k <= s.length <= 5 * 10^4
# s 由小写英文字母组成
# letter 是一个小写英文字母，在 s 中至少出现 repetition 次
#
#
#
from collections import deque
"""
方法一：贪心
我们可以逐位来考虑。我们希望每一位都尽可能小，但同时需要满足以下条件：

1.这一位的位置应当大于上一位的位置；
2.这一位后面需要有足够多的字母，以使得总长度能够达到 K；
3.这一位后面需要有足够多的 letter，以使得 letter 的个数能够达到 repetition。

针对 1，我们使用 26 个队列来存储 26 个字母的位置；
针对 3，我们预处理出每个位置后面 letter 的个数。

接下来，我们就进行逐位枚举。对于每一位，我们都枚举 a 到 z ，如果枚举到一个
字母能够满足条件，就选用这个字母，同时进行相应的更新操作：

1.更新上一位的位置；
2.更新队列；
3.如果这个字母恰好是 letter，更新 repetition。

因为题目保证了至少有 repetition 个 letter，所以一定有解，不需要考虑无解的情况。
"""


# @lc code=start
class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str,
                            repetition: int) -> str:
        n = len(s)
        rem = [0] * n
        for i in range(n - 2, -1, -1):
            rem[i] = rem[i + 1] + int(s[i + 1] == letter)

        pos = [deque() for _ in range(26)]
        for i, ch in enumerate(s):
            pos[ord(ch) - ord('a')].append(i)

        last = -1
        ans = []
        for i in range(k):
            for j in range(26):
                while pos[j] and pos[j][0] < last:
                    pos[j].popleft()

                ch = chr(j + ord('a'))
                need = repetition - int(ch == letter)
                if (pos[j] and k - i - 1 >= need and rem[pos[j][0]] >= need
                        and n - pos[j][0] - 1 >= k - i - 1):
                    ans.append(ch)
                    last = pos[j][0]
                    pos[j].popleft()
                    if ch == letter:
                        repetition -= 1
                    break

        return ''.join(ans)


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.smallestSubsequence(s="leet", k=3, letter="e", repetition=1))
    print(solu.smallestSubsequence(s="leetcode", k=4, letter="e",
                                   repetition=2))
    print(solu.smallestSubsequence(s="bb", k=2, letter="b", repetition=2))
