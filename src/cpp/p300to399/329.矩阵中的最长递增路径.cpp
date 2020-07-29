/*
 * @lc app=leetcode.cn id=329 lang=cpp
 *
 * [329] 矩阵中的最长递增路径
 *
 * https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/description/
 *
 * algorithms
 * Hard (41.36%)
 * Likes:    287
 * Dislikes: 0
 * Total Accepted:    30.5K
 * Total Submissions: 66K
 * Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
 *
 * 给定一个整数矩阵，找出最长递增路径的长度。
 * 
 * 对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
 * 
 * 示例 1:
 * 
 * 输入: nums = 
 * [
 * ⁠ [9,9,4],
 * ⁠ [6,6,8],
 * ⁠ [2,1,1]
 * ] 
 * 输出: 4 
 * 解释: 最长递增路径为 [1, 2, 6, 9]。
 * 
 * 示例 2:
 * 
 * 输入: nums = 
 * [
 * ⁠ [3,4,5],
 * ⁠ [3,2,6],
 * ⁠ [2,2,1]
 * ] 
 * 输出: 4 
 * 解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
 * 
 * 
 */

/**
 * @File    :   329.矩阵中的最长递增路径.cpp
 * @Time    :   2020/07/29 10:22:53
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
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        if (matrix.size() == 0 || matrix[0].size() == 0) {
            return 0;
        }

        int m = matrix.size(), n = matrix[0].size();
        vector<vector<int>> memo(m, vector<int>(n));

        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                ans = max(ans, dfs(matrix, memo, i, j));
            }
        }

        return ans;
    }

    int dfs(vector<vector<int>>& mat, vector<vector<int>>& memo, int x, int y) {
        if (memo[x][y] != 0) {
            return memo[x][y];
        }

        memo[x][y] = 1;
        int d[] = {0, 1, 0, -1, 0};

        for (int i = 0; i < 4; i++) {
            int nx = x + d[i], ny = y + d[i + 1];
            if (nx < 0 || nx >= mat.size() || ny < 0 || ny >= mat[0].size() ||
                mat[nx][ny] <= mat[x][y]) {
                continue;
            }
            memo[x][y] = max(memo[x][y], 1 + dfs(mat, memo, nx, ny));
        }

        return memo[x][y];
    }
};
// @lc code=end
