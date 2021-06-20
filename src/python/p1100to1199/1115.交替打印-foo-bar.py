#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1115.交替打印-foo-bar.py
@Time    :   2021/06/21 00:12:25
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1115 lang=python3
#
# [1115] 交替打印FooBar
#
# https://leetcode-cn.com/problems/print-foobar-alternately/description/
#
# concurrency
# Medium (55.88%)
# Likes:    116
# Dislikes: 0
# Total Accepted:    37.3K
# Total Submissions: 66.8K
# Testcase Example:  '1'
#
# 我们提供一个类：
#
#
# class FooBar {
# ⁠ public void foo() {
# for (int i = 0; i < n; i++) {
# print("foo");
# }
# ⁠ }
#
# ⁠ public void bar() {
# for (int i = 0; i < n; i++) {
# print("bar");
# }
# ⁠ }
# }
#
#
# 两个不同的线程将会共用一个 FooBar 实例。其中一个线程将会调用 foo() 方法，另一个线程将会调用 bar() 方法。
#
# 请设计修改程序，以确保 "foobar" 被输出 n 次。
#
#
#
# 示例 1:
#
#
# 输入: n = 1
# 输出: "foobar"
# 解释: 这里有两个线程被异步启动。其中一个调用 foo() 方法, 另一个调用 bar() 方法，"foobar" 将被输出一次。
#
#
# 示例 2:
#
#
# 输入: n = 2
# 输出: "foobarfoobar"
# 解释: "foobar" 将被输出两次。
#
#
#

# @lc code=start
import threading


class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock1 = threading.Lock()
        self.lock1.acquire()
        self.lock2 = threading.Lock()

    def foo(self, printFoo: 'Callable[[], None]') -> None:  # noqa F821
        for i in range(self.n):
            self.lock2.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.lock1.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:  # noqa F821
        for i in range(self.n):
            self.lock1.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.lock2.release()


# @lc code=end
