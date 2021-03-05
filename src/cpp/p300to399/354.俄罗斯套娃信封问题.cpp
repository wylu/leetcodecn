/*
 * @lc app=leetcode.cn id=354 lang=cpp
 *
 * [354] 俄罗斯套娃信封问题
 *
 * https://leetcode-cn.com/problems/russian-doll-envelopes/description/
 *
 * algorithms
 * Hard (42.80%)
 * Likes:    451
 * Dislikes: 0
 * Total Accepted:    47.9K
 * Total Submissions: 111.9K
 * Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
 *
 * 给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。
 * 
 * 当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
 * 
 * 请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
 * 
 * 注意：不允许旋转信封。
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
 * 输出：3
 * 解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
 * 
 * 示例 2：
 * 
 * 
 * 输入：envelopes = [[1,1],[1,1],[1,1]]
 * 输出：1
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= envelopes.length <= 5000
 * envelopes[i].length == 2
 * 1 <= wi, hi <= 10^4
 * 
 * 
 */

/**
 * @File    :   354.俄罗斯套娃信封问题.cpp
 * @Time    :   2021/03/05 09:36:27
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
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        if (envelopes.empty()) return 0;

        sort(envelopes.begin(), envelopes.end(),
             [](const auto& e1, const auto& e2) {
                 return e1[0] < e2[0] || (e1[0] == e2[0] && e1[1] > e2[1]);
             });

        int n = envelopes.size();
        vector<int> f = {envelopes[0][1]};

        for (int i = 1; i < n; i++) {
            if (envelopes[i][1] > f.back()) {
                f.push_back(envelopes[i][1]);
            } else {
                auto it = lower_bound(f.begin(), f.end(), envelopes[i][1]);
                *it = envelopes[i][1];
            }
        }

        return f.size();
    }
};
// @lc code=end
