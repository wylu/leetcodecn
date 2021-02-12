/*
 * @lc app=leetcode.cn id=119 lang=cpp
 *
 * [119] 杨辉三角 II
 *
 * https://leetcode-cn.com/problems/pascals-triangle-ii/description/
 *
 * algorithms
 * Easy (64.41%)
 * Likes:    251
 * Dislikes: 0
 * Total Accepted:    98.5K
 * Total Submissions: 153K
 * Testcase Example:  '3'
 *
 * 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
 * 
 * 
 * 
 * 在杨辉三角中，每个数是它左上方和右上方的数的和。
 * 
 * 示例:
 * 
 * 输入: 3
 * 输出: [1,3,3,1]
 * 
 * 
 * 进阶：
 * 
 * 你可以优化你的算法到 O(k) 空间复杂度吗？
 * 
 */

/**
 * @File    :   119.杨辉三角-ii.cpp
 * @Time    :   2021/02/12 21:34:38
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
    vector<int> getRow(int rowIndex) {
        vector<int> pre = {1};
        for (int n = 1; n <= rowIndex; n++) {
            vector<int> cur(n + 1);
            cur[0] = 1;
            for (int i = 1; i < n; i++) {
                cur[i] = pre[i - 1] + pre[i];
            }
            cur[n] = 1;
            pre = cur;
        }
        return pre;
    }
};
// @lc code=end
