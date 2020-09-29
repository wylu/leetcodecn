#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1520.最多的不重叠子字符串.py
@Time    :   2020/09/29 14:45:02
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1520 lang=python3
#
# [1520] 最多的不重叠子字符串
#
# https://leetcode-cn.com/problems/maximum-number-of-non-overlapping-substrings/description/
#
# algorithms
# Hard (30.45%)
# Likes:    43
# Dislikes: 0
# Total Accepted:    1.8K
# Total Submissions: 6K
# Testcase Example:  '"adefaddaccc"'
#
# 给你一个只包含小写字母的字符串 s ，你需要找到 s 中最多数目的非空子字符串，满足如下条件：
#
#
# 这些字符串之间互不重叠，也就是说对于任意两个子字符串 s[i..j] 和 s[k..l] ，要么 j < k 要么 i > l 。
# 如果一个子字符串包含字符 char ，那么 s 中所有 char 字符都应该在这个子字符串中。
#
#
# 请你找到满足上述条件的最多子字符串数目。如果有多个解法有相同的子字符串数目，请返回这些子字符串总长度最小的一个解。可以证明最小总长度解是唯一的。
#
# 请注意，你可以以 任意 顺序返回最优解的子字符串。
#
#
#
# 示例 1：
#
# 输入：s = "adefaddaccc"
# 输出：["e","f","ccc"]
# 解释：下面为所有满足第二个条件的子字符串：
# [
# "adefaddaccc"
# "adefadda",
# "ef",
# "e",
# ⁠ "f",
# "ccc",
# ]
# 如果我们选择第一个字符串，那么我们无法再选择其他任何字符串，所以答案为 1 。如果我们选择 "adefadda" ，剩下子字符串中我们只可以选择
# "ccc" ，它是唯一不重叠的子字符串，所以答案为 2 。同时我们可以发现，选择 "ef" 不是最优的，因为它可以被拆分成 2
# 个子字符串。所以最优解是选择 ["e","f","ccc"] ，答案为 3 。不存在别的相同数目子字符串解。
#
#
# 示例 2：
#
# 输入：s = "abbaccd"
# 输出：["d","bb","cc"]
# 解释：注意到解 ["d","abba","cc"] 答案也为 3 ，但它不是最优解，因为它的总长度更长。
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 10^5
# s 只包含小写英文字母。
#
#
#
from typing import List
"""
方法一：贪心

思路与算法

由于要求「如果一个子字符串包含字符 c，那么 s 中所有 c 字符都应该在
这个子字符串中」，且要使最后的总长度尽可能的小，因此最多不会有超过
字符集大小 Σ 数量的子字符串。

假设当前找到了包含字符 a 的符合条件的最短字符串 s[la,ra]，看起来
s[la-1,ra] 或者 s[la,ra+1] 也可能作为一个符合条件的字符串，但是
要使最后的「长度和最小」，因此我们只需要关注包含每个字符的「最短
字符串」即可。

所以解决问题的第一步是需要预处理出字符集中每个字符对应的最短字符串，
由于字符集很小，我们可以暴力处理这一部分的答案。首先遍历字符串，
确定字符 i 第一次出现的位置 li 和最后一次出现的位置 ri，由于
[li,ri] 中间可能存在其他字符，因此为了满足题目的第二点
要求，我们需要遍历 [li,ri] 中的所有字符，利用它们的左右端点来更新
li 和 ri，保证「如果一个子字符串包含字符 c，那么 s 中所有 c 字符
都应该在这个子字符串中」。

预处理完以后，将每个字符串的起止位置看作一个个线段 [li,ri]，那么
问题可转化为：“有一个 [0,n−1] 的一维数轴，其中 n=s.length，我们
需要用尽可能多的线段去覆盖这个数轴，且线段间互不相交，线段之和最小”。
这是一个很经典的贪心问题，我们只需要将得到的线段按右端点为第一关
键字，长度为第二关键字排序，然后从前往后遍历线段，每次遇到可以加入
的（与已加入的线段无重叠）线段，就贪心地将其加入数组即可。

贪心思路的正确性可以考虑如下例子：对于两个线段 [l1,r1] 和 [l2,r2]，
其中 r2 > r1 且 l2 <= r1，如果我们选择 [l2,r2] 这个线段，那么剩下
可分配的数轴就变少了，这对于最后得到的答案一定是不会更优的，因此最佳
的策略是贪心地选择第一个线段 [l1,r1]。
"""


# @lc code=start
class Seg:
    def __init__(self, left=-1, right=-1):
        self.left = left
        self.right = right

    def __lt__(self, obj):
        if self.right == obj.right:
            return self.left > obj.left
        return self.right < obj.right


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        segs = [Seg() for _ in range(26)]

        # 预处理左右端点
        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')
            if segs[idx].left == -1:
                segs[idx].left = segs[idx].right = i
            else:
                segs[idx].right = i

        # 计算符合要求的区间
        opts = []
        for seg in segs:
            if seg.left == -1:
                continue
            i, lt, rt = seg.left, seg.left, seg.right
            keep_left = True
            while i <= rt:
                j = ord(s[i]) - ord('a')
                if segs[j].left < lt or segs[j].right > rt:
                    # 如果左端点有更新，假设这个备选区间一定需要拓展到【L,R】才封闭，
                    # 那从L出发的字符区间向右拓展也会达到【L,R】，所以直接退出即可，
                    # 这里退出还可以去重，保证只有一组【L,R】
                    if segs[j].left < lt:
                        keep_left = False
                        break
                    rt = max(rt, segs[j].right)
                i += 1
            if keep_left:
                opts.append(Seg(lt, rt))

        # 贪心选取
        opts.sort()
        ans = []
        end = -1
        for seg in opts:
            if seg.left > end:
                ans.append(s[seg.left:seg.right + 1])
                end = seg.right

        return ans


# @lc code=end

# class Solution:
#     def maxNumOfSubstrings(self, s: str) -> List[str]:
#         segs = [Seg() for _ in range(26)]

#         # 预处理左右端点
#         for i in range(len(s)):
#             idx = ord(s[i]) - ord('a')
#             if segs[idx].left == -1:
#                 segs[idx].left = segs[idx].right = i
#             else:
#                 segs[idx].right = i

#         # 扩展更新左右端点
#         for seg in segs:
#             if seg.left == -1:
#                 continue
#             i = seg.left
#             while i <= seg.right:
#                 ci = ord(s[i]) - ord('a')
#                 if seg.left <= segs[ci].left and seg.right >= segs[ci].right:
#                     i += 1
#                     continue
#                 seg.left = min(seg.left, segs[ci].left)
#                 seg.right = max(seg.right, segs[ci].right)
#                 i = seg.left

#         # 贪心选取
#         segs.sort()
#         ans = []
#         end = -1
#         for seg in segs:
#             if seg.left > end:
#                 ans.append(s[seg.left:seg.right + 1])
#                 end = seg.right

#         return ans

if __name__ == "__main__":
    solu = Solution()
    print(solu.maxNumOfSubstrings('adefaddaccc'))
    print(solu.maxNumOfSubstrings('abab'))
