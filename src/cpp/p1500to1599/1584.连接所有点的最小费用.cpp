/*
 * @lc app=leetcode.cn id=1584 lang=cpp
 *
 * [1584] 连接所有点的最小费用
 *
 * https://leetcode-cn.com/problems/min-cost-to-connect-all-points/description/
 *
 * algorithms
 * Medium (66.55%)
 * Likes:    115
 * Dislikes: 0
 * Total Accepted:    18.7K
 * Total Submissions: 28.1K
 * Testcase Example:  '[[0,0],[2,2],[3,10],[5,2],[7,0]]'
 *
 * 给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。
 * 
 * 连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示
 * val 的绝对值。
 * 
 * 请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 
 * 
 * 输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
 * 输出：20
 * 解释：
 * 
 * 我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
 * 注意到任意两个点之间只有唯一一条路径互相到达。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：points = [[3,12],[-2,5],[-4,1]]
 * 输出：18
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：points = [[0,0],[1,1],[1,0],[-1,1]]
 * 输出：4
 * 
 * 
 * 示例 4：
 * 
 * 
 * 输入：points = [[-1000000,-1000000],[1000000,1000000]]
 * 输出：4000000
 * 
 * 
 * 示例 5：
 * 
 * 
 * 输入：points = [[0,0]]
 * 输出：0
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= points.length <= 1000
 * -10^6 <= xi, yi <= 10^6
 * 所有点 (xi, yi) 两两不同。
 * 
 * 
 */

/**
 * @File    :   1584.连接所有点的最小费用.cpp
 * @Time    :   2021/01/20 18:41:04
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :   最小生成树
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size();
        vector<vector<int>> cost(n, vector<int>(n));
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                cost[i][j] = abs(points[i][0] - points[j][0]) +
                             abs(points[i][1] - points[j][1]);
                cost[j][i] = cost[i][j];
            }
        }

        int ans = 0;
        vector<bool> used(n);
        vector<int> mincost(n, INT32_MAX);
        mincost[0] = 0;

        while (true) {
            int v = -1;
            for (int u = 0; u < n; u++) {
                if (!used[u] and (v == -1 || mincost[u] < mincost[v])) v = u;
            }

            if (v == -1) break;

            ans += mincost[v];
            used[v] = true;
            for (int u = 0; u < n; u++) {
                mincost[u] = min(mincost[u], cost[u][v]);
            }
        }

        return ans;
    }
};
// @lc code=end
