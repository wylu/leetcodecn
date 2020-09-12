#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   503.下一个更大元素-ii.py
@Time    :   2020/09/12 10:40:49
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#
# https://leetcode-cn.com/problems/next-greater-element-ii/description/
#
# algorithms
# Medium (57.36%)
# Likes:    186
# Dislikes: 0
# Total Accepted:    30.1K
# Total Submissions: 52.5K
# Testcase Example:  '[1,2,1]'
#
# 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x
# 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。
#
# 示例 1:
#
#
# 输入: [1,2,1]
# 输出: [2,-1,2]
# 解释: 第一个 1 的下一个更大的数是 2；
# 数字 2 找不到下一个更大的数；
# 第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
#
#
# 注意: 输入数组的长度不会超过 10000。
#
#
from typing import List
"""
方法一：单调栈

我们可以使用单调栈来解决这个问题。

我们首先把第一个元素 A[1] 放入栈，随后对于第二个元素 A[2]，如果 A[2] > A[1]，
那么我们就找到了 A[1] 的下一个更大元素 A[2]，此时就可以把 A[1] 出栈并把 A[2]
入栈；如果 A[2] <= A[1]，我们就仅把 A[2] 入栈。对于第三个元素 A[3]，此时栈中
有若干个元素，那么所有比 A[3] 小的元素都找到了下一个更大元素（即 A[3]），因此
可以出栈，在这之后，我们将 A[3] 入栈，以此类推。

可以发现，我们维护了一个单调栈，栈中的元素从栈顶到栈底是单调不降的。当我们遇到
一个新的元素 A[i] 时，我们判断栈顶元素是否小于 A[i]，如果是，那么栈顶元素的下
一个更大元素即为 A[i]，我们将栈顶元素出栈。重复这一操作，直到栈为空或者栈顶
元素大于 A[i]。此时我们将 A[i] 入栈，保持栈的单调性，并对接下来的
A[i + 1], A[i + 2] ... 执行同样的操作。

由于这道题的数组是循环数组，因此我们需要将每个元素都入栈两次。这样可能会有元素
出栈找过一次，即得到了超过一个“下一个更大元素”，我们只需要保留第一个出栈的结果
即可。
"""


# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        n = len(nums)
        ans, stack = [-1] * n, []
        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                ans[stack.pop()] = nums[i % n]
            stack.append(i % n)

        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.nextGreaterElements([1, 2, 1]))
    print(solu.nextGreaterElements([1, 1, 1]))
    print(solu.nextGreaterElements([3, 2, 1]))
    print(solu.nextGreaterElements([1, 2, 3]))
