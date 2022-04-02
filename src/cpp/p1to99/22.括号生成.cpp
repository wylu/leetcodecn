/*
 * @lc app=leetcode.cn id=22 lang=cpp
 *
 * [22] 括号生成
 *
 * https://leetcode-cn.com/problems/generate-parentheses/description/
 *
 * algorithms
 * Medium (77.38%)
 * Likes:    2515
 * Dislikes: 0
 * Total Accepted:    468.9K
 * Total Submissions: 606K
 * Testcase Example:  '3'
 *
 * 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：n = 3
 * 输出：["((()))","(()())","(())()","()(())","()()()"]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：n = 1
 * 输出：["()"]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= n <= 8
 * 
 * 
 */

/**
 * @File    :   22.括号生成.cpp
 * @Time    :   2022/04/02 21:19:10
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
    vector<string> ans;
    string stk;
    int n;

public:
    vector<string> generateParenthesis(int n) {
        this->n = n;
        dfs(0, 0);
        return ans;
    }

    void dfs(int cur, int lc) {
        if (cur == 2 * n) {
            ans.push_back(stk);
            return;
        }

        if (lc < n) {
            stk.push_back('(');
            dfs(cur + 1, lc + 1);
            stk.pop_back();
        }

        if (lc > cur - lc) {
            stk.push_back(')');
            dfs(cur + 1, lc);
            stk.pop_back();
        }
    }
};
// @lc code=end
