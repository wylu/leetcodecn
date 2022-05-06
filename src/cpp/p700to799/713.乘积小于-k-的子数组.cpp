/*
 * @lc app=leetcode.cn id=713 lang=cpp
 *
 * [713] 乘积小于 K 的子数组
 *
 * https://leetcode-cn.com/problems/subarray-product-less-than-k/description/
 *
 * algorithms
 * Medium (45.47%)
 * Likes:    434
 * Dislikes: 0
 * Total Accepted:    47.1K
 * Total Submissions: 103.7K
 * Testcase Example:  '[10,5,2,6]\n100'
 *
 * 给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：nums = [10,5,2,6], k = 100
 * 输出：8
 * 解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2],、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
 * 需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：nums = [1,2,3], k = 0
 * 输出：0
 * 
 * 
 * 
 * 提示: 
 * 
 * 
 * 1 <= nums.length <= 3 * 10^4
 * 1 <= nums[i] <= 1000
 * 0 <= k <= 10^6
 * 
 * 
 */

#include <bits/stdc++.h>
using namespace std;

/**
 * @File    :   713.乘积小于-k-的子数组.cpp
 * @Time    :   2022/05/05 09:30:08
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        if (k <= 1) return 0;
        int ans = 0, n = nums.size();
        for (int left = 0, right = 0, cur = 1; right < n; right++) {
            cur *= nums[right];
            while (cur >= k) cur /= nums[left++];
            ans += right - left + 1;
        }
        return ans;
    }
};
// @lc code=end
