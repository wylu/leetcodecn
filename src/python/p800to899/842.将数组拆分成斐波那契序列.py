#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   842.将数组拆分成斐波那契序列.py
@Time    :   2020/12/08 22:32:08
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=842 lang=python3
#
# [842] 将数组拆分成斐波那契序列
#
# https://leetcode-cn.com/problems/split-array-into-fibonacci-sequence/description/
#
# algorithms
# Medium (48.83%)
# Likes:    170
# Dislikes: 0
# Total Accepted:    20.4K
# Total Submissions: 41.8K
# Testcase Example:  '"123456579"'
#
# 给定一个数字字符串 S，比如 S = "123456579"，我们可以将它分成斐波那契式的序列 [123, 456, 579]。
#
# 形式上，斐波那契式序列是一个非负整数列表 F，且满足：
#
#
# 0 <= F[i] <= 2^31 - 1，（也就是说，每个整数都符合 32 位有符号整数类型）；
# F.length >= 3；
# 对于所有的0 <= i < F.length - 2，都有 F[i] + F[i+1] = F[i+2] 成立。
#
#
# 另外，请注意，将字符串拆分成小块时，每个块的数字一定不要以零开头，除非这个块是数字 0 本身。
#
# 返回从 S 拆分出来的任意一组斐波那契式的序列块，如果不能拆分则返回 []。
#
#
#
# 示例 1：
#
# 输入："123456579"
# 输出：[123,456,579]
#
#
# 示例 2：
#
# 输入: "11235813"
# 输出: [1,1,2,3,5,8,13]
#
#
# 示例 3：
#
# 输入: "112358130"
# 输出: []
# 解释: 这项任务无法完成。
#
#
# 示例 4：
#
# 输入："0123"
# 输出：[]
# 解释：每个块的数字不能以零开头，因此 "01"，"2"，"3" 不是有效答案。
#
#
# 示例 5：
#
# 输入: "1101111"
# 输出: [110, 1, 111]
# 解释: 输出 [11,0,11,11] 也同样被接受。
#
#
#
#
# 提示：
#
#
# 1 <= S.length <= 200
# 字符串 S 中只含有数字。
#
#
#
from typing import List
"""
方法一：回溯 + 剪枝
将给定的字符串拆分成斐波那契式序列，可以通过回溯的方法实现。

使用列表存储拆分出的数，回溯过程中维护该列表的元素，列表初始为空。遍历
字符串的所有可能的前缀，作为当前被拆分出的数，然后对剩余部分继续拆分，
直到整个字符串拆分完毕。

根据斐波那契式序列的要求，从第 3 个数开始，每个数都等于前 2 个数的和，
因此从第 3 个数开始，需要判断拆分出的数是否等于前 2 个数的和，只有满足
要求时才进行拆分，否则不进行拆分。

回溯过程中，还有三处可以进行剪枝操作。

拆分出的数如果不是 0，则不能以 0 开头，因此如果字符串剩下的部分以 0
开头，就不需要考虑拆分出长度大于 1 的数，因为长度大于 1 的数以 0 开头
是不符合要求的，不可能继续拆分得到斐波那契式序列；

拆分出的数必须符合 32 位有符号整数类型，即每个数必须在 [0,2^31-1] 的
范围内，如果拆分出的数大于 2^31-1，则不符合要求，长度更大的数的数值也
一定更大，一定也大于 2^31-1，因此不可能继续拆分得到斐波那契式序列；

如果列表中至少有 2 个数，并且拆分出的数已经大于最后 2 个数的和，
就不需要继续尝试拆分了。

当整个字符串拆分完毕时，如果列表中至少有 3 个数，则得到一个符合要求
的斐波那契式序列，返回列表。如果没有找到符合要求的斐波那契式序列，
则返回空列表。

实现方面，回溯需要带返回值，表示是否存在符合要求的斐波那契式序列。
"""


# @lc code=start
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        ans, n = [], len(S)
        INT_MAX = 0x7FFFFFFF

        def backtrack(offset: int, f0: int, f1: int) -> bool:
            if offset == n:
                return len(ans) > 2

            f2 = 0
            for i in range(offset, n):
                # 每个块的数字不能以 0 开头，除非这个块是数字 0 本身
                if i > offset and S[offset] == '0':
                    break

                f2 = f2 * 10 + int(S[i])
                # 每个整数都符合 32 位有符号整数类型
                if f2 > INT_MAX:
                    break

                if len(ans) >= 2:
                    if f2 < f0 + f1:
                        continue
                    elif f2 > f0 + f1:
                        # 拆分出的数已经大于最后 2 个数的和
                        break

                ans.append(f2)
                if backtrack(i + 1, f1, f2):
                    return True
                ans.pop()

            return False

        backtrack(0, 0, 0)
        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.splitIntoFibonacci("123456579"))
    print(solu.splitIntoFibonacci("11235813"))
    print(solu.splitIntoFibonacci("112358130"))
    print(solu.splitIntoFibonacci("0123"))
    print(solu.splitIntoFibonacci("1101111"))
