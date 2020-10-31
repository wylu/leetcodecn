#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   380.常数时间插入、删除和获取随机元素.py
@Time    :   2020/10/31 22:38:43
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] 常数时间插入、删除和获取随机元素
#
# https://leetcode-cn.com/problems/insert-delete-getrandom-o1/description/
#
# algorithms
# Medium (49.16%)
# Likes:    222
# Dislikes: 0
# Total Accepted:    18.7K
# Total Submissions: 38K
# Testcase Example:
# '["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]\n'
# + '[[],[1],[2],[2],[],[1],[2],[]]'
#
# 设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。
#
#
# insert(val)：当元素 val 不存在时，向集合中插入该项。
# remove(val)：元素 val 存在时，从集合中移除该项。
# getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。
#
#
# 示例 :
#
#
# // 初始化一个空的集合。
# RandomizedSet randomSet = new RandomizedSet();
#
# // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
# randomSet.insert(1);
#
# // 返回 false ，表示集合中不存在 2 。
# randomSet.remove(2);
#
# // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
# randomSet.insert(2);
#
# // getRandom 应随机返回 1 或 2 。
# randomSet.getRandom();
#
# // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
# randomSet.remove(1);
#
# // 2 已在集合中，所以返回 false 。
# randomSet.insert(2);
#
# // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
# randomSet.getRandom();
#
#
#
import random


# @lc code=start
class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.idx = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set.
        Returns true if the set did not already contain the specified element.
        """
        ans = not (val in self.idx)
        self.nums.append(val)
        self.idx[val] = len(self.nums) - 1
        return ans

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set.
        Returns true if the set contained the specified element.
        """
        if val not in self.idx:
            return False

        i = self.idx[val]
        del self.idx[val]
        j = len(self.nums) - 1
        if i != j:
            self.nums[i] = self.nums[j]
            self.idx[self.nums[i]] = i

        self.nums.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[random.randrange(0, len(self.nums))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
