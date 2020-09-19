/*
 * @lc app=leetcode.cn id=60 lang=cpp
 *
 * [60] 第k个排列
 *
 * https://leetcode-cn.com/problems/permutation-sequence/description/
 *
 * algorithms
 * Medium (50.56%)
 * Likes:    359
 * Dislikes: 0
 * Total Accepted:    55.7K
 * Total Submissions: 110.2K
 * Testcase Example:  '3\n3'
 *
 * 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
 * 
 * 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
 * 
 * 
 * "123"
 * "132"
 * "213"
 * "231"
 * "312"
 * "321"
 * 
 * 
 * 给定 n 和 k，返回第 k 个排列。
 * 
 * 说明：
 * 
 * 
 * 给定 n 的范围是 [1, 9]。
 * 给定 k 的范围是[1,  n!]。
 * 
 * 
 * 示例 1:
 * 
 * 输入: n = 3, k = 3
 * 输出: "213"
 * 
 * 
 * 示例 2:
 * 
 * 输入: n = 4, k = 9
 * 输出: "2314"
 * 
 * 
 */

/**
 * @File    :   60.第k个排列.cpp
 * @Time    :   2020/09/19 12:20:51
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
    string getPermutation(int n, int k) {
        vector<int> frac(n + 1, 1);
        for (int i = 1; i <= n; i++) {
            frac[i] = frac[i - 1] * i;
        }

        vector<char> ans;
        vector<int> used(n + 1, 1);
        k--;
        for (int i = 1; i <= n; i++) {
            int r = k / frac[n - i] + 1;
            for (int j = 1; j <= n; j++) {
                r -= used[j];
                if (r == 0) {
                    used[j] = 0;
                    ans.emplace_back(j + '0');
                    break;
                }
            }
            k %= frac[n - i];
        }

        string s;
        s.insert(s.begin(), ans.begin(), ans.end());
        return s;
    }
};
// @lc code=end
