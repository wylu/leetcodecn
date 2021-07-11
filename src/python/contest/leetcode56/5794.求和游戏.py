#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5794.求和游戏.py
@Time    :   2021/07/10 22:56:03
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num) // 2
        tot_left = tot_right = 0
        cnt_left = cnt_right = 0
        for i, ch in enumerate(num):
            if i < n:
                if ch == '?':
                    cnt_left += 1
                else:
                    tot_left += ord(ch) - ord('0')
            else:
                if ch == '?':
                    cnt_right += 1
                else:
                    tot_right += ord(ch) - ord('0')

        if (cnt_left + cnt_right) % 2 != 0:
            return True

        min_cnt = min(cnt_left, cnt_right)
        cnt_left -= min_cnt
        cnt_right -= min_cnt

        if cnt_left == 0 and cnt_right == 0:
            return not (tot_left == tot_right)

        if cnt_left == 0:
            half = cnt_right // 2
            return ((tot_left < half * 9 + tot_right)
                    or (tot_left > half * 9 + tot_right))
        else:
            half = cnt_left // 2
            return ((tot_right < half * 9 + tot_left)
                    or (tot_right > half * 9 + tot_left))


if __name__ == '__main__':
    solu = Solution()
    # print(solu.sumGame(num="5023"))
    # print(solu.sumGame(num="25??"))
    # print(solu.sumGame(num="?3295???"))
    # print(solu.sumGame(num="?00?"))
    # print(solu.sumGame(num="?01?"))
    # print('----------------------------------------')
    # print(solu.sumGame(num="??"))
    # print(solu.sumGame(num="0???"))
    # print(solu.sumGame(num="9???"))
    # print('----------------------------------------')
    # print(solu.sumGame(num="??09????"))
    # print(solu.sumGame(num="??09??????"))
    # print(solu.sumGame(num="81??"))
    # print('----------------------------------------')
    # print(solu.sumGame(num="54208?183?"))

    num = ("?0?91172275656701?361205452?62??99?9??4478?796"
           "7373994600735??4?079246???5827572?81087461?089")
    print(solu.sumGame(num=num))
