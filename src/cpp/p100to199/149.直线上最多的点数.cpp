/*
 * @lc app=leetcode.cn id=149 lang=cpp
 *
 * [149] 直线上最多的点数
 *
 * https://leetcode-cn.com/problems/max-points-on-a-line/description/
 *
 * algorithms
 * Hard (26.96%)
 * Likes:    260
 * Dislikes: 0
 * Total Accepted:    25.9K
 * Total Submissions: 96.7K
 * Testcase Example:  '[[1,1],[2,2],[3,3]]'
 *
 * 给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：points = [[1,1],[2,2],[3,3]]
 * 输出：3
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
 * 输出：4
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= points.length <= 300
 * points[i].length == 2
 * -10^4 <= xi, yi <= 10^4
 * points 中的所有点 互不相同
 * 
 * 
 */

/**
 * @File    :   149.直线上最多的点数.cpp
 * @Time    :   2021/06/25 14:23:11
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：朴素解法（枚举直线 + 枚举统计）
 * 我们知道，两个点可以确定一条线。
 * 
 * 因此一个朴素的做法是先枚举两条点（确定一条线），然后检查其余点是否落在该线中。
 * 
 * 为了避免除法精度问题，当我们枚举两个点 i 和 j 时，不直接计算其对应直线的
 * 斜率和截距，而是通过判断 i 和 j 与第三个点 k 形成的两条直线斜率是否相等
 * （斜率相等的两条直线要么平行，要么重合，平行需要 4 个点来唯一确定，我们只有
 * 3 个点，所以可以直接判定两直线重合）。
 * 
 *     (x1, y1), (x2, y2), (x3, y3)
 * 
 *     k1 = (y2 - y1) / (x2 - x1)
 *     k2 = (y3 - y1) / (x3 - x1)
 * 
 *     k1 = k2  ->  (y2 - y1) / (x2 - x1) = (y3 - y1) / (x3 - x1)
 *              ->  (y2 - y1) * (x3 - x1) = (y3 - y1) * (x2 - x1)
 * 
 * 方法二：优化（枚举直线 + 哈希表统计）
 * 根据「朴素解法」的思路，枚举所有直线的过程不可避免，但统计点数的过程可以优化。
 * 
 * 具体的，我们可以先枚举所有可能出现的 直线斜率（根据两点确定一条直线，即枚举
 * 所有的「点对」），使用「哈希表」统计所有 斜率 对应的点的数量，在所有值中取个
 * max 即是答案。
 * 
 * 一些细节：在使用「哈希表」进行保存时，为了避免精度问题，我们直接使用字符串
 * 进行保存，同时需要将 斜率 约干净。
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
#define PII pair<int, int>

class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        int n = points.size();
        int ans = 1;
        map<PII, int> lines;
        for (int i = 0; i < n; i++) {
            lines.clear();
            int x1 = points[i][0], y1 = points[i][1];
            for (int j = i + 1; j < n; j++) {
                int x2 = points[j][0], y2 = points[j][1];
                int dx = x1 - x2, dy = y1 - y2;
                int d = gcd(dx, dy);
                PII line = {dx / d, dy / d};
                lines[line]++;
                ans = max(ans, lines[line] + 1);
            }
        }
        return ans;
    }

    int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }
};
// @lc code=end

// class Solution {
// public:
//     int maxPoints(vector<vector<int>>& points) {
//         int n = points.size();
//         int ans = 1;
//         for (int i = 0; i < n; i++) {
//             int x1 = points[i][0], y1 = points[i][1];
//             for (int j = i + 1; j < n; j++) {
//                 int x2 = points[j][0], y2 = points[j][1];
//                 int cnt = 2;
//                 for (int k = j + 1; k < n; k++) {
//                     int x3 = points[k][0], y3 = points[k][1];
//                     if ((y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)) cnt++;
//                 }
//                 ans = max(ans, cnt);
//             }
//         }
//         return ans;
//     }
// };
