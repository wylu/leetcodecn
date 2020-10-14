/*
 * @lc app=leetcode.cn id=1002 lang=cpp
 *
 * [1002] 查找常用字符
 *
 * https://leetcode-cn.com/problems/find-common-characters/description/
 *
 * algorithms
 * Easy (72.73%)
 * Likes:    137
 * Dislikes: 0
 * Total Accepted:    25.8K
 * Total Submissions: 35.5K
 * Testcase Example:  '["bella","label","roller"]'
 *
 * 给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3
 * 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
 * 
 * 你可以按任意顺序返回答案。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：["bella","label","roller"]
 * 输出：["e","l","l"]
 * 
 * 
 * 示例 2：
 * 
 * 输入：["cool","lock","cook"]
 * 输出：["c","o"]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= A.length <= 100
 * 1 <= A[i].length <= 100
 * A[i][j] 是小写字母
 * 
 * 
 */

/**
 * @File    :   1002.查找常用字符.cpp
 * @Time    :   2020/10/14 11:35:27
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
    vector<string> commonChars(vector<string>& A) {
        int n = A.size();
        vector<int> freq(26, INT32_MAX);
        for (int i = 0; i < n; i++) {
            int tmp[26] = {0};
            for (auto ch : A[i]) tmp[ch - 'a']++;
            for (int j = 0; j < 26; j++) freq[j] = min(freq[j], tmp[j]);
        }

        vector<string> ans;
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < freq[i]; j++) {
                ans.emplace_back(1, i + 'a');
            }
        }

        return ans;
    }
};
// @lc code=end
