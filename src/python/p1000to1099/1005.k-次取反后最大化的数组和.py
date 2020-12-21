#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1005.k-次取反后最大化的数组和.py
@Time    :   2020/12/21 22:46:14
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1005 lang=python3
#
# [1005] K 次取反后最大化的数组和
#
# https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations/description/
#
# algorithms
# Easy (53.30%)
# Likes:    66
# Dislikes: 0
# Total Accepted:    13.4K
# Total Submissions: 25.1K
# Testcase Example:  '[4,2,3]\n1'
#
# 给定一个整数数组 A，我们只能用以下方法修改该数组：我们选择某个索引 i 并将 A[i] 替换为 -A[i]，然后总共重复这个过程 K
# 次。（我们可以多次选择同一个索引 i。）
#
# 以这种方式修改数组后，返回数组可能的最大和。
#
#
#
# 示例 1：
#
# 输入：A = [4,2,3], K = 1
# 输出：5
# 解释：选择索引 (1,) ，然后 A 变为 [4,-2,3]。
#
#
# 示例 2：
#
# 输入：A = [3,-1,0,2], K = 3
# 输出：6
# 解释：选择索引 (1, 2, 2) ，然后 A 变为 [3,1,0,2]。
#
#
# 示例 3：
#
# 输入：A = [2,-3,-1,5,-4], K = 2
# 输出：13
# 解释：选择索引 (1, 4) ，然后 A 变为 [2,3,-1,5,4]。
#
#
#
#
# 提示：
#
#
# 1 <= A.length <= 10000
# 1 <= K <= 10000
# -100 <= A[i] <= 100
#
#
#
from typing import List
"""
第一步：将数组按照绝对值大小从大到小排序，「注意要按照绝对值的大小」
第二步：从前向后遍历，遇到负数将其变为正数，同时 K--
第三步：如果 K 还大于 0，那么反复转变数值最小的元素，将 K 用完
第四步：求和
"""


# @lc code=start
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort(key=lambda x: abs(x), reverse=True)

        i, n = 0, len(nums)
        while k > 0 and i < n:
            if nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
            i += 1

        if k > 0 and k % 2 == 1:
            nums[-1] = -nums[-1]

        return sum(nums)


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.largestSumAfterKNegations([4, 2, 3], 1))
    print(solu.largestSumAfterKNegations([3, -1, 0, 2], 3))
    print(solu.largestSumAfterKNegations([2, -3, -1, 5, -4], 2))
