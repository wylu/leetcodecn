/*
 * @lc app=leetcode.cn id=1717 lang=cpp
 *
 * [1717] 删除子字符串的最大得分
 *
 * https://leetcode-cn.com/problems/maximum-score-from-removing-substrings/description/
 *
 * algorithms
 * Medium (44.62%)
 * Likes:    21
 * Dislikes: 0
 * Total Accepted:    2.7K
 * Total Submissions: 6.1K
 * Testcase Example:  '"cdbcbbaaabab"\n4\n5'
 *
 * 给你一个字符串 s 和两个整数 x 和 y 。你可以执行下面两种操作任意次。
 * 
 * 
 * 删除子字符串 "ab" 并得到 x 分。
 * 
 * 
 * 比方说，从 "cabxbae" 删除 ab ，得到 "cxbae" 。
 * 
 * 
 * 删除子字符串"ba" 并得到 y 分。
 * 
 * 比方说，从 "cabxbae" 删除 ba ，得到 "cabxe" 。
 * 
 * 
 * 
 * 
 * 请返回对 s 字符串执行上面操作若干次能得到的最大得分。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：s = "cdbcbbaaabab", x = 4, y = 5
 * 输出：19
 * 解释：
 * - 删除 "cdbcbbaaabab" 中加粗的 "ba" ，得到 s = "cdbcbbaaab" ，加 5 分。
 * - 删除 "cdbcbbaaab" 中加粗的 "ab" ，得到 s = "cdbcbbaa" ，加 4 分。
 * - 删除 "cdbcbbaa" 中加粗的 "ba" ，得到 s = "cdbcba" ，加 5 分。
 * - 删除 "cdbcba" 中加粗的 "ba" ，得到 s = "cdbc" ，加 5 分。
 * 总得分为 5 + 4 + 5 + 5 = 19 。
 * 
 * 示例 2：
 * 
 * 输入：s = "aabbaaxybbaabb", x = 5, y = 4
 * 输出：20
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= s.length <= 10^5
 * 1 <= x, y <= 10^4
 * s 只包含小写英文字母。
 * 
 * 
 */

/**
 * @File    :   1717.删除子字符串的最大得分.cpp
 * @Time    :   2022/03/26 11:15:46
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
    int ans = 0;

public:
    int maximumGain(string s, int x, int y) {
        if (x > y) {
            getab(s, x);
            getba(s, y);
        } else {
            getba(s, y);
            getab(s, x);
        }
        return ans;
    }

    void getab(string &s, int z) {
        string t;
        for (auto ch : s) {
            t.push_back(ch);
            while (t.size() >= 2 && t[t.size() - 2] == 'a' &&
                   t[t.size() - 1] == 'b') {
                ans += z;
                t.pop_back();
                t.pop_back();
            }
        }
        s = move(t);
    }

    void getba(string &s, int z) {
        string t;
        for (auto ch : s) {
            t.push_back(ch);
            while (t.size() >= 2 && t[t.size() - 2] == 'b' &&
                   t[t.size() - 1] == 'a') {
                ans += z;
                t.pop_back();
                t.pop_back();
            }
        }
        s = move(t);
    }
};
// @lc code=end
