/*
 * @lc app=leetcode.cn id=763 lang=cpp
 *
 * [763] 划分字母区间
 *
 * https://leetcode-cn.com/problems/partition-labels/description/
 *
 * algorithms
 * Medium (75.78%)
 * Likes:    323
 * Dislikes: 0
 * Total Accepted:    36.2K
 * Total Submissions: 47.8K
 * Testcase Example:  '"ababcbacadefegdehijhklij"'
 *
 * 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：S = "ababcbacadefegdehijhklij"
 * 输出：[9,7,8]
 * 解释：
 * 划分结果为 "ababcbaca", "defegde", "hijhklij"。
 * 每个字母最多出现在一个片段中。
 * 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * S的长度在[1, 500]之间。
 * S只包含小写字母 'a' 到 'z' 。
 * 
 * 
 */

/**
 * @File    :   763.划分字母区间.cpp
 * @Time    :   2020/10/22 17:02:04
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
    vector<int> partitionLabels(string s) {
        int last[26] = {0};
        for (int i = 0; i < s.length(); i++) last[s[i] - 'a'] = i;

        vector<int> ans;
        int start = 0, end = 0;
        for (int i = 0; i < s.length(); i++) {
            end = max(end, last[s[i] - 'a']);
            if (i == end) {
                ans.emplace_back(end - start + 1);
                start = end + 1;
            }
        }

        return ans;
    }
};
// @lc code=end
