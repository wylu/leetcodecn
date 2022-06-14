/*
 * @lc app=leetcode.cn id=498 lang=cpp
 *
 * [498] 对角线遍历
 *
 * https://leetcode.cn/problems/diagonal-traverse/description/
 *
 * algorithms
 * Medium (54.58%)
 * Likes:    363
 * Dislikes: 0
 * Total Accepted:    81.5K
 * Total Submissions: 149.6K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * 给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：mat = [[1,2,3],[4,5,6],[7,8,9]]
 * 输出：[1,2,4,7,5,3,6,8,9]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：mat = [[1,2],[3,4]]
 * 输出：[1,2,3,4]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * m == mat.length
 * n == mat[i].length
 * 1 <= m, n <= 10^4
 * 1 <= m * n <= 10^4
 * -10^5 <= mat[i][j] <= 10^5
 * 
 * 
 */

#include <bits/stdc++.h>
using namespace std;

/**
 * @File    :   498.对角线遍历.cpp
 * @Time    :   2022/06/14 23:45:32
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        int x = 1, y = -1;
        int dx = -1, dy = 1;

        vector<int> ans;
        int c = m * n;
        while (c--) {
            x += dx;
            y += dy;
            if (y >= n) {
                // 超出右边界
                x += 2;
                y -= 1;
                dx = 1, dy = -1;
            } else if (x < 0) {
                // 超出上边界
                x += 1;
                dx = 1, dy = -1;
            } else if (x >= m) {
                // 超出下边界
                x -= 1;
                y += 2;
                dx = -1, dy = 1;
            } else if (y < 0) {
                // 超出左边界
                y += 1;
                dx = -1, dy = 1;
            }
            ans.push_back(mat[x][y]);
        }

        return ans;
    }
};
// @lc code=end
