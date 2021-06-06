#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5779.装包裹的最小浪费空间.py
@Time    :   2021/06/06 21:03:28
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import bisect
from typing import List


class Solution:
    def minWastedSpace(self, packages: List[int],
                       boxes: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(packages)

        packages.sort()

        # 计算 packages 的前缀和
        ps = [0] * (n + 1)
        for i in range(n):
            ps[i + 1] = ps[i] + packages[i]

        ans = float("inf")
        for box in boxes:
            box.sort()

            # 如果最大包裹的尺寸大于最大箱子的尺寸，那么一定不满足，直接跳过
            if packages[-1] > box[-1]:
                continue

            # 指向还未被放入箱子的第一个包裹
            left = 0
            # 总浪费空间
            total = 0

            for y in box:
                # 如果当前箱子 y 的尺寸小于 left 指向的包裹，那么无需进行二分查找
                if y < packages[left]:
                    continue

                right = bisect.bisect_right(packages, y, left)

                total += (right - left) * y - (ps[right] - ps[left])
                left = right

                # 如果所有包裹都已经被放入箱子，可以提前退出
                if left == n:
                    break

            ans = min(ans, total)

        return -1 if ans == float("inf") else ans % MOD


if __name__ == '__main__':
    solu = Solution()
    print(solu.minWastedSpace(packages=[2, 3, 5], boxes=[[4, 8], [2, 8]]))

    packages = [2, 3, 5]
    boxes = [[1, 4], [2, 3], [3, 4]]
    print(solu.minWastedSpace(packages, boxes))

    packages = [3, 5, 8, 10, 11, 12]
    boxes = [[12], [11, 9], [10, 5, 14]]
    print(solu.minWastedSpace(packages, boxes))
