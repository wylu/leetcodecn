/*
 * @lc app=leetcode.cn id=65 lang=cpp
 *
 * [65] 有效数字
 *
 * https://leetcode-cn.com/problems/valid-number/description/
 *
 * algorithms
 * Hard (23.99%)
 * Likes:    209
 * Dislikes: 0
 * Total Accepted:    30.4K
 * Total Submissions: 126.6K
 * Testcase Example:  '"0"'
 *
 * 有效数字（按顺序）可以分成以下几个部分：
 * 
 * 
 * 一个 小数 或者 整数
 * （可选）一个 'e' 或 'E' ，后面跟着一个 整数
 * 
 * 
 * 小数（按顺序）可以分成以下几个部分：
 * 
 * 
 * （可选）一个符号字符（'+' 或 '-'）
 * 下述格式之一：
 * 
 * 至少一位数字，后面跟着一个点 '.'
 * 至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
 * 一个点 '.' ，后面跟着至少一位数字
 * 
 * 
 * 
 * 
 * 整数（按顺序）可以分成以下几个部分：
 * 
 * 
 * （可选）一个符号字符（'+' 或 '-'）
 * 至少一位数字
 * 
 * 
 * 部分有效数字列举如下：
 * 
 * 
 * ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7",
 * "+6e-1", "53.5e93", "-123.456e789"]
 * 
 * 
 * 部分无效数字列举如下：
 * 
 * 
 * ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
 * 
 * 
 * 给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：s = "0"
 * 输出：true
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：s = "e"
 * 输出：false
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：s = "."
 * 输出：false
 * 
 * 
 * 示例 4：
 * 
 * 
 * 输入：s = ".1"
 * 输出：true
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= s.length <= 20
 * s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，或者点 '.' 。
 * 
 * 
 */

/**
 * @File    :   65.有效数字.cpp
 * @Time    :   2021/06/17 10:12:14
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：确定有限状态自动机
 * 预备知识
 * 
 * 确定有限状态自动机（以下简称「自动机」）是一类计算模型。它包含一系列状态，
 * 这些状态中：
 * 
 * - 有一个特殊的状态，被称作「初始状态」。
 * - 还有一系列状态被称为「接受状态」，它们组成了一个特殊的集合。其中，一个
 *   状态可能既是「初始状态」，也是「接受状态」。
 * 
 * 起初，这个自动机处于「初始状态」。随后，它顺序地读取字符串中的每一个字符，
 * 并根据当前状态和读入的字符，按照某个事先约定好的「转移规则」，从当前状态
 * 转移到下一个状态；当状态转移完成后，它就读取下一个字符。当字符串全部读取
 * 完毕后，如果自动机处于某个「接受状态」，则判定该字符串「被接受」；否则，
 * 判定该字符串「被拒绝」。
 * 
 * 注意：如果输入的过程中某一步转移失败了，即不存在对应的「转移规则」，此时
 * 计算将提前中止。在这种情况下我们也判定该字符串「被拒绝」。
 * 
 * 一个自动机，总能够回答某种形式的「对于给定的输入字符串 S，判断其是否满足
 * 条件 P」的问题。在本题中，条件 P 即为「构成合法的表示数值的字符串」。
 * 
 * 自动机驱动的编程，可以被看做一种暴力枚举方法的延伸：它穷尽了在任何一种
 * 情况下，对应任何的输入，需要做的事情。
 * 
 * 自动机在计算机科学领域有着广泛的应用。在算法领域，它与大名鼎鼎的字符串查找
 * 算法「KMP 算法」有着密切的关联；在工程领域，它是实现「正则表达式」的基础。
 * 
 * 问题描述
 * 
 * 在 C++ 文档 中，描述了一个合法的数值字符串应当具有的格式。具体而言，
 * 它包含以下部分：
 * 
 * - 符号位，即 +、- 两种符号
 * - 整数部分，即由若干字符 0-9 组成的字符串
 * - 小数点
 * - 小数部分，其构成与整数部分相同
 * - 指数部分，其中包含开头的字符 e（大写小写均可）、可选的符号位，和整数部分
 * 
 * 在上面描述的五个部分中，每个部分都不是必需的，但也受一些额外规则的制约，如：
 * 
 * - 如果符号位存在，其后面必须跟着数字或小数点。
 * - 小数点的前后两侧，至少有一侧是数字。
 * 
 * 思路与算法
 * 
 * 根据上面的描述，现在可以定义自动机的「状态集合」了。那么怎么挖掘出所有可能
 * 的状态呢？一个常用的技巧是，用「当前处理到字符串的哪个部分」当作状态的表述。
 * 根据这一技巧，不难挖掘出所有状态：
 * 
 * 0. 初始状态
 * 1. 符号位
 * 2. 整数部分
 * 3. 左侧有整数的小数点
 * 4. 左侧无整数的小数点（根据前面的第二条额外规则，需要对左侧有无整数的两种
 *    小数点做区分）
 * 5. 小数部分
 * 6. 字符 e
 * 7. 指数部分的符号位
 * 8. 指数部分的整数部分
 * 
 * 下一步是找出「初始状态」和「接受状态」的集合。根据题意，「初始状态」应当为
 * 状态 0，而「接受状态」的集合则为状态 2、状态 3、状态 5 以及状态 8。换言之，
 * 字符串的末尾要么是空格，要么是数字，要么是小数点，但前提是小数点的前面有数字。
 * 
 * 最后，需要定义「转移规则」。结合数值字符串应当具备的格式，将自动机转移的
 * 过程以图解的方式表示出来：
 * 
 * https://assets.leetcode-cn.com/solution-static/65/1.png
 * 
 * 比较上图与「预备知识」一节中对自动机的描述，可以看出有一点不同：
 * 
 * 我们没有单独地考虑每种字符，而是划分为若干类。由于全部 10 个数字字符彼此之间
 * 都等价，因此只需定义一种统一的「数字」类型即可。对于正负号也是同理。
 * 
 * 在实际代码中，我们需要处理转移失败的情况。为了处理这种情况，我们可以创建一个
 * 特殊的拒绝状态。如果当前状态下没有对应读入字符的「转移规则」，我们就转移到
 * 这个特殊的拒绝状态。一旦自动机转移到这个特殊状态，我们就可以立即判定该字符串
 * 不「被接受」。
 * 
 * 方法二：
 * 
 * 表示数值的字符串遵循模式 A[.[B]][e|EC] 或者 .B[e|EC]，其中：
 * 
 * A 为数值的整数部分（可能以 '+' 或 '-' 开头的 0-9 的数位串）
 * B 紧跟着小数点为数值的小数部分（0-9 的数位串）
 * C 紧跟 'e' 或 'E' 为数值的指数部分（可能以 '+' 或 '-' 开头的 0-9 的数位串）
 * 
 * 在小数里可能没有整数部分，如小数 .123 等于 0.123，因此 A 部分不是必需的。
 * 如果一个数没有整数部分，那么它的小数部分不能为空。
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
    enum State {
        STATE_INITIAL,
        STATE_INT_SIGN,
        STATE_INTEGER,
        STATE_POINT,
        STATE_POINT_WITHOUT_INT,
        STATE_FRACTION,
        STATE_EXP,
        STATE_EXP_SIGN,
        STATE_EXP_NUMBER
    };

    enum CharType {
        CHAR_NUMBER,
        CHAR_EXP,
        CHAR_POINT,
        CHAR_SIGN,
        CHAR_ILLEGAL
    };

    CharType toCharType(char ch) {
        if (isdigit(ch)) {
            return CHAR_NUMBER;
        } else if (ch == 'e' || ch == 'E') {
            return CHAR_EXP;
        } else if (ch == '.') {
            return CHAR_POINT;
        } else if (ch == '-' || ch == '+') {
            return CHAR_SIGN;
        } else {
            return CHAR_ILLEGAL;
        }
    }

    unordered_map<State, unordered_map<CharType, State>> transfer{
        {STATE_INITIAL,
         {{CHAR_SIGN, STATE_INT_SIGN},
          {CHAR_NUMBER, STATE_INTEGER},
          {CHAR_POINT, STATE_POINT_WITHOUT_INT}}},
        {STATE_INT_SIGN,
         {{CHAR_NUMBER, STATE_INTEGER}, {CHAR_POINT, STATE_POINT_WITHOUT_INT}}},
        {STATE_INTEGER,
         {{CHAR_NUMBER, STATE_INTEGER},
          {CHAR_POINT, STATE_POINT},
          {CHAR_EXP, STATE_EXP}}},
        {STATE_POINT, {{CHAR_NUMBER, STATE_FRACTION}, {CHAR_EXP, STATE_EXP}}},
        {STATE_POINT_WITHOUT_INT, {{CHAR_NUMBER, STATE_FRACTION}}},
        {STATE_FRACTION,
         {{CHAR_NUMBER, STATE_FRACTION}, {CHAR_EXP, STATE_EXP}}},
        {STATE_EXP,
         {{CHAR_SIGN, STATE_EXP_SIGN}, {CHAR_NUMBER, STATE_EXP_NUMBER}}},
        {STATE_EXP_SIGN, {{CHAR_NUMBER, STATE_EXP_NUMBER}}},
        {STATE_EXP_NUMBER, {{CHAR_NUMBER, STATE_EXP_NUMBER}}}};

public:
    bool isNumber(string s) {
        State state = STATE_INITIAL;
        for (auto ch : s) {
            CharType ctype = toCharType(ch);
            if (!transfer[state].count(ctype)) return false;
            state = transfer[state][ctype];
        }
        return (state == STATE_INTEGER || state == STATE_POINT ||
                state == STATE_FRACTION || state == STATE_EXP_NUMBER);
    }
};
// @lc code=end

// class Solution {
//     int idx = 0;

// public:
//     bool isNumber(string s) {
//         idx = 0;
//         int n = s.length();
//         // A[.B][e|EC]
//         // .B[e|EC]
//         bool A = scanInteger(s);

//         if (idx < n && s[idx] == '.') {
//             idx++;
//             bool B = scanUnsignedInteger(s);
//             A = A || B;
//         }

//         if (idx < n && (s[idx] == 'e' || s[idx] == 'E')) {
//             idx++;
//             bool C = scanInteger(s);
//             A = A && C;
//         }

//         return A && idx == n;
//     }

//     bool scanInteger(string s) {
//         if (s[idx] == '-' || s[idx] == '+') idx++;
//         return scanUnsignedInteger(s);
//     }

//     bool scanUnsignedInteger(string s) {
//         int start = idx;
//         while (isdigit(s[idx])) idx++;
//         return start != idx;
//     }
// };

int main(int argc, char const *argv[]) {
    Solution solu;
    vector<string> valids = {"2",    "0089",  "-0.1",    "+3.14",
                             "4.",   "-.9",   "2e10",    "-90E3",
                             "3e+7", "+6e-1", "53.5e93", "-123.456e789"};
    vector<string> invalids = {"abc",    "1a",  "1e",  "e3",
                               "99e2.5", "--6", "-+3", "95a54e53"};
    for (auto &s : valids) {
        cout << s << " " << solu.isNumber(s) << endl;
    }

    for (auto &s : invalids) {
        cout << s << " " << solu.isNumber(s) << endl;
    }

    return 0;
}
