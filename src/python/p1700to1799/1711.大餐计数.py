#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1711.大餐计数.py
@Time    :   2021/01/04 20:01:57
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1711 lang=python3
#
# [1711] 大餐计数
#
# https://leetcode-cn.com/problems/count-good-meals/description/
#
# algorithms
# Medium (19.89%)
# Likes:    15
# Dislikes: 0
# Total Accepted:    2.7K
# Total Submissions: 13.8K
# Testcase Example:  '[1,3,5,7,9]'
#
# 大餐 是指 恰好包含两道不同餐品 的一餐，其美味程度之和等于 2 的幂。
#
# 你可以搭配 任意 两道餐品做一顿大餐。
#
# 给你一个整数数组 deliciousness ，其中 deliciousness[i] 是第 i^​​​​​​​​​​​​​​
# 道餐品的美味程度，返回你可以用数组中的餐品做出的不同 大餐 的数量。结果需要对 10^9 + 7 取余。
#
# 注意，只要餐品下标不同，就可以认为是不同的餐品，即便它们的美味程度相同。
#
#
#
# 示例 1：
#
#
# 输入：deliciousness = [1,3,5,7,9]
# 输出：4
# 解释：大餐的美味程度组合为 (1,3) 、(1,7) 、(3,5) 和 (7,9) 。
# 它们各自的美味程度之和分别为 4 、8 、8 和 16 ，都是 2 的幂。
#
#
# 示例 2：
#
#
# 输入：deliciousness = [1,1,1,3,3,3,7]
# 输出：15
# 解释：大餐的美味程度组合为 3 种 (1,1) ，9 种 (1,3) ，和 3 种 (1,7) 。
#
#
#
# 提示：
#
#
# 1 <= deliciousness.length <= 10^5
# 0 <= deliciousness[i] <= 2^20
#
#
#
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        cnt = defaultdict(int)
        for num in deliciousness:
            cnt[num] += 1

        ans = 0
        for first in sorted(cnt.keys()):
            for i in range(22):
                second = (1 << i) - first
                if second < first:
                    continue

                if first == second:
                    ans += cnt[first] * (cnt[first] - 1) // 2
                else:
                    ans += cnt[first] * cnt[second]

        return ans % 1000000007


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.countPairs([1, 3, 5, 7, 9]))
    print(solu.countPairs([1, 1, 1, 3, 3, 3, 7]))
