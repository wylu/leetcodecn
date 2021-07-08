/*
 * @lc app=leetcode.cn id=930 lang=cpp
 *
 * [930] 和相同的二元子数组
 *
 * https://leetcode-cn.com/problems/binary-subarrays-with-sum/description/
 *
 * algorithms
 * Medium (45.69%)
 * Likes:    118
 * Dislikes: 0
 * Total Accepted:    9.6K
 * Total Submissions: 20.9K
 * Testcase Example:  '[1,0,1,0,1]\n2'
 *
 * 给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。
 * 
 * 子数组 是数组的一段连续部分。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：nums = [1,0,1,0,1], goal = 2
 * 输出：4
 * 解释：
 * 如下面黑体所示，有 4 个满足题目要求的子数组：
 * [1,0,1,0,1]
 * [1,0,1,0,1]
 * [1,0,1,0,1]
 * [1,0,1,0,1]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：nums = [0,0,0,0,0], goal = 0
 * 输出：15
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= nums.length <= 3 * 10^4
 * nums[i] 不是 0 就是 1
 * 0 <= goal <= nums.length
 * 
 * 
 */

/**
 * @File    :   930.和相同的二元子数组.cpp
 * @Time    :   2021/07/08 08:54:46
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
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        int n = nums.size();
        vector<int> ps(n + 1);
        for (int i = 0; i < n; i++) {
            ps[i + 1] = ps[i] + nums[i];
        }

        unordered_map<int, int> counter;
        counter[ps[0]]++;

        int ans = 0, sum = 0;
        for (auto num : nums) {
            sum += num;
            int need = sum - goal;
            if (counter.count(need)) ans += counter[need];
            counter[sum]++;
        }

        return ans;
    }
};
// @lc code=end
