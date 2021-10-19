#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   211.添加与搜索单词-数据结构设计.py
@Time    :   2021/10/19 14:02:49
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#
# https://leetcode-cn.com/problems/design-add-and-search-words-data-structure/description/
#
# algorithms
# Medium (49.79%)
# Likes:    328
# Dislikes: 0
# Total Accepted:    37.8K
# Total Submissions: 75.9K
# Testcase Example:
# '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n'
# + '[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# 请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。
#
# 实现词典类 WordDictionary ：
#
#
# WordDictionary() 初始化词典对象
# void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
# bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些
# '.' ，每个 . 都可以表示任何一个字母。
#
#
#
#
# 示例：
#
#
# 输入：
#
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# 输出：
# [null,null,null,null,false,true,true,true]
#
# 解释：
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
#
#
#
#
# 提示：
#
#
# 1 <= word.length <= 500
# addWord 中的 word 由小写英文字母组成
# search 中的 word 由 '.' 或小写英文字母组成
# 最多调用 50000 次 addWord 和 search
#
#
#


# @lc code=start
class Trie:
    def __init__(self) -> None:
        self.children = {}
        self.flag = False

    def insert(self, word: str) -> None:
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.flag = True

    def search(self, word: str, s: int) -> bool:
        cur = self
        for i in range(s, len(word)):
            ch = word[i]
            if ch == '.':
                for _, child in cur.children.items():
                    if child.search(word, i + 1):
                        return True
                return False

            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return cur.flag


class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
