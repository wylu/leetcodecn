/*
 * @lc app=leetcode.cn id=51 lang=cpp
 *
 * [51] N 皇后
 *
 * https://leetcode-cn.com/problems/n-queens/description/
 *
 * algorithms
 * Hard (73.88%)
 * Likes:    1254
 * Dislikes: 0
 * Total Accepted:    198.4K
 * Total Submissions: 268.6K
 * Testcase Example:  '4'
 *
 * n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
 * 
 * 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
 * 
 * 
 * 
 * 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：n = 4
 * 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
 * 解释：如上图所示，4 皇后问题存在两个不同的解法。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：n = 1
 * 输出：[["Q"]]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= n <= 9
 * 
 * 
 * 
 * 
 */

/**
 * @File    :   51.n-皇后.cpp
 * @Time    :   2022/04/01 21:05:48
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
    int n, m;
    vector<vector<string>> ans;
    vector<string> board;
    vector<bool> cols, hills, dales;

public:
    vector<vector<string>> solveNQueens(int n) {
        this->n = n;
        m = 2 * n - 1;
        board = vector<string>(n, string(n, '.'));
        cols = vector<bool>(n);
        hills = vector<bool>(m);
        dales = vector<bool>(m);
        dfs(0);
        return ans;
    }

    void dfs(int x) {
        if (x == n) {
            ans.emplace_back(vector<string>(board));
            return;
        }
        for (int y = 0; y < n; y++) {
            if (cols[y] || hills[x + y] || dales[(y - x + m) % m]) continue;
            board[x][y] = 'Q', cols[y] = true;
            hills[x + y] = true, dales[(y - x + m) % m] = true;
            dfs(x + 1);
            board[x][y] = '.', cols[y] = false;
            hills[x + y] = false, dales[(y - x + m) % m] = false;
        }
    }
};
// @lc code=end
