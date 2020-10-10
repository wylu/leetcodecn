#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   42.接雨水.py
@Time    :   2020/10/10 11:35:46
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (52.75%)
# Likes:    1729
# Dislikes: 0
# Total Accepted:    154.8K
# Total Submissions: 293.3K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
#
# 示例:
#
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
#
#
from typing import List
"""
https://leetcode-cn.com/problems/trapping-rain-water/solution/jie-yu-shui-by-leetcode/

方法 1：暴力
直观想法

直接按问题描述进行。对于数组中的每个元素，我们找出下雨后水能达到的最高位置，
等于两边最大高度的较小值减去当前高度的值。

算法

初始化 ans=0
从左向右扫描数组：
  初始化 max_left=0 和 max_right=0
  从当前元素向左扫描并更新：max_left=max(max_left,height[j])
  从当前元素向右扫描并更新：max_right=max(max_right,height[j])
  将 min(max_left,max_right)−height[i] 累加到 ans

方法 2：动态编程
直观想法

在暴力方法中，我们仅仅为了找到最大值每次都要向左和向右扫描一次。但是我们
可以提前存储这个值。因此，可以通过动态编程解决。

算法

找到数组中从下标 i 到最左端最高的条形块高度 left_max。
找到数组中从下标 i 到最右端最高的条形块高度 right_max。
扫描数组 height 并更新答案：
  累加 min(max_left[i],max_right[i])−height[i] 到 ans 上

方法 4：使用双指针
直观想法

和方法 2 相比，我们不从左和从右分开计算，我们想办法一次完成遍历。
从动态编程方法的示意图中我们注意到，只要 right_max[i] > left_max[i]
（元素 0 到元素 6），积水高度将由 left_max 决定，类似地
left_max[i] > right_max[i]（元素 8 到元素 11）。所以我们可以认为
如果一端有更高的条形块（例如右端），积水的高度依赖于当前方向的高度
（从左到右）。当我们发现另一侧（右侧）的条形块高度不是最高的，我们则
开始从相反的方向遍历（从右到左）。我们必须在遍历时维护 left_max 和
right_max ，但是我们现在可以使用两个指针交替进行，实现 1 次遍历
即可完成。

算法

初始化 left 指针为 0 并且 right 指针为 size-1
While left<right, do:
  If height[left] < height[right]
    If height[left] >= left_max, 更新 left_max
    Else 累加 left_max − height[left] 到 ans
    left = left + 1.
  Else
    If height[right] >= right_max, 更新 right_max
    Else 累加 right_max − height[right] 到 ans
    right = right - 1.
"""


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        ans = 0
        left_max, right_max = 0, 0
        left, right = 0, len(height) - 1
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1

        return ans


# @lc code=end

# 方法 2：动态编程
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if not height:
#             return 0

#         n = len(height)
#         max_lefts, max_rights = [0] * n, [0] * n
#         max_lefts[0], max_rights[n - 1] = height[0], height[n - 1]
#         for i in range(1, n):
#             max_lefts[i] = max(height[i], max_lefts[i - 1])
#         for i in range(n - 2, -1, -1):
#             max_rights[i] = max(height[i], max_rights[i + 1])

#         ans = 0
#         for i in range(1, len(height) - 1):
#             ans += min(max_lefts[i], max_rights[i]) - height[i]
#         return ans

# 方法 1：暴力（超时）
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         ans = 0
#         for i in range(1, len(height) - 1):
#             max_left, max_right = 0, 0
#             for j in range(i, -1, -1):
#                 max_left = max(max_left, height[j])
#             for j in range(i, len(height)):
#                 max_right = max(max_right, height[j])
#             ans += min(max_left, max_right) - height[i]
#         return ans

if __name__ == "__main__":
    solu = Solution()
    print(solu.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(solu.trap([2, 0, 2]))
    print(solu.trap([]))
