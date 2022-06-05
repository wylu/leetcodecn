/*
 * @lc app=leetcode.cn id=478 lang=cpp
 *
 * [478] 在圆内随机生成点
 *
 * https://leetcode.cn/problems/generate-random-point-in-a-circle/description/
 *
 * algorithms
 * Medium (45.48%)
 * Likes:    89
 * Dislikes: 0
 * Total Accepted:    11.7K
 * Total Submissions: 25.9K
 * Testcase Example:  '["Solution","randPoint","randPoint","randPoint"]\n[[1.0,0.0,0.0],[],[],[]]'
 *
 * 给定圆的半径和圆心的位置，实现函数 randPoint ，在圆中产生均匀随机点。
 * 
 * 实现 Solution 类:
 * 
 * 
 * Solution(double radius, double x_center, double y_center) 用圆的半径 radius
 * 和圆心的位置 (x_center, y_center) 初始化对象
 * randPoint() 返回圆内的一个随机点。圆周上的一点被认为在圆内。答案作为数组返回 [x, y] 。
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入: 
 * ["Solution","randPoint","randPoint","randPoint"]
 * [[1.0, 0.0, 0.0], [], [], []]
 * 输出: [null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]
 * 解释:
 * Solution solution = new Solution(1.0, 0.0, 0.0);
 * solution.randPoint ();//返回[-0.02493，-0.38077]
 * solution.randPoint ();//返回[0.82314,0.38945]
 * solution.randPoint ();//返回[0.36572,0.17248]
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 0 < radius <= 10^8
 * -10^7 <= x_center, y_center <= 10^7
 * randPoint 最多被调用 3 * 10^4 次
 * 
 * 
 */

#include <bits/stdc++.h>
using namespace std;

/**
 * @File    :   478.在圆内随机生成点.cpp
 * @Time    :   2022/06/05 09:46:53
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
class Solution {
    mt19937 gen{random_device{}()};
    uniform_real_distribution<double> dis;
    double r, cx, cy;

public:
    Solution(double radius, double x_center, double y_center)
        : dis(-radius, radius), r(radius), cx(x_center), cy(y_center) {}

    vector<double> randPoint() {
        while (true) {
            double x = dis(gen), y = dis(gen);
            if (x * x + y * y <= r * r) {
                return {cx + x, cy + y};
            }
        }
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(radius, x_center, y_center);
 * vector<double> param_1 = obj->randPoint();
 */
// @lc code=end
