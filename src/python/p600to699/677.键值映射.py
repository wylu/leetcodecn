#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   677.键值映射.py
@Time    :   2021/11/14 17:42:23
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=677 lang=python3
#
# [677] 键值映射
#
# https://leetcode-cn.com/problems/map-sum-pairs/description/
#
# algorithms
# Medium (65.21%)
# Likes:    161
# Dislikes: 0
# Total Accepted:    27.9K
# Total Submissions: 42.8K
# Testcase Example:  '["MapSum","insert","sum","insert","sum"]\n'
# + '[[],["apple",3],["ap"],["app",2],["ap"]]'
#
# 实现一个 MapSum 类，支持两个方法，insert 和 sum：
#
#
# MapSum() 初始化 MapSum 对象
# void insert(String key, int val) 插入 key-val 键值对，字符串表示键 key ，整数表示值 val 。如果键
# key 已经存在，那么原来的键值对将被替代成新的键值对。
# int sum(string prefix) 返回所有以该前缀 prefix 开头的键 key 的值的总和。
#
#
#
#
# 示例：
#
#
# 输入：
# ["MapSum", "insert", "sum", "insert", "sum"]
# [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
# 输出：
# [null, null, 3, null, 5]
#
# 解释：
# MapSum mapSum = new MapSum();
# mapSum.insert("apple", 3);
# mapSum.sum("ap");           // return 3 (apple = 3)
# mapSum.insert("app", 2);
# mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
#
#
#
#
# 提示：
#
#
# 1 <= key.length, prefix.length <= 50
# key 和 prefix 仅由小写英文字母组成
# 1 <= val <= 1000
# 最多调用 50 次 insert 和 sum
#
#
#

# @lc code=start
from typing import Optional


class Trie:
    def __init__(self, parent: Optional['Trie'] = None) -> None:
        self.val = 0
        self.total = 0
        self.children = {}
        self.parent = parent

    def insert(self, key: str, val: int) -> None:
        cur = self
        for ch in key:
            if ch not in cur.children:
                cur.children[ch] = Trie(parent=cur)
            cur = cur.children[ch]

        pre = cur
        while pre:
            pre.total += val - cur.val
            pre = pre.parent

        cur.val = val

    def search(self, prefix: str) -> int:
        cur = self
        for ch in prefix:
            if ch not in cur.children:
                return 0
            cur = cur.children[ch]
        return cur.total


class MapSum:
    def __init__(self):
        self.tire = Trie()

    def insert(self, key: str, val: int) -> None:
        self.tire.insert(key, val)

    def sum(self, prefix: str) -> int:
        return self.tire.search(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# @lc code=end
