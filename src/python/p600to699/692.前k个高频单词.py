#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   692.前k个高频单词.py
@Time    :   2021/05/05 18:34:51
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=692 lang=python3
#
# [692] 前K个高频单词
#
# https://leetcode-cn.com/problems/top-k-frequent-words/description/
#
# algorithms
# Medium (52.16%)
# Likes:    244
# Dislikes: 0
# Total Accepted:    28.6K
# Total Submissions: 54.8K
# Testcase Example:  '["i", "love", "leetcode", "i", "love", "coding"]\n2'
#
# 给一非空的单词列表，返回前 k 个出现次数最多的单词。
#
# 返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。
#
# 示例 1：
#
#
# 输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# 输出: ["i", "love"]
# 解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
# ⁠   注意，按字母顺序 "i" 在 "love" 之前。
#
#
#
#
# 示例 2：
#
#
# 输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
# k = 4
# 输出: ["the", "is", "sunny", "day"]
# 解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
# ⁠   出现次数依次为 4, 3, 2 和 1 次。
#
#
#
#
# 注意：
#
#
# 假定 k 总为有效值， 1 ≤ k ≤ 集合元素数。
# 输入的单词均由小写字母组成。
#
#
#
#
# 扩展练习：
#
#
# 尝试以 O(n log k) 时间复杂度和 O(n) 空间复杂度解决。
#
#
#
from collections import Counter
import heapq
from typing import List
"""
方法一：排序

计算每个单词的频率，并使用使用这些频率的自定义排序关系对单词进行排序。
然后取前 k 个元素。

方法二：堆

计算每个单词的频率，然后将其添加到存储到大小为 k 的小根堆中。它将频率
最小的候选项放在堆的顶部。最后，我们从堆中弹出最多 k 次，并反转结果，
就可以得到前 k 个高频单词。

在 Python 中，我们使用 heapq.heapify，它可以在线性时间内将列表转换为堆，
从而简化了我们的工作。
"""


# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        pq = [(-freq, word) for word, freq in counter.items()]
        heapq.heapify(pq)
        return [heapq.heappop(pq)[1] for _ in range(k)]


# @lc code=end

# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:
#         counter = Counter(words)
#         candidates = list(counter.keys())
#         candidates.sort(key=lambda w: (-counter[w], w))
#         return candidates[:k]

if __name__ == '__main__':
    solu = Solution()
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    print(solu.topKFrequent(words, k=2))

    words = [
        "the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"
    ]
    print(solu.topKFrequent(words, k=4))
