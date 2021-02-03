#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   480.滑动窗口中位数.py
@Time    :   2021/02/03 21:36:14
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=480 lang=python3
#
# [480] 滑动窗口中位数
#
# https://leetcode-cn.com/problems/sliding-window-median/description/
#
# algorithms
# Hard (43.19%)
# Likes:    222
# Dislikes: 0
# Total Accepted:    18.9K
# Total Submissions: 43.9K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# 中位数是有序序列最中间的那个数。如果序列的长度是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。
#
# 例如：
#
#
# [2,3,4]，中位数是 3
# [2,3]，中位数是 (2 + 3) / 2 = 2.5
#
#
# 给你一个数组 nums，有一个长度为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1
# 位。你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。
#
#
#
# 示例：
#
# 给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。
#
#
# 窗口位置                      中位数
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       1
# ⁠1 [3  -1  -3] 5  3  6  7      -1
# ⁠1  3 [-1  -3  5] 3  6  7      -1
# ⁠1  3  -1 [-3  5  3] 6  7       3
# ⁠1  3  -1  -3 [5  3  6] 7       5
# ⁠1  3  -1  -3  5 [3  6  7]      6
#
#
# 因此，返回该滑动窗口的中位数数组 [1,-1,-1,3,5,6]。
#
#
#
# 提示：
#
#
# 你可以假设 k 始终有效，即：k 始终小于输入的非空数组的元素个数。
# 与真实值误差在 10 ^ -5 以内的答案将被视作正确答案。
#
#
#
import heapq
from collections import defaultdict
from typing import List
"""
前言
本题是「295. 数据流的中位数」的进阶版本。

我们首先思考一下完成本题需要做哪些事情：

1.初始时，我们需要将数组 nums 中的前 k 个元素放入一个滑动窗口，并且
  求出它们的中位数；
2.随后滑动窗口会向右进行移动。每一次移动后，会将一个新的元素放入滑动
  窗口，并且将一个旧的元素移出滑动窗口，最后再求出它们的中位数。

因此，我们需要设计一个「数据结构」，用来维护滑动窗口，并且需要提供如下的
三个接口：

- insert(num)：将一个数 num 加入数据结构；
- erase(num)：将一个数 num 移出数据结构；
- getMedian()：返回当前数据结构中所有数的中位数。

方法一：双优先队列 + 延迟删除
思路与算法

我们可以使用两个优先队列（堆）维护所有的元素，第一个优先队列 small
是一个大根堆，它负责维护所有元素中较小的那一半；第二个优先队列 large
是一个小根堆，它负责维护所有元素中较大的那一半。具体地，如果当前需要维护
的元素个数为 x，那么 small 中维护了 ceil(x/2) 个元素，large 中维护了
floor(x/2) 个元素。也就是说：

small 中的元素个数要么与 large 中的元素个数相同，要么比 large 中的元素
个数恰好多 1 个。

这样设计的好处在于：当二者包含的元素个数相同时，它们各自的堆顶元素的
平均值即为中位数；而当 small 包含的元素多了一个时，small 的堆顶元素
即为中位数。这样 getMedian() 就设计完成了。

而对于 insert(num) 而言，如果当前两个优先队列都为空，那么根据元素个数
的要求，我们必须将这个元素加入 small；如果 small 非空（显然不会存在
small 空而 large 非空的情况），我们就可以将 num 与 small 的堆顶元素
top 比较：

- 如果 num <= top，我们就将其加入 small 中；
- 如果 num > top，我们就将其加入 large 中。

在成功地加入元素 num 之后，两个优先队列的元素个数可能会变得不符合要求。
由于我们只加入了一个元素，那么不符合要求的情况只能是下面的二者之一：

- small 比 large 的元素个数多了 2 个；
- small 比 large 的元素个数少了 1 个。

对于第一种情况，我们将 small 的堆顶元素放入 large；对于第二种情况，
我们将 large 的堆顶元素放入 small，这样就可以解决问题了，insert(num)
也就设计完成了。

然而对于 erase(num) 而言，设计起来就不是那么容易了，因为我们知道，
优先队列是不支持移出非堆顶元素这一操作的，因此我们可以考虑使用「延迟删除」
的技巧，即：

当我们需要移出优先队列中的某个元素时，我们只将这个删除操作「记录」下来，
而不去真的删除这个元素。当这个元素出现在 small 或者 large 的堆顶时，
我们再去将其移出对应的优先队列。

「延迟删除」使用到的辅助数据结构一般为哈希表 delayed，其中的每个键值对
(num, freq)，表示元素 num 还需要被删除 freq 次。「优先队列 + 延迟删除」
有非常多种设计方式，体现在「延迟删除」的时机选择。在本题解中，我们使用
一种比较容易编写代码的设计方式，即：

我们保证在任意操作 insert(num)，erase(num)，getMedian() 完成之后
（或者说任意操作开始之前），small 和 large 的堆顶元素都是不需要被
「延迟删除」的。这样设计的好处在于：我们无需更改 getMedian() 的设计，
只需要略加修改 insert(num) 即可。

我们首先设计一个辅助函数 prune(heap)，它的作用很简单，就是对 heap
这个优先队列（small 或者 large 之一），不断地弹出其需要被删除的堆顶元素，
并且减少 delayed 中对应项的值。在 prune(heap) 完成之后，我们就可以保证
heap 的堆顶元素是不需要被「延迟删除」的。

这样我们就可以在 prune(heap) 的基础上设计另一个辅助函数 makeBalance()，
它的作用即为调整 small 和 large 中的元素个数，使得二者的元素个数满足
要求。由于有了 erase(num) 以及「延迟删除」，我们在将一个优先队列的堆顶
元素放入另一个优先队列时，第一个优先队列的堆顶元素可能是需要删除的。
因此我们就可以用 makeBalance() 将 prune(heap) 封装起来，它的逻辑如下：

- 如果 small 和 large 中的元素个数满足要求，则不进行任何操作；
- 如果 small 比 large 的元素个数多了 2 个，那么我们我们将 small 的堆顶
  元素放入 large。此时 small 的对应元素可能是需要删除的，因此我们调用
  prune(small)；
- 如果 small 比 large 的元素个数少了 1 个，那么我们将 large 的堆顶元素
  放入 small。此时 large 的对应的元素可能是需要删除的，因此我们调用
  prune(large)。

此时，我们只需要在原先 insert(num) 的设计的最后加上一步 makeBalance()
即可。然而对于 erase(num)，我们还是需要进行一些思考的：

- 如果 num 与 small 和 large 的堆顶元素都不相同，那么 num 是需要被
  「延迟删除」的，我们将其在哈希表中的值增加 1；
- 否则，例如 num 与 small 的堆顶元素相同，那么该元素是可以理解被删除的。
  虽然我们没有实现「立即删除」这个辅助函数，但只要我们将 num 在哈希表中
  的值增加 1，并且调用「延迟删除」的辅助函数 prune(small)，那么就相当于
  实现了「立即删除」的功能。

无论是「立即删除」还是「延迟删除」，其中一个优先队列中的元素个数发生了
变化（减少了 1），因此我们还需要用 makeBalance() 调整元素的个数。

此时，所有的接口都已经设计完成了。由于 insert(num) 和 erase(num) 的
最后一步都是 makeBalance()，而 makeBalance() 的最后一步是 prune(heap)，
因此我们就保证了任意操作完成之后，small 和 large 的堆顶元素都是不需要被
「延迟删除」的。

结语
读者可以尝试回答如下的两个问题来检验自己是否掌握了该方法：

- 在 insert(num) 的最后我们加上了一步 makeBalance()，其中包括可能进行
  的 prune(heap) 操作，这对于 insert(num) 操作而言是否是必要的？
- 在 insert(num) 的过程中，如果我们将 insert(num) 放入了 large 中，
  并且 num 恰好出现在 large 的堆顶位置，且两个优先队列的元素个数满足要求，
  不需要进行调整。此时会不会出现 num 是一个需要被「延迟删除」的元素的情况，
  这样就不满足在 insert(num) 操作完成之后 large 的堆顶是不需要被
  「延迟删除」的要求了？

答案

- 是必要的。举个例子：在 insert(num) 操作之前，large 的堆顶元素是有效的，
  但其中第二小的元素是需要被删除的。此时，如果我们将一个很大的元素加入
  large 中，并且 large 包含的元素数量超过了 small，那么我们就需要将
  large 的堆顶元素放入 small 中。这样一来，large 的堆顶元素就变成了那个
  需要被删除的第二小的元素了，所以 prune(heap) 操作是必要的。
- 不可能会出现这种情况，假设出现了这种情况，那么 num 显然不会等于 large
  原先的堆顶元素，因为 large 原先的堆顶元素一定是不需要被删除的。那么 num
  满足：
            small的堆顶元素 < num < large的堆顶元素
  由于 small 是大根堆，large 是小根堆，因此根本就不存在与 num 值相同的
  元素，也就不可能会被延迟删除了。
"""


# @lc code=start
class DualHeap:
    def __init__(self, k: int):
        # 大根堆，维护较小的一半元素，注意 python 没有大根堆，
        # 需要将所有元素取相反数并使用小根堆
        self.small = []
        # 小根堆，维护较大的一半元素
        self.large = []
        # 哈希表，记录「延迟删除」的元素，key 为元素，value 为需要删除的次数
        self.delayed = defaultdict(int)

        self.k = k
        # small 和 large 当前包含的元素个数，需要扣除被「延迟删除」的元素
        self.smallSize = 0
        self.largeSize = 0

    def prune(self, heap: List[int]) -> None:
        # 不断地弹出 heap 的堆顶元素，并且更新哈希表
        while heap:
            num = heap[0]
            if heap is self.small:
                num = -num

            if num not in self.delayed:
                break

            heapq.heappop(heap)
            self.delayed[num] -= 1
            if self.delayed[num] == 0:
                del self.delayed[num]

    def makeBalance(self) -> None:
        # 调整 small 和 large 中的元素个数，使得二者的元素个数满足要求
        if self.smallSize > self.largeSize + 1:
            # small 比 large 元素多 2 个
            heapq.heappush(self.large, -self.small[0])
            heapq.heappop(self.small)
            self.smallSize -= 1
            self.largeSize += 1
            # small 堆顶元素被移除，需要进行 prune
            self.prune(self.small)
        elif self.smallSize < self.largeSize:
            # large 比 small 元素多 1 个
            heapq.heappush(self.small, -self.large[0])
            heapq.heappop(self.large)
            self.smallSize += 1
            self.largeSize -= 1
            # large 堆顶元素被移除，需要进行 prune
            self.prune(self.large)

    def insert(self, num: int) -> None:
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.smallSize += 1
        else:
            heapq.heappush(self.large, num)
            self.largeSize += 1
        self.makeBalance()

    def erase(self, num: int) -> None:
        self.delayed[num] += 1
        if num <= -self.small[0]:
            self.smallSize -= 1
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.largeSize -= 1
            if num == self.large[0]:
                self.prune(self.large)
        self.makeBalance()

    def getMedian(self) -> float:
        if self.k % 2 == 1:
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        dh = DualHeap(k)
        for num in nums[:k]:
            dh.insert(num)

        ans = [dh.getMedian()]
        for i in range(k, len(nums)):
            dh.insert(nums[i])
            dh.erase(nums[i - k])
            ans.append(dh.getMedian())

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.medianSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
