/*
 * @lc app=leetcode.cn id=13 lang=cpp
 *
 * [13] 罗马数字转整数
 *
 * https://leetcode-cn.com/problems/roman-to-integer/description/
 *
 * algorithms
 * Easy (63.06%)
 * Likes:    1346
 * Dislikes: 0
 * Total Accepted:    387.4K
 * Total Submissions: 614.5K
 * Testcase Example:  '"III"'
 *
 * 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
 * 
 * 
 * 字符          数值
 * I             1
 * V             5
 * X             10
 * L             50
 * C             100
 * D             500
 * M             1000
 * 
 * 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V +
 * II 。
 * 
 * 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数
 * 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
 * 
 * 
 * I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
 * X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
 * C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
 * 
 * 
 * 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
 * 
 * 
 * 
 * 示例 1:
 * 
 * 
 * 输入: "III"
 * 输出: 3
 * 
 * 示例 2:
 * 
 * 
 * 输入: "IV"
 * 输出: 4
 * 
 * 示例 3:
 * 
 * 
 * 输入: "IX"
 * 输出: 9
 * 
 * 示例 4:
 * 
 * 
 * 输入: "LVIII"
 * 输出: 58
 * 解释: L = 50, V= 5, III = 3.
 * 
 * 
 * 示例 5:
 * 
 * 
 * 输入: "MCMXCIV"
 * 输出: 1994
 * 解释: M = 1000, CM = 900, XC = 90, IV = 4.
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= s.length <= 15
 * s 仅含字符 ('I', 'V', 'X', 'L', 'C', 'D', 'M')
 * 题目数据保证 s 是一个有效的罗马数字，且表示整数在范围 [1, 3999] 内
 * 题目所给测试用例皆符合罗马数字书写规则，不会出现跨位等情况。
 * IL 和 IM 这样的例子并不符合题目要求，49 应该写作 XLIX，999 应该写作 CMXCIX 。
 * 关于罗马数字的详尽书写规则，可以参考 罗马数字 - Mathematics 。
 * 
 * 
 */

/**
 * @File    :   13.罗马数字转整数.cpp
 * @Time    :   2021/05/15 21:35:07
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：模拟
 * 思路
 * 
 * 通常情况下，罗马数字中小的数字在大的数字的右边。若输入的字符串满足该情况，
 * 那么可以将每个字符视作一个单独的值，累加每个字符对应的数值即可。
 * 
 * 例如 XXVII 可视作 X+X+V+I+I = 10+10+5+1+1 = 27。
 * 
 * 若存在小的数字在大的数字的左边的情况，根据规则需要减去小的数字。对于这种
 * 情况，我们也可以将每个字符视作一个单独的值，若一个数字右侧的数字比它大，
 * 则将该数字的符号取反。
 * 
 * 例如 XIV 可视作 X-I+V = 10-1+5 = 14。
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> symbolValues = {
            {'I', 1},   {'V', 5},   {'X', 10},   {'L', 50},
            {'C', 100}, {'D', 500}, {'M', 1000},
        };
        int n = s.length();
        int ans = symbolValues[s[n - 1]];

        for (int i = 0; i < n - 1; i++) {
            if (symbolValues[s[i]] < symbolValues[s[i + 1]]) {
                ans -= symbolValues[s[i]];
            } else {
                ans += symbolValues[s[i]];
            }
        }

        return ans;
    }
};
// @lc code=end
