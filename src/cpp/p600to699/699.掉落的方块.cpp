/*
 * @lc app=leetcode.cn id=699 lang=cpp
 *
 * [699] 掉落的方块
 *
 * https://leetcode.cn/problems/falling-squares/description/
 *
 * algorithms
 * Hard (54.33%)
 * Likes:    99
 * Dislikes: 0
 * Total Accepted:    7K
 * Total Submissions: 12.9K
 * Testcase Example:  '[[1,2],[2,3],[6,1]]'
 *
 * 在无限长的数轴（即 x 轴）上，我们根据给定的顺序放置对应的正方形方块。
 * 
 * 第 i 个掉落的方块（positions[i] = (left, side_length)）是正方形，其中 left
 * 表示该方块最左边的点位置(positions[i][0])，side_length 表示该方块的边长(positions[i][1])。
 * 
 * 每个方块的底部边缘平行于数轴（即 x 轴），并且从一个比目前所有的落地方块更高的高度掉落而下。在上一个方块结束掉落，并保持静止后，才开始掉落新方块。
 * 
 * 
 * 方块的底边具有非常大的粘性，并将保持固定在它们所接触的任何长度表面上（无论是数轴还是其他方块）。邻接掉落的边不会过早地粘合在一起，因为只有底边才具有粘性。
 * 
 * 
 * 
 * 返回一个堆叠高度列表 ans 。每一个堆叠高度 ans[i] 表示在通过 positions[0], positions[1], ...,
 * positions[i] 表示的方块掉落结束后，目前所有已经落稳的方块堆叠的最高高度。
 * 
 * 
 * 
 * 
 * 
 * 示例 1:
 * 
 * 输入: [[1, 2], [2, 3], [6, 1]]
 * 输出: [2, 5, 5]
 * 解释:
 * 
 * 第一个方块 positions[0] = [1, 2] 掉落：
 * _aa
 * _aa
 * -------
 * 方块最大高度为 2 。
 * 
 * 第二个方块 positions[1] = [2, 3] 掉落：
 * __aaa
 * __aaa
 * __aaa
 * _aa__
 * _aa__
 * --------------
 * 方块最大高度为5。
 * 大的方块保持在较小的方块的顶部，不论它的重心在哪里，因为方块的底部边缘有非常大的粘性。
 * 
 * 第三个方块 positions[1] = [6, 1] 掉落：
 * __aaa
 * __aaa
 * __aaa
 * _aa
 * _aa___a
 * -------------- 
 * 方块最大高度为5。
 * 
 * 因此，我们返回结果[2, 5, 5]。
 * 
 * 
 * 
 * 
 * 示例 2:
 * 
 * 输入: [[100, 100], [200, 100]]
 * 输出: [100, 100]
 * 解释: 相邻的方块不会过早地卡住，只有它们的底部边缘才能粘在表面上。
 * 
 * 
 * 
 * 
 * 注意:
 * 
 * 
 * 1 <= positions.length <= 1000.
 * 1 <= positions[i][0] <= 10^8.
 * 1 <= positions[i][1] <= 10^6.
 * 
 * 
 * 
 * 
 */

#include <bits/stdc++.h>
using namespace std;

/**
 * @File    :   699.掉落的方块.cpp
 * @Time    :   2022/05/26 10:19:51
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
class Solution {
public:
    vector<int> fallingSquares(vector<vector<int>>& positions) {
        int n = positions.size();
        vector<int> ans(n);

        map<int, int> heights;
        // 初始时从 0 开始的所有点的堆叠高度都是 0
        heights[0] = 0;

        for (int i = 0; i < n; i++) {
            int size = positions[i][1];
            int left = positions[i][0],
                right = positions[i][0] + positions[i][1] - 1;
            auto lp = heights.upper_bound(left),
                 rp = heights.upper_bound(right);
            // 记录 right + 1 对应的堆叠高度（如果 right + 1 不在 heightMap 中）
            int rh = prev(rp)->second;

            // 更新第 i 个掉落的方块的堆叠高度
            int h = 0;
            for (auto p = prev(lp); p != rp; p++) {
                h = max(h, p->second + size);
            }

            // 清除 heights 中位于 (left, right) 内的点
            heights.erase(lp, rp);

            // 更新 left 的变化
            heights[left] = h;
            if (rp == heights.end() || rp->first != right + 1) {
                heights[right + 1] = rh;
            }

            ans[i] = i > 0 ? max(ans[i - 1], h) : h;
        }

        return ans;
    }
};
// @lc code=end

// class Solution {
// public:
//     vector<int> fallingSquares(vector<vector<int>>& positions) {
//         int n = positions.size();
//         vector<int> heights(n);
//         for (int i = 0; i < n; i++) {
//             int l1 = positions[i][0], r1 = positions[i][0] + positions[i][1];
//             heights[i] = positions[i][1];
//             for (int j = 0; j < i; j++) {
//                 int l2 = positions[j][0],
//                     r2 = positions[j][0] + positions[j][1];
//                 if (r1 > l2 && r2 > l1) {
//                     heights[i] = max(heights[i], heights[j] + positions[i][1]);
//                 }
//             }
//         }

//         for (int i = 1; i < n; i++) {
//             heights[i] = max(heights[i], heights[i - 1]);
//         }

//         return heights;
//     }
// };
