#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   208.实现-trie-前缀树.py
@Time    :   2021/04/14 22:18:51
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#
# https://leetcode-cn.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (70.08%)
# Likes:    718
# Dislikes: 0
# Total Accepted:    107.5K
# Total Submissions: 150.6K
# Testcase Example:
# '["Trie","insert","search","search","startsWith","insert","search"]\n'
# + '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# Trie（发音类似 "try"）或者说 前缀树
# 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。
#
# 请你实现 Trie 类：
#
#
# Trie() 初始化前缀树对象。
# void insert(String word) 向前缀树中插入字符串 word 。
# boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false
# 。
# boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true
# ；否则，返回 false 。
#
#
#
#
# 示例：
#
#
# 输入
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# 输出
# [null, null, true, false, true, null, true]
#
# 解释
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // 返回 True
# trie.search("app");     // 返回 False
# trie.startsWith("app"); // 返回 True
# trie.insert("app");
# trie.search("app");     // 返回 True
#
#
#
#
# 提示：
#
#
# 1 <= word.length, prefix.length <= 2000
# word 和 prefix 仅由小写英文字母组成
# insert、search 和 startsWith 调用次数 总计 不超过 3 * 10^4 次
#
#
#


# @lc code=start
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.next = [None] * 26
        self.flag = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if not cur.next[idx]:
                cur.next[idx] = Trie()
            cur = cur.next[idx]
        cur.flag = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.searchPrefix(word)
        return cur is not None and cur.flag

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts
        with the given prefix.
        """
        return self.searchPrefix(prefix) is not None

    def searchPrefix(self, prefix: str) -> 'Trie':
        cur = self
        for ch in prefix:
            ch = ord(ch) - ord('a')
            if not cur.next[ch]:
                return
            cur = cur.next[ch]
        return cur


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
