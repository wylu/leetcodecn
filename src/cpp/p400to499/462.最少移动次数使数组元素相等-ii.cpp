/*
 * @lc app=leetcode.cn id=462 lang=cpp
 *
 * [462] 最少移动次数使数组元素相等 II
 *
 * https://leetcode.cn/problems/minimum-moves-to-equal-array-elements-ii/description/
 *
 * algorithms
 * Medium (61.75%)
 * Likes:    196
 * Dislikes: 0
 * Total Accepted:    27.3K
 * Total Submissions: 44.2K
 * Testcase Example:  '[1,2,3]'
 *
 * 给你一个长度为 n 的整数数组 nums ，返回使所有数组元素相等需要的最少移动数。
 * 
 * 在一步操作中，你可以使数组中的一个元素加 1 或者减 1 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：nums = [1,2,3]
 * 输出：2
 * 解释：
 * 只需要两步操作（每步操作指南使一个元素加 1 或减 1）：
 * [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：nums = [1,10,2,9]
 * 输出：16
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * n == nums.length
 * 1 <= nums.length <= 10^5
 * -10^9 <= nums[i] <= 10^9
 * 
 * 
 */

#include <bits/stdc++.h>
using namespace std;

/**
 * @File    :   462.最少移动次数使数组元素相等-ii.cpp
 * @Time    :   2022/05/19 10:49:26
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
class Solution {
public:
    int minMoves2(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int middle = nums[n / 2];

        int ans = 0;
        for (int i = 0; i < n; i++) ans += abs(nums[i] - middle);

        return ans;
    }
};
// @lc code=end
