/*
 * @lc app=leetcode.cn id=1034 lang=cpp
 *
 * [1034] 边框着色
 *
 * https://leetcode-cn.com/problems/coloring-a-border/description/
 *
 * algorithms
 * Medium (42.39%)
 * Likes:    16
 * Dislikes: 0
 * Total Accepted:    2.3K
 * Total Submissions: 5.4K
 * Testcase Example:  '[[1,1],[1,2]]\n0\n0\n3'
 *
 * 给出一个二维整数网格 grid，网格中的每个值表示该位置处的网格块的颜色。
 * 
 * 只有当两个网格块的颜色相同，而且在四个方向中任意一个方向上相邻时，它们属于同一连通分量。
 * 
 * 连通分量的边界是指连通分量中的所有与不在分量中的正方形相邻（四个方向上）的所有正方形，或者在网格的边界上（第一行/列或最后一行/列）的所有正方形。
 * 
 * 给出位于 (r0, c0) 的网格块和颜色 color，使用指定颜色 color 为所给网格块的连通分量的边界进行着色，并返回最终的网格 grid
 * 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3
 * 输出：[[3, 3], [3, 2]]
 * 
 * 
 * 示例 2：
 * 
 * 输入：grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3
 * 输出：[[1, 3, 3], [2, 3, 3]]
 * 
 * 
 * 示例 3：
 * 
 * 输入：grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2
 * 输出：[[2, 2, 2], [2, 1, 2], [2, 2, 2]]
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= grid.length <= 50
 * 1 <= grid[0].length <= 50
 * 1 <= grid[i][j] <= 1000
 * 0 <= r0 < grid.length
 * 0 <= c0 < grid[0].length
 * 1 <= color <= 1000
 * 
 * 
 * 
 * 
 */

/**
 * @File    :   1034.边框着色.cpp
 * @Time    :   2020/08/23 21:41:54
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
    int d[5] = {0, 1, 0, -1, 0};
    int n, m;
    vector<vector<bool>> visit;

public:
    vector<vector<int>> colorBorder(vector<vector<int>>& grid, int r0, int c0,
                                    int color) {
        n = grid.size(), m = grid[0].size();
        visit = vector<vector<bool>>(n, vector<bool>(m, false));
        int old = grid[r0][c0];
        if (old == color) {
            return grid;
        }

        dfs(grid, r0, c0, old, color);
        return grid;
    }

    void dfs(vector<vector<int>>& grid, int x, int y, int old, int color) {
        visit[x][y] = true;
        if (x == 0 || x == n - 1 || y == 0 || y == m - 1) {
            grid[x][y] = color;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + d[i], ny = y + d[i + 1];
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visit[nx][ny]) {
                if (grid[nx][ny] == old) {
                    dfs(grid, nx, ny, old, color);
                } else {
                    grid[x][y] = color;
                }
            }
        }
    }
};
// @lc code=end

int main(int argc, char const* argv[]) {
    Solution solu;
    vector<vector<int>> grid = {{1, 1}, {1, 2}};
    solu.colorBorder(grid, 0, 0, 3);
    return 0;
}
