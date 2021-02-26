#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1178.猜字谜.py
@Time    :   2021/02/26 21:50:10
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1178 lang=python3
#
# [1178] 猜字谜
#
# https://leetcode-cn.com/problems/number-of-valid-words-for-each-puzzle/description/
#
# algorithms
# Hard (43.15%)
# Likes:    166
# Dislikes: 0
# Total Accepted:    13.3K
# Total Submissions: 30.8K
# Testcase Example:
# '["aaaa","asas","able","ability","actt","actor","access"]\n' +
# '["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]'
#
# 外国友人仿照中国字谜设计了一个英文版猜字谜小游戏，请你来猜猜看吧。
#
# 字谜的迷面 puzzle 按字符串形式给出，如果一个单词 word 符合下面两个条件，那么它就可以算作谜底：
#
#
# 单词 word 中包含谜面 puzzle 的第一个字母。
# 单词 word 中的每一个字母都可以在谜面 puzzle 中找到。
# 例如，如果字谜的谜面是 "abcdefg"，那么可以作为谜底的单词有 "faced", "cabbage", 和 "baggage"；而
# "beefed"（不含字母 "a"）以及 "based"（其中的 "s" 没有出现在谜面中）都不能作为谜底。
#
#
# 返回一个答案数组 answer，数组中的每个元素 answer[i] 是在给出的单词列表 words 中可以作为字谜迷面 puzzles[i]
# 所对应的谜底的单词数目。
#
#
#
# 示例：
#
#
# 输入：
# words = ["aaaa","asas","able","ability","actt","actor","access"],
# puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
# 输出：[1,1,3,2,4,0]
# 解释：
# 1 个单词可以作为 "aboveyz" 的谜底 : "aaaa"
# 1 个单词可以作为 "abrodyz" 的谜底 : "aaaa"
# 3 个单词可以作为 "abslute" 的谜底 : "aaaa", "asas", "able"
# 2 个单词可以作为 "absoryz" 的谜底 : "aaaa", "asas"
# 4 个单词可以作为 "actresz" 的谜底 : "aaaa", "asas", "actt", "access"
# 没有单词可以作为 "gaswxyz" 的谜底，因为列表中的单词都不含字母 'g'。
#
#
#
#
# 提示：
#
#
# 1 <= words.length <= 10^5
# 4 <= words[i].length <= 50
# 1 <= puzzles.length <= 10^4
# puzzles[i].length == 7
# words[i][j], puzzles[i][j] 都是小写英文字母。
# 每个 puzzles[i] 所包含的字符都不重复。
#
#
#
from collections import defaultdict
from typing import List
"""
前言
我们首先需要理解清楚题目中的字谜规则：

对于单词 word 以及谜面 puzzle，设 Sw 表示 word 中出现的字母组成的「不重复」
集合，Sp 表示 puzzle 中出现的字母组成的集合（由于题目中规定了 puzzle 中出现的
字母是不重复的，因此这个集合本身也是「不重复」的）。

如果存在 Sp 的一个子集 Sp'，并且 Sp' 包含 puzzle 中的首字母，使得 Sw = Sp'，
那么 word 就是 puzzle 的谜底。

因此，我们可以设计出解决该字谜问题的一个算法流程：

首先我们计算出每一个 word 对应的集合 Sw，存放在某一「数据结构」中，便于后续
操作中的快速查找；

随后我们依次枚举每一个 puzzle，计算出其对应的集合 Sp，并枚举满足要求的子集
Sp'。对于每一个 Sp'，我们在「数据结构」中查找其出现的次数，那么所有的 Sp'
出现次数之和就是 puzzle 对应的谜底个数。

存放 Sw 对应的「数据结构」可以有多种选择，本篇题解中会介绍较为常用的两种。

方法一：二进制状态压缩
思路与算法

由于题目中规定 word 和 puzzle 均只包含小写字母，因此 Sw 和 Sp 的大小最多为
26，我们可以考虑使用一个长度为 26 的二进制数 bw 或 bp 来表示这一集合。

对于 bw 从低到高的第 i 个二进制位（i 从 0 开始编号），如果 Sw 中包含第 i 个
小写字母，那么对应的二进制位为 1，否则为 0。

因此我们可以使用一个哈希映射来表示需要的「数据结构」：对于哈希映射中的每一个
键值对，其中的键表示一个长度为 26 的二进制数，值表示其出现的次数，即数组
words 中多少个 word 压缩成的二进制数等于键。构造哈希映射的过程也很简单：
我们只需要遍历每一个 word，并遍历 word 中的每一个字母，将对应位置的二进制位
标记为 1，这样就计算出了 word 对应的二进制表示，将其在哈希映射中作为键对应的
值增加 1 即可。

对于 puzzle 对应的 bp，我们可以通过相同的方法求出，那么接下来就需要枚举 bp
的子集 bp' 了。枚举一个二进制数的子集也有多种方法，这里介绍常用的两种：

第一种：由于题目中规定 puzzle 的长度恰好为 7，因此我们可以枚举所有 6 位的
二进制数（因为 puzzle 中的首字母必须要出现，因此最高位必须是 1，我们只需要
枚举剩余的 6 位就行了）。对于每个枚举出的 6 位二进制数，我们遍历 puzzle
中除了首字母以外的其余 6 个字母，只有当二进制位为 1 时，我们才将 puzzle
中的字母在二进制表示中的二进制位标记位 1。这样我们就得到了每一个 bp' 对应
的二进制表示。

第二种：我们也可以使用通用的「枚举二进制子集」的方法，下面给出伪代码：

function get_subset(bitmask)
    subset = bitmask
    answer = [bitmask]
    while subset != 0
        subset = (subset - 1) & bitmask
        put subset into the answer list
    end while
    return answer
end function

其中 bitmask 表示一个二进制数，subset 会遍历所有 bitmask 的子集，并将
所有的子集放入 answer 中。需要注意的是，bitmask 本身也是 bitmask 的一个
子集，因此 answer 在初始时就包含 bitmask 本身。

与第一种方法类似，我们需要保证 puzzle 中的首字母必须要出现，因此在使用
第二种方法枚举子集时，我们先将首字母对应的二进制位标记为 0，每枚举到一个
子集，就将首字母对应的二进制位标记为 1，这样得到的子集都是满足要求的。

在得到了 bp 的子集 bp' 后，我们将 bp' 在哈希映射中对应的值累计入答案，这样
bp 的所有子集的累加和就是其作为谜面的谜底数量。

细节

在遍历 word 时，如果 bw 中包含的 1 的数量大于 7，那么它一定无法作为谜底，
因此我们无需将其加入哈希映射中。
"""


# @lc code=start
class Solution:
    def findNumOfValidWords(self, words: List[str],
                            puzzles: List[str]) -> List[int]:
        def s2b(s: str) -> int:
            mask = 0
            for ch in s:
                mask |= (1 << (ord(ch) - ord('a')))
            return mask

        freq = defaultdict(int)
        for word in words:
            mask = s2b(word)
            if str(bin(mask)).count('1') <= 7:
                freq[mask] += 1

        ans = []
        for puzzle in puzzles:
            first = s2b(puzzle[:1])
            total = freq[first]  # 空集
            subset = mask = s2b(puzzle[1:])

            # 枚举子集
            while subset != 0:
                total += freq[first | subset]
                subset = (subset - 1) & mask

            ans.append(total)

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
    puzzles = [
        "aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"
    ]
    print(solu.findNumOfValidWords(words, puzzles))
