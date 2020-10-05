/*
 * @lc app=leetcode.cn id=18 lang=cpp
 *
 * [18] 四数之和
 *
 * https://leetcode-cn.com/problems/4sum/description/
 *
 * algorithms
 * Medium (38.63%)
 * Likes:    594
 * Dislikes: 0
 * Total Accepted:    114.3K
 * Total Submissions: 295.9K
 * Testcase Example:  '[1,0,-1,0,-2,2]\n0'
 *
 * 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c
 * + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
 * 
 * 注意：
 * 
 * 答案中不可以包含重复的四元组。
 * 
 * 示例：
 * 
 * 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
 * 
 * 满足要求的四元组集合为：
 * [
 * ⁠ [-1,  0, 0, 1],
 * ⁠ [-2, -1, 1, 2],
 * ⁠ [-2,  0, 0, 2]
 * ]
 * 
 * 
 */

/**
 * @File    :   18.四数之和.cpp
 * @Time    :   2020/10/05 10:24:59
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
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> ans;
        sort(nums.begin(), nums.end());

        int n = nums.size();
        for (int a = 0; a < n - 3; a++) {
            if (a > 0 && nums[a] == nums[a - 1]) continue;

            for (int b = a + 1; b < n - 2; b++) {
                if (b > a + 1 && nums[b] == nums[b - 1]) continue;

                int d = n - 1;
                for (int c = b + 1; c < n - 1; c++) {
                    if (c > b + 1 && nums[c] == nums[c - 1]) continue;

                    while (c < d &&
                           nums[a] + nums[b] + nums[c] + nums[d] > target) {
                        d--;
                    }

                    if (c == d) {
                        break;
                    }

                    if (nums[a] + nums[b] + nums[c] + nums[d] == target) {
                        ans.emplace_back(
                            vector<int>({nums[a], nums[b], nums[c], nums[d]}));
                    }
                }
            }
        }

        return ans;
    }
};
// @lc code=end
