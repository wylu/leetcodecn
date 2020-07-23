/*
 * @lc app=leetcode.cn id=64 lang=cpp
 *
 * [64] 最小路径和
 *
 * https://leetcode-cn.com/problems/minimum-path-sum/description/
 *
 * algorithms
 * Medium (66.66%)
 * Likes:    544
 * Dislikes: 0
 * Total Accepted:    107.9K
 * Total Submissions: 162K
 * Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
 *
 * 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
 * 
 * 说明：每次只能向下或者向右移动一步。
 * 
 * 示例:
 * 
 * 输入:
 * [
 * [1,3,1],
 * ⁠ [1,5,1],
 * ⁠ [4,2,1]
 * ]
 * 输出: 7
 * 解释: 因为路径 1→3→1→1→1 的总和最小。
 * 
 * 
 */

/**
 * @File    :   64.最小路径和.cpp
 * @Time    :   2020/07/23 18:00:08
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * Dynamic Programing
 * 
 * State:
 *     dp[i][j]: 表示从 grid[0][0] 到 grid[i][j] 的最小路径和
 * 
 * Initial State:
 *     dp[0][0] = grid[0][0]
 *     dp[i][0] = dp[i-1][0] + grid[i][0] (0 < i < m)
 *     dp[0][j] = dp[0][j-1] + grid[0][j] (0 < j < n)
 * 
 * State Transition:
 *     0 < i < m
 *     0 < j < n
 *     dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
 * 
 * 因为每一行的值都只与当前行和上一行的值有关，所以可以用滚动数组优化空间复杂度。
 */

#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        if (grid.empty() || grid[0].empty()) {
            return -1;
        }

        int m = grid.size(), n = grid[0].size();
        int dp[n];
        dp[0] = grid[0][0];
        for (int i = 1; i < n; i++) {
            dp[i] = dp[i - 1] + grid[0][i];
        }

        for (int i = 1; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (j == 0) {
                    dp[j] = dp[j] + grid[i][j];
                } else {
                    dp[j] = min(dp[j - 1], dp[j]) + grid[i][j];
                }
            }
        }

        return dp[n - 1];
    }
};
// @lc code=end
