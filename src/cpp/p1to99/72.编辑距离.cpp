/*
 * @lc app=leetcode.cn id=72 lang=cpp
 *
 * [72] 编辑距离
 *
 * https://leetcode-cn.com/problems/edit-distance/description/
 *
 * algorithms
 * Hard (59.98%)
 * Likes:    1199
 * Dislikes: 0
 * Total Accepted:    89.1K
 * Total Submissions: 148.6K
 * Testcase Example:  '"horse"\n"ros"'
 *
 * 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
 * 
 * 你可以对一个单词进行如下三种操作：
 * 
 * 
 * 插入一个字符
 * 删除一个字符
 * 替换一个字符
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：word1 = "horse", word2 = "ros"
 * 输出：3
 * 解释：
 * horse -> rorse (将 'h' 替换为 'r')
 * rorse -> rose (删除 'r')
 * rose -> ros (删除 'e')
 * 
 * 
 * 示例 2：
 * 
 * 输入：word1 = "intention", word2 = "execution"
 * 输出：5
 * 解释：
 * intention -> inention (删除 't')
 * inention -> enention (将 'i' 替换为 'e')
 * enention -> exention (将 'n' 替换为 'x')
 * exention -> exection (将 'n' 替换为 'c')
 * exection -> execution (插入 'u')
 * 
 * 
 */

/**
 * @File    :   72.编辑距离.cpp
 * @Time    :   2020/10/21 15:21:54
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * https://leetcode.com/problems/edit-distance/discuss/25846/C%2B%2B-O(n)-space-DP
 * 
 * To apply DP, we define the state dp[i][j] to be the minimum number
 * of operations to convert word1[0..i) to word2[0..j).
 * 
 * For the base case, that is, to convert a string to an empty string,
 * the mininum number of operations (deletions) is just the length of
 * the string. So we have dp[i][0] = i and dp[0][j] = j.
 * 
 * For the general case to convert word1[0..i) to word2[0..j), we break
 * this problem down into sub-problems. Suppose we have already known
 * how to convert word1[0..i - 1) to word2[0..j - 1) (dp[i - 1][j - 1]),
 * if word1[i - 1] == word2[j - 1], then no more operation is needed
 * and dp[i][j] = dp[i - 1][j - 1].
 * 
 * If word1[i - 1] != word2[j - 1], we need to consider three cases.
 * 
 *   1. Replace word1[i - 1] by word2[j - 1]
 *      (dp[i][j] = dp[i - 1][j - 1] + 1);
 *   2. If word1[0..i - 1) = word2[0..j) then delete word1[i - 1]
 *      (dp[i][j] = dp[i - 1][j] + 1);
 *   3. If word1[0..i) + word2[j - 1] = word2[0..j) then insert
 *      word2[j - 1] to word1[0..i) (dp[i][j] = dp[i][j - 1] + 1).
 * 
 * So when word1[i - 1] != word2[j - 1], dp[i][j] will just be the
 * minimum of the above three cases.
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.length(), n = word2.length();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        for (int i = 0; i <= m; i++) dp[i][0] = i;
        for (int j = 0; j <= n; j++) dp[0][j] = j;

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = 1 + min(dp[i - 1][j - 1],
                                       min(dp[i - 1][j], dp[i][j - 1]));
                }
            }
        }

        return dp[m][n];
    }
};
// @lc code=end
