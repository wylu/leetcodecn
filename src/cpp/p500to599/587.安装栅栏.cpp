/*
 * @lc app=leetcode.cn id=587 lang=cpp
 *
 * [587] 安装栅栏
 *
 * https://leetcode-cn.com/problems/erect-the-fence/description/
 *
 * algorithms
 * Hard (58.87%)
 * Likes:    162
 * Dislikes: 0
 * Total Accepted:    9.6K
 * Total Submissions: 16.4K
 * Testcase Example:  '[[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]'
 *
 * 在一个二维的花园中，有一些用 (x, y)
 * 坐标表示的树。由于安装费用十分昂贵，你的任务是先用最短的绳子围起所有的树。只有当所有的树都被绳子包围时，花园才能围好栅栏。你需要找到正好位于栅栏边界上的树的坐标。
 * 
 * 
 * 
 * 示例 1:
 * 
 * 输入: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
 * 输出: [[1,1],[2,0],[4,2],[3,3],[2,4]]
 * 解释:
 * 
 * 
 * 
 * 示例 2:
 * 
 * 输入: [[1,2],[2,2],[4,2]]
 * 输出: [[1,2],[2,2],[4,2]]
 * 解释:
 * 
 * 即使树都在一条直线上，你也需要先用绳子包围它们。
 * 
 * 
 * 
 * 
 * 注意:
 * 
 * 
 * 所有的树应当被围在一起。你不能剪断绳子来包围树或者把树分成一组以上。
 * 输入的整数在 0 到 100 之间。
 * 花园至少有一棵树。
 * 所有树的坐标都是不同的。
 * 输入的点没有顺序。输出顺序也没有要求。
 * 
 */

#include <bits/stdc++.h>
using namespace std;

/**
 * @File    :   587.安装栅栏.cpp
 * @Time    :   2022/04/23 17:32:09
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> outerTrees(vector<vector<int>> &trees) {
        int n = trees.size();
        if (n < 4) return trees;

        auto cross = [](const vector<int> &p, const vector<int> &q,
                        const vector<int> &r) -> int {
            return (q[0] - p[0]) * (r[1] - q[1]) -
                   (q[1] - p[1]) * (r[0] - q[0]);
        };

        // 按照 x 大小进行排序，如果 x 相同，则按照 y 的大小进行排序
        sort(trees.begin(), trees.end(),
             [](const vector<int> &a, const vector<int> &b) -> bool {
                 return a[0] == b[0] ? a[1] < b[1] : a[0] < b[0];
             });

        vector<int> stk;
        vector<bool> used(n, false);
        // stk[0] 需要入栈两次，不进行标记
        stk.emplace_back(0);

        // 求出凸包的下半部分
        for (int i = 1; i < n; i++) {
            while (stk.size() > 1 && cross(trees[stk[stk.size() - 2]],
                                           trees[stk.back()], trees[i]) < 0) {
                used[stk.back()] = false;
                stk.pop_back();
            }
            used[i] = true;
            stk.emplace_back(i);
        }

        int m = stk.size();
        // 求出凸包的上半部分
        for (int i = n - 2; i >= 0; i--) {
            if (!used[i]) {
                while (stk.size() > m &&
                       cross(trees[stk[stk.size() - 2]], trees[stk.back()],
                             trees[i]) < 0) {
                    used[stk.back()] = false;
                    stk.pop_back();
                }
                used[i] = true;
                stk.emplace_back(i);
            }
        }

        // stk[0] 同时参与凸包的上半部分检测，因此需去掉重复的 stk[0]
        stk.pop_back();
        vector<vector<int>> res;
        for (auto &v : stk) {
            res.emplace_back(trees[v]);
        }
        return res;
    }
};
// @lc code=end
