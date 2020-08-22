/*
 * @lc app=leetcode.cn id=336 lang=cpp
 *
 * [336] 回文对
 *
 * https://leetcode-cn.com/problems/palindrome-pairs/description/
 *
 * algorithms
 * Hard (39.63%)
 * Likes:    174
 * Dislikes: 0
 * Total Accepted:    18K
 * Total Submissions: 45.3K
 * Testcase Example:  '["abcd","dcba","lls","s","sssll"]'
 *
 * 给定一组 互不相同 的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j]
 * ，可拼接成回文串。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：["abcd","dcba","lls","s","sssll"]
 * 输出：[[0,1],[1,0],[3,2],[2,4]] 
 * 解释：可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
 * 
 * 
 * 示例 2：
 * 
 * 输入：["bat","tab","cat"]
 * 输出：[[0,1],[1,0]] 
 * 解释：可拼接成的回文串为 ["battab","tabbat"]
 * 
 */

/**
 * @File    :   336.回文对.cpp
 * @Time    :   2020/08/21 23:55:27
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
    unordered_map<string, int> indices;

public:
    vector<vector<int>> palindromePairs(vector<string>& words) {
        int n = words.size();
        for (int i = 0; i < n; i++) {
            string word = words[i].substr();
            reverse(word.begin(), word.end());
            indices.emplace(word, i);
        }

        vector<vector<int>> ans;
        for (int i = 0; i < n; i++) {
            int m = words[i].length();
            for (int j = 0; j < m + 1; j++) {
                // 判断后缀是否为回文
                if (isPalindrome(words[i], j, m - 1)) {
                    int right_id = findWord(words[i], 0, j - 1);
                    if (right_id != -1 && right_id != i) {
                        ans.push_back({i, right_id});
                    }
                }

                // 判断前缀是否为回文
                if (j && isPalindrome(words[i], 0, j - 1)) {
                    int left_id = findWord(words[i], j, m - 1);
                    if (left_id != -1 && left_id != i) {
                        ans.push_back({left_id, i});
                    }
                }
            }
        }

        return ans;
    }

    int findWord(const string& s, int left, int right) {
        auto iter = indices.find(s.substr(left, right - left + 1));
        return iter == indices.end() ? -1 : iter->second;
    }

    bool isPalindrome(const string& s, int left, int right) {
        for (int i = left, j = right; i < j; i++, j--) {
            if (s[i] != s[j]) {
                return false;
            }
        }
        return true;
    }
};
// @lc code=end

int main(int argc, char const* argv[]) {
    Solution solu;
    vector<string> words = {"bat", "tab", "cat"};
    vector<vector<int>> ans = solu.palindromePairs(words);
    return 0;
}
