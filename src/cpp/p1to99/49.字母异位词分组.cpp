/*
 * @lc app=leetcode.cn id=49 lang=cpp
 *
 * [49] 字母异位词分组
 *
 * https://leetcode-cn.com/problems/group-anagrams/description/
 *
 * algorithms
 * Medium (63.81%)
 * Likes:    487
 * Dislikes: 0
 * Total Accepted:    111.9K
 * Total Submissions: 175.3K
 * Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
 *
 * 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
 * 
 * 示例:
 * 
 * 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
 * 输出:
 * [
 * ⁠ ["ate","eat","tea"],
 * ⁠ ["nat","tan"],
 * ⁠ ["bat"]
 * ]
 * 
 * 说明：
 * 
 * 
 * 所有输入均为小写字母。
 * 不考虑答案输出的顺序。
 * 
 * 
 */

/**
 * @File    :   49.字母异位词分组.cpp
 * @Time    :   2020/10/12 13:53:59
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
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> words;
        for (auto s : strs) {
            string t = s.substr();
            sort(t.begin(), t.end());
            auto it = words.find(t);
            if (it == words.end()) words[t] = {};
            words[t].emplace_back(s);
        }
        vector<vector<string>> ans;
        for (auto it = words.begin(); it != words.end(); it++) {
            ans.emplace_back(it->second);
        }
        return ans;
    }
};
// @lc code=end
