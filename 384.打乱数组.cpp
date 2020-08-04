/*
 * @lc app=leetcode.cn id=384 lang=cpp
 *
 * [384] 打乱数组
 *
 * https://leetcode-cn.com/problems/shuffle-an-array/description/
 *
 * algorithms
 * Medium (52.39%)
 * Likes:    83
 * Dislikes: 0
 * Total Accepted:    23.3K
 * Total Submissions: 44.3K
 * Testcase Example:  '["Solution","shuffle","reset","shuffle"]\n[[[1,2,3]],[],[],[]]'
 *
 * 打乱一个没有重复元素的数组。
 * 
 * 
 * 
 * 示例:
 * 
 * // 以数字集合 1, 2 和 3 初始化数组。
 * int[] nums = {1,2,3};
 * Solution solution = new Solution(nums);
 * 
 * // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
 * solution.shuffle();
 * 
 * // 重设数组到它的初始状态[1,2,3]。
 * solution.reset();
 * 
 * // 随机返回数组[1,2,3]打乱后的结果。
 * solution.shuffle();
 * 
 * 
 */

/**
 * @File    :   384.打乱数组.cpp
 * @Time    :   2020/08/04 22:39:46
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
    vector<int> origin;
    vector<int> nums;

public:
    Solution(vector<int>& nums) {
        origin = nums;
        this->nums.assign(origin.begin(), origin.end());
    }

    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        nums.clear();
        nums.assign(origin.begin(), origin.end());
        return nums;
    }

    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        for (int i = 0; i < nums.size(); i++) {
            int j = i + rand() % (nums.size() - i);
            swap(nums[i], nums[j]);
        }
        return nums;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */
// @lc code=end
