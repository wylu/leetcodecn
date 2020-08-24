#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   20.表示数值的字符串.py
@Time    :   2020/08/24 13:47:21
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
方法一：确定有限状态自动机
预备知识

确定有限状态自动机（以下简称「自动机」）是一类计算模型。它包含一系列状态，
这些状态中：

有一个特殊的状态，被称作「初始状态」。

还有一系列状态被称为「接受状态」，它们组成了一个特殊的集合。其中，一个状态
可能既是「初始状态」，也是「接受状态」。

起初，这个自动机处于「初始状态」。随后，它顺序地读取字符串中的每一个字符，
并根据当前状态和读入的字符，按照某个事先约定好的「转移规则」，从当前状态
转移到下一个状态；当状态转移完成后，它就读取下一个字符。当字符串全部读取
完毕后，如果自动机处于某个「接受状态」，则判定该字符串「被接受」；否则，
判定该字符串「被拒绝」。

注意：如果输入的过程中某一步转移失败了，即不存在对应的「转移规则」，此时
计算将提前中止。在这种情况下我们也判定该字符串「被拒绝」。

一个自动机，总能够回答某种形式的「对于给定的输入字符串 S，判断其是否满足
条件 P」的问题。在本题中，条件 P 即为「构成合法的表示数值的字符串」。

自动机驱动的编程，可以被看做一种暴力枚举方法的延伸：它穷尽了在任何一种
情况下，对应任何的输入，需要做的事情。自动机在计算机科学领域有着广泛的
应用。在算法领域，它与大名鼎鼎的字符串查找算法「KMP」算法有着密切的关联；
在工程领域，它是实现「正则表达式」的基础。


思路与算法

根据上面的描述，现在可以定义自动机的「状态集合」了。那么怎么挖掘出所有
可能的状态呢？一个常用的技巧是，用「当前处理到字符串的哪个部分」当作
状态的表述。根据这一技巧，不难挖掘出所有状态：

   1.起始的空格
   2.符号位
   3.整数部分
   4.左侧有整数的小数点
   5.左侧无整数的小数点
   6.小数部分
   7.字符 e
   8.指数部分的符号位
   9.指数部分的整数部分
  10.末尾的空格

下一步是找出「初始状态」和「接受状态」的集合。根据题意，「初始状态」应当
为状态 1，而「接受状态」的集合则为状态 3、状态 4、状态 6、状态 9 以及
状态 10。换言之，字符串的末尾要么是空格，要么是数字，要么是小数点，
但前提是小数点的前面有数字。

最后，需要定义「转移规则」。结合数值字符串应当具备的格式，将自动机转移的
过程以图解的方式表示出来：
https://assets.leetcode-cn.com/solution-static/jianzhi_20/jianzhi_20_fig1.png

在实际代码中，我们需要处理转移失败的情况。例如当位于状态 1（起始空格）时，
没有对应字符 e 的状态。为了处理这种情况，我们可以创建一个特殊的拒绝状态。
如果当前状态下没有对应读入字符的「转移规则」，我们就转移到这个特殊的拒绝
状态。一旦自动机转移到这个特殊状态，我们就可以立即判定该字符串不「被接受」。
"""
from enum import Enum


class Solution:
    def isNumber(self, s: str) -> bool:
        State = Enum('State', [
            'INITIAL', 'INT_SIGN', 'INTEGER', 'POINT', 'POINT_WITHOUT_INT',
            'FRACTION', 'EXP', 'EXP_SIGN', 'EXP_NUMBER', 'END'
        ])

        CharType = Enum('CharType',
                        ['NUMBER', 'EXP', 'POINT', 'SIGN', 'SPACE', 'ILLEGAL'])

        def toCharType(ch: str) -> CharType:
            if ch.isdigit():
                return CharType.NUMBER
            elif ch.lower() == 'e':
                return CharType.EXP
            elif ch == '.':
                return CharType.POINT
            elif ch == '+' or ch == '-':
                return CharType.SIGN
            elif ch == ' ':
                return CharType.SPACE
            else:
                return CharType.ILLEGAL

        transfer = {
            State.INITIAL: {
                CharType.SPACE: State.INITIAL,
                CharType.SIGN: State.INT_SIGN,
                CharType.NUMBER: State.INTEGER,
                CharType.POINT: State.POINT_WITHOUT_INT
            },
            State.INT_SIGN: {
                CharType.NUMBER: State.INTEGER,
                CharType.POINT: State.POINT_WITHOUT_INT
            },
            State.INTEGER: {
                CharType.NUMBER: State.INTEGER,
                CharType.EXP: State.EXP,
                CharType.POINT: State.POINT,
                CharType.SPACE: State.END
            },
            State.POINT: {
                CharType.NUMBER: State.FRACTION,
                CharType.EXP: State.EXP,
                CharType.SPACE: State.END
            },
            State.POINT_WITHOUT_INT: {
                CharType.NUMBER: State.FRACTION
            },
            State.FRACTION: {
                CharType.NUMBER: State.FRACTION,
                CharType.EXP: State.EXP,
                CharType.SPACE: State.END
            },
            State.EXP: {
                CharType.SIGN: State.EXP_SIGN,
                CharType.NUMBER: State.EXP_NUMBER
            },
            State.EXP_SIGN: {
                CharType.NUMBER: State.EXP_NUMBER
            },
            State.EXP_NUMBER: {
                CharType.NUMBER: State.EXP_NUMBER,
                CharType.SPACE: State.END
            },
            State.END: {
                CharType.SPACE: State.END
            }
        }

        st = State.INITIAL
        for ch in s:
            ct = toCharType(ch)
            if ct not in transfer[st]:
                return False
            st = transfer[st][ct]

        ACCEPT = (State.INTEGER, State.POINT, State.FRACTION, State.EXP_NUMBER,
                  State.END)
        return st in ACCEPT
