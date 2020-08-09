#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   93.复原ip地址.py
@Time    :   2020/08/09 22:16:36
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#
# https://leetcode-cn.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (47.20%)
# Likes:    374
# Dislikes: 0
# Total Accepted:    69.2K
# Total Submissions: 142.5K
# Testcase Example:  '"25525511135"'
#
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
#
# 有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。
#
#
#
# 示例:
#
# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]
#
#
from typing import List


# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s or len(s) < 4 or len(s) > 12:
            return []

        ans = []
        segments = [0] * 4

        def dfs(seg_id: int, seg_start: int):
            # 如果找到了 4 段 IP 地址并且遍历完了字符串，那么就是一种答案
            if seg_id == 4:
                if seg_start == len(s):
                    ans.append('.'.join(str(seg) for seg in segments))
                return

            # 如果还没有找到 4 段 IP 地址就已经遍历完了字符串，那么提前回溯
            if seg_start == len(s):
                return

            # 由于不能有前导零，如果当前数字为 0，那么这一段 IP 地址只能为 0
            if s[seg_start] == '0':
                segments[seg_id] = 0
                dfs(seg_id + 1, seg_start + 1)
                return

            # 一般情况，枚举每一种可能性并递归
            addr = 0
            for seg_end in range(seg_start, len(s)):
                addr = addr * 10 + (ord(s[seg_end]) - ord('0'))
                if 0 < addr <= 255:
                    segments[seg_id] = addr
                    dfs(seg_id + 1, seg_end + 1)
                else:
                    break

        dfs(0, 0)
        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.restoreIpAddresses('25525511135'))
    print(solu.restoreIpAddresses('0000'))
    print(solu.restoreIpAddresses('010010'))
