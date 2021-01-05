/*
 * @lc app=leetcode.cn id=1712 lang=cpp
 *
 * [1712] 将数组分成三个子数组的方案数
 *
 * https://leetcode-cn.com/problems/ways-to-split-array-into-three-subarrays/description/
 *
 * algorithms
 * Medium (25.36%)
 * Likes:    23
 * Dislikes: 0
 * Total Accepted:    1.8K
 * Total Submissions: 7.1K
 * Testcase Example:  '[1,1,1]'
 *
 * 我们称一个分割整数数组的方案是 好的 ，当它满足：
 * 
 * 
 * 数组被分成三个 非空 连续子数组，从左至右分别命名为 left ， mid ， right 。
 * left 中元素和小于等于 mid 中元素和，mid 中元素和小于等于 right 中元素和。
 * 
 * 
 * 给你一个 非负 整数数组 nums ，请你返回 好的 分割 nums 方案数目。由于答案可能会很大，请你将结果对 10^9 + 7 取余后返回。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：nums = [1,1,1]
 * 输出：1
 * 解释：唯一一种好的分割方案是将 nums 分成 [1] [1] [1] 。
 * 
 * 示例 2：
 * 
 * 
 * 输入：nums = [1,2,2,2,5,0]
 * 输出：3
 * 解释：nums 总共有 3 种好的分割方案：
 * [1] [2] [2,2,5,0]
 * [1] [2,2] [2,5,0]
 * [1,2] [2,2] [5,0]
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：nums = [3,2,1]
 * 输出：0
 * 解释：没有好的分割方案。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 3 <= nums.length <= 10^5
 * 0 <= nums[i] <= 10^4
 * 
 * 
 */

/**
 * @File    :   1712.将数组分成三个子数组的方案数.cpp
 * @Time    :   2021/01/05 09:09:31
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
    int waysToSplit(vector<int>& nums) {
        int n = nums.size();
        vector<int> ps(n + 1);
        for (int i = 0; i < n; i++) {
            ps[i + 1] = ps[i] + nums[i];
        }

        int ans = 0, MOD = 1000000007;
        for (int i = 1; i < n - 1 && ps[i] * 3 <= ps[n]; i++) {
            int lo = searchLeft(ps, i, n);
            int hi = searchRight(ps, i, n);
            ans = (ans + hi - lo + 1) % MOD;
        }

        return ans % MOD;
    }

    int searchLeft(vector<int>& ps, int i, int n) {
        int lo = i + 1, hi = n - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (ps[mid] - ps[i] < ps[i]) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return lo;
    }

    int searchRight(vector<int>& ps, int i, int n) {
        int lo = i + 1, hi = n - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (ps[n] - ps[mid] >= ps[mid] - ps[i]) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return hi;
    }
};
// @lc code=end
