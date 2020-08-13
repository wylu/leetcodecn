#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   43.字符串相乘.py
@Time    :   2020/08/05 23:35:54
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#
# https://leetcode-cn.com/problems/multiply-strings/description/
#
# algorithms
# Medium (42.56%)
# Likes:    406
# Dislikes: 0
# Total Accepted:    77.6K
# Total Submissions: 182.2K
# Testcase Example:  '"2"\n"3"'
#
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#
# 示例 1:
#
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
#
# 示例 2:
#
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
#
# 说明：
#
#
# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
#
#
#
"""
优化竖式

该算法是通过两数相乘时，乘数某位与被乘数某位相乘，与产生结果的位置的规律来完成。
具体规律如下：

乘数 num1 位数为 M，被乘数 num2 位数为 N，num1 * num2 结果 res 最大总位数为
M+N，num1[i] * num2[j] 的结果为 tmp(位数为两位，"0x","xy"的形式)，其第一位
位于 res[i+j]，第二位位于 res[i+j+1]。

结合下图更容易理解：

         index 1  | | |1|2|3| (index i)
         index 0  | | | |4|5| (index j)
                  -----------
                  | | | |1|5|
                  | | |1|0| |
                  | |0|5| | |
                  -----------
                  | | |1|2| |
    indices[1,2]  | |0|8| | | indices[i+j, i+j+1]
                  |0|4| | | |
                  -----------
            index  0 1 2 3 4
"""


# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if not num1 or not num2:
            return ''
        if num1 == '0' or num2 == '0':
            return '0'

        l1, l2 = len(num1), len(num2)
        ans = [0] * (l1 + l2)

        for i in range(l1 - 1, -1, -1):
            n1 = int(num1[i])
            for j in range(l2 - 1, -1, -1):
                n2 = int(num2[j])

                tmp = ans[i + j + 1] + n1 * n2
                ans[i + j + 1] = tmp % 10
                ans[i + j] += tmp // 10

        k = 0
        while ans[k] == 0:
            k += 1

        return ''.join(map(str, ans[k:]))


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.multiply('123', '456'))
    print(solu.multiply('123', '0'))
