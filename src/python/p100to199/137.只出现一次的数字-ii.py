#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   137.只出现一次的数字-ii.py
@Time    :   2020/12/09 22:02:59
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#
# https://leetcode-cn.com/problems/single-number-ii/description/
#
# algorithms
# Medium (68.22%)
# Likes:    468
# Dislikes: 0
# Total Accepted:    46.5K
# Total Submissions: 68.2K
# Testcase Example:  '[2,2,3,2]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
#
# 说明：
#
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 示例 1:
#
# 输入: [2,2,3,2]
# 输出: 3
#
#
# 示例 2:
#
# 输入: [0,1,0,1,0,1,99]
# 输出: 99
#
#
from typing import List
"""
方法一：哈希表
思路与算法

我们可以使用哈希映射统计数组中每个元素的出现次数。对于哈希映射中的
每个键值对，键表示一个元素，值表示其出现的次数。

在统计完成后，我们遍历哈希映射即可找出只出现一次的元素。

方法二：依次确定每一个二进制位
思路与算法

为了方便叙述，我们称「只出现了一次的元素」为「答案」。

由于数组中的元素都在 int（即 32 位整数）范围内，因此我们可以依次
计算答案的每一个二进制位是 0 还是 1。

具体地，考虑答案的第 i 个二进制位（i 从 0 开始编号），它可能为 0
或 1。对于数组中非答案的元素，每一个元素都出现了 3 次，对应着第 i
个二进制位的 3 个 0 或 3 个 1，无论是哪一种情况，它们的和都是 3
的倍数（即和为 0 或 3）。因此：

答案的第 i 个二进制位就是数组中所有元素的第 i 个二进制位之和除以
3 的余数。

这样一来，对于数组中的每一个元素 x，我们使用位运算 (x >> i) & 1
得到 x 的第 i 个二进制位，并将它们相加再对 3 取余，得到的结果一定
为 0 或 1，即为答案的第 i 个二进制位。

细节

需要注意的是，如果使用的语言对「有符号整数类型」和「无符号整数类型」
没有区分，那么可能会得到错误的答案。这是因为「有符号整数类型」
（即 int 类型）的第 31 个二进制位（即最高位）是补码意义下的符号位，
对应着 -2^31，而「无符号整数类型」由于没有符号，第 31 个二进制位
对应着 2^31。因此在某些语言（例如 Python）中需要对最高位进行特殊
判断。

方法三：位运算符：NOT，AND 和 XOR
思路

为了区分出现一次的数字和出现三次的数字，使用两个位掩码：
seen_once 和 seen_twice。思路是：
  - 仅当 seen_twice 未变时，改变 seen_once。
  - 仅当 seen_once 未变时，改变seen_twice。

位掩码 seen_once 仅保留出现一次的数字，不保留出现三次的数字。
"""


# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            if sum((num >> i) & 1 for num in nums) % 3:
                if i == 31:
                    ans -= 1 << i
                else:
                    ans |= 1 << i
        return ans


# @lc code=end

# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         seen_once = seen_twice = 0
#         for num in nums:
#             # first appearance:
#             # add num to seen_once
#             # don't add to seen_twice because of presence in seen_once

#             # second appearance:
#             # remove num from seen_once
#             # add num to seen_twice

#             # third appearance:
#             # don't add to seen_once because of presence in seen_twice
#             # remove num from seen_twice
#             seen_once = ~seen_twice & (seen_once ^ num)
#             seen_twice = ~seen_once & (seen_twice ^ num)
#         return seen_once

if __name__ == "__main__":
    solu = Solution()
    print(solu.singleNumber([2, 2, 3, 2]))
    print(solu.singleNumber([0, 1, 0, 1, 0, 1, 99]))
    print(solu.singleNumber([-1, -2, -2, -2]))
