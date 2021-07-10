#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   981.基于时间的键值存储.py
@Time    :   2021/07/10 15:27:51
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=981 lang=python3
#
# [981] 基于时间的键值存储
#
# https://leetcode-cn.com/problems/time-based-key-value-store/description/
#
# algorithms
# Medium (51.53%)
# Likes:    109
# Dislikes: 0
# Total Accepted:    11.4K
# Total Submissions: 22.1K
# Testcase Example:
# '["TimeMap","set","get","get","set","get","get"]\n' +
# '[[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]'
#
# 创建一个基于时间的键值存储类 TimeMap，它支持下面两个操作：
#
# 1. set(string key, string value, int timestamp)
#
#
# 存储键 key、值 value，以及给定的时间戳 timestamp。
#
#
# 2. get(string key, int timestamp)
#
#
# 返回先前调用 set(key, value, timestamp_prev) 所存储的值，其中 timestamp_prev <=
# timestamp。
# 如果有多个这样的值，则返回对应最大的  timestamp_prev 的那个值。
# 如果没有值，则返回空字符串（""）。
#
#
#
#
# 示例 1：
#
# 输入：inputs = ["TimeMap","set","get","get","set","get","get"], inputs =
# [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
# 输出：[null,null,"bar","bar",null,"bar2","bar2"]
# 解释：
# TimeMap kv;
# kv.set("foo", "bar", 1); // 存储键 "foo" 和值 "bar" 以及时间戳 timestamp = 1
# kv.get("foo", 1);  // 输出 "bar"
# kv.get("foo", 3); // 输出 "bar" 因为在时间戳 3 和时间戳 2 处没有对应 "foo" 的值，所以唯一的值位于时间戳 1
# 处（即 "bar"）
# kv.set("foo", "bar2", 4);
# kv.get("foo", 4); // 输出 "bar2"
# kv.get("foo", 5); // 输出 "bar2"
#
#
#
# 示例 2：
#
# 输入：inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs =
# [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
# 输出：[null,null,null,"","high","high","low","low"]
#
#
#
#
# 提示：
#
#
# 所有的键/值字符串都是小写的。
# 所有的键/值字符串长度都在 [1, 100] 范围内。
# 所有 TimeMap.set 操作中的时间戳 timestamps 都是严格递增的。
# 1 <= timestamp <= 10^7
# TimeMap.set 和 TimeMap.get 函数在每个测试用例中将（组合）调用总计 120000 次。
#
#
#
# import bisect
from collections import defaultdict


# @lc code=start
class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        idx = self.search(key, timestamp) - 1
        return self.data[key][idx][1] if idx >= 0 else ''

    def search(self, key: str, timestamp: int) -> int:
        """search right bound"""
        left, right = 0, len(self.data[key])
        while left < right:
            mid = (left + right) // 2
            if self.data[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        return left


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

# class Node(object):
#     def __init__(self, timestamp: int, value: str) -> None:
#         self.timestamp = timestamp
#         self.value = value

#     def __lt__(self, other: 'Node') -> bool:
#         return self.timestamp < other.timestamp

#     # def __repr__(self):
#     #     return f'Node(value:{self.value},timestamp:{self.timestamp})'

# class TimeMap:
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.data = defaultdict(list)

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         self.data[key].append(Node(timestamp, value))

#     def get(self, key: str, timestamp: int) -> str:
#         idx = bisect.bisect_right(self.data[key], Node(timestamp, 0)) - 1
#         if idx < 0:
#             return ''
#         return self.data[key][idx].value

# ---------------------------------------------------------------

# from sortedcontainers import SortedList  # noqa: F401

# class TimeMap:
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.data = {}
#         self.order = defaultdict(SortedList)

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         self.order[key].add(timestamp)
#         self.data[key + '-' + str(timestamp)] = value

#     def get(self, key: str, timestamp: int) -> str:
#         idx = self.order[key].bisect_right(timestamp) - 1
#         if idx < 0:
#             return ''
#         return self.data[key + '-' + str(self.order[key][idx])]

if __name__ == '__main__':
    time_map = TimeMap()
    time_map.set('foo', 'bar', 1)
    print(time_map.get('foo', 1))
    print(time_map.get('foo', 3))
    time_map.set('foo', 'bar2', 4)
    print(time_map.get('foo', 4))
    print(time_map.get('foo', 5))

    print('---------------------------------')

    time_map = TimeMap()
    time_map.set('love', 'high', 10)
    time_map.set('love', 'low', 20)
    print(time_map.get('love', 5))
    print(time_map.get('love', 10))
    print(time_map.get('love', 15))
    print(time_map.get('love', 20))
    print(time_map.get('love', 25))
