#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   721.账户合并.py
@Time    :   2021/01/18 22:33:16
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=721 lang=python3
#
# [721] 账户合并
#
# https://leetcode-cn.com/problems/accounts-merge/description/
#
# algorithms
# Medium (44.74%)
# Likes:    204
# Dislikes: 0
# Total Accepted:    18.8K
# Total Submissions: 41.9K
# Testcase Example:
# '[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]'
#
# 给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称
# (name)，其余元素是 emails 表示该账户的邮箱地址。
#
#
# 现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。
#
# 合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是按字符 ASCII 顺序排列的邮箱地址。账户本身可以以任意顺序返回。
#
#
#
# 示例 1：
#
#
# 输入：
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John",
# "johnnybravo@mail.com"], ["John", "johnsmith@mail.com",
# "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# 输出：
# [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
# ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# 解释：
# 第一个和第三个 John 是同一个人，因为他们有共同的邮箱地址 "johnsmith@mail.com"。
# 第二个 John 和 Mary 是不同的人，因为他们的邮箱地址没有被其他帐户使用。
# 可以以任何顺序返回这些列表，例如答案 [['Mary'，'mary@mail.com']，['John'，'johnnybravo@mail.com']，
# ['John'，'john00@mail.com'，'john_newyork@mail.com'，'johnsmith@mail.com']]
# 也是正确的。
#
#
#
#
# 提示：
#
#
# accounts的长度将在[1，1000]的范围内。
# accounts[i]的长度将在[1，10]的范围内。
# accounts[i][j]的长度将在[1，30]的范围内。
#
#
#
from collections import defaultdict
from typing import List


# @lc code=start
class UnionFind:
    def __init__(self, n: int):
        self.par = list(range(n))

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> None:
        self.par[self.find(x)] = self.par[self.find(y)]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email2name = {}
        email2indice = {}
        n = 0
        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                if account[i] not in email2name:
                    email2name[account[i]] = name
                    email2indice[account[i]] = n
                    n += 1

        uf = UnionFind(n)
        for account in accounts:
            for i in range(2, len(account)):
                uf.union(email2indice[account[i - 1]],
                         email2indice[account[i]])

        block2emails = defaultdict(list)
        for email, indice in email2indice.items():
            bid = uf.find(indice)
            block2emails[bid].append(email)

        ans = []
        for emails in block2emails.values():
            name = email2name[emails[0]]
            emails.sort()
            ans.append([name] + emails)

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
                ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["Mary", "mary@mail.com"]]
    print(solu.accountsMerge(accounts))
