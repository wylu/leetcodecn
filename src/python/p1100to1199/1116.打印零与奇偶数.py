#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1116.打印零与奇偶数.py
@Time    :   2021/06/20 23:47:00
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1116 lang=python3
#
# [1116] 打印零与奇偶数
#
# https://leetcode-cn.com/problems/print-zero-even-odd/description/
#
# concurrency
# Medium (50.83%)
# Likes:    101
# Dislikes: 0
# Total Accepted:    19.3K
# Total Submissions: 37.9K
# Testcase Example:  '2'
#
# 假设有这么一个类：
#
# class ZeroEvenOdd {
# public ZeroEvenOdd(int n) { ... }      // 构造函数
# ⁠ public void zero(printNumber) { ... }  // 仅打印出 0
# ⁠ public void even(printNumber) { ... }  // 仅打印出 偶数
# ⁠ public void odd(printNumber) { ... }   // 仅打印出 奇数
# }
#
#
# 相同的一个 ZeroEvenOdd 类实例将会传递给三个不同的线程：
#
#
# 线程 A 将调用 zero()，它只输出 0 。
# 线程 B 将调用 even()，它只输出偶数。
# 线程 C 将调用 odd()，它只输出奇数。
#
#
# 每个线程都有一个 printNumber 方法来输出一个整数。请修改给出的代码以输出整数序列 010203040506... ，其中序列的长度必须为
# 2n。
#
#
#
# 示例 1：
#
# 输入：n = 2
# 输出："0102"
# 说明：三条线程异步执行，其中一个调用 zero()，另一个线程调用 even()，最后一个线程调用odd()。正确的输出为 "0102"。
#
#
# 示例 2：
#
# 输入：n = 5
# 输出："0102030405"
#
#
#

# @lc code=start
import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.e_zero = threading.Event()
        self.e_zero.set()
        self.e_odd = threading.Event()
        self.e_even = threading.Event()
        self.cur = 0

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:  # noqa F821
        for _ in range(self.n):
            self.e_zero.wait()
            printNumber(0)
            self.e_zero.clear()
            if self.cur % 2 == 0:
                self.e_odd.set()
            else:
                self.e_even.set()

    def even(self, printNumber: 'Callable[[int], None]') -> None:  # noqa F821
        for i in range(2, self.n + 1, 2):
            self.e_even.wait()
            self.cur = i
            printNumber(i)
            self.e_even.clear()
            self.e_zero.set()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:  # noqa F821
        for i in range(1, self.n + 1, 2):
            self.e_odd.wait()
            self.cur = i
            printNumber(i)
            self.e_odd.clear()
            self.e_zero.set()


# @lc code=end
