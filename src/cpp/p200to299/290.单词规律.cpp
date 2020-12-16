/*
 * @lc app=leetcode.cn id=290 lang=cpp
 *
 * [290] 单词规律
 *
 * https://leetcode-cn.com/problems/word-pattern/description/
 *
 * algorithms
 * Easy (45.56%)
 * Likes:    276
 * Dislikes: 0
 * Total Accepted:    58.6K
 * Total Submissions: 128.5K
 * Testcase Example:  '"abba"\n"dog cat cat dog"'
 *
 * 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
 * 
 * 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
 * 
 * 示例1:
 * 
 * 输入: pattern = "abba", str = "dog cat cat dog"
 * 输出: true
 * 
 * 示例 2:
 * 
 * 输入:pattern = "abba", str = "dog cat cat fish"
 * 输出: false
 * 
 * 示例 3:
 * 
 * 输入: pattern = "aaaa", str = "dog cat cat dog"
 * 输出: false
 * 
 * 示例 4:
 * 
 * 输入: pattern = "abba", str = "dog dog dog dog"
 * 输出: false
 * 
 * 说明:
 * 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    
 * 
 */

/**
 * @File    :   290.单词规律.cpp
 * @Time    :   2020/12/16 21:44:37
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
    bool wordPattern(string pattern, string s) {
        unordered_map<string, char> w2c;
        unordered_set<char> seen;

        vector<string> words = split(s, ' ');
        if (words.size() != pattern.length()) return false;

        for (int i = 0; i < words.size(); i++) {
            if (w2c.count(words[i]) == 0) {
                if (seen.count(pattern[i]) > 0) return false;
                w2c[words[i]] = pattern[i];
                seen.insert(pattern[i]);
            } else if (w2c[words[i]] != pattern[i]) {
                return false;
            }
        }

        return true;
    }

    vector<string> split(string s, char sep) {
        vector<string> res;
        string word;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == sep) {
                if (!word.empty()) res.emplace_back(word);
                word = "";
            } else {
                word += s[i];
            }
        }
        if (!word.empty()) res.emplace_back(word);
        return res;
    }
};
// @lc code=end
