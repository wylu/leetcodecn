#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   401.二进制手表.py
@Time    :   2021/06/21 19:05:32
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#
# https://leetcode-cn.com/problems/binary-watch/description/
#
# algorithms
# Easy (59.42%)
# Likes:    295
# Dislikes: 0
# Total Accepted:    43.1K
# Total Submissions: 72.5K
# Testcase Example:  '1'
#
# 二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。每个 LED 代表一个 0 或
# 1，最低位在右侧。
#
#
# 例如，下面的二进制手表读取 "3:25" 。
#
#
#
#
# （图源：WikiMedia - Binary clock samui moon.jpg ，许可协议：Attribution-ShareAlike 3.0
# Unported (CC BY-SA 3.0) ）
#
# 给你一个整数 turnedOn ，表示当前亮着的 LED 的数量，返回二进制手表可以表示的所有可能时间。你可以 按任意顺序 返回答案。
#
# 小时不会以零开头：
#
#
# 例如，"01:00" 是无效的时间，正确的写法应该是 "1:00" 。
#
#
# 分钟必须由两位数组成，可能会以零开头：
#
#
# 例如，"10:2" 是无效的时间，正确的写法应该是 "10:02" 。
#
#
#
#
# 示例 1：
#
#
# 输入：turnedOn = 1
# 输出：["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
#
#
# 示例 2：
#
#
# 输入：turnedOn = 9
# 输出：[]
#
#
#
#
# 提示：
#
#
# 0 <= turnedOn <= 10
#
#
#
from typing import List


# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for state in range(1 << 10):
            if bin(state).count('1') != turnedOn:
                continue

            hour = state & ((1 << 4) - 1)
            minute = state >> 4

            if hour < 12 and minute < 60:
                fill = ':0' if minute < 10 else ':'
                ans.append(str(hour) + fill + str(minute))

        return ans


# @lc code=end

# class Solution:
#     def readBinaryWatch(self, turnedOn: int) -> List[str]:
#         leds = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
#         ans = []
#         for state in range(1 << 10):
#             if bin(state).count('1') != turnedOn:
#                 continue

#             hour = minute = 0
#             for i in range(len(leds)):
#                 if state & (1 << i) == 0:
#                     continue

#                 if i < 4:
#                     hour += leds[i]
#                 else:
#                     minute += leds[i]

#             if hour < 12 and minute < 60:
#                 fill = ':0' if minute < 10 else ':'
#                 ans.append(str(hour) + fill + str(minute))

#         return ans

if __name__ == '__main__':
    solu = Solution()
    print(solu.readBinaryWatch(1))
    print(solu.readBinaryWatch(9))
    print(solu.readBinaryWatch(0))
