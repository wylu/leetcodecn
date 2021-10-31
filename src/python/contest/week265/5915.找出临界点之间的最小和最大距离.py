#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5915.找出临界点之间的最小和最大距离.py
@Time    :   2021/10/31 10:31:41
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self,
                                   head: Optional[ListNode]) -> List[int]:
        nums = []
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next

        ans = [-1, -1]
        n = len(nums)
        indices = []
        for i in range(1, n - 1):
            if (nums[i - 1] > nums[i] < nums[i + 1]
                    or nums[i - 1] < nums[i] > nums[i + 1]):
                indices.append(i)

                if len(indices) > 1:
                    if ans[0] == -1:
                        ans[0] = indices[-1] - indices[-2]
                    else:
                        ans[0] = min(ans[0], indices[-1] - indices[-2])

        if len(indices) > 1:
            ans[1] = indices[-1] - indices[0]

        return ans
