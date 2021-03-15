/*
 * @lc app=leetcode.cn id=54 lang=cpp
 *
 * [54] 螺旋矩阵
 *
 * https://leetcode-cn.com/problems/spiral-matrix/description/
 *
 * algorithms
 * Medium (45.65%)
 * Likes:    708
 * Dislikes: 0
 * Total Accepted:    130.9K
 * Total Submissions: 286.8K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
 * 输出：[1,2,3,6,9,8,7,4,5]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
 * 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * m == matrix.length
 * n == matrix[i].length
 * 1 <= m, n <= 10
 * -100 <= matrix[i][j] <= 100
 * 
 * 
 */

/**
 * @File    :   54.螺旋矩阵.cpp
 * @Time    :   2021/03/15 22:00:02
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
    vector<int> spiralOrder(vector<vector<int>> &matrix) {
        vector<int> ans;
        int c = 0, m = matrix.size(), n = matrix[0].size();
        while (c <= (m - 1) / 2 && c <= (n - 1) / 2) {
            prtClockwise(matrix, ans, c++);
        }
        return ans;
    }

    void prtClockwise(vector<vector<int>> &matrix, vector<int> &ans, int cur) {
        int m = matrix.size(), n = matrix[0].size();
        int eX = m - cur, eY = n - cur;
        for (int i = cur; i < eY; i++) {
            ans.push_back(matrix[cur][i]);
        }

        if (eX - cur > 1) {
            for (int i = cur + 1; i < eX; i++) {
                ans.push_back(matrix[i][eY - 1]);
            }

            if (eY - cur > 1) {
                for (int i = eY - 2; i >= cur; i--) {
                    ans.push_back(matrix[eX - 1][i]);
                }

                if (eX - cur > 2) {
                    for (int i = eX - 2; i > cur; i--) {
                        ans.push_back(matrix[i][cur]);
                    }
                }
            }
        }
    }
};
// @lc code=end
