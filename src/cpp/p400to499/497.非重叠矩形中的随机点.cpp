/*
 * @lc app=leetcode.cn id=497 lang=cpp
 *
 * [497] 非重叠矩形中的随机点
 *
 * https://leetcode.cn/problems/random-point-in-non-overlapping-rectangles/description/
 *
 * algorithms
 * Medium (41.30%)
 * Likes:    90
 * Dislikes: 0
 * Total Accepted:    12.3K
 * Total Submissions: 29.8K
 * Testcase Example:  '["Solution","pick","pick","pick","pick","pick"]\n' +
  '[[[[-2,-2,1,1],[2,2,4,6]]],[],[],[],[],[]]'
 *
 * 给定一个由非重叠的轴对齐矩形的数组 rects ，其中 rects[i] = [ai, bi, xi, yi] 表示 (ai, bi) 是第 i
 * 个矩形的左下角点，(xi, yi) 是第 i
 * 个矩形的右上角点。设计一个算法来随机挑选一个被某一矩形覆盖的整数点。矩形周长上的点也算做是被矩形覆盖。所有满足要求的点必须等概率被返回。
 * 
 * 在给定的矩形覆盖的空间内的任何整数点都有可能被返回。
 * 
 * 请注意 ，整数点是具有整数坐标的点。
 * 
 * 实现 Solution 类:
 * 
 * 
 * Solution(int[][] rects) 用给定的矩形数组 rects 初始化对象。
 * int[] pick() 返回一个随机的整数点 [u, v] 在给定的矩形所覆盖的空间内。
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 
 * 
 * 输入: 
 * ["Solution", "pick", "pick", "pick", "pick", "pick"]
 * [[[[-2, -2, 1, 1], [2, 2, 4, 6]]], [], [], [], [], []]
 * 输出: 
 * [null, [1, -2], [1, -1], [-1, -2], [-2, -2], [0, 0]]
 * 
 * 解释：
 * Solution solution = new Solution([[-2, -2, 1, 1], [2, 2, 4, 6]]);
 * solution.pick(); // 返回 [1, -2]
 * solution.pick(); // 返回 [1, -1]
 * solution.pick(); // 返回 [-1, -2]
 * solution.pick(); // 返回 [-2, -2]
 * solution.pick(); // 返回 [0, 0]
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= rects.length <= 100
 * rects[i].length == 4
 * -10^9 <= ai < xi <= 10^9
 * -10^9 <= bi < yi <= 10^9
 * xi - ai <= 2000
 * yi - bi <= 2000
 * 所有的矩形不重叠。
 * pick 最多被调用 10^4 次。
 * 
 * 
 */

#include <bits/stdc++.h>
using namespace std;

/**
 * @File    :   497.非重叠矩形中的随机点.cpp
 * @Time    :   2022/06/09 14:30:56
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
class Solution {
    vector<vector<int>>& rects;
    vector<int> ps{0};
    mt19937 gen{random_device{}()};

public:
    Solution(vector<vector<int>>& rects) : rects(rects) {
        for (auto& r : rects) {
            ps.emplace_back(ps.back() + (r[2] - r[0] + 1) * (r[3] - r[1] + 1));
        }
    }

    vector<int> pick() {
        uniform_int_distribution<int> dis(0, ps.back() - 1);
        int k = dis(gen) % ps.back();
        int i = upper_bound(ps.begin(), ps.end(), k) - ps.begin() - 1;
        int a = rects[i][0], b = rects[i][1], y = rects[i][3];
        int da = (k - ps[i]) / (y - b + 1), db = (k - ps[i]) % (y - b + 1);
        return {a + da, b + db};
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(rects);
 * vector<int> param_1 = obj->pick();
 */
// @lc code=end
