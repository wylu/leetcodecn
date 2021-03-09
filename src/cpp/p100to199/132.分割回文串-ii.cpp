/*
 * @lc app=leetcode.cn id=132 lang=cpp
 *
 * [132] 分割回文串 II
 *
 * https://leetcode-cn.com/problems/palindrome-partitioning-ii/description/
 *
 * algorithms
 * Hard (48.84%)
 * Likes:    380
 * Dislikes: 0
 * Total Accepted:    38.9K
 * Total Submissions: 79.6K
 * Testcase Example:  '"aab"'
 *
 * 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
 * 
 * 返回符合要求的 最少分割次数 。
 * 
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：s = "aab"
 * 输出：1
 * 解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：s = "a"
 * 输出：0
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：s = "ab"
 * 输出：1
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= s.length <= 2000
 * s 仅由小写英文字母组成
 * 
 * 
 * 
 * 
 */

/**
 * @File    :   132.分割回文串-ii.cpp
 * @Time    :   2021/03/09 08:57:52
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：动态规划
 * 思路与算法
 * 
 * 设 f[i] 表示字符串的前缀 s[0..i] 的最少分割次数。要想得出 f[i] 的值，我们
 * 可以考虑枚举 s[0..i] 分割出的最后一个回文串，这样我们就可以写出状态转移方程：
 * 
 *     f[i] = min{f[j]} + 1  (0 <= j < i, 其中 s[j+1..i] 是一个回文串)
 * 
 * 即我们枚举最后一个回文串的起始位置 j+1，保证 s[j+1..i] 是一个回文串，那么
 * f[i] 就可以从 f[j] 转移而来，附加 1 次额外的分割次数。
 * 
 * 注意到上面的状态转移方程中，我们还少考虑了一种情况，即 s[0..i] 本身就是一个
 * 回文串。此时其不需要进行任何分割，即：f[i] = 0
 * 
 * 那么我们如何知道 s[j+1..i] 或者 s[0..i] 是否为回文串呢？我们可以使用与
 * 「131. 分割回文串的官方题解」中相同的预处理方法，将字符串 s 的每个子串是否
 * 为回文串预先计算出来，即：
 * 
 * 设 g(i, j) 表示 s[i..j] 是否为回文串，那么有状态转移方程：
 * 
 *     g(i, j) = True,                          i >= j
 *     g(i, j) = g(i+1, j−1) && (s[i] = s[j]),   otherwise
 * 
 * 其中 && 表示逻辑与运算，即 s[i..j] 为回文串，当且仅当其为空串（i>j），
 * 其长度为 1（i=j），或者首尾字符相同且 s[i+1..j-1] 为回文串。
 * 
 * 这样一来，我们只需要 O(1) 的时间就可以判断任意 s[i..j] 是否为回文串了。
 * 通过动态规划计算出所有的 f 值之后，最终的答案即为 f[n-1]，其中 n 是字符串
 * s 的长度。
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int minCut(string s) {
        int n = s.length();
        vector<vector<bool>> g(n, vector<bool>(n, true));
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                g[i][j] = g[i + 1][j - 1] && (s[i] == s[j]);
            }
        }

        vector<int> f(n, n);
        for (int i = 0; i < n; i++) {
            if (g[0][i]) {
                f[i] = 0;
            } else {
                for (int j = 0; j < i; j++) {
                    if (g[j + 1][i]) {
                        f[i] = min(f[i], f[j] + 1);
                    }
                }
            }
        }

        return f[n - 1];
    }
};
// @lc code=end
