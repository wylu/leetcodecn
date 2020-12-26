#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5621.无法吃午餐的学生数量.py
@Time    :   2020/12/26 22:30:38
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import deque
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)

        flag = True
        while flag:
            flag = False
            for _ in range(len(students)):
                if students[0] == sandwiches[0]:
                    students.popleft()
                    sandwiches.popleft()
                    flag = True
                else:
                    students.append(students.popleft())

        return len(students)


if __name__ == "__main__":
    solu = Solution()
    print(solu.countStudents([1, 1, 0, 0], [0, 1, 0, 1]))
    print(solu.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))
