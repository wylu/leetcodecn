/*
 * @lc app=leetcode.cn id=84 lang=cpp
 *
 * [84] 柱状图中最大的矩形
 *
 * https://leetcode-cn.com/problems/largest-rectangle-in-histogram/description/
 *
 * algorithms
 * Hard (41.93%)
 * Likes:    1022
 * Dislikes: 0
 * Total Accepted:    100.5K
 * Total Submissions: 239.6K
 * Testcase Example:  '[2,1,5,6,2,3]'
 *
 * 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
 * 
 * 求在该柱状图中，能够勾勒出来的矩形的最大面积。
 * 
 * 
 * 
 * 
 * 
 * 以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
 * 
 * 
 * 
 * 
 * 
 * 图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
 * 
 * 
 * 
 * 示例:
 * 
 * 输入: [2,1,5,6,2,3]
 * 输出: 10
 * 
 */

/**
 * @File    :   84.柱状图中最大的矩形.cpp
 * @Time    :   2020/11/21 00:20:34
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
    int largestRectangleArea(vector<int>& heights) {
        heights.insert(heights.begin(), 0);
        heights.emplace_back(0);

        stack<int> st;
        st.push(0);

        int ans = 0, n = heights.size();
        for (int i = 1; i < n; i++) {
            while (heights[st.top()] > heights[i]) {
                int h = heights[st.top()];
                st.pop();
                int w = i - st.top() - 1;
                ans = max(ans, h * w);
            }
            st.push(i);
        }

        return ans;
    }
};
// @lc code=end

int main(int argc, char const* argv[]) {
    Solution solu;
    vector<int> heights = {2, 1, 5, 6, 2, 3};
    cout << solu.largestRectangleArea(heights) << endl;
    return 0;
}
