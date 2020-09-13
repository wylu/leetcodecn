/*
 * @lc app=leetcode.cn id=229 lang=cpp
 *
 * [229] 求众数 II
 *
 * https://leetcode-cn.com/problems/majority-element-ii/description/
 *
 * algorithms
 * Medium (43.51%)
 * Likes:    247
 * Dislikes: 0
 * Total Accepted:    20.1K
 * Total Submissions: 46.1K
 * Testcase Example:  '[3,2,3]'
 *
 * 给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
 * 
 * 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。
 * 
 * 示例 1:
 * 
 * 输入: [3,2,3]
 * 输出: [3]
 * 
 * 示例 2:
 * 
 * 输入: [1,1,1,3,3,2,2,2]
 * 输出: [1,2]
 * 
 */

/**
 * @File    :   229.求众数-ii.cpp
 * @Time    :   2020/09/13 18:19:45
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
    vector<int> majorityElement(vector<int>& nums) {
        if (nums.empty()) {
            return {};
        }
        int cnt1 = 0, cdd1 = nums[0];
        int cnt2 = 0, cdd2 = nums[0];

        for (auto num : nums) {
            if (num == cdd1) {
                cnt1++;
                continue;
            }
            if (num == cdd2) {
                cnt2++;
                continue;
            }

            if (cnt1 == 0) {
                cdd1 = num;
                cnt1++;
                continue;
            }
            if (cnt2 == 0) {
                cdd2 = num;
                cnt2++;
                continue;
            }

            cnt1--, cnt2--;
        }

        cnt1 = 0, cnt2 = 0;
        for (auto num : nums) {
            if (num == cdd1) {
                cnt1++;
            } else if (num == cdd2) {
                cnt2++;
            }
        }

        vector<int> ans;
        if (cnt1 > nums.size() / 3) {
            ans.emplace_back(cdd1);
        }
        if (cnt2 > nums.size() / 3) {
            ans.emplace_back(cdd2);
        }

        return ans;
    }
};
// @lc code=end
