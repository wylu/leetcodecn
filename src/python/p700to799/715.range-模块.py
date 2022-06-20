#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   715.range-模块.py
@Time    :   2022/06/20 14:26:31
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=715 lang=python3
#
# [715] Range 模块
#
# https://leetcode.cn/problems/range-module/description/
#
# algorithms
# Hard (51.39%)
# Likes:    144
# Dislikes: 0
# Total Accepted:    9K
# Total Submissions: 17.6K
# Testcase Example:
# '["RangeModule","addRange","removeRange","queryRange","queryRange","queryRange"]\n'
# + '[[],[10,20],[14,16],[10,14],[13,15],[16,17]]'
#
# Range模块是跟踪数字范围的模块。设计一个数据结构来跟踪表示为 半开区间 的范围并查询它们。
#
# 半开区间 [left, right) 表示所有 left <= x < right 的实数 x 。
#
# 实现 RangeModule 类:
#
#
# RangeModule() 初始化数据结构的对象。
# void addRange(int left, int right) 添加 半开区间 [left,
# right)，跟踪该区间中的每个实数。添加与当前跟踪的数字部分重叠的区间时，应当添加在区间 [left, right)
# 中尚未跟踪的任何数字到该区间中。
# boolean queryRange(int left, int right) 只有在当前正在跟踪区间 [left, right)
# 中的每一个实数时，才返回 true ，否则返回 false 。
# void removeRange(int left, int right) 停止跟踪 半开区间 [left, right)
# 中当前正在跟踪的每个实数。
#
#
#
#
# 示例 1：
#
#
# 输入
# ["RangeModule", "addRange", "removeRange", "queryRange", "queryRange",
# "queryRange"]
# [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
# 输出
# [null, null, null, true, false, true]
#
# 解释
# RangeModule rangeModule = new RangeModule();
# rangeModule.addRange(10, 20);
# rangeModule.removeRange(14, 16);
# rangeModule.queryRange(10, 14); 返回 true （区间 [10, 14) 中的每个数都正在被跟踪）
# rangeModule.queryRange(13, 15); 返回 false（未跟踪区间 [13, 15) 中像 14, 14.03, 14.17
# 这样的数字）
# rangeModule.queryRange(16, 17); 返回 true （尽管执行了删除操作，区间 [16, 17) 中的数字 16
# 仍然会被跟踪）
#
#
#
#
# 提示：
#
#
# 1 <= left < right <= 10^9
# 在单个测试用例中，对 addRange 、  queryRange 和 removeRange 的调用总数不超过 10^4 次
#
#
#

# @lc code=start
from sortedcontainers import SortedDict


class RangeModule:
    def __init__(self):
        self.sd = SortedDict()

    def addRange(self, left: int, right: int) -> None:
        i = self.sd.bisect_right(left)
        if i != 0:
            j = i - 1
            if self.sd.values()[j] >= right:
                return
            if self.sd.values()[j] >= left:
                left = self.sd.keys()[j]
                self.sd.popitem(j)
                i -= 1

        while i < len(self.sd) and self.sd.keys()[i] <= right:
            right = max(right, self.sd.values()[i])
            self.sd.popitem(i)

        self.sd[left] = right

    def queryRange(self, left: int, right: int) -> bool:
        i = self.sd.bisect_right(left)
        if i == 0:
            return False

        return self.sd.values()[i - 1] >= right

    def removeRange(self, left: int, right: int) -> None:
        i = self.sd.bisect_right(left)
        if i != 0:
            j = i - 1
            ri = self.sd.values()[j]
            if ri >= right:
                li = self.sd.keys()[j]
                if li == left:
                    self.sd.popitem(j)
                else:
                    self.sd[li] = left
                if right != ri:
                    self.sd[right] = ri
                return
            elif ri > left:
                self.sd[self.sd.keys()[j]] = left

        while i < len(self.sd) and self.sd.keys()[i] < right:
            if self.sd.values()[i] <= right:
                self.sd.popitem(i)
            else:
                self.sd[right] = self.sd.values()[i]
                self.sd.popitem(i)
                break


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
# @lc code=end
