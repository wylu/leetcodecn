/*
 * @lc app=leetcode.cn id=525 lang=cpp
 *
 * [525] 连续数组
 *
 * https://leetcode-cn.com/problems/contiguous-array/description/
 *
 * algorithms
 * Medium (49.55%)
 * Likes:    306
 * Dislikes: 0
 * Total Accepted:    16.9K
 * Total Submissions: 34.2K
 * Testcase Example:  '[0,1]'
 *
 * 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。
 * 
 * 
 * 
 * 示例 1:
 * 
 * 
 * 输入: nums = [0,1]
 * 输出: 2
 * 说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
 * 
 * 示例 2:
 * 
 * 
 * 输入: nums = [0,1,0]
 * 输出: 2
 * 说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= nums.length <= 10^5
 * nums[i] 不是 0 就是 1
 * 
 * 
 */

/**
 * @File    :   525.连续数组.cpp
 * @Time    :   2021/06/04 09:01:59
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
    int findMaxLength(vector<int>& nums) {
        int n = nums.size();
        vector<int> ps(n + 1);
        for (int i = 0; i < n; i++) ps[i + 1] = ps[i] + (nums[i] ? 1 : -1);

        int ans = 0;
        unordered_map<int, int> seen;
        for (int i = 0; i <= n; i++) {
            if (seen.count(ps[i])) {
                ans = max(ans, i - seen[ps[i]]);
            } else {
                seen[ps[i]] = i;
            }
        }

        return ans;
    }
};
// @lc code=end
