#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   406.根据身高重建队列.py
@Time    :   2020/11/16 13:32:19
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#
# https://leetcode-cn.com/problems/queue-reconstruction-by-height/description/
#
# algorithms
# Medium (69.78%)
# Likes:    603
# Dislikes: 0
# Total Accepted:    56.5K
# Total Submissions: 80.8K
# Testcase Example:  '[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]'
#
# 假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。
# 编写一个算法来重建这个队列。
#
# 注意：
# 总人数少于1100人。
#
# 示例
#
#
# 输入:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# 输出:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
#
#
#
from functools import cmp_to_key
from typing import List
"""
贪心算法：高个子先站好位，矮个子插入到 K 位置上，前面肯定有 K 个高个子，
矮个子再插到前面也满足 K 的要求

1.排序规则：按照先 H 高度降序，K 个数升序排序
2.遍历排序后的数组，根据 K 插入到 K 的位置上
"""


# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        def cmp(x: List[int], y: List[int]) -> int:
            return x[1] - y[1] if x[0] == y[0] else y[0] - x[0]

        people.sort(key=cmp_to_key(cmp))
        ans = []
        for item in people:
            ans.insert(item[1], item)

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print(solu.reconstructQueue(people))
