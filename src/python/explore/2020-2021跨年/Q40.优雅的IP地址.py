#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   Q40.优雅的IP地址.py
@Time    :   2020/12/28 13:55:30
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
https://leetcode-cn.com/leetbook/read/interesting-algorithm-puzzles-for-programmers/9i00p1/

方法一：枚举二进制 + 判断
https://leetcode-cn.com/circle/discuss/YmmSCq/
思路与算法

我们可以想到两种枚举方法：

枚举十进制 IP 地址，并判断对应的二进制是否左右对称；
枚举二进制 IP 地址，并判断对应的十进制是否恰好包含 [0, 9]。

对于第一种枚举方法，我们需要枚举 [0, 9] 的所有排列，并且对于每一种
排列需要枚举 IP 地址的分隔位置，这样编码较为困难。而对于第二种枚举
方法，二进制 IP 地址是固定 8 位分隔的，这样编码较为简单。因此我们
尝试第二种。

由于二进制 IP 地址是左右对称的，因此我们只需要枚举前 16 位，对于
后 16 位只需要将其反转即可。在枚举时，我们可以枚举 [0, 2^16) 中
的所有十进制数，并使用位运算

    (mask >> i) & 1

得到 mask 的从低到高第 i 个（从 0 开始编号）二进制位。其中 >>
表示右移运算，& 表示按位与运算。借助位运算，我们就可以分别得到
mask 的「高 8 位」「低 8 位」「反转后的高 8 位」「反转后的低 8 位」
这 4 个二进制表示对应的十进制数。

接下来我们只需要检查这 4 个十进制数是否恰好包含 [0, 9] 各一次，
我们可以使用数组、哈希表等任何简单的数据结构，对它们按位进行计数即可。
"""
from typing import List


class Solution:
    def elegantIpAddress(self) -> List[str]:
        ans = []

        def check(ip: List[int]) -> bool:
            flags = [False] * 10
            for ch in ''.join(ip):
                digit = int(ch)
                if flags[digit]:
                    return False
                flags[digit] = True
            return all(flags)

        for mask in range(1 << 16):
            ip = [0] * 4

            # 高 8 位
            for i in range(15, 7, -1):
                ip[0] = ip[0] * 2 + ((mask >> i) & 1)

            # 低 8 位
            for i in range(7, -1, -1):
                ip[1] = ip[1] * 2 + ((mask >> i) & 1)

            # 反转后的高 8 位
            for i in range(8):
                ip[2] = ip[2] * 2 + ((mask >> i) & 1)

            # 反转后的低 8 位
            for i in range(8, 16):
                ip[3] = ip[3] * 2 + ((mask >> i) & 1)

            ip = list(map(str, ip))
            if check(ip):
                ans.append('.'.join(ip))

        return ans


if __name__ == "__main__":
    solu = Solution()
    # [
    #   '34.179.205.68', '34.205.179.68',
    #   '68.179.205.34', '68.205.179.34',
    #   '179.34.68.205', '179.68.34.205',
    #   '205.34.68.179', '205.68.34.179'
    # ]
    print(solu.elegantIpAddress())
