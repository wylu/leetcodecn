#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1542.找出最长的超赞子字符串.py
@Time    :   2020/08/10 22:15:42
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1542 lang=python3
#
# [1542] 找出最长的超赞子字符串
#
# https://leetcode-cn.com/problems/find-longest-awesome-substring/description/
#
# algorithms
# Hard (29.05%)
# Likes:    14
# Dislikes: 0
# Total Accepted:    887
# Total Submissions: 3.1K
# Testcase Example:  '"3242415"'
#
# 给你一个字符串 s 。请返回 s 中最长的 超赞子字符串 的长度。
#
# 「超赞子字符串」需满足满足下述两个条件：
#
#
# 该字符串是 s 的一个非空子字符串
# 进行任意次数的字符交换后，该字符串可以变成一个回文字符串
#
#
#
#
# 示例 1：
#
# 输入：s = "3242415"
# 输出：5
# 解释："24241" 是最长的超赞子字符串，交换其中的字符后，可以得到回文 "24142"
#
#
# 示例 2：
#
# 输入：s = "12345678"
# 输出：1
#
#
# 示例 3：
#
# 输入：s = "213123"
# 输出：6
# 解释："213123" 是最长的超赞子字符串，交换其中的字符后，可以得到回文 "231132"
#
#
# 示例 4：
#
# 输入：s = "00"
# 输出：2
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 10^5
# s 仅由数字组成
#
#
#
"""
前缀和 + 状态压缩

每个子串我们只关心每个数字出现的次数是奇数次还是偶数次。
符合条件的 "超赞子字符串" 只有 2 种可能：
  1. 所有字符都出现偶数次；
  2. 除一个字符出现奇数次，其余所有字符都出现偶数次；

（1）所有字符都出现偶数次
对于这种情况，所有字符异或后等于 0，我们使用 0 来标记该状态

（2）除一个字符出现奇数次，其余所有字符都出现偶数次
对于这种情况，又可分为 10 种状态：
  - 0 出现奇数次，我们使用 1 << 0 来标记该状态
  - 1 出现奇数次，我们使用 1 << 1 来标记该状态
  - 2 出现奇数次，我们使用 1 << 2 来标记该状态
  - 3 出现奇数次，我们使用 1 << 3 来标记该状态
      ...
  - 9 出现奇数次，我们使用 1 << 9 来标记该状态

我们从左往右扫描字符串，记录其每个前缀对应的 state 值。
若一个字符串 s[i...j] 为第 1 类回文串， 则存在 i 使得 s[0...i-1] xor s[0...j] = 0;
若一个字符串 s[i...j] 为第 2 类回文串， 则存在 i 使得 s[0...i-1] xor s[0...j]
的二进制表示中仅有 1 位 1（共10种可能）;

以上两种共计 11 种情况， 我们只需判断每种可能是否存在即可。
时间复杂度 O(nC)，C 为字符集大小。
"""


# @lc code=start
class Solution:
    def longestAwesome(self, s: str) -> int:
        good = [0]
        for i in range(10):
            good.append(1 << i)

        first = [-1] * (1 << 10)
        first[0] = 0

        ans = 0
        state = 0
        for i in range(1, len(s) + 1):
            c = int(s[i - 1])
            state ^= (1 << c)

            if first[state] == -1:
                first[state] = i

            for g in good:
                need = g ^ state
                if first[need] != -1:
                    ans = max(ans, i - first[need])

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.longestAwesome('3242415'))
    print(solu.longestAwesome('0123'))
