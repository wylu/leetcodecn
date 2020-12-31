#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   Q69.蓝白歌会.py
@Time    :   2020/12/31 21:47:28
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
方法一：状态压缩 + 预处理 + 广度优先搜索
思路与算法

首先我们可以明确的是，对于任意一个「起始状态」，我们可以使用广度优先搜索
的方法，得出其变成某一个「终止状态」需要的移动次数。

然而枚举每一个「起始状态」并进行一次广度优先搜索，会使得代码运行较长的
时间。这是因为当 m=6, n=4 时，「起始状态」就已经有 2^(6*4)≈1.7*10^7
种了。因此我们可以使用记忆化的方法，将搜索过程中遇到的每一个状态对应的
移动次数都存储下来，在后续的搜索中，就无需进行重复搜索了。

如果我们将上面的过程反过来进行考虑，就可以发现，实际上我们是从 4 个终止
状态开始进行广度优先搜索，直到把所有的状态都搜索过一次为止。如果我们的
广度优先搜索最终进行了 x 轮，那么说明移动次数最多需要 x 次，并且第 x 轮
时在队列中的所有状态，就是我们所要求出的状态。

因此我们就可以使用广度优先搜索算法解决本题，然而我们还需要考虑如下的
几个问题：

如何表示一个状态？如果使用 6*4 的数组表示状态，可能会不便于对其进行存储、
哈希去重、或者在搜索时变化成为相邻的下一个的状态；

如果我们设计出了一种表示状态的方法，如何得到其相邻的状态？在本题中，相邻
的状态即为「将两个相邻的颜色不同的人交换位置」。

对于第一个问题，我们可以想到使用二进制状态压缩的方法来表示一个状态。直观
上来看，我们将蓝色看成 1，白色看成 0，就可以将 6*4 的数组压缩成一个 24
位的二进制数。在使用状态压缩后，我们可以使用一个整数类型存储一个状态，
在广度优先搜索中进行哈希去重，防止重复搜索也很方便。

对于第二个问题，我们如何快速地得到一个状态的相邻状态呢？我们可以借助一些
位运算的技巧来快速进行计算。对于状态 mask，我们希望交换它的第 i 位和
第 j 位，并且这两个位置对应的二进制位不相同（即一个为 0，一个为 1）。
在「不相同」的前提下，即我们希望把一个 0 变成 1，而把另一个 1 变成 0，
这使得我们想到异或运算：我们只要将 mask 与 2^i + 2^ 进行异或，就可以将
第 i 位和第 j 位从 0 变成 1 或者从 1 变成 0，也就间接完成了交换。对于
其余的位置，2^i + 2^j 的二进制位都是 0，那么异或之后 mask 的对应位置
也不会发生变化。

那么如何判断 mask 的第 i 位和第 j 位是否不同呢？我们同样可以借助位运算：

如果 mask 的第 i 位和第 j 位均为 0，那么 mask 与 2^i + 2^j 进行与运算
会得到 0；

如果 mask 的第 i 位和第 j 位均为 1，那么 mask 与 2^i + 2^j 进行与运算
会得到 2^i + 2^j；

如果 mask 第 i 位和第 j 位不同，即我们需要找出的情况，那么 mask 与
2^i + 2^j 进行与运算会得到 2^i 或者 2^j。

这样一来，我们在进行广度优先搜索之前，首先预处理出所有的 2^i + 2^j，其中
i 和 j 要么相差 1（左右相邻），要么相差 N（前后相邻）。在广度优先搜索的
过程中，对于当前的状态 mask，我们遍历所有预处理出的 2^i + 2^j，使用
与运算判断是否可以进行交换，并使用异或运算完成交换，即可快速地得到 mask
的所有相邻的状态。
"""
from collections import deque
from typing import List


class Solution:
    def nhk(self, m: int, n: int) -> int:
        states = self.getEndStates(m, n)
        q = deque(states)
        # 哈希表记录状态是否出现过，以及状态对应的步数
        seen = {state: 0 for state in states}

        # 预处理所有的 2^i+2^j 交换
        swap_masks = []
        for i in range(m):
            for j in range(n):
                pos = i * n + j
                # 左右相邻
                if j > 0:
                    swap_masks.append((1 << pos) + (1 << (pos - 1)))
                # 上下相邻
                if i > 0:
                    swap_masks.append((1 << pos) + (1 << (pos - n)))

        ans = 0
        while q:
            ans = len(q)
            for _ in range(ans):
                mask = q.popleft()
                for swap_mask in swap_masks:
                    if ((mask & swap_mask) != swap_mask
                            and (mask & swap_mask) != 0):
                        next_mask = mask ^ swap_mask
                        if next_mask not in seen:
                            q.append(next_mask)
                            seen[next_mask] = seen[mask] + 1

        return ans

    def getEndStates(self, m: int, n: int) -> List[int]:
        total_bits = m * n
        half_bits = total_bits // 2

        state1 = (1 << half_bits) - 1
        state2 = (1 << total_bits) - 1 - state1

        state3 = 0
        for i in range(m):
            cur = 0
            for j in range(n // 2, n):
                cur |= (1 << j)
            state3 = (state3 << n) | cur

        state4 = (1 << total_bits) - 1 - state3
        # 上白下蓝、上蓝下白、左蓝右白、左白右蓝
        return [state1, state2, state3, state4]


if __name__ == "__main__":
    solu = Solution()
    print(solu.nhk(6, 4))
