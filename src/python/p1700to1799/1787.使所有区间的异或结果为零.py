#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1787.使所有区间的异或结果为零.py
@Time    :   2021/05/25 22:21:54
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1787 lang=python3
#
# [1787] 使所有区间的异或结果为零
#
# https://leetcode-cn.com/problems/make-the-xor-of-all-segments-equal-to-zero/description/
#
# algorithms
# Hard (64.45%)
# Likes:    102
# Dislikes: 0
# Total Accepted:    8.9K
# Total Submissions: 13.8K
# Testcase Example:  '[1,2,0,3,0]\n1'
#
# 给你一个整数数组 nums​​​ 和一个整数 k​​​​​ 。区间 [left, right]（left ）的 异或结果 是对下标位于 left 和
# right（包括 left 和 right ）之间所有元素进行 XOR 运算的结果：nums[left] XOR nums[left+1] XOR ...
# XOR nums[right] 。
#
# 返回数组中 要更改的最小元素数 ，以使所有长度为 k 的区间异或结果等于零。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,0,3,0], k = 1
# 输出：3
# 解释：将数组 [1,2,0,3,0] 修改为 [0,0,0,0,0]
#
#
# 示例 2：
#
#
# 输入：nums = [3,4,5,2,1,7,3,4,7], k = 3
# 输出：3
# 解释：将数组 [3,4,5,2,1,7,3,4,7] 修改为 [3,4,7,3,4,7,3,4,7]
#
#
# 示例 3：
#
#
# 输入：nums = [1,2,4,1,2,5,1,2,6], k = 3
# 输出：3
# 解释：将数组[1,2,4,1,2,5,1,2,6] 修改为 [1,2,3,1,2,3,1,2,3]
#
#
#
# 提示：
#
#
# 1 <= k <= nums.length <= 2000
# ​​​​​​0 <= nums[i] < 2^10
#
#
#
from collections import Counter
from typing import List
"""
方法一：动态规划
思路与算法

设数组 nums 的长度为 n。首先我们需要分析出数组 nums 在修改之后应当具有哪些性质。

由于任意长度为 k 的区间异或结果等于 0，那么对于任意的 i，有：

    nums[i] ⊕ nums[i+1] ⊕ ⋯ ⊕ nums[i+k−1] = 0    (1)

以及：

    nums[i+1] ⊕ nums[i+2] ⊕ ⋯ ⊕ nums[i+k] = 0    (2)

其中 ⊕ 表示异或运算。根据异或运算的性质 a ⊕ b ⊕ b = a，将 (1)(2) 两式联立，
即可得到：

    nums[i] ⊕ nums[i+k] = 0

其等价于 nums[i] = nums[i+k]。因此我们可以得出一个重要的结论：

数组 nums 在修改之后是一个以 k 为周期的周期性数组，即 ∀i∈[0,n−k), nums[i] = nums[i+k]。

因此，我们可以将数组 nums 按照下标对 k 取模的结果 0, 1, ⋯, k−1 分成 k 个组，
每个组内的元素必须要相等，并且这 k 个组对应的元素的异或和为 0，即：

    nums[0] ⊕ nums[1] ⊕ ⋯ ⊕ nums[k−1] = 0

只要满足上述的要求，修改后的数组的所有长度为 k 的区间异或结果一定等于 0。

对于第 i 个组，我们可以使用哈希映射来存储该组内的元素以及每个元素出现的次数，
这样一来，我们就可以尝试使用动态规划来解决本题了。

设 f(i,mask) 表示我们已经处理了第 0, 1, ⋯, i 个组，并且这些组对应元素的异或和：

    nums[0] ⊕ nums[1] ⊕ ⋯ ⊕ nums[i]

为 mask 的前提下，这些组总计最少需要修改的元素个数。在进行状态转移时，我们可以
枚举第 i 组被修改成了哪个数。假设其被修改成了 x，那么第 0, 1, ⋯, i−1 个组对应
的元素的异或和即为 mask ⊕ x，因此我们可以得到状态转移方程：

    f(i,mask) = min{f(i−1,mask⊕x) + size(i) − count(i,x)}

其中 size(i) 表示第 i 个组里的元素个数，count(i,x) 表示第 i 个组里元素 x 的
次数，它们的值都可以通过哈希映射得到。上述状态转移方程的意义即为：如果我们选择
将第 i 组全部修改为 x，那么有 count(i,x) 个数是无需修改的，这样就需要修改
size(i) − count(i,x) 次。

动态规划的时间复杂度是多少呢？我们发现这并不好估计，这是因为 x 可以很小，也可以
很大，它并没有一个固定的范围。然而我们可以发现，题目中规定了 nums[i] < 2^10，
也就是 nums[i] 的二进制表示的位数不超过 10。因此我们可以断定，x 的上限就是 2^10。

如果 x >= 2^10，那么 x 的二进制表示的最高位 1 是在数组 nums 的其它元素中没有
出现过的，因此根据异或的性质，要想将最终的异或结果变为 0，我们需要将另一个组的
所有元素改为 y，且 y 有与 x 相同的高位 1。这样一来，我们不如将 x 和 y 的高位
1 移除，让它们都在 [0, 2^10) 的范围内，这样更容易增大 count(i,x)，减少最终的
修改次数。

当我们确定了 x 的上限，就可以计算出动态规划的时间复杂度了。状态的数量有
k × 2^10 个，对于每一个状态，我们需要枚举 x 来进行状态转移，而 x 的数量同样有
2^10 个，因此时间复杂度为 O(2^20 * k) = O(2^20 * n)，数量级约为 2 × 10^9，
超出了时间限制，因此我们必须要进行优化。

优化

对于未优化的状态转移方程：

    f(i,mask) = min{f(i−1,mask⊕x) + size(i) − count(i,x)}

首先 size(i) 是与 x 无关的常量，我们可以将其移出最小值的限制，即：

    f(i,mask) = size(i) + min{f(i−1,mask⊕x) − count(i,x)}

由于我们需要求的是「最小值」，因此在状态转移方程中添加若干大于等于「最小值」的项，
对最终的答案不会产生影响。

考虑 count(i,x) 这一项，如果 x 没有在哈希表中出现，那么这一项的值为 0，否则
这一项的值大于 0。即：

- 如果 x 没有在哈希表中出现，那么转移的状态为：
    f(i−1,mask⊕x)
- 如果 x 在哈希表中出现，那么转移的状态为：
    f(i−1,mask⊕x) − count(i,x)
  它严格小于 f(i−1,mask⊕x)。如果我们在状态转移方程中添加 f(i−1,mask⊕x)，
  最终的答案不会变化。

因此我们可以将状态转移方程变化为：

    f(i,mask) = size(i) + min{t1,t2}

其中 t1 对应 x 在哈希表中出现的状态，即：

    t1 = min{f(i−1,mask⊕x) − count(i,x)}     x ∈ HashTable(i)

t2 对应 x 不在哈希表中出现的状态，以及 x 在哈希表中出现并且我们额外添加的状态，即：

    t2 = min{f(i−1, mask⊕x)}

由于 mask 的取值范围是 [0, 2^10)，x 的取值范围也是 [0, 2^10)，因此 mask ⊕ x
的取值范围就是 [0, 2^10)，与 x 无关。也就是说：

    t2 就是所有状态 f(i-1,..) 中的最小值。

那么优化后的动态规划的时间复杂度是多少呢？对于第 i 组，我们需要计算出第 i-1 组
对应的状态 f(i-1,..) 中的最小值，时间复杂度为 O(2^10)，即为 t2 部分的状态转移。
而对于 t1 部分，状态转移的次数等于第 i 组哈希映射的大小，小于等于 size(i)。
因此总的时间复杂度为：

    O(sum(2^10+size(i))) = O(2^10 * k + n)   其中 i = [0, k-1]

最终的答案即为 f(k-1,0)。

细节

由于 f(i,..) 只会从 f(i-1,..) 转移而来，因此我们可以使用两个长度为 2^10 的一维
数组代替二维数组，交替地进行状态转移，减少空间复杂度。

此外，当 i=0 时，f(-1,..) 都是需要特殊考虑的边界条件。由于 f(-1,..) 表示没有
考虑任何组时的异或和，因此该异或和一定为 0，即 f(-1,0) = 0。其它的状态都是不合法
的状态，我们可以将它们赋予一个极大值 ∞。
"""


# @lc code=start
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        # x 的范围为 [0, 2^10)
        MAXX = 2**10

        n = len(nums)
        f = [float("inf")] * MAXX
        # 边界条件 f(-1,0) = 0
        f[0] = 0

        for i in range(k):
            # 第 i 个组的哈希映射
            count = Counter()
            size = 0
            for j in range(i, n, k):
                count[nums[j]] += 1
                size += 1

            # 求出 t2
            t2min = min(f)

            g = [t2min] * MAXX
            for mask in range(MAXX):
                # t1 则需要枚举 x 才能求出
                for x, countx in count.items():
                    g[mask] = min(g[mask], f[mask ^ x] - countx)

            # 别忘了加上 size
            f = [val + size for val in g]

        return f[0]


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.minChanges(nums=[1, 2, 0, 3, 0], k=1))
    print(solu.minChanges(nums=[3, 4, 5, 2, 1, 7, 3, 4, 7], k=3))
    print(solu.minChanges(nums=[1, 2, 4, 1, 2, 5, 1, 2, 6], k=3))
