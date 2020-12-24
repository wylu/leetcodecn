#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1114.按序打印.py
@Time    :   2020/12/24 23:31:41
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1114 lang=python3
#
# [1114] 按序打印
#
# https://leetcode-cn.com/problems/print-in-order/description/
#
# concurrency
# Easy (64.43%)
# Likes:    217
# Dislikes: 0
# Total Accepted:    50.8K
# Total Submissions: 78.9K
# Testcase Example:  '[1,2,3]'
#
# 我们提供了一个类：
#
# public class Foo {
# public void first() { print("first"); }
# public void second() { print("second"); }
# public void third() { print("third"); }
# }
#
# 三个不同的线程将会共用一个 Foo 实例。
#
#
# 线程 A 将会调用 first() 方法
# 线程 B 将会调用 second() 方法
# 线程 C 将会调用 third() 方法
#
#
# 请设计修改程序，以确保 second() 方法在 first() 方法之后被执行，third() 方法在 second() 方法之后被执行。
#
#
#
# 示例 1:
#
# 输入: [1,2,3]
# 输出: "firstsecondthird"
# 解释:
# 有三个线程会被异步启动。
# 输入 [1,2,3] 表示线程 A 将会调用 first() 方法，线程 B 将会调用 second() 方法，线程 C 将会调用 third() 方法。
# 正确的输出是 "firstsecondthird"。
#
#
# 示例 2:
#
# 输入: [1,3,2]
# 输出: "firstsecondthird"
# 解释:
# 输入 [1,3,2] 表示线程 A 将会调用 first() 方法，线程 B 将会调用 third() 方法，线程 C 将会调用 second() 方法。
# 正确的输出是 "firstsecondthird"。
#
#
#
# 提示：
#
#
# 尽管输入中的数字似乎暗示了顺序，但是我们并不保证线程在操作系统中的调度顺序。
# 你看到的输入格式主要是为了确保测试的全面性。
#
#
#
import threading


# @lc code=start
class Foo:
    def __init__(self):
        self.lock1 = threading.Lock()
        self.lock1.acquire()
        self.lock2 = threading.Lock()
        self.lock2.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:  # noqa F821
        # printFirst() outputs "first".
        printFirst()
        self.lock1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:  # noqa F821
        self.lock1.acquire()
        # printSecond() outputs "second".
        printSecond()
        self.lock2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:  # noqa F821
        self.lock2.acquire()
        # printThird() outputs "third".
        printThird()
        self.lock2.release()


# @lc code=end
