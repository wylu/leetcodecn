#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2013.检测正方形.py
@Time    :   2022/01/26 10:48:12
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=2013 lang=python3
#
# [2013] 检测正方形
#
# https://leetcode-cn.com/problems/detect-squares/description/
#
# algorithms
# Medium (46.02%)
# Likes:    36
# Dislikes: 0
# Total Accepted:    6.4K
# Total Submissions: 14K
# Testcase Example:
# '["DetectSquares","add","add","add","count","count","add","count"]\n'
# + '[[],[[3,10]],[[11,2]],[[3,2]],[[11,10]],[[14,8]],[[11,2]],[[11,10]]]'
#
# 给你一个在 X-Y 平面上的点构成的数据流。设计一个满足下述要求的算法：
#
#
# 添加 一个在数据流中的新点到某个数据结构中。可以添加 重复 的点，并会视作不同的点进行处理。
# 给你一个查询点，请你从数据结构中选出三个点，使这三个点和查询点一同构成一个 面积为正 的 轴对齐正方形 ，统计 满足该要求的方案数目。
#
#
# 轴对齐正方形 是一个正方形，除四条边长度相同外，还满足每条边都与 x-轴 或 y-轴 平行或垂直。
#
# 实现 DetectSquares 类：
#
#
# DetectSquares() 使用空数据结构初始化对象
# void add(int[] point) 向数据结构添加一个新的点 point = [x, y]
# int count(int[] point) 统计按上述方式与点 point = [x, y] 共同构造 轴对齐正方形 的方案数。
#
#
#
#
# 示例：
#
#
# 输入：
# ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
# [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11,
# 10]]]
# 输出：
# [null, null, null, null, 1, 0, null, 2]
#
# 解释：
# DetectSquares detectSquares = new DetectSquares();
# detectSquares.add([3, 10]);
# detectSquares.add([11, 2]);
# detectSquares.add([3, 2]);
# detectSquares.count([11, 10]); // 返回 1 。你可以选择：
# ⁠                              //   - 第一个，第二个，和第三个点
# detectSquares.count([14, 8]);  // 返回 0 。查询点无法与数据结构中的这些点构成正方形。
# detectSquares.add([11, 2]);    // 允许添加重复的点。
# detectSquares.count([11, 10]); // 返回 2 。你可以选择：
# ⁠                              //   - 第一个，第二个，和第三个点
# ⁠                              //   - 第一个，第三个，和第四个点
#
#
#
#
# 提示：
#
#
# point.length == 2
# 0 <= x, y <= 1000
# 调用 add 和 count 的 总次数 最多为 5000
#
#
#
from collections import Counter
from collections import defaultdict
from typing import List
"""
方法一：哈希表
思路

先考虑如何实现 int count(int[] point)，记输入的 point 的横纵坐标分别为 x 和 y。
则形成的正方形的上下两条边中，其中一条边的纵坐标为 y， 我们枚举另一条边的纵坐标为
col，则正方形的边长 d 为 |y - col| 且大于 0。有了其中一个点的坐标 (x, y) 和一条
横边的纵坐标 col，我们可以得到正方形的四个点的坐标分别为 (x, y)，(x, col)，(x+d, y)，(x+d, col)
或 (x, y)，(x, col)，(x-d, y)，(x-d, col)。

据此，我们可以用一个哈希表来存储 void add(int[] point) 函数中加入的点。先把点
按照行来划分，键为行的纵坐标，值为另一个哈希表，其中键为该行中的点的横坐标，
值为这样的点的个数。因为点会重复出现，所以计算正方形的个数时需要把另外三个坐标
出现的次数相乘。
"""


# @lc code=start
class DetectSquares:
    def __init__(self):
        self.map = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.map[y][x] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        x, y = point

        if y not in self.map:
            return 0

        ycnt = self.map[y]

        for col, ccnt in self.map.items():
            if col != y:
                # 根据对称性，这里可以不用取绝对值
                e = col - y
                ans += ccnt[x] * ycnt[x + e] * ccnt[x + e]
                ans += ccnt[x] * ycnt[x - e] * ccnt[x - e]

        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
# @lc code=end

if __name__ == '__main__':
    obj = DetectSquares()
    for point in [[419, 351], [798, 351], [798, 730]]:
        obj.add(point)

    print(obj.count([419, 730]))

    for point in [[998, 1], [0, 999], [998, 999]]:
        obj.add(point)

    print(obj.count([0, 1]))
