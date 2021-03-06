/*
 * @lc app=leetcode.cn id=1658 lang=cpp
 *
 * [1658] 将 x 减到 0 的最小操作数
 *
 * https://leetcode-cn.com/problems/minimum-operations-to-reduce-x-to-zero/description/
 *
 * algorithms
 * Medium (21.55%)
 * Likes:    19
 * Dislikes: 0
 * Total Accepted:    2.2K
 * Total Submissions: 10.1K
 * Testcase Example:  '[1,1,4,2,3]\n5'
 *
 * 给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要
 * 修改 数组以供接下来的操作使用。
 * 
 * 如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：nums = [1,1,4,2,3], x = 5
 * 输出：2
 * 解释：最佳解决方案是移除后两个元素，将 x 减到 0 。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：nums = [5,6,7,8,9], x = 4
 * 输出：-1
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：nums = [3,2,20,1,1,3], x = 10
 * 输出：5
 * 解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^4
 * 1 <= x <= 10^9
 * 
 * 
 */

/**
 * @File    :   1658.将-x-减到-0-的最小操作数.cpp
 * @Time    :   2020/11/16 17:53:55
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 本题类似186周赛的第二题可获得的最大点数，找外部最小即找中间最大。
 * 方法一：前缀和 + hash表
 * 方法二：双指针 + 滑动窗口
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int target = accumulate(nums.begin(), nums.end(), 0) - x;
        int ans = -1, tot = 0;
        int left = 0, right = 0, n = nums.size();

        while (left < n) {
            if (right < n) tot += nums[right++];
            while (left <= right && tot > target) tot -= nums[left++];
            if (tot == target) ans = max(ans, right - left);
            if (right == n && tot <= target) break;
        }

        return ans == -1 ? -1 : n - ans;
    }
};
// @lc code=end
