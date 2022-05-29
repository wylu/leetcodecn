#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6079.价格减免.py
@Time    :   2022/05/29 10:35:05
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:

    def discountPrices(self, sentence: str, discount: int) -> str:
        ans = []
        words = sentence.split()
        for word in words:
            if word[0] != '$' or not word[1:].isdigit():
                ans.append(word)
                continue
            ans.append(f'${int(word[1:]) * (100 - discount) / 100:.2f}')
        return ' '.join(ans)


if __name__ == '__main__':
    solu = Solution()
    sentence = "1 2 $3 4 $5 $6 7 8$ $9 $10$"
    discount = 100
    print(solu.discountPrices(sentence, discount))
