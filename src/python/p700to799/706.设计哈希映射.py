#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   706.设计哈希映射.py
@Time    :   2021/03/14 11:52:29
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=706 lang=python3
#
# [706] 设计哈希映射
#
# https://leetcode-cn.com/problems/design-hashmap/description/
#
# algorithms
# Easy (62.13%)
# Likes:    143
# Dislikes: 0
# Total Accepted:    30.3K
# Total Submissions: 48.9K
# Testcase Example:
# '["MyHashMap","put","put","get","get","put","get","remove","get"]\n' +
# '[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]'
#
# 不使用任何内建的哈希表库设计一个哈希映射（HashMap）。
#
# 实现 MyHashMap 类：
#
#
# MyHashMap() 用空映射初始化对象
# void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key
# 已经存在于映射中，则更新其对应的值 value 。
# int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
# void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。
#
#
#
#
# 示例：
#
#
# 输入：
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# 输出：
# [null, null, null, 1, -1, null, 1, null, -1]
#
# 解释：
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // myHashMap 现在为 [[1,1]]
# myHashMap.put(2, 2); // myHashMap 现在为 [[1,1], [2,2]]
# myHashMap.get(1);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,2]]
# myHashMap.get(3);    // 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]]
# myHashMap.put(2, 1); // myHashMap 现在为 [[1,1], [2,1]]（更新已有的值）
# myHashMap.get(2);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,1]]
# myHashMap.remove(2); // 删除键为 2 的数据，myHashMap 现在为 [[1,1]]
# myHashMap.get(2);    // 返回 -1（未找到），myHashMap 现在为 [[1,1]]
#
#
#
#
# 提示：
#
#
# 0 <= key, value <= 10^6
# 最多调用 10^4 次 put、get 和 remove 方法
#
#
#
#
# 进阶：你能否不使用内置的 HashMap 库解决此问题？
#
#


# @lc code=start
class MyHashMap:
    def __init__(self):
        """Initialize your data structure here."""
        self.base = 769
        self.data = [[] for _ in range(self.base)]

    def _get_hash(self, key: int) -> int:
        return key % self.base

    def _contains(self, key: int) -> int:
        i = self._get_hash(key)
        for j, item in enumerate(self.data[i]):
            if item[0] == key:
                return i, j
        return i, -1

    def put(self, key: int, value: int) -> None:
        """value will always be non-negative."""
        i, j = self._contains(key)
        if j == -1:
            self.data[i].append((key, value))
        else:
            self.data[i][j] = (key, value)

    def get(self, key: int) -> int:
        """Returns the value to which the specified key is mapped,
        or -1 if this map contains no mapping for the key"""
        i, j = self._contains(key)
        return -1 if j == -1 else self.data[i][j][1]

    def remove(self, key: int) -> None:
        """Removes the mapping of the specified value key if this
        map contains a mapping for the key
        """
        i, j = self._contains(key)
        if j != -1:
            self.data[i].remove(self.data[i][j])


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end
