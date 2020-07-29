#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   7.整数反转.py
@Time    :   2020/07/27 22:02:55
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (34.47%)
# Likes:    2063
# Dislikes: 0
# Total Accepted:    415.3K
# Total Submissions: 1.2M
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#
#
# 示例 2:
#
# 输入: -123
# 输出: -321
#
#
# 示例 3:
#
# 输入: 120
# 输出: 21
#
#
# 注意:
#
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
#
#
"""
解题思路
取余%实现弹出
开始对负数直接取余，发现会出错（可能就我这个小白不知道），改成了对绝对值操作，最后在返回值加符号
然后在累加结果前做溢出判断，在加之后在判断不符合题目描述的 ‘环境只能存储得下 32 位的有符号整数’

代码

class Solution(object):
    def reverse(self, x):
        rev=0
        max=1<<31 if x<0 else (1<<31)-1
        absx=abs(x)
        while absx!=0:
            pop=absx%10
            absx=absx//10
            if rev>(max//10) or (rev==max//10 and pop>max%10):
                return 0
            rev=rev*10+pop
        return (rev if x>0 else -rev)
"""


# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        MAX = (1 << 31) if x < 0 else (1 << 31) - 1
        sign = 1 if x >= 0 else -1
        ans, x = 0, abs(x)

        while x != 0:
            pop = x % 10
            x //= 10

            if ans > MAX // 10 or (ans == MAX // 10 and pop > MAX % 10):
                return 0

            ans = ans * 10 + pop

        return sign * ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.reverse(-123))
    print(solu.reverse(1463847412))
