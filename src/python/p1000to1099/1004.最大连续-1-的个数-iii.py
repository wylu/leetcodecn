#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1004.最大连续-1-的个数-iii.py
@Time    :   2021/02/19 17:03:32
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#
# https://leetcode-cn.com/problems/max-consecutive-ones-iii/description/
#
# algorithms
# Medium (60.19%)
# Likes:    209
# Dislikes: 0
# Total Accepted:    36.8K
# Total Submissions: 61.2K
# Testcase Example:  '[1,1,1,0,0,0,1,1,1,1,0]\n2'
#
# 给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。
#
# 返回仅包含 1 的最长（连续）子数组的长度。
#
#
#
# 示例 1：
#
# 输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# 输出：6
# 解释：
# [1,1,1,0,0,1,1,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 6。
#
# 示例 2：
#
# 输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# 输出：10
# 解释：
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 10。
#
#
#
# 提示：
#
#
# 1 <= A.length <= 20000
# 0 <= K <= A.length
# A[i] 为 0 或 1
#
#
#
from typing import List
"""
前言
对于数组 A 的区间 [left,right] 而言，只要它包含不超过 K 个 0，我们就
可以根据它构造出一段满足要求，并且长度为 right−left+1 的区间。

因此，我们可以将该问题进行如下的转化，即：

对于任意的右端点 right，希望找到最小的左端点 left，使得 [left,right]
包含不超过 K 个 0。

只要我们枚举所有可能的右端点，将得到的区间的长度取最大值，即可得到答案。

要想快速判断一个区间内 0 的个数，我们可以考虑将数组 A 中的 0 变成 1，
1 变成 0。此时，我们对数组 A 求出前缀和，记为数组 P，那么 [left,right]
中包含不超过 K 个 1（注意这里就不是 0 了），当且仅当二者的前缀和之差：
    P[right]−P[left−1]
小于等于 K。这样一来，我们就可以容易地解决这个问题了。

方法一：二分查找
思路与算法

P[right]−P[left−1] ≤ K 等价于 P[left−1] ≥ P[right]−K   (1)

也就是说，我们需要找到最小的满足 (1) 式的 left。由于数组 A 中仅包含 0/1，
因此前缀和数组是一个单调递增的数组，我们就可以使用二分查找的方法得到 left。

细节

注意到 (1) 式的左侧的下标是 left−1 而不是 left，那么我们在构造前缀和数组时，
可以将前缀和整体向右移动一位，空出 P[0] 的位置，即：

P[0] = 0
P[i] = P[i−1] + (1−A[i−1])
​
此时，我们在数组 P 上二分查找到的下标即为 left 本身，同时我们也避免了原先
left=0 时 left−1=−1 不在数组合法的下标范围中的边界情况。

方法二：滑动窗口
思路与算法

我们继续观察 (1) 式，由于前缀和数组 P 是单调递增的，那么 (1) 式的右侧
P[right]−K 同样也是单调递增的。因此，我们可以发现：

随着 right 的增大，满足 (1) 式的最小的 left 值是单调递增的。

这样一来，我们就可以使用滑动窗口来实时地维护 left 和 right 了。在 right
向右移动的过程中，我们同步移动 left，直到 left 为首个（即最小的）满足 (1)
式的位置，此时我们就可以使用此区间对答案进行更新了。

细节

当我们使用滑动窗口代替二分查找解决本题时，就不需要显式地计算并保存出前缀和
数组了。我们只需要知道 left 和 right 作为下标在前缀和数组中对应的值，因此
我们只需要用两个变量 lsum 和 rsum 记录 left 和 right 分别对应的前缀和即可。
"""


# @lc code=start
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        lsum = rsum = 0
        ans = left = right = 0
        while right < n:
            rsum += 1 - A[right]
            while lsum < rsum - K:
                lsum += 1 - A[left]
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.longestOnes(A=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], K=2))
    print(
        solu.longestOnes(
            A=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], K=3))
