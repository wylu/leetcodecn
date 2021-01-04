#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   bisect_demo.py
@Time    :   2021/01/04 20:16:14
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :   https://docs.python.org/zh-cn/3/library/bisect.html
"""
import bisect

if __name__ == "__main__":
    # bisect_left
    nums = [1, 2, 3, 4, 5]
    target = 3
    print('nums: {}, target: {}, res: {}'.format(
        nums, target, bisect.bisect_left(nums, target)))

    nums = [1, 2, 3, 4, 5]
    target = 1
    print('nums: {}, target: {}, res: {}'.format(
        nums, target, bisect.bisect_left(nums, target)))

    nums = [1, 2, 3, 4, 5]
    target = 5
    print('nums: {}, target: {}, res: {}'.format(
        nums, target, bisect.bisect_left(nums, target)))

    nums = [1, 2, 4, 5]
    target = 3
    print('nums: {}, target: {}, res: {}'.format(
        nums, target, bisect.bisect_left(nums, target)))

    nums = [1, 2, 3, 3, 3, 4, 5]
    target = 3
    print('nums: {}, target: {}, res: {}'.format(
        nums, target, bisect.bisect_left(nums, target)))

    print('=============================================')

    # bisect_right
    nums = [1, 2, 3, 4, 5]
    target = 3
    print('nums: {}, target: {}, res: {}'.format(
        nums, target, bisect.bisect_right(nums, target)))

    nums = [1, 2, 3, 4, 5]
    target = 1
    print('nums: {}, target: {}, res: {}'.format(
        nums, target, bisect.bisect_right(nums, target)))

    nums = [1, 2, 3, 4, 5]
    target = 5
    print('nums: {}, target: {}, res: {}'.format(
        nums, target, bisect.bisect_right(nums, target)))

    nums = [1, 2, 4, 5]
    target = 3
    print('nums: {}, target: {}, res: {}'.format(
        nums, target, bisect.bisect_right(nums, target)))

    nums = [1, 2, 3, 3, 3, 4, 5]
    target = 3
    print('nums: {}, target: {}, res: {}'.format(
        nums, target, bisect.bisect_right(nums, target)))
