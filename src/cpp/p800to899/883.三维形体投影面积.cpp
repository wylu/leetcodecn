/*
 * @lc app=leetcode.cn id=883 lang=cpp
 *
 * [883] 三维形体投影面积
 *
 * https://leetcode-cn.com/problems/projection-area-of-3d-shapes/description/
 *
 * algorithms
 * Easy (75.93%)
 * Likes:    111
 * Dislikes: 0
 * Total Accepted:    32K
 * Total Submissions: 42.2K
 * Testcase Example:  '[[1,2],[3,4]]'
 *
 * 在 n x n 的网格 grid 中，我们放置了一些与 x，y，z 三轴对齐的 1 x 1 x 1 立方体。
 * 
 * 每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。
 * 
 * 现在，我们查看这些立方体在 xy 、yz 和 zx 平面上的投影。
 * 
 * 投影 就像影子，将 三维 形体映射到一个 二维 平面上。从顶部、前面和侧面看立方体时，我们会看到“影子”。
 * 
 * 返回 所有三个投影的总面积 。
 * 
 * 
 * 示例 1：
 * 
 * https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/02/shadow.png
 * 
 * 输入：[[1,2],[3,4]]
 * 输出：17
 * 解释：这里有该形体在三个轴对齐平面上的三个投影(“阴影部分”)。
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入：grid = [[2]]
 * 输出：5
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：[[1,0],[0,2]]
 * 输出：8
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * n == grid.length == grid[i].length
 * 1 <= n <= 50
 * 0 <= grid[i][j] <= 50
 * 
 * 
 */

#include <bits/stdc++.h>
using namespace std;

/**
 * @File    :   883.三维形体投影面积.cpp
 * @Time    :   2022/04/26 16:44:58
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
class Solution {
public:
    int projectionArea(vector<vector<int>>& grid) {
        int ans = 0, n = grid.size();
        for (int i = 0; i < n; i++) {
            int xz = 0, yz = 0;
            for (int j = 0; j < n; j++) {
                ans += grid[i][j] ? 1 : 0;
                xz = max(xz, grid[i][j]);
                yz = max(yz, grid[j][i]);
            }
            ans += xz + yz;
        }
        return ans;
    }
};
// @lc code=end

// class Solution {
// public:
//     int projectionArea(vector<vector<int>>& grid) {
//         int ans = 0, n = grid.size();
//         vector<int> xz(n), yz(n);
//         for (int x = 0; x < n; x++) {
//             for (int y = 0; y < n; y++) {
//                 if (grid[x][y]) {
//                     ans++;
//                     xz[x] = max(xz[x], grid[x][y]);
//                     yz[y] = max(yz[y], grid[x][y]);
//                 }
//             }
//         }
//         ans += accumulate(xz.begin(), xz.end(), 0);
//         ans += accumulate(yz.begin(), yz.end(), 0);
//         return ans;
//     }
// };
