#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   726.原子的数量.py
@Time    :   2021/07/05 22:03:41
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=726 lang=python3
#
# [726] 原子的数量
#
# https://leetcode-cn.com/problems/number-of-atoms/description/
#
# algorithms
# Hard (54.87%)
# Likes:    190
# Dislikes: 0
# Total Accepted:    16.4K
# Total Submissions: 30K
# Testcase Example:  '"H2O"'
#
# 给定一个化学式formula（作为字符串），返回每种原子的数量。
#
# 原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。
#
# 如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2
# 这个表达是不可行的。
#
# 两个化学式连在一起是新的化学式。例如 H2O2He3Mg4 也是化学式。
#
# 一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。
#
# 给定一个化学式 formula ，返回所有原子的数量。格式为：第一个（按字典序）原子的名字，跟着它的数量（如果数量大于
# 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。
#
#
#
# 示例 1：
#
#
# 输入：formula = "H2O"
# 输出："H2O"
# 解释：
# 原子的数量是 {'H': 2, 'O': 1}。
#
#
# 示例 2：
#
#
# 输入：formula = "Mg(OH)2"
# 输出："H2MgO2"
# 解释：
# 原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。
#
#
# 示例 3：
#
#
# 输入：formula = "K4(ON(SO3)2)2"
# 输出："K4N2O14S4"
# 解释：
# 原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。
#
#
# 示例 4：
#
#
# 输入：formula = "Be32"
# 输出："Be32"
#
#
#
#
# 提示：
#
#
# 1 <= formula.length <= 1000
# formula 由小写英文字母、数字 '(' 和 ')' 组成。
# formula 是有效的化学式。
#
#
#
from collections import defaultdict
"""
方法一：栈 + 哈希表
对于括号序列相关的题目，通用的解法是使用递归或栈。本题中我们将使用栈解决。

从左到右遍历该化学式，并使用哈希表记录当前层遍历到的原子及其数量，因此
初始时需将一个空的哈希表压入栈中。对于当前遍历的字符：

如果是左括号，将一个空的哈希表压入栈中，进入下一层。

如果不是括号，则读取一个原子名称，若后面还有数字，则读取一个数字，否则
将该原子后面的数字视作 1。然后将原子及数字加入栈顶的哈希表中。

如果是右括号，则说明遍历完了当前层，若括号右侧还有数字，则读取该数字 num，
否则将该数字视作 1。然后将栈顶的哈希表弹出，将弹出的哈希表中的原子数量与
num 相乘，加到上一层的原子数量中。

遍历结束后，栈顶的哈希表即为化学式中的原子及其个数。遍历哈希表，取出所有
「原子-个数」对加入数组中，对数组按照原子字典序排序，然后遍历数组，按题目
要求拼接成答案。
"""


# @lc code=start
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        i, n = 0, len(formula)

        def parseAtom() -> str:
            nonlocal i
            atom = [formula[i]]  # 扫描首字母
            i += 1
            while i < n and 'a' <= formula[i] <= 'z':
                # 扫描首字母后的小写字母
                atom.append(formula[i])
                i += 1
            return ''.join(atom)

        def parseNum() -> int:
            nonlocal i
            if i == n or not formula[i].isdigit():
                return 1  # 不是数字，视作 1
            num = 0
            while i < n and '0' <= formula[i] <= '9':
                # 扫描数字
                num = num * 10 + ord(formula[i]) - ord('0')
                i += 1
            return num

        stk = [defaultdict(int)]
        while i < n:
            ch = formula[i]
            if ch == '(':
                i += 1
                stk.append(defaultdict(int))
            elif ch == ')':
                i += 1
                num = parseNum()  # 括号右侧数字
                counter = stk.pop()  # 弹出括号内的原子数量
                for atom, cnt in counter.items():
                    # 将括号内的原子数量乘上 num，加到上一层的原子数量中
                    stk[-1][atom] += cnt * num
            else:
                atom = parseAtom()
                num = parseNum()
                stk[-1][atom] += num

        atomNum = [(atom, num) for atom, num in stk[-1].items()]
        atomNum.sort()

        ans = []
        for atom, num in atomNum:
            ans.append(atom)
            if num > 1:
                ans.append(str(num))
        return ''.join(ans)


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.countOfAtoms(formula="H2O"))
    print(solu.countOfAtoms(formula="Mg(OH)2"))
    print(solu.countOfAtoms(formula="K4(ON(SO3)2)2"))
    print(solu.countOfAtoms(formula="Be32"))
