/*
 * @lc app=leetcode.cn id=719 lang=cpp
 *
 * [719] 找出第 k 小的距离对
 *
 * https://leetcode-cn.com/problems/find-k-th-smallest-pair-distance/description/
 *
 * algorithms
 * Hard (33.94%)
 * Likes:    120
 * Dislikes: 0
 * Total Accepted:    5.3K
 * Total Submissions: 15.6K
 * Testcase Example:  '[1,3,1]\n1'
 *
 * 给定一个整数数组，返回所有数对之间的第 k 个最小距离。一对 (A, B) 的距离被定义为 A 和 B 之间的绝对差值。
 * 
 * 示例 1:
 * 
 * 
 * 输入：
 * nums = [1,3,1]
 * k = 1
 * 输出：0 
 * 解释：
 * 所有数对如下：
 * (1,3) -> 2
 * (1,1) -> 0
 * (3,1) -> 2
 * 因此第 1 个最小距离的数对是 (1,1)，它们之间的距离为 0。
 * 
 * 
 * 提示:
 * 
 * 
 * 2 <= len(nums) <= 10000.
 * 0 <= nums[i] < 1000000.
 * 1 <= k <= len(nums) * (len(nums) - 1) / 2.
 * 
 * 
 */

/**
 * @File    :   719.找出第-k-小的距离对.cpp
 * @Time    :   2020/10/06 00:28:34
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
    int smallestDistancePair(vector<int>& nums, int k) {
        int n = nums.size();
        sort(nums.begin(), nums.end());

        auto ok = [&](int dist) {
            int cnt = 0, i = 0;
            for (int j = 0; j < n; j++) {
                while (nums[j] - nums[i] > dist) i++;
                cnt += j - i;
            }
            return cnt < k;
        };

        int left = 0, right = nums[n - 1] - nums[0];
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (ok(mid)) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }
};
// @lc code=end
