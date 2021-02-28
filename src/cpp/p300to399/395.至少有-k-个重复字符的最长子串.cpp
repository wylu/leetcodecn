/*
 * @lc app=leetcode.cn id=395 lang=cpp
 *
 * [395] 至少有 K 个重复字符的最长子串
 *
 * https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
 *
 * algorithms
 * Medium (50.59%)
 * Likes:    392
 * Dislikes: 0
 * Total Accepted:    33.9K
 * Total Submissions: 67.1K
 * Testcase Example:  '"aaabb"\n3'
 *
 * 给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：s = "aaabb", k = 3
 * 输出：3
 * 解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：s = "ababbc", k = 2
 * 输出：5
 * 解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= s.length <= 10^4
 * s 仅由小写英文字母组成
 * 1 <= k <= 10^5
 * 
 * 
 */

/**
 * @File    :   395.至少有-k-个重复字符的最长子串.cpp
 * @Time    :   2021/02/28 12:14:19
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
    int longestSubstring(string s, int k) {
        int cnts[26] = {0};
        for (auto ch : s) cnts[ch - 'a']++;

        char sep = '#';
        for (int i = 0; i < 26; i++) {
            if (cnts[i] > 0 && cnts[i] < k) {
                sep = i + 'a';
                break;
            }
        }

        if (sep == '#') return s.length();

        vector<string> res;
        split(s, sep, res);
        int ans = 0;
        for (auto& s : res) ans = max(ans, longestSubstring(s, k));
        return ans;
    }

    void split(const string& s, const char sep, vector<string>& res) {
        istringstream iss(s);  // 输入流
        string buf;            // 接收缓冲
        while (getline(iss, buf, sep)) res.push_back(buf);
    }
};
// @lc code=end
