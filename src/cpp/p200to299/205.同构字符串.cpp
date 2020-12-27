/*
 * @lc app=leetcode.cn id=205 lang=cpp
 *
 * [205] 同构字符串
 *
 * https://leetcode-cn.com/problems/isomorphic-strings/description/
 *
 * algorithms
 * Easy (48.41%)
 * Likes:    293
 * Dislikes: 0
 * Total Accepted:    68.9K
 * Total Submissions: 141.6K
 * Testcase Example:  '"egg"\n"add"'
 *
 * 给定两个字符串 s 和 t，判断它们是否是同构的。
 * 
 * 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
 * 
 * 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
 * 
 * 示例 1:
 * 
 * 输入: s = "egg", t = "add"
 * 输出: true
 * 
 * 
 * 示例 2:
 * 
 * 输入: s = "foo", t = "bar"
 * 输出: false
 * 
 * 示例 3:
 * 
 * 输入: s = "paper", t = "title"
 * 输出: true
 * 
 * 说明:
 * 你可以假设 s 和 t 具有相同的长度。
 * 
 */

/**
 * @File    :   205.同构字符串.cpp
 * @Time    :   2020/12/27 18:38:32
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
    bool isIsomorphic(string s, string t) {
        if (s.length() != t.length()) return false;

        unordered_map<char, char> s2t, t2s;
        int n = s.length();

        for (int i = 0; i < n; i++) {
            if ((s2t.count(s[i]) && s2t[s[i]] != t[i]) ||
                (t2s.count(t[i]) && t2s[t[i]] != s[i])) {
                return false;
            }
            s2t[s[i]] = t[i];
            t2s[t[i]] = s[i];
        }

        return true;
    }
};
// @lc code=end
