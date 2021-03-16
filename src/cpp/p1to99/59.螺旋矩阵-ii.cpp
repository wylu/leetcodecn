/*
 * @lc app=leetcode.cn id=59 lang=cpp
 *
 * [59] 螺旋矩阵 II
 *
 * https://leetcode-cn.com/problems/spiral-matrix-ii/description/
 *
 * algorithms
 * Medium (79.71%)
 * Likes:    353
 * Dislikes: 0
 * Total Accepted:    79.1K
 * Total Submissions: 99K
 * Testcase Example:  '3'
 *
 * 给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：n = 3
 * 输出：[[1,2,3],[8,9,4],[7,6,5]]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：n = 1
 * 输出：[[1]]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= n <= 20
 * 
 * 
 */

/**
 * @File    :   59.螺旋矩阵-ii.cpp
 * @Time    :   2021/03/16 14:14:12
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
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> ans(n, vector<int>(n));
        for (int i = 0, cur = 1, cnt = (n - 1) / 2; i <= cnt; i++) {
            int e = n - i;
            for (int j = i; j < e; j++) {
                ans[i][j] = cur++;
            }

            for (int j = i + 1; j < e; j++) {
                ans[j][e - 1] = cur++;
            }

            for (int j = e - 2; j >= i; j--) {
                ans[e - 1][j] = cur++;
            }

            for (int j = e - 2; j > i; j--) {
                ans[j][i] = cur++;
            }
        }
        return ans;
    }
};
// @lc code=end
