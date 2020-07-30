/*
 * @lc app=leetcode.cn id=28 lang=cpp
 *
 * [28] 实现 strStr()
 *
 * https://leetcode-cn.com/problems/implement-strstr/description/
 *
 * algorithms
 * Easy (39.73%)
 * Likes:    515
 * Dislikes: 0
 * Total Accepted:    205.4K
 * Total Submissions: 517.2K
 * Testcase Example:  '"hello"\n"ll"'
 *
 * 实现 strStr() 函数。
 * 
 * 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置
 * (从0开始)。如果不存在，则返回  -1。
 * 
 * 示例 1:
 * 
 * 输入: haystack = "hello", needle = "ll"
 * 输出: 2
 * 
 * 
 * 示例 2:
 * 
 * 输入: haystack = "aaaaa", needle = "bba"
 * 输出: -1
 * 
 * 
 * 说明:
 * 
 * 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
 * 
 * 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
 * 
 */

/**
 * @File    :   28.实现-str-str.cpp
 * @Time    :   2020/07/30 17:20:47
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
public:
    int strStr(string s, string p) {
        if (p.empty()) {
            return 0;
        }
        if (s.empty()) {
            return -1;
        }

        vector<int> next(p.length(), -1);
        calNext(next, p);

        int ls = s.length(), lp = p.length();
        int i = 0, j = 0;
        while (i < ls && j < lp) {
            if (j == -1 || s[i] == p[j]) {
                i++;
                j++;
            } else {
                j = next[j];
            }
        }

        return (j == lp) ? i - j : -1;
    }

    void calNext(vector<int> &next, string p) {
        int k = -1, j = 0;
        while (j < p.length() - 1) {
            if (k == -1 || p[k] == p[j]) {
                k++;
                j++;
                next[j] = k;
            } else {
                k = next[k];
            }
        }
    }
};
// @lc code=end

int main(int argc, char const *argv[]) {
    Solution solu = Solution();
    cout << solu.strStr("hello", "ll") << endl;
    return 0;
}
