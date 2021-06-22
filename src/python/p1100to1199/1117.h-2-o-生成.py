#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1117.h-2-o-生成.py
@Time    :   2021/06/22 19:33:56
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1117 lang=python3
#
# [1117] H2O 生成
#
# https://leetcode-cn.com/problems/building-h2o/description/
#
# concurrency
# Medium (51.77%)
# Likes:    85
# Dislikes: 0
# Total Accepted:    15.2K
# Total Submissions: 29.4K
# Testcase Example:  '"HOH"'
#
# 现在有两种线程，氧 oxygen 和氢 hydrogen，你的目标是组织这两种线程来产生水分子。
#
# 存在一个屏障（barrier）使得每个线程必须等候直到一个完整水分子能够被产生出来。
#
# 氢和氧线程会被分别给予 releaseHydrogen 和 releaseOxygen 方法来允许它们突破屏障。
#
# 这些线程应该三三成组突破屏障并能立即组合产生一个水分子。
#
# 你必须保证产生一个水分子所需线程的结合必须发生在下一个水分子产生之前。
#
# 换句话说:
#
#
# 如果一个氧线程到达屏障时没有氢线程到达，它必须等候直到两个氢线程到达。
# 如果一个氢线程到达屏障时没有其它线程到达，它必须等候直到一个氧线程和另一个氢线程到达。
#
#
# 书写满足这些限制条件的氢、氧线程同步代码。
#
#
#
# 示例 1:
#
# 输入: "HOH"
# 输出: "HHO"
# 解释: "HOH" 和 "OHH" 依然都是有效解。
#
#
# 示例 2:
#
# 输入: "OOHHHH"
# 输出: "HHOHHO"
# 解释: "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH" 和
# "OHHOHH" 依然都是有效解。
#
#
#
#
# 提示：
#
#
# 输入字符串的总长将会是 3n, 1 ≤ n ≤ 50；
# 输入字符串中的 “H” 总数将会是 2n 。
# 输入字符串中的 “O” 总数将会是 n 。
#
#
#

# @lc code=start
import threading


class H2O:
    def __init__(self):
        self.b = threading.Barrier(3)
        self.h = threading.Semaphore(2)
        self.o = threading.Semaphore(1)

    def hydrogen(self,
                 releaseHydrogen: 'Callable[[], None]') -> None:  # noqa F821
        self.h.acquire()
        self.b.wait()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.h.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:  # noqa F821
        self.o.acquire()
        self.b.wait()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.o.release()


# @lc code=end
