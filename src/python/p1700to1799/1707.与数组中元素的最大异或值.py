#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1707.与数组中元素的最大异或值.py
@Time    :   2021/01/02 22:55:20
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1707 lang=python3
#
# [1707] 与数组中元素的最大异或值
#
# https://leetcode-cn.com/problems/maximum-xor-with-an-element-from-array/description/
#
# algorithms
# Hard (41.59%)
# Likes:    11
# Dislikes: 0
# Total Accepted:    1.2K
# Total Submissions: 2.9K
# Testcase Example:  '[0,1,2,3,4]\n[[3,1],[1,3],[5,6]]'
#
# 给你一个由非负整数组成的数组 nums 。另有一个查询数组 queries ，其中 queries[i] = [xi, mi] 。
#
# 第 i 个查询的答案是 xi 和任何 nums 数组中不超过 mi 的元素按位异或（XOR）得到的最大值。换句话说，答案是 max(nums[j] XOR
# xi) ，其中所有 j 均满足 nums[j] <= mi 。如果 nums 中的所有元素都大于 mi，最终答案就是 -1 。
#
# 返回一个整数数组 answer 作为查询的答案，其中 answer.length == queries.length 且 answer[i] 是第 i
# 个查询的答案。
#
#
#
# 示例 1：
#
# 输入：nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
# 输出：[3,3,7]
# 解释：
# 1) 0 和 1 是仅有的两个不超过 1 的整数。0 XOR 3 = 3 而 1 XOR 3 = 2 。二者中的更大值是 3 。
# 2) 1 XOR 2 = 3.
# 3) 5 XOR 2 = 7.
#
#
# 示例 2：
#
# 输入：nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
# 输出：[15,-1,5]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length, queries.length <= 10^5
# queries[i].length == 2
# 0 <= nums[j], xi, mi <= 10^9
#
#
#
from typing import List
"""
方法一：字典树+记录分支最小值（超时）
我们可以使用 0-1 字典树存储数组中的元素。因为每个查询还包含一个上界 mi，
所以我们在字典树的每个节点额外存储以当前节点为根节点的子树中的最小元素。
其作用是：如果某一子树的最小元素都超过了 mi，则没有必要继续对这一子树
进行搜索。

考虑一次查询。我们从最高位开始逐位处理：
  - 如果 xi 的当前位为 1，我们应当优先走当前位为 0 的分支；否则，我们
    尝试走当前位为 1 的分支；如果分支不存在，或分支的最小元素也超过了 mi，
    则本查询无解。
  - 如果 xi 的当前位为 0，我们应当优先走当前位为 1 的分支，但要求这一
    分支的最小元素不超过 mi；否则，我们尝试走当前位为 0 的分支。

如果我们顺利地走到了最低位，就得到了这一查询的最优解。

时间复杂度 O((N+Q)logMAXN)。
空间复杂度 O(NlogMAXN+Q)。

方法二：字典树+离线处理
思路：
首先排个序，用离线的思路，避免为小于 m 的限制头疼；然后问题就转变成了：
“如何设计一个数据结构，使得在 O(logN) 的时间复杂度内找到任意自然数 x
与集合内所有元素的最大异或值？”

异或运算是按位的，而比较运算是从高位到低位，因此我们可以设计一个
Tries 树，树的每一层对应数字的每一位，而根节点对应最高位。

每次查询前，将满足要求的元素放入字典树；查询时也是由高位到低位进行，
根据 x 每一位是 0 还是 1 决定选择的子节点。
"""


# @lc code=start
class Solution:
    def maximizeXor(self, nums: List[int],
                    queries: List[List[int]]) -> List[int]:
        ans = [-1] * len(queries)
        i, root = 0, []
        nums.sort()

        for p, (x, m) in sorted(enumerate(queries), key=lambda x: x[1][1]):
            while i < len(nums) and nums[i] <= m:
                cur = root
                for d in range(30, -1, -1):
                    if not cur:
                        cur.append([])
                        cur.append([])
                    cur = cur[(nums[i] >> d) & 1]
                cur.append(nums[i])
                i += 1

            cur = root
            if not root:
                ans[p] = -1
                continue

            for d in range(30, -1, -1):
                choice = (x >> d) & 1 ^ 1
                if (not cur[choice]):
                    choice ^= 1
                cur = cur[choice]
            ans[p] = x ^ cur[0]

        return ans


# @lc code=end

# 字典树+离线处理
# class TrieNode:
#     def __init__(self):
#         self.val = None
#         self.children = [None, None]

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, num: int) -> None:
#         cur = self.root
#         for i in range(30, -1, -1):
#             bit = 1 if num & (1 << i) else 0
#             if not cur.children[bit]:
#                 cur.children[bit] = TrieNode()
#             cur = cur.children[bit]
#         cur.val = num

#     def search(self, x: int) -> int:
#         if not any(self.root.children):
#             return -1

#         cur = self.root
#         for i in range(30, -1, -1):
#             if x & (1 << i):
#                 cur = cur.children[0] if cur.children[0] else cur.children[1]
#             else:
#                 cur = cur.children[1] if cur.children[1] else cur.children[0]

#         return cur.val ^ x

# class Solution:
#     def maximizeXor(self, nums: List[int],
#                     queries: List[List[int]]) -> List[int]:
#         nums.sort()
#         indices = [i for i in range(len(queries))]
#         indices.sort(key=lambda x: queries[x][1])

#         ans = [-1] * len(queries)
#         i, n = 0, len(nums)
#         tire = Trie()
#         for idx in indices:
#             x, m = queries[idx]
#             while i < n and nums[i] <= m:
#                 tire.insert(nums[i])
#                 i += 1
#             ans[idx] = tire.search(x)

#         return ans

# 超时
# class TrieNode:
#     def __init__(self):
#         self.minimum = 0x7FFFFFFF
#         self.children = [None, None]

# class Solution:
#     def maximizeXor(self, nums: List[int],
#                     queries: List[List[int]]) -> List[int]:
#         root = TrieNode()
#         for num in nums:
#             p = root
#             for i in range(30, -1, -1):
#                 bit = 1 if num & (1 << i) else 0
#                 if not p.children[bit]:
#                     p.children[bit] = TrieNode()
#                 p = p.children[bit]
#                 p.minimum = min(p.minimum, num)

#         def search(x: int, m: int) -> int:
#             p, ret = root, 0
#             for i in range(30, -1, -1):
#                 if x & (1 << i):
#                     if p.children[0]:
#                         p = p.children[0]
#                         ret ^= (1 << i)
#                     elif p.children[1] and p.children[1].minimum <= m:
#                         p = p.children[1]
#                     else:
#                         return -1
#                 else:
#                     if p.children[1] and p.children[1].minimum <= m:
#                         p = p.children[1]
#                         ret ^= (1 << i)
#                     elif p.children[0]:
#                         p = p.children[0]
#                     else:
#                         return -1
#             return ret

#         return [search(x, m) for x, m in queries]

if __name__ == "__main__":
    solu = Solution()
    nums = [0, 1, 2, 3, 4]
    queries = [[3, 1], [1, 3], [5, 6]]
    print(solu.maximizeXor(nums, queries))

    nums = [5, 2, 4, 6, 6, 3]
    queries = [[12, 4], [8, 1], [6, 3]]
    print(solu.maximizeXor(nums, queries))
