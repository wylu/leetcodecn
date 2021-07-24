#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1736.替换隐藏数字得到的最晚时间.py
@Time    :   2021/07/24 21:18:57
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1736 lang=python3
#
# [1736] 替换隐藏数字得到的最晚时间
#
# https://leetcode-cn.com/problems/latest-time-by-replacing-hidden-digits/description/
#
# algorithms
# Easy (44.27%)
# Likes:    46
# Dislikes: 0
# Total Accepted:    22.9K
# Total Submissions: 51.7K
# Testcase Example:  '"2?:?0"'
#
# 给你一个字符串 time ，格式为  hh:mm（小时：分钟），其中某几位数字被隐藏（用 ? 表示）。
#
# 有效的时间为 00:00 到 23:59 之间的所有时间，包括 00:00 和 23:59 。
#
# 替换 time 中隐藏的数字，返回你可以得到的最晚有效时间。
#
#
#
# 示例 1：
#
#
# 输入：time = "2?:?0"
# 输出："23:50"
# 解释：以数字 '2' 开头的最晚一小时是 23 ，以 '0' 结尾的最晚一分钟是 50 。
#
#
# 示例 2：
#
#
# 输入：time = "0?:3?"
# 输出："09:39"
#
#
# 示例 3：
#
#
# 输入：time = "1?:22"
# 输出："19:22"
#
#
#
#
# 提示：
#
#
# time 的格式为 hh:mm
# 题目数据保证你可以由输入的字符串生成有效的时间
#
#
#


# @lc code=start
class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)
        if time[3] == '?':
            time[3] = '5'
        if time[4] == '?':
            time[4] = '9'

        if time[0] == '?' and time[1] == '?':
            time[0], time[1] = '2', '3'
        elif time[0] == '?':
            time[0] = '2' if time[1] <= '3' else '1'
        elif time[1] == '?':
            time[1] = '9' if time[0] <= '1' else '3'

        return ''.join(time)


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.maximumTime(time="2?:?0"))
    print(solu.maximumTime(time="0?:3?"))
    print(solu.maximumTime(time="1?:22"))
    print(solu.maximumTime(time="00:01"))
