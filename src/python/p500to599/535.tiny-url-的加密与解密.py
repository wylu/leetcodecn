#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   535.tiny-url-的加密与解密.py
@Time    :   2022/06/29 14:54:03
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=535 lang=python3
#
# [535] TinyURL 的加密与解密
#
# https://leetcode.cn/problems/encode-and-decode-tinyurl/description/
#
# algorithms
# Medium (86.79%)
# Likes:    187
# Dislikes: 0
# Total Accepted:    30.5K
# Total Submissions: 35.1K
# Testcase Example:  '"https://leetcode.com/problems/design-tinyurl"'
#
# TinyURL 是一种 URL 简化服务， 比如：当你输入一个 URL
# https://leetcode.com/problems/design-tinyurl 时，它将返回一个简化的URL
# http://tinyurl.com/4e9iAk 。请你设计一个类来加密与解密 TinyURL 。
#
# 加密和解密算法如何设计和运作是没有限制的，你只需要保证一个 URL 可以被加密成一个 TinyURL ，并且这个 TinyURL
# 可以用解密方法恢复成原本的 URL 。
#
# 实现 Solution 类：
#
#
#
#
# Solution() 初始化 TinyURL 系统对象。
# String encode(String longUrl) 返回 longUrl 对应的 TinyURL 。
# String decode(String shortUrl) 返回 shortUrl 原本的 URL 。题目数据保证给定的 shortUrl
# 是由同一个系统对象加密的。
#
#
#
#
# 示例：
#
#
# 输入：url = "https://leetcode.com/problems/design-tinyurl"
# 输出："https://leetcode.com/problems/design-tinyurl"
#
# 解释：
# Solution obj = new Solution();
# string tiny = obj.encode(url); // 返回加密后得到的 TinyURL 。
# string ans = obj.decode(tiny); // 返回解密后得到的原本的 URL 。
#
#
#
#
# 提示：
#
#
# 1 <= url.length <= 10^4
# 题目数据保证 url 是一个有效的 URL
#
#
#
#
#


# @lc code=start
class Codec:
    def __init__(self) -> None:
        self.id = 0
        self.db = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        self.id += 1
        self.db[self.id] = longUrl
        return 'http://tinyurl.com/%s' % self.id

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.db[int(shortUrl[shortUrl.rfind('/') + 1:])]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end
