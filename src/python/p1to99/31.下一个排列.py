#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   31.下一个排列.py
@Time    :   2020/09/09 22:48:32
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# https://leetcode-cn.com/problems/next-permutation/description/
#
# algorithms
# Medium (34.49%)
# Likes:    651
# Dislikes: 0
# Total Accepted:    87.4K
# Total Submissions: 253.5K
# Testcase Example:  '[1,2,3]'
#
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
# 必须原地修改，只允许使用额外常数空间。
#
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#
#
from typing import List
"""
思路：

我们希望下一个数比当前数大，这样才满足“下一个排列”的定义。因此只需要
将后面的「大数」与前面的「小数」交换，就能得到一个更大的数。比如 123456，
将 5 和 6 交换就能得到一个更大的数 123465。

我们还希望下一个数增加的幅度尽可能的小，这样才满足“下一个排列与当前排列紧邻”
的要求。为了满足这个要求，我们需要：
  - 在尽可能靠右的低位进行交换，需要从后向前查找；
  - 将一个 尽可能小的「大数」 与前面的「小数」交换。比如 123465，
    下一个排列应该把 5 和 4 交换而不是把 6 和 4 交换；
  - 将「大数」换到前面后，需要将「大数」后面的所有数重置为升序，
    升序排列就是最小的排列。以 123465 为例：首先按照上一步，交换 5 和 4，
    得到 123564；然后需要将 5 之后的数重置为升序，得到 123546。
    显然 123546 比 123564 更小，123546 就是 123465 的下一个排列；
"""


# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(s: int, e: int) -> None:
            while s < e:
                nums[s], nums[e] = nums[e], nums[s]
                s += 1
                e -= 1

        n = len(nums)
        i = n - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1

        if i == 0:
            reverse(0, n - 1)
        else:
            i, j = i - 1, i - 1
            while i < n - 1 and nums[i + 1] > nums[j]:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
            reverse(j + 1, n - 1)


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    nums = [1, 2, 3]
    solu.nextPermutation(nums)
    print(nums)
    nums = [3, 2, 1]
    solu.nextPermutation(nums)
    print(nums)
    nums = [1, 1, 5]
    solu.nextPermutation(nums)
    print(nums)
