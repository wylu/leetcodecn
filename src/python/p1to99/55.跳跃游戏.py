#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   55.跳跃游戏.py
@Time    :   2020/10/12 14:23:05
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
# https://leetcode-cn.com/problems/jump-game/description/
#
# algorithms
# Medium (41.16%)
# Likes:    865
# Dislikes: 0
# Total Accepted:    160.4K
# Total Submissions: 389.6K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个位置。
#
# 示例 1:
#
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
#
#
# 示例 2:
#
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
#
#
#
from typing import List
"""
方法一：贪心

我们可以用贪心的方法解决这个问题。

设想一下，对于数组中的任意一个位置 y，我们如何判断它是否可以到达？根据
题目的描述，只要存在一个位置 x，它本身可以到达，并且它跳跃的最大长度为
x + nums[x]，这个值大于等于 y，即 x + nums[x] >= y，那么位置 y 也
可以到达。

换句话说，对于每一个可以到达的位置 x，它使得 x+1, x+2, ⋯, x+nums[x]
这些连续的位置都可以到达。

这样以来，我们依次遍历数组中的每一个位置，并实时维护 最远可以到达的位置。
对于当前遍历到的位置 x，如果它在 最远可以到达的位置 的范围内，那么我们
就可以从起点通过若干次跳跃到达该位置，因此我们可以用 x + nums[x] 更新
最远可以到达的位置。

在遍历的过程中，如果 最远可以到达的位置 大于等于数组中的最后一个位置，
那就说明最后一个位置可达，我们就可以直接返回 True 作为答案。反之，如果
在遍历结束后，最后一个位置仍然不可达，我们就返回 False 作为答案。

以题目中的示例一 [2, 3, 1, 1, 4] 为例：

我们一开始在位置 0，可以跳跃的最大长度为 2，因此最远可以到达的位置被
更新为 2；我们遍历到位置 1，由于 1 <= 2，因此位置 1 可达。我们用 1
加上它可以跳跃的最大长度 3，将最远可以到达的位置更新为 4。由于 4 大于
等于最后一个位置 4，因此我们直接返回 True。

我们再来看看题目中的示例二 [3, 2, 1, 0, 4]

我们一开始在位置 0，可以跳跃的最大长度为 3，因此最远可以到达的位置被
更新为 3；我们遍历到位置 1，由于 1 <= 3，因此位置 1 可达，加上它可以
跳跃的最大长度 2 得到 3，没有超过最远可以到达的位置；位置 2、位置 3
同理，最远可以到达的位置不会被更新；我们遍历到位置 4，由于 4 > 3，
因此位置 4 不可达，我们也就不考虑它可以跳跃的最大长度了。在遍历完成
之后，位置 4 仍然不可达，因此我们返回 False。
"""


# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, most = len(nums), 0
        for i in range(n):
            if i <= most:
                most = max(most, i + nums[i])
        return most >= n - 1


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.canJump([2, 3, 1, 1, 4]))
    print(solu.canJump([3, 2, 1, 0, 4]))
    print(solu.canJump([0]))
    print(solu.canJump([2, 0]))
    print(solu.canJump([5, 4, 3, 2, 1, 1, 0, 0]))
