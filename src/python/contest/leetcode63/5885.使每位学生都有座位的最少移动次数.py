#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5885.使每位学生都有座位的最少移动次数.py
@Time    :   2021/10/16 22:31:19
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        ans = 0
        for seat, stu in zip(seats, students):
            ans += abs(stu - seat)
        return ans
