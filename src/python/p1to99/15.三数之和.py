#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   15.三数之和.py
@Time    :   2020/09/24 15:22:11
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (29.55%)
# Likes:    2610
# Dislikes: 0
# Total Accepted:    332.6K
# Total Submissions: 1.1M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？请你找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#
#
# 示例：
#
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#
#
from typing import List
"""
方法一：排序 + 双指针

题目中要求找到所有「不重复」且和为 0 的三元组，这个「不重复」的要求使得我们
无法简单地使用三重循环枚举所有的三元组。这是因为在最坏的情况下，数组中的元素
全部为 0，即

    [0, 0, 0, 0, 0, ..., 0, 0, 0]

任意一个三元组的和都为 0。如果我们直接使用三重循环枚举三元组，会得到 O(N^3)
个满足题目要求的三元组（其中 N 是数组的长度）时间复杂度至少为 O(N^3)。在这
之后，我们还需要使用哈希表进行去重操作，得到不包含重复三元组的最终答案，又
消耗了大量的空间。这个做法的时间复杂度和空间复杂度都很高，因此我们要换一种
思路来考虑这个问题。

「不重复」的本质是什么？我们保持三重循环的大框架不变，只需要保证：
  - 第二重循环枚举到的元素不小于当前第一重循环枚举到的元素；
  - 第三重循环枚举到的元素不小于当前第二重循环枚举到的元素。

也就是说，我们枚举的三元组 (a, b, c) 满足 a <= b <= c，保证了只有
(a, b, c) 这个顺序会被枚举到，而 (b, a, c)、(c, b, a) 等等这些不会，
这样就减少了重复。要实现这一点，我们可以将数组中的元素从小到大进行排序，
随后使用普通的三重循环就可以满足上面的要求。

同时，对于每一重循环而言，相邻两次枚举的元素不能相同，否则也会造成重复。
举个例子，如果排完序的数组为

    [0, 1, 2, 2, 2, 3]
    ^  ^  ^

我们使用三重循环枚举到的第一个三元组为 (0, 1, 2)，如果第三重循环继续
枚举下一个元素，那么仍然是三元组 (0, 1, 2)，产生了重复。因此我们需要
将第三重循环「跳到」下一个不相同的元素，即数组中的最后一个元素 3，
枚举三元组 (0, 1, 3)。

下面给出了改进的方法的伪代码实现：

nums.sort()
for first = 0 .. n-1
    // 只有和上一次枚举的元素不相同，我们才会进行枚举
    if first == 0 or nums[first] != nums[first-1] then
        for second = first+1 .. n-1
            if second == first+1 or nums[second] != nums[second-1] then
                for third = second+1 .. n-1
                    if third == second+1 or nums[third] != nums[third-1] then
                        // 判断是否有 a+b+c==0
                        check(first, second, third)

这种方法的时间复杂度仍然为 O(N^3)，毕竟我们还是没有跳出三重循环的大框架。
然而它是很容易继续优化的，可以发现，如果我们固定了前两重循环枚举到的元素
a 和 b，那么只有唯一的 c 满足 a + b + c = 0。当第二重循环往后枚举一个
元素 b' 时，由于 b' > b，那么满足 a + b' + c' = 0 的 c' 一定有 c' < c，
即 c' 在数组中一定出现在 c 的左侧。也就是说，我们可以从小到大枚举 b，
同时从大到小枚举 c，即第二重循环和第三重循环实际上是并列的关系。

有了这样的发现，我们就可以保持第二重循环不变，而将第三重循环变成一个从
数组最右端开始向左移动的指针，从而得到下面的伪代码：

nums.sort()
for first = 0 .. n-1
    if first == 0 or nums[first] != nums[first-1] then
        // 第三重循环对应的指针
        third = n-1
        for second = first+1 .. n-1
            if second == first+1 or nums[second] != nums[second-1] then
                // 向左移动指针，直到 a+b+c 不大于 0
                while nums[first]+nums[second]+nums[third] > 0
                    third = third-1
                // 判断是否有 a+b+c==0
                check(first, second, third)

这个方法就是我们常说的「双指针」，当我们需要枚举数组中的两个元素时，
如果我们发现随着第一个元素的递增，第二个元素是递减的，那么就可以使用
双指针的方法，将枚举的时间复杂度从 O(N^2) 减少至 O(N)。为什么是
O(N) 呢？这是因为在枚举的过程每一步中，「左指针」会向右移动一个位置
（也就是题目中的 b），而「右指针」会向左移动若干个位置，这个与数组的
元素有关，但我们知道它一共会移动的位置数为 O(N)，均摊下来，每次也
向左移动一个位置，因此时间复杂度为 O(N)。

注意到我们的伪代码中还有第一重循环，时间复杂度为 O(N)，因此枚举的
总时间复杂度为 O(N^2)。由于排序的时间复杂度为 O(NlogN)，在渐进意义
下小于前者，因此算法的总时间复杂度为 O(N^2)。

上述的伪代码中还有一些细节需要补充，例如我们需要保持左指针一直在
右指针的左侧（即满足 b <= c），具体可以参考下面的代码，均给出了
详细的注释。
"""


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans, n = [], len(nums)
        nums.sort()

        # 枚举 a
        for first in range(n - 2):
            # 需要和上一次枚举的数不同
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            # c 对应的指针初始指向数组的最右端
            third = n - 1

            # 枚举 b
            for second in range(first + 1, n - 1):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue

                # 需要保证 b 的指针在 c 的指针的左侧
                while (second < third
                       and nums[first] + nums[second] + nums[third] > 0):
                    third -= 1

                # 如果指针重合，随着 b 后续的增加，不会有满足 a+b+c=0
                # 且 b<c 的 c 了，可以直接退出循环
                if second == third:
                    break

                if nums[first] + nums[second] + nums[third] == 0:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.threeSum([-1, 0, 1, 2, -1, -4]))
