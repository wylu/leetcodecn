/*
 * @lc app=leetcode.cn id=52 lang=cpp
 *
 * [52] N皇后 II
 *
 * https://leetcode-cn.com/problems/n-queens-ii/description/
 *
 * algorithms
 * Hard (80.57%)
 * Likes:    158
 * Dislikes: 0
 * Total Accepted:    36.2K
 * Total Submissions: 45K
 * Testcase Example:  '4'
 *
 * n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
 * 
 * 
 * 
 * 上图为 8 皇后问题的一种解法。
 * 
 * 给定一个整数 n，返回 n 皇后不同的解决方案的数量。
 * 
 * 示例:
 * 
 * 输入: 4
 * 输出: 2
 * 解释: 4 皇后问题存在如下两个不同的解法。
 * [
 * [".Q..",  // 解法 1
 * "...Q",
 * "Q...",
 * "..Q."],
 * 
 * ["..Q.",  // 解法 2
 * "Q...",
 * "...Q",
 * ".Q.."]
 * ]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一或
 * N-1 步，可进可退。（引用自 百度百科 - 皇后 ）
 * 
 * 
 */

/**
 * @File    :   52.n皇后-ii.cpp
 * @Time    :   2020/10/17 09:23:20
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 两个有用的细节。
 * 
 * （1）一行只可能有一个皇后且一列也只可能有一个皇后。这意味着没有必要
 * 在棋盘上考虑所有的方格。只需要按列循环即可。
 * （2）对于所有的主对角线有 行号 - 列号 = 常数，对于所有的次对角线有
 * 行号 + 列号 = 常数。
 * 
 * 这可以让我们标记已经在攻击范围下的对角线并且检查一个方格 (行号, 列号)
 * 是否处在攻击位置。
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
    vector<bool> cols;
    vector<bool> dales;  // 主对角线（左上->右下）
    vector<bool> hills;  // 副对角线（右上->左下）
    vector<vector<char>> board;
    int n;
    int ans = 0;

public:
    int totalNQueens(int n) {
        if (n <= 0) return 0;

        this->n = n;
        cols = vector<bool>(n, false);
        dales = vector<bool>(2 * n - 1, false);
        hills = vector<bool>(2 * n - 1, false);
        board = vector<vector<char>>(n, vector<char>(n, '.'));

        dfs(0);
        return ans;
    }

    void dfs(int x) {
        if (x == n) {
            ans++;
            return;
        }
        for (int y = 0; y < n; y++) {
            if (ok(x, y)) {
                int sub = (x - y + dales.size()) % dales.size(), add = x + y;
                cols[y] = true, dales[sub] = true, hills[add] = true;
                dfs(x + 1);
                cols[y] = false, dales[sub] = false, hills[add] = false;
            }
        }
    }

    bool ok(int x, int y) {
        int sub = (x - y + dales.size()) % dales.size(), add = x + y;
        return !(cols[y] || dales[sub] || hills[add]);
    }
};
// @lc code=end
