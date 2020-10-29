#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   4.寻找两个正序数组的中位数.py
@Time    :   2020/10/05 19:02:38
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (38.80%)
# Likes:    3266
# Dislikes: 0
# Total Accepted:    267.8K
# Total Submissions: 690K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。
#
# 进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
#
#
#
# 示例 1：
#
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#
#
# 示例 2：
#
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#
#
# 示例 3：
#
# 输入：nums1 = [0,0], nums2 = [0,0]
# 输出：0.00000
#
#
# 示例 4：
#
# 输入：nums1 = [], nums2 = [1]
# 输出：1.00000
#
#
# 示例 5：
#
# 输入：nums1 = [2], nums2 = []
# 输出：2.00000
#
#
#
#
# 提示：
#
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
#
#
#
from typing import List
"""
二分查找

https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/

方法二：划分数组
思路与算法

为了使用划分的方法解决这个问题，需要理解「中位数的作用是什么」。在统计中，
中位数被用来：

将一个集合划分为两个长度相等的子集，其中一个子集中的元素总是大于另一个
子集中的元素。

如果理解了中位数的划分作用，就很接近答案了。

首先，在任意位置 i 将 A 划分成两个部分：

           left_A            |          right_A
    A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]

由于 A 中有 m 个元素， 所以有 m+1 种划分的方法（i∈[0,m]）。

len(left_A) = i, len(right_A) = m−i.

注意：当 i = 0 时，left_A 为空集， 而当 i = m 时, right_A 为空集。

采用同样的方式，在任意位置 j 将 B 划分成两个部分：

           left_B            |          right_B
    B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]

将 left_A 和 left_B 放入一个集合，并将 right_A 和 right_B 放入
另一个集合。再把这两个新的集合分别命名为 left_part 和 right_part：

          left_part          |         right_part
    A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
    B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]

当 A 和 B 的总长度是偶数时，如果可以确认：

len(left_part) = len(right_part)
max(left_part) ≤ min(right_part)

那么，{A,B} 中的所有元素已经被划分为相同长度的两个部分，且前一部分
中的元素总是小于或等于后一部分中的元素。中位数就是前一部分的最大值
和后一部分的最小值的平均值：

          max(left_part) + min(right_part)
median = --------------------------------
                         2
​
当 A 和 B 的总长度是奇数时，如果可以确认：

len(left_part) = len(right_part)+1
max(left_part) ≤ min(right_part)

那么，{A,B} 中的所有元素已经被划分为两个部分，前一部分比后一部分
多一个元素，且前一部分中的元素总是小于或等于后一部分中的元素。
中位数就是前一部分的最大值：

median = max(left_part)

第一个条件对于总长度是偶数和奇数的情况有所不同，但是可以将两种情况合并。
第二个条件对于总长度是偶数和奇数的情况是一样的。

要确保这两个条件，只需要保证：

i + j = m - i + n - j（当 m+n 为偶数）或 i + j = m - i + n - j + 1
（当 m+n 为奇数）。等号左侧为前一部分的元素个数，等号右侧为后一部分的
元素个数。将 i 和 j 全部移到等号左侧，我们就可以得到
i + j = ((m + n + 1) / 2)。这里的分数结果只保留整数部分。

0 ≤ i ≤ m，0 ≤ j ≤ n。如果我们规定 A 的长度小于等于 B 的长度，即
m ≤ n。这样对于任意的 i∈[0,m]，都有 j = ((m+n+1) / 2) − i∈[0,n]，
那么我们在 [0, m] 的范围内枚举 i 并得到 j，就不需要额外的性质了。

  - 如果 A 的长度较大，那么我们只要交换 A 和 B 即可。
  - 如果 m > n ，那么得出的 j 有可能是负数。

B[j−1] ≤ A[i] 以及 A[i−1] ≤ B[j]，即前一部分的最大值小于等于后一部分
的最小值。

为了简化分析，假设 A[i−1], B[j−1], A[i], B[j] 总是存在。对于
i=0、i=m、j=0、j=n 这样的临界条件，我们只需要规定 A[−1]=B[−1]=−∞，
A[m]=B[n]=∞ 即可。这也是比较直观的：当一个数组不出现在前一部分时，
对应的值为负无穷，就不会对前一部分的最大值产生影响；当一个数组不出现在
后一部分时，对应的值为正无穷，就不会对后一部分的最小值产生影响。

所以我们需要做的是：

在 [0, m] 中找到 i，使得：
  B[j−1]≤A[i] 且 A[i−1]≤B[j]，其中 j = (m + n + 1) / 2 - i

我们证明它等价于：

在 [0, m] 中找到最大的 i，使得：

A[i−1]≤B[j]，其中 j = (m + n + 1) / 2 - i

这是因为：

当 i 从 0∼m 递增时，A[i−1] 递增，B[j] 递减，所以一定存在一个最大的
i 满足 A[i−1] ≤ B[j]；

如果 i 是最大的，那么说明 i+1 不满足。将 i+1 带入可以得到
A[i] > B[j-1]，也就是 B[j - 1] < A[i]，就和我们进行等价变换前 i
的性质一致了（甚至还要更强）。

因此我们可以对 i 在 [0, m] 的区间上进行二分搜索，找到最大的满足
A[i−1] ≤ B[j] 的 i 值，就得到了划分的方法。此时，划分前一部分元素中
的最大值，以及划分后一部分元素中的最小值，才可能作为就是这两个数组的
中位数。
"""


# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        totLeft = (m + n + 1) // 2

        left, right = 0, m
        while left < right:
            i = (left + right + 1) // 2
            j = totLeft - i
            if nums1[i - 1] <= nums2[j]:
                left = i
            else:
                right = i - 1

        i = (left + right + 1) // 2
        j = totLeft - i
        INT_MIN, INT_MAX = -0x80000000, 0x7FFFFFFF
        maxLeft1 = INT_MIN if i == 0 else nums1[i - 1]
        minRight1 = INT_MAX if i == m else nums1[i]
        maxLeft2 = INT_MIN if j == 0 else nums2[j - 1]
        minRight2 = INT_MAX if j == n else nums2[j]

        if (m + n) % 2 == 0:
            return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
        return max(maxLeft1, maxLeft2)


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.findMedianSortedArrays([1, 3], [2]))
    print(solu.findMedianSortedArrays([1, 2], [3, 4]))
    print(solu.findMedianSortedArrays([0, 0], [0, 0]))
    print(solu.findMedianSortedArrays([], [1]))
    print(solu.findMedianSortedArrays([2], []))
