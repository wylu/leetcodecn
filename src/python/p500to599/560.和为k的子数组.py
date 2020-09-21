#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   560.和为k的子数组.py
@Time    :   2020/09/21 13:34:34
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#
# https://leetcode-cn.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (45.05%)
# Likes:    610
# Dislikes: 0
# Total Accepted:    71.2K
# Total Submissions: 158.1K
# Testcase Example:  '[1,1,1]\n2'
#
# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
#
# 示例 1 :
#
#
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
#
#
# 说明 :
#
#
# 数组的长度为 [1, 20,000]。
# 数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
#
#
#
from typing import List
"""
方法一：枚举（超时）

思路和算法

考虑以 i 结尾和为 k 的连续子数组个数，我们需要统计符合条件的下标 j 的个数，
其中 0 <= j <= i 且 [j..i] 这个子数组的和恰好为 k。

我们可以枚举 [0..i] 里所有的下标 j 来判断是否符合条件，可能有读者会认为
假定我们确定了子数组的开头和结尾，还需要 O(n) 的时间复杂度遍历子数组来求和，
那样复杂度就将达到 O(n^3) 从而无法通过所有测试用例。但是如果我们知道 [j,i]
子数组的和，就能 O(1) 推出 [j−1,i] 的和，因此这部分的遍历求和是不需要的，
我们在枚举下标 j 的时候已经能 O(1) 求出 [j,i] 的子数组之和。

方法二：前缀和 + 哈希表优化

思路和算法

我们可以基于方法一利用数据结构进行进一步的优化，我们知道方法一的瓶颈在于
对每个 i，我们需要枚举所有的 j 来判断是否符合条件，这一步是否可以优化呢？
答案是可以的。

我们定义 pre[i] 为 [0..i] 里所有数的和，则 pre[i] 可以由 pre[i−1] 递推
而来，即：

    pre[i] = pre[i−1] + nums[i]

那么「[j..i] 这个子数组和为 k 」这个条件我们可以转化为

    pre[i] − pre[j−1] == k

简单移项可得符合条件的下标 j 需要满足

    pre[j−1] == pre[i] − k

所以我们考虑以 i 结尾的和为 k 的连续子数组个数时只要统计有多少个前缀和为
pre[i] − k 的 pre[j] 即可。我们建立哈希表 mp，以和为键，出现次数为对应
的值，记录 pre[i] 出现的次数，从左往右边更新 mp 边计算答案，那么以 i
结尾的答案 mp[pre[i]−k] 即可在 O(1) 时间内得到。最后的答案即为所有下标
结尾的和为 k 的子数组个数之和。

需要注意的是，从左往右边更新边计算的时候已经保证了 mp[pre[i]−k] 里记录的
pre[j] 的下标范围是 0 <= j <= i。同时，由于 pre[i] 的计算只与前一项的
答案有关，因此我们可以不用建立 pre 数组，直接用 pre 变量来记录 pre[i−1]
的答案即可。

下面的动画描述了这一过程：

https://leetcode-cn.com/problems/subarray-sum-equals-k/solution/he-wei-kde-zi-shu-zu-by-leetcode-solution/
"""


# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        pre, mp = 0, {0: 1}
        for num in nums:
            pre += num
            ans += mp.get(pre - k, 0)
            mp[pre] = mp.get(pre, 0) + 1
        return ans


# @lc code=end

# 方法一：枚举（超时）
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         ans, n = 0, len(nums)
#         for i in range(n):
#             cur = 0
#             for j in range(i, -1, -1):
#                 cur += nums[j]
#                 if cur == k:
#                     ans += 1
#         return ans

if __name__ == '__main__':
    solu = Solution()
    print(solu.subarraySum([1, 1, 1], 2))
    print(solu.subarraySum([1, 1, 1], 0))
