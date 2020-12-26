/*
 * @lc app=leetcode.cn id=85 lang=cpp
 *
 * [85] 最大矩形
 *
 * https://leetcode-cn.com/problems/maximal-rectangle/description/
 *
 * algorithms
 * Hard (50.36%)
 * Likes:    739
 * Dislikes: 0
 * Total Accepted:    56.9K
 * Total Submissions: 113.1K
 * Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
 *
 * 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：matrix =
 * [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
 * 输出：6
 * 解释：最大矩形如上图所示。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：matrix = []
 * 输出：0
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：matrix = [["0"]]
 * 输出：0
 * 
 * 
 * 示例 4：
 * 
 * 
 * 输入：matrix = [["1"]]
 * 输出：1
 * 
 * 
 * 示例 5：
 * 
 * 
 * 输入：matrix = [["0","0"]]
 * 输出：0
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * rows == matrix.length
 * cols == matrix[0].length
 * 0 
 * matrix[i][j] 为 '0' 或 '1'
 * 
 * 
 */

/**
 * @File    :   85.最大矩形.cpp
 * @Time    :   2020/12/26 21:30:20
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 参考 84. 柱状图中最大的矩形
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return 0;

        int ans = 0, m = matrix.size(), n = matrix[0].size();
        vector<int> heights(n + 2);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == '0') {
                    heights[j + 1] = 0;
                } else {
                    heights[j + 1] += 1;
                }
            }
            ans = max(ans, largestRectangleArea(heights));
        }

        return ans;
    }

    int largestRectangleArea(vector<int>& heights) {
        int ans = 0, n = heights.size();
        stack<int> st;
        st.push(0);

        for (int i = 1; i < n; i++) {
            while (heights[i] < heights[st.top()]) {
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
