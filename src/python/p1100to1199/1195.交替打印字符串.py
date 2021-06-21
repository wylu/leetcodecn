#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1195.交替打印字符串.py
@Time    :   2021/06/21 22:55:05
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1195 lang=python3
#
# [1195] 交替打印字符串
#
# https://leetcode-cn.com/problems/fizz-buzz-multithreaded/description/
#
# concurrency
# Medium (63.26%)
# Likes:    53
# Dislikes: 0
# Total Accepted:    11.9K
# Total Submissions: 18.8K
# Testcase Example:  '15'
#
# 编写一个可以从 1 到 n 输出代表这个数字的字符串的程序，但是：
#
#
# 如果这个数字可以被 3 整除，输出 "fizz"。
# 如果这个数字可以被 5 整除，输出 "buzz"。
# 如果这个数字可以同时被 3 和 5 整除，输出 "fizzbuzz"。
#
#
# 例如，当 n = 15，输出： 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13,
# 14, fizzbuzz。
#
# 假设有这么一个类：
#
#
# class FizzBuzz {
# public FizzBuzz(int n) { ... }               // constructor
# ⁠ public void fizz(printFizz) { ... }          // only output "fizz"
# ⁠ public void buzz(printBuzz) { ... }          // only output "buzz"
# ⁠ public void fizzbuzz(printFizzBuzz) { ... }  // only output "fizzbuzz"
# ⁠ public void number(printNumber) { ... }      // only output the numbers
# }
#
# 请你实现一个有四个线程的多线程版  FizzBuzz， 同一个 FizzBuzz 实例会被如下四个线程使用：
#
#
# 线程A将调用 fizz() 来判断是否能被 3 整除，如果可以，则输出 fizz。
# 线程B将调用 buzz() 来判断是否能被 5 整除，如果可以，则输出 buzz。
# 线程C将调用 fizzbuzz() 来判断是否同时能被 3 和 5 整除，如果可以，则输出 fizzbuzz。
# 线程D将调用 number() 来实现输出既不能被 3 整除也不能被 5 整除的数字。
#
#
#
#
# 提示：
#
#
# 本题已经提供了打印字符串的相关方法，如 printFizz() 等，具体方法名请参考答题模板中的注释部分。
#
#
#
#
#

# @lc code=start
import threading


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.sema = threading.Semaphore(0)
        self.sema3 = threading.Semaphore(0)
        self.sema5 = threading.Semaphore(0)
        self.sema35 = threading.Semaphore(0)
        self.cur = 1

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:  # noqa F821
        while True:
            self.sema3.acquire()
            if self.cur > self.n:
                break
            printFizz()
            self.sema.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:  # noqa F821
        while True:
            self.sema5.acquire()
            if self.cur > self.n:
                break
            printBuzz()
            self.sema.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self,
                 printFizzBuzz: 'Callable[[], None]') -> None:  # noqa F821
        while True:
            self.sema35.acquire()
            if self.cur > self.n:
                break
            printFizzBuzz()
            self.sema.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self,
               printNumber: 'Callable[[int], None]') -> None:  # noqa F821
        while self.cur <= self.n:
            if self.cur % 3 == 0 and self.cur % 5 == 0:
                self.sema35.release()
            elif self.cur % 3 == 0:
                self.sema3.release()
            elif self.cur % 5 == 0:
                self.sema5.release()
            else:
                printNumber(self.cur)
                self.sema.release()

            self.sema.acquire()
            self.cur += 1

        self.sema3.release()
        self.sema5.release()
        self.sema35.release()


# @lc code=end
