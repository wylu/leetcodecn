#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   460.lfu-缓存.py
@Time    :   2021/10/02 11:05:17
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=460 lang=python3
#
# [460] LFU 缓存
#
# https://leetcode-cn.com/problems/lfu-cache/description/
#
# algorithms
# Hard (43.80%)
# Likes:    444
# Dislikes: 0
# Total Accepted:    33.9K
# Total Submissions: 77.3K
# Testcase Example:
# '["LFUCache","put","put","get","put","get","get","put","get","get","get"]\n'
# + '[[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]'
#
# 请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。
#
# 实现 LFUCache 类：
#
#
# LFUCache(int capacity) - 用数据结构的容量 capacity 初始化对象
# int get(int key) - 如果键存在于缓存中，则获取键的值，否则返回 -1。
# void put(int key, int value) -
# 如果键已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量时，则应该在插入新项之前，使最不经常使用的项无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除
# 最近最久未使用 的键。
#
#
# 注意「项的使用次数」就是自插入该项以来对其调用 get 和 put 函数的次数之和。使用次数会在对应项被移除后置为 0 。
#
# 为了确定最不常使用的键，可以为缓存中的每个键维护一个 使用计数器 。使用计数最小的键是最久未使用的键。
#
# 当一个键首次插入到缓存中时，它的使用计数器被设置为 1 (由于 put 操作)。对缓存中的键执行 get 或 put
# 操作，使用计数器的值将会递增。
#
#
#
# 示例：
#
#
# 输入：
# ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get",
# "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# 输出：
# [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
#
# 解释：
# // cnt(x) = 键 x 的使用计数
# // cache=[] 将显示最后一次使用的顺序（最左边的元素是最近的）
# LFUCache lFUCache = new LFUCache(2);
# lFUCache.put(1, 1);   // cache=[1,_], cnt(1)=1
# lFUCache.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
# lFUCache.get(1);      // 返回 1
# ⁠                     // cache=[1,2], cnt(2)=1, cnt(1)=2
# lFUCache.put(3, 3);   // 去除键 2 ，因为 cnt(2)=1 ，使用计数最小
# ⁠                     // cache=[3,1], cnt(3)=1, cnt(1)=2
# lFUCache.get(2);      // 返回 -1（未找到）
# lFUCache.get(3);      // 返回 3
# ⁠                     // cache=[3,1], cnt(3)=2, cnt(1)=2
# lFUCache.put(4, 4);   // 去除键 1 ，1 和 3 的 cnt 相同，但 1 最久未使用
# ⁠                     // cache=[4,3], cnt(4)=1, cnt(3)=2
# lFUCache.get(1);      // 返回 -1（未找到）
# lFUCache.get(3);      // 返回 3
# ⁠                     // cache=[3,4], cnt(4)=1, cnt(3)=3
# lFUCache.get(4);      // 返回 4
# ⁠                     // cache=[3,4], cnt(4)=2, cnt(3)=3
#
#
#
# 提示：
#
#
# 0 <= capacity, key, value <= 10^4
# 最多调用 10^5 次 get 和 put 方法
#
#
#
#
# 进阶：你可以为这两种操作设计时间复杂度为 O(1) 的实现吗？
#
#
from collections import defaultdict
"""
方法二：双哈希表
思路和算法

我们定义两个哈希表，第一个 freq_table 以频率 freq 为索引，每个索引
存放一个双向链表，这个链表里存放所有使用频率为 freq 的缓存，缓存里
存放三个信息，分别为键 key，值 value，以及使用频率 freq。第二个
key_table 以键值 key 为索引，每个索引存放对应缓存在 freq_table
中链表里的内存地址，这样我们就能利用两个哈希表来使得两个操作的时间
复杂度均为 O(1)。同时需要记录一个当前缓存最少使用的频率 minFreq，
这是为了删除操作服务的。

对于 get(key) 操作，我们能通过索引 key 在 key_table 中找到缓存在
freq_table 中的链表的内存地址，如果不存在直接返回 -1，否则我们能
获取到对应缓存的相关信息，这样我们就能知道缓存的键值还有使用频率，
直接返回 key 对应的值即可。

但是我们注意到 get 操作后这个缓存的使用频率加一了，所以我们需要更新
缓存在哈希表 freq_table 中的位置。已知这个缓存的键 key，值 value，
以及使用频率 freq，那么该缓存应该存放到 freq_table 中 freq + 1 索引
下的链表中。所以我们在当前链表中 O(1) 删除该缓存对应的节点，根据情况
更新 minFreq 值，然后将其O(1) 插入到 freq + 1 索引下的链表头完成更新。
这其中的操作复杂度均为 O(1)。你可能会疑惑更新的时候为什么是插入到链表头，
这其实是为了保证缓存在当前链表中从链表头到链表尾的插入时间是有序的，
为下面的删除操作服务。

对于 put(key, value) 操作，我们先通过索引 key在 key_table 中查看
是否有对应的缓存，如果有的话，其实操作等价于 get(key) 操作，唯一的
区别就是我们需要将当前的缓存里的值更新为 value。如果没有的话，相当于
是新加入的缓存，如果缓存已经到达容量，需要先删除最近最少使用的缓存，
再进行插入。

先考虑插入，由于是新插入的，所以缓存的使用频率一定是 1，所以我们将缓存
的信息插入到 freq_table 中 1 索引下的列表头即可，同时更新
key_table[key] 的信息，以及更新 minFreq = 1。

那么剩下的就是删除操作了，由于我们实时维护了 minFreq，所以我们能够知道
freq_table 里目前最少使用频率的索引，同时因为我们保证了链表中从链表头到
链表尾的插入时间是有序的，所以 freq_table[minFreq] 的链表中链表尾的节点
即为使用频率最小且插入时间最早的节点，我们删除它同时根据情况更新 minFreq，
整个时间复杂度均为 O(1)。
"""


# @lc code=start
class Node:
    def __init__(self, key=0, val=0, freq=0) -> None:
        self.prev = None
        self.next = None
        self.key = key
        self.val = val
        self.freq = freq

    def insert(self, node: 'Node') -> None:
        node.prev = self
        node.next = self.next
        self.next.prev = node
        self.next = node


class DLinkedList:
    def __init__(self) -> None:
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.freq_map = defaultdict(DLinkedList)
        self.key_map = {}

    def get(self, key: int) -> int:
        if key in self.key_map:
            self.increase(self.key_map[key])
            return self.key_map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.key_map:
            node = self.key_map[key]
            node.val = value
        else:
            node = Node(key=key, val=value)
            self.key_map[key] = node
            self.size += 1

        if self.size > self.capacity:
            self.size -= 1
            deleted = self.delete(self.freq_map[self.min_freq].tail.prev)
            self.key_map.pop(deleted)

        self.increase(node)

    def increase(self, node: Node) -> None:
        node.freq += 1
        self.delete(node)
        self.freq_map[node.freq].head.insert(node)
        if node.freq == 1:
            self.min_freq = 1
        elif self.min_freq == node.freq - 1:
            head = self.freq_map[node.freq - 1].head
            tail = self.freq_map[node.freq - 1].tail
            if head.next is tail:
                self.min_freq = node.freq

    def delete(self, node: Node) -> int:
        if node.prev:
            node.prev.next = node.next
            node.next.prev = node.prev

            head = self.freq_map[node.freq].head
            tail = self.freq_map[node.freq].tail
            if node.prev is head and node.next is tail:
                self.freq_map.pop(node.freq)

        return node.key


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
