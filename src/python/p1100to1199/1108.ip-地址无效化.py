#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1108.ip-地址无效化.py
@Time    :   2022/06/21 16:55:40
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1108 lang=python3
#
# [1108] IP 地址无效化
#
# https://leetcode.cn/problems/defanging-an-ip-address/description/
#
# algorithms
# Easy (85.36%)
# Likes:    105
# Dislikes: 0
# Total Accepted:    93K
# Total Submissions: 109K
# Testcase Example:  '"1.1.1.1"'
#
# 给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。
#
# 所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。
#
#
#
# 示例 1：
#
# 输入：address = "1.1.1.1"
# 输出："1[.]1[.]1[.]1"
#
#
# 示例 2：
#
# 输入：address = "255.100.50.0"
# 输出："255[.]100[.]50[.]0"
#
#
#
#
# 提示：
#
#
# 给出的 address 是一个有效的 IPv4 地址
#
#
#


# @lc code=start
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


# @lc code=end
