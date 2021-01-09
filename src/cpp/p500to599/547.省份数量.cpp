/*
 * @lc app=leetcode.cn id=547 lang=cpp
 *
 * [547] 省份数量
 *
 * https://leetcode-cn.com/problems/number-of-provinces/description/
 *
 * algorithms
 * Medium (61.10%)
 * Likes:    468
 * Dislikes: 0
 * Total Accepted:    108.3K
 * Total Submissions: 177.3K
 * Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
 *
 * 
 * 
 * 有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c
 * 间接相连。
 * 
 * 省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
 * 
 * 给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而
 * isConnected[i][j] = 0 表示二者不直接相连。
 * 
 * 返回矩阵中 省份 的数量。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
 * 输出：2
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
 * 输出：3
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= n <= 200
 * n == isConnected.length
 * n == isConnected[i].length
 * isConnected[i][j] 为 1 或 0
 * isConnected[i][i] == 1
 * isConnected[i][j] == isConnected[j][i]
 * 
 * 
 * 
 * 
 */

/**
 * @File    :   547.省份数量.cpp
 * @Time    :   2021/01/09 10:23:21
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
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        vector<bool> visited(n);

        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(isConnected, visited, n, i);
                ans++;
            }
        }

        return ans;
    }

    void dfs(vector<vector<int>>& isConnected, vector<bool>& visited, int n,
             int i) {
        visited[i] = true;
        for (int j = 0; j < n; j++) {
            if (isConnected[i][j] && !visited[j]) {
                dfs(isConnected, visited, n, j);
            }
        }
    }
};
// @lc code=end
