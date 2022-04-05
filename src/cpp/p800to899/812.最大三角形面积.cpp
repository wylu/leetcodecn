/*
 * @lc app=leetcode.cn id=812 lang=cpp
 *
 * [812] 最大三角形面积
 *
 * https://leetcode-cn.com/problems/largest-triangle-area/description/
 *
 * algorithms
 * Easy (63.19%)
 * Likes:    100
 * Dislikes: 0
 * Total Accepted:    12.7K
 * Total Submissions: 20.2K
 * Testcase Example:  '[[0,0],[0,1],[1,0],[0,2],[2,0]]'
 *
 * 给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。
 * 
 * 
 * 示例:
 * 输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
 * 输出: 2
 * 解释: 
 * 这五个点如下图所示。组成的橙色三角形是最大的，面积为2。
 * 
 * 
 * 
 * 
 * 注意: 
 * 
 * 
 * 3 <= points.length <= 50.
 * 不存在重复的点。
 * -50 <= points[i][j] <= 50.
 * 结果误差值在 10^-6 以内都认为是正确答案。
 * 
 * 
 */

/**
 * @File    :   812.最大三角形面积.cpp
 * @Time    :   2022/04/05 11:38:06
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
    double largestTriangleArea(vector<vector<int>>& points) {
        auto area = [&](int i, int j, int k) -> double {
            vector<int>&pi = points[i], &pj = points[j], &pk = points[k];
            return 0.5 * abs(pi[0] * pj[1] + pj[0] * pk[1] + pk[0] * pi[1] -
                             pi[1] * pj[0] - pj[1] * pk[0] - pk[1] * pi[0]);
        };
        int n = points.size();
        double ans = 0;
        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    ans = max(ans, area(i, j, k));
                }
            }
        }
        return ans;
    }
};
// @lc code=end
