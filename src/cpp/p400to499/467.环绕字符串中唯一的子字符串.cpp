/*
 * @lc app=leetcode.cn id=467 lang=cpp
 *
 * [467] 环绕字符串中唯一的子字符串
 *
 * https://leetcode.cn/problems/unique-substrings-in-wraparound-string/description/
 *
 * algorithms
 * Medium (49.98%)
 * Likes:    287
 * Dislikes: 0
 * Total Accepted:    24.1K
 * Total Submissions: 48.2K
 * Testcase Example:  '"a"'
 *
 * 把字符串 s 看作是 “abcdefghijklmnopqrstuvwxyz” 的无限环绕字符串，所以 s 看起来是这样的：
 * 
 * 
 * "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd...." . 
 * 
 * 
 * 现在给定另一个字符串 p 。返回 s 中 唯一 的 p 的 非空子串 的数量 。 
 * 
 * 
 * 
 * 示例 1:
 * 
 * 
 * 输入: p = "a"
 * 输出: 1
 * 解释: 字符串 s 中只有一个"a"子字符。
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入: p = "cac"
 * 输出: 2
 * 解释: 字符串 s 中的字符串“cac”只有两个子串“a”、“c”。.
 * 
 * 
 * 示例 3:
 * 
 * 
 * 输入: p = "zab"
 * 输出: 6
 * 解释: 在字符串 s 中有六个子串“z”、“a”、“b”、“za”、“ab”、“zab”。
 * 
 * 
 * 
 * 
 * 提示:
 * 
 * 
 * 1 <= p.length <= 10^5
 * p 由小写英文字母构成
 * 
 * 
 */

#include <bits/stdc++.h>
using namespace std;

/**
 * @File    :   467.环绕字符串中唯一的子字符串.cpp
 * @Time    :   2022/05/25 17:34:45
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
class Solution {
public:
    int findSubstringInWraproundString(string p) {
        vector<int> dp(26, 0);
        dp[p[0] - 'a'] = 1;
        int n = p.length(), k = 1;
        for (int i = 1; i < n; i++) {
            // 字符之差为 1 或 -25
            if ((p[i] - p[i - 1] + 26) % 26 != 1) k = 0;
            dp[p[i] - 'a'] = max(dp[p[i] - 'a'], ++k);
        }
        return accumulate(dp.begin(), dp.end(), 0);
    }
};
// @lc code=end
