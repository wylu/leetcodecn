#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1720.解码异或后的数组.py
@Time    :   2021/05/06 13:46:10
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1720 lang=python3
#
# [1720] 解码异或后的数组
#
# https://leetcode-cn.com/problems/decode-xored-array/description/
#
# algorithms
# Easy (87.87%)
# Likes:    43
# Dislikes: 0
# Total Accepted:    25.8K
# Total Submissions: 29.4K
# Testcase Example:  '[1,2,3]\n1'
#
# 未知 整数数组 arr 由 n 个非负整数组成。
#
# 经编码后变为长度为 n - 1 的另一个整数数组 encoded ，其中 encoded[i] = arr[i] XOR arr[i + 1]
# 。例如，arr = [1,0,2,1] 经编码后得到 encoded = [1,2,3] 。
#
# 给你编码后的数组 encoded 和原数组 arr 的第一个元素 first（arr[0]）。
#
# 请解码返回原数组 arr 。可以证明答案存在并且是唯一的。
#
#
#
# 示例 1：
#
#
# 输入：encoded = [1,2,3], first = 1
# 输出：[1,0,2,1]
# 解释：若 arr = [1,0,2,1] ，那么 first = 1 且 encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] =
# [1,2,3]
#
#
# 示例 2：
#
#
# 输入：encoded = [6,2,7,3], first = 4
# 输出：[4,2,0,7,4]
#
#
#
#
# 提示：
#
#
# 2 <= n <= 10^4
# encoded.length == n - 1
# 0 <= encoded[i] <= 10^5
# 0 <= first <= 10^5
#
#
#
from typing import List


# @lc code=start
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        for num in encoded:
            ans.append(num ^ ans[-1])
        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.decode(encoded=[1, 2, 3], first=1))
    print(solu.decode(encoded=[6, 2, 7, 3], first=4))
