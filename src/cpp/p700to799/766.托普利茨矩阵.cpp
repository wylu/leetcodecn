/*
 * @lc app=leetcode.cn id=766 lang=cpp
 *
 * [766] 托普利茨矩阵
 *
 * https://leetcode-cn.com/problems/toeplitz-matrix/description/
 *
 * algorithms
 * Easy (70.86%)
 * Likes:    210
 * Dislikes: 0
 * Total Accepted:    47.8K
 * Total Submissions: 67.5K
 * Testcase Example:  '[[1,2,3,4],[5,1,2,3],[9,5,1,2]]'
 *
 * 给你一个 m x n 的矩阵 matrix 。如果这个矩阵是托普利茨矩阵，返回 true ；否则，返回 false 。
 * 
 * 如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
 * 输出：true
 * 解释：
 * 在上述矩阵中, 其对角线为: 
 * "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"。 
 * 各条对角线上的所有元素均相同, 因此答案是 True 。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：matrix = [[1,2],[2,2]]
 * 输出：false
 * 解释：
 * 对角线 "[1, 2]" 上的元素不同。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * m == matrix.length
 * n == matrix[i].length
 * 1 <= m, n <= 20
 * 0 <= matrix[i][j] <= 99
 * 
 * 
 * 
 * 
 * 进阶：
 * 
 * 
 * 如果矩阵存储在磁盘上，并且内存有限，以至于一次最多只能将矩阵的一行加载到内存中，该怎么办？
 * 如果矩阵太大，以至于一次只能将不完整的一行加载到内存中，该怎么办？
 * 
 * 
 */

/**
 * @File    :   766.托普利茨矩阵.cpp
 * @Time    :   2021/02/23 08:56:09
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
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i > 0 && j > 0 && matrix[i][j] != matrix[i - 1][j - 1]) {
                    return false;
                }
            }
        }
        return true;
    }
};
// @lc code=end
