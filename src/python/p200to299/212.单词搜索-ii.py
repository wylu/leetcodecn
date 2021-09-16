#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   212.单词搜索-ii.py
@Time    :   2021/09/16 09:10:18
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#
# https://leetcode-cn.com/problems/word-search-ii/description/
#
# algorithms
# Hard (45.36%)
# Likes:    454
# Dislikes: 0
# Total Accepted:    42.9K
# Total Submissions: 94.6K
# Testcase Example:
# '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n'
# + '["oath","pea","eat","rain"]'
#
# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。
#
# 单词必须按照字母顺序，通过 相邻的单元格
# 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
#
#
#
# 示例 1：
#
#
# 输入：board =
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# 输出：["eat","oath"]
#
#
# 示例 2：
#
#
# 输入：board = [["a","b"],["c","d"]], words = ["abcb"]
# 输出：[]
#
#
#
#
# 提示：
#
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] 是一个小写英文字母
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10
# words[i] 由小写英文字母组成
# words 中的所有字符串互不相同
#
#
#
from collections import defaultdict
from typing import List
"""
方法一：回溯 + 字典树
预备知识

前缀树（字典树）是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。
前缀树可以用 O(|S|) 的时间复杂度完成如下操作，其中 |S| 是插入字符串或查询
前缀的长度：

向前缀树中插入字符串 word；

查询前缀串 prefix 是否为已经插入到前缀树中的任意一个字符串 word 的前缀；

前缀树的实现可以参考「208. 实现 Trie (前缀树) 的官方题解」。

思路和算法

根据题意，我们需要逐个遍历二维网格中的每一个单元格；然后搜索从该单元格出发
的所有路径，找到其中对应 words 中的单词的路径。因为这是一个回溯的过程，
所以我们有如下算法：

遍历二维网格中的所有单元格。

深度优先搜索所有从当前正在遍历的单元格出发的、由相邻且不重复的单元格组成的
路径。因为题目要求同一个单元格内的字母在一个单词中不能被重复使用；所以我们
在深度优先搜索的过程中，每经过一个单元格，都将该单元格的字母临时修改为特殊
字符（例如 #），以避免再次经过该单元格。

如果当前路径是 words 中的单词，则将其添加到结果集中。如果当前路径是 words
中任意一个单词的前缀，则继续搜索；反之，如果当前路径不是 words 中任意一个
单词的前缀，则剪枝。我们可以将 words 中的所有字符串先添加到前缀树中，而后
用 O(|S|) 的时间复杂度查询当前路径是否为 words 中任意一个单词的前缀。

在具体实现中，我们需要注意如下情况：

因为同一个单词可能在多个不同的路径中出现，所以我们需要使用哈希集合对结果集
去重。

在回溯的过程中，我们不需要每一步都判断完整的当前路径是否是 words 中任意
一个单词的前缀；而是可以记录下路径中每个单元格所对应的前缀树结点，每次只
需要判断新增单元格的字母是否是上一个单元格对应前缀树结点的子结点即可。
"""


# @lc code=start
class Trie:
    def __init__(self) -> None:
        self.children = defaultdict(Trie)
        self.word = ""

    def insert(self, word: str) -> None:
        cur = self
        for ch in word:
            cur = cur.children[ch]
        cur.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        d = (0, 1, 0, -1, 0)
        ans = set()
        m, n = len(board), len(board[0])

        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(cur: Trie, x: int, y: int) -> None:
            if board[x][y] not in cur.children:
                return

            ch = board[x][y]

            cur = cur.children[ch]
            if cur.word:
                ans.add(cur.word)

            board[x][y] = '#'
            for i in range(4):
                nx, ny = x + d[i], y + d[i + 1]
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] != '#':
                    dfs(cur, nx, ny)
            board[x][y] = ch

        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)

        return list(ans)


# @lc code=end

if __name__ == '__main__':
    solu = Solution()

    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"],
             ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    print(solu.findWords(board, words))

    board = [["a", "b"], ["c", "d"]]
    words = ["abcb"]
    print(solu.findWords(board, words))
