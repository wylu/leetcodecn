#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5906.句子中的有效单词数.py
@Time    :   2021/10/24 10:30:25
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def countValidWords(self, sentence: str) -> int:
        def check(token: str) -> bool:
            cnt = {'-': 0, '!': 0, '.': 0, ',': 0}
            n = len(token)
            for i, ch in enumerate(token):
                if '0' <= ch <= '9':
                    return False
                if ch == '-' and (i == 0 or i == n - 1
                                  or not ('a' <= token[i - 1] <= 'z')
                                  or not ('a' <= token[i + 1] <= 'z')):
                    return False
                if ch in '!.,' and i != n - 1:
                    return False

                if 'a' <= ch <= 'z':
                    continue

                cnt[ch] += 1

            return cnt['-'] <= 1 and cnt['!'] + cnt['.'] + cnt[','] <= 1

        ans = 0
        for token in sentence.split():
            if check(token):
                ans += 1

        return ans


if __name__ == '__main__':
    solu = Solution()
    sentence = "cat and  dog"
    print(solu.countValidWords(sentence))

    sentence = "!this  1-s b8d!"
    print(solu.countValidWords(sentence))

    sentence = "alice and  bob are playing stone-game10"
    print(solu.countValidWords(sentence))

    sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
    print(solu.countValidWords(sentence))

    sentence = (
        " 62   nvtk0wr4f  8 qt3r! w1ph 1l ,e0d 0n 2v 7c.  n06huu2n9 s9   "
        "ui4 nsr!d7olr  q-, vqdo!btpmtmui.bb83lf g .!v9-lg 2fyoykex uy5a "
        "8v whvu8 .y sc5 -0n4 zo pfgju 5u 4 3x,3!wl  fv4   s  aig cf j1 a"
        " i  8m5o1  !u n!.1tz87d3 .9    n a3  .xb1p9f  b1i a j8s2 cugf l4"
        "94cx1! hisceovf3 8d93 sg 4r.f1z9w   4- cb r97jo hln3s h2 o .  8d"
        "x08as7l!mcmc isa49afk i1 fk,s e !1 ln rt2vhu 4ks4zq c w  o- 6  5"
        "!.n8ten0 6mk 2k2y3e335,yj  h p3 5 -0  5g1c  tr49, ,qp9 -v p  7p4"
        "v110926wwr h x wklq u zo 16. !8  u63n0c l3 yckifu 1cgz t.i   lh "
        "w xa l,jt   hpi ng-gvtk8 9 j u9qfcd!2  kyu42v dmv.cst6i5fo rxhw4"
        "wvp2 1 okc8!  z aribcam0  cp-zp,!e x  agj-gb3 !om3934 k vnuo056h"
        " g7 t-6j! 8w8fncebuj-lq    inzqhw v39,  f e 9. 50 , ru3r  mbuab "
        " 6  wz dw79.av2xp . gbmy gc s6pi pra4fo9fwq k   j-ppy -3vpf   o "
        "k4hy3 -!..5s ,2 k5 j p38dtd   !i   b!fgj,nx qgif ")
    print(solu.countValidWords(sentence))
