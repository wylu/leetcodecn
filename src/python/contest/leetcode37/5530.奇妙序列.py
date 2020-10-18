#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5530.奇妙序列.py
@Time    :   2020/10/17 23:12:23
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Fancy:
    def __init__(self):
        pass

    def append(self, val: int) -> None:
        pass

    def addAll(self, inc: int) -> None:
        pass

    def multAll(self, m: int) -> None:
        pass

    def getIndex(self, idx: int) -> int:
        pass


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)

if __name__ == "__main__":
    fancy = Fancy()
    fancy.append(2)  # 奇妙序列：[2]
    fancy.addAll(3)  # 奇妙序列：[2+3] -> [5]
    fancy.append(7)  # 奇妙序列：[5, 7]
    fancy.multAll(2)  # 奇妙序列：[5*2, 7*2] -> [10, 14]
    print(fancy.getIndex(0))  # 返回 10
    fancy.addAll(3)  # 奇妙序列：[10+3, 14+3] -> [13, 17]
    fancy.append(10)  # 奇妙序列：[13, 17, 10]
    fancy.multAll(2)  # 奇妙序列：[13*2, 17*2, 10*2] -> [26, 34, 20]
    print(fancy.getIndex(0))  # 返回 26
    print(fancy.getIndex(1))  # 返回 34
    print(fancy.getIndex(2))  # 返回 20
