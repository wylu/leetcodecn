/*
 * @lc app=leetcode.cn id=1559 lang=cpp
 *
 * [1559] 二维网格图中探测环
 *
 * https://leetcode-cn.com/problems/detect-cycles-in-2d-grid/description/
 *
 * algorithms
 * Hard (32.37%)
 * Likes:    7
 * Dislikes: 0
 * Total Accepted:    1.8K
 * Total Submissions: 5.6K
 * Testcase Example:  '[["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]'
 *
 * 给你一个二维字符网格数组 grid ，大小为 m x n ，你需要检查 grid 中是否存在 相同值 形成的环。
 * 
 * 一个环是一条开始和结束于同一个格子的长度 大于等于 4
 * 的路径。对于一个给定的格子，你可以移动到它上、下、左、右四个方向相邻的格子之一，可以移动的前提是这两个格子有 相同的值 。
 * 
 * 同时，你也不能回到上一次移动时所在的格子。比方说，环  (1, 1) -> (1, 2) -> (1, 1) 是不合法的，因为从 (1, 2) 移动到
 * (1, 1) 回到了上一次移动时的格子。
 * 
 * 如果 grid 中有相同值形成的环，请你返回 true ，否则返回 false 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 
 * 输入：grid =
 * [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
 * 输出：true
 * 解释：如下图所示，有 2 个用不同颜色标出来的环：
 * 
 * 
 * 
 * 示例 2：
 * 
 * 
 * 
 * 输入：grid =
 * [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
 * 输出：true
 * 解释：如下图所示，只有高亮所示的一个合法环：
 * 
 * 
 * 
 * 示例 3：
 * 
 * 
 * 
 * 输入：grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
 * 输出：false
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * m == grid.length
 * n == grid[i].length
 * 1 <= m <= 500
 * 1 <= n <= 500
 * grid 只包含小写英文字母。
 * 
 * 
 */

/**
 * @File    :   1559.二维网格图中探测环.cpp
 * @Time    :   2020/09/04 22:47:59
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

public:
    bool containsCycle(vector<vector<char>>& grid) {
        n = grid.size(), m = grid[0].size();
        vector<vector<bool>> visit(n, vector<bool>(m));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visit[i][j] && dfs(grid, i, j, -1, -1, visit)) {
                    return true;
                }
            }
        }

        return false;
    }

    bool dfs(vector<vector<char>>& grid, int x, int y, int px, int py,
             vector<vector<bool>>& visit) {
        visit[x][y] = true;
        int d[5] = {0, 1, 0, -1, 0};
        for (int i = 0; i < 4; i++) {
            int nx = x + d[i], ny = y + d[i + 1];

            if (nx == px && ny == py) {
                continue;
            }

            if (0 <= nx && nx < n && 0 <= ny && ny < m &&
                grid[nx][ny] == grid[x][y]) {
                if (visit[nx][ny] || dfs(grid, nx, ny, x, y, visit)) {
                    return true;
                }
            }
        }
        return false;
    }
};
// @lc code=end
