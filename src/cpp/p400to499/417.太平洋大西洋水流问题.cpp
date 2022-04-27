/*
 * @lc app=leetcode.cn id=417 lang=cpp
 *
 * [417] 太平洋大西洋水流问题
 *
 * https://leetcode-cn.com/problems/pacific-atlantic-water-flow/description/
 *
 * algorithms
 * Medium (53.34%)
 * Likes:    431
 * Dislikes: 0
 * Total Accepted:    50.3K
 * Total Submissions: 94.3K
 * Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
 *
 * 有一个 m × n 的矩形岛屿，与 太平洋 和 大西洋 相邻。 “太平洋” 处于大陆的左边界和上边界，而 “大西洋” 处于大陆的右边界和下边界。
 * 
 * 这个岛被分割成一个由若干方形单元格组成的网格。给定一个 m x n 的整数矩阵 heights ， heights[r][c] 表示坐标 (r, c)
 * 上单元格 高于海平面的高度 。
 * 
 * 岛上雨水较多，如果相邻单元格的高度 小于或等于 当前单元格的高度，雨水可以直接向北、南、东、西流向相邻单元格。水可以从海洋附近的任何单元格流入海洋。
 * 
 * 返回 网格坐标 result 的 2D列表 ，其中 result[i] = [ri, ci] 表示雨水可以从单元格 (ri, ci) 流向
 * 太平洋和大西洋 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 
 * 
 * 输入: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
 * 输出: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入: heights = [[2,1],[1,2]]
 * 输出: [[0,0],[0,1],[1,0],[1,1]]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * m == heights.length
 * n == heights[r].length
 * 1 <= m, n <= 200
 * 0 <= heights[r][c] <= 10^5
 * 
 * 
 */

#include <bits/stdc++.h>
using namespace std;

/**
 * @File    :   417.太平洋大西洋水流问题.cpp
 * @Time    :   2022/04/27 16:26:58
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 雨水的流动方向是从高到低，每个单元格上的雨水只能流到高度小于等于当前单元格
 * 的相邻单元格。从一个单元格开始，通过搜索的方法模拟雨水的流动，则可以判断
 * 雨水是否可以从该单元格流向海洋。
 * 
 * 如果直接以每个单元格作为起点模拟雨水的流动，则会重复遍历每个单元格，导致
 * 时间复杂度过高。为了降低时间复杂度，可以从矩阵的边界开始反向搜索寻找雨水
 * 流向边界的单元格，反向搜索时，每次只能移动到高度相同或更大的单元格。
 * 
 * 由于矩阵的左边界和上边界是太平洋，矩阵的右边界和下边界是大西洋，因此从矩阵
 * 的左边界和上边界开始反向搜索即可找到雨水流向太平洋的单元格，从矩阵的右边界
 * 和下边界开始反向搜索即可找到雨水流向大西洋的单元格。
 * 
 * 可以使用深度优先搜索实现反向搜索，搜索过程中需要记录每个单元格是否可以从
 * 太平洋反向到达以及是否可以从大西洋反向到达。反向搜索结束之后，遍历每个网格，
 * 如果一个网格既可以从太平洋反向到达也可以从大西洋反向到达，则该网格满足太平洋
 * 和大西洋都可以到达，将该网格添加到答案中。
 */

// @lc code=start
class Solution {
    int m, n;
    int d[5] = {0, 1, 0, -1, 0};
    vector<vector<int>> hts;

public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        m = heights.size(), n = heights[0].size(), hts = heights;
        vector<bool> pacific(m * n), atlantic(m * n);

        for (int i = 0; i < m; i++) dfs(i, 0, pacific);
        for (int j = 1; j < n; j++) dfs(0, j, pacific);
        for (int i = 0; i < m; i++) dfs(i, n - 1, atlantic);
        for (int j = 0; j < n - 1; j++) dfs(m - 1, j, atlantic);

        vector<vector<int>> ans;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i * n + j] && atlantic[i * n + j]) {
                    ans.push_back({i, j});
                }
            }
        }

        return ans;
    }

    void dfs(int x, int y, vector<bool>& ocean) {
        if (ocean[x * n + y]) return;

        ocean[x * n + y] = true;
        for (int i = 0; i < 4; i++) {
            int nx = x + d[i], ny = y + d[i + 1];
            if (nx >= 0 && nx < m && ny >= 0 && ny < n &&
                hts[nx][ny] >= hts[x][y]) {
                dfs(nx, ny, ocean);
            }
        }
    }
};
// @lc code=end
