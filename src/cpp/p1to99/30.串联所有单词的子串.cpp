/*
 * @lc app=leetcode.cn id=30 lang=cpp
 *
 * [30] 串联所有单词的子串
 *
 * https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/description/
 *
 * algorithms
 * Hard (32.56%)
 * Likes:    377
 * Dislikes: 0
 * Total Accepted:    48.8K
 * Total Submissions: 149.9K
 * Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
 *
 * 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
 * 
 * 注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：
 * ⁠ s = "barfoothefoobarman",
 * ⁠ words = ["foo","bar"]
 * 输出：[0,9]
 * 解释：
 * 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
 * 输出的顺序不重要, [9,0] 也是有效答案。
 * 
 * 
 * 示例 2：
 * 
 * 输入：
 * ⁠ s = "wordgoodgoodgoodbestword",
 * ⁠ words = ["word","good","best","word"]
 * 输出：[]
 * 
 * 
 */

/**
 * @File    :   30.串联所有单词的子串.cpp
 * @Time    :   2020/11/13 10:49:39
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * We use an unordered_map<string, int> counts to record the expected
 * times of each word and another unordered_map<string, int> seen to
 * record the times we have seen. Then we check for every possible
 * position of i. Once we meet an unexpected word or the times of
 * some word is larger than its expected times, we stop the check.
 * If we finish the check successfully, push i to the result indexes.
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        if (s.empty() || words.empty()) return {};

        unordered_map<string, int> cnts;
        for (auto& word : words) cnts[word]++;

        int m = s.size(), n = words.size(), wl = words[0].size();
        auto check = [&](string ss) -> bool {
            unordered_map<string, int> seen;
            for (int i = 0; i < ss.size(); i += wl) {
                seen[ss.substr(i, wl)]++;
            }

            if (seen.size() != cnts.size()) return false;
            for (auto& it : seen) {
                if (cnts.find(it.first) == cnts.end() ||
                    it.second != cnts[it.first])
                    return false;
            }

            return true;
        };

        vector<int> ans;
        for (int i = 0; i < m - n * wl + 1; i++) {
            if (check(s.substr(i, n * wl))) {
                ans.emplace_back(i);
            }
        }
        return ans;
    }
};
// @lc code=end

void prtAns(vector<int>& ans) {
    for (auto num : ans) {
        cout << num << " ";
    }
    cout << endl;
}

int main(int argc, char const* argv[]) {
    Solution solu;
    string s = "barfoothefoobarman";
    vector<string> words = {"foo", "bar"};
    vector<int> ans = solu.findSubstring(s, words);
    prtAns(ans);
    return 0;
}
