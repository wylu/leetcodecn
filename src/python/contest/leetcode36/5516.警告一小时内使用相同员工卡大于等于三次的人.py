#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5516.警告一小时内使用相同员工卡大于等于三次的人.py
@Time    :   2020/10/03 22:35:50
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        pairs = []
        for i in range(len(keyName)):
            hour, minute = keyTime[i].split(':')
            pairs.append((keyName[i], int(hour) * 60 + int(minute)))

        pairs.sort()
        ans = []
        name, cnt = pairs[0][0], 1
        for i in range(1, len(pairs)):
            if pairs[i][0] != name:
                name, cnt = pairs[i][0], 1
                continue

            cnt += 1
            if cnt >= 3 and pairs[i][1] - pairs[i - 2][1] <= 60:
                if not ans or ans[-1] != name:
                    ans.append(name)

        return ans


if __name__ == "__main__":
    solu = Solution()
    keyName = ["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"]
    keyTime = ["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]
    print(solu.alertNames(keyName, keyTime))
