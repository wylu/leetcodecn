#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1202.交换字符串中的元素.py
@Time    :   2021/01/11 22:27:56
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1202 lang=python3
#
# [1202] 交换字符串中的元素
#
# https://leetcode-cn.com/problems/smallest-string-with-swaps/description/
#
# algorithms
# Medium (47.92%)
# Likes:    179
# Dislikes: 0
# Total Accepted:    18K
# Total Submissions: 37.3K
# Testcase Example:  '"dcab"\n[[0,3],[1,2]]'
#
# 给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0
# 开始）。
#
# 你可以 任意多次交换 在 pairs 中任意一对索引处的字符。
#
# 返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。
#
#
#
# 示例 1:
#
# 输入：s = "dcab", pairs = [[0,3],[1,2]]
# 输出："bacd"
# 解释：
# 交换 s[0] 和 s[3], s = "bcad"
# 交换 s[1] 和 s[2], s = "bacd"
#
#
# 示例 2：
#
# 输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# 输出："abcd"
# 解释：
# 交换 s[0] 和 s[3], s = "bcad"
# 交换 s[0] 和 s[2], s = "acbd"
# 交换 s[1] 和 s[2], s = "abcd"
#
# 示例 3：
#
# 输入：s = "cba", pairs = [[0,1],[1,2]]
# 输出："abc"
# 解释：
# 交换 s[0] 和 s[1], s = "bca"
# 交换 s[1] 和 s[2], s = "bac"
# 交换 s[0] 和 s[1], s = "abc"
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 10^5
# 0 <= pairs.length <= 10^5
# 0 <= pairs[i][0], pairs[i][1] < s.length
# s 中只含有小写英文字母
#
#
#
from collections import defaultdict
from typing import List
"""
方法一：并查集
思路及解法

既然可以任意地交换通过「索引对」直接相连的字符，那么我们也任意地交换
通过「索引对」间接相连的字符。我们利用这个性质将该字符串抽象：将每
一个字符抽象为「点」，那么这些「索引对」即为「边」，我们只需要维护这个
「图」的连通性即可。对于同属一个连通块（极大连通子图）内的字符，我们
可以任意地交换它们。

这样我们的思路就很清晰了：利用并查集维护任意两点的连通性，将同属一个
连通块内的点提取出来，直接排序后放置回其在字符串中的原位置即可。
"""


# @lc code=start
class UnionFind:
    def __init__(self, n: int):
        self.par = list(range(n))

    def union(self, x: int, y: int) -> None:
        self.par[self.find(x)] = self.find(y)

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        if not pairs:
            return s

        n = len(s)
        uf = UnionFind(n)
        for i, j in pairs:
            uf.union(i, j)

        blocks = defaultdict(list)
        for i in range(n):
            blocks[uf.find(i)].append(s[i])

        for block in blocks.values():
            block.sort(reverse=True)

        ans = []
        for i in range(n):
            ans.append(blocks[uf.find(i)].pop())

        return ''.join(ans)


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2]]))

    s = "dcab"
    pairs = [[0, 3], [1, 2], [0, 2]]
    print(solu.smallestStringWithSwaps(s, pairs))

    print(solu.smallestStringWithSwaps(s="cba", pairs=[[0, 1], [1, 2]]))
