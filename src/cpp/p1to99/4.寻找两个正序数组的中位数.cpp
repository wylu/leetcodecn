/*
 * @lc app=leetcode.cn id=4 lang=cpp
 *
 * [4] 寻找两个正序数组的中位数
 *
 * https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
 *
 * algorithms
 * Hard (38.80%)
 * Likes:    3266
 * Dislikes: 0
 * Total Accepted:    267.8K
 * Total Submissions: 690K
 * Testcase Example:  '[1,3]\n[2]'
 *
 * 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。
 * 
 * 进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：nums1 = [1,3], nums2 = [2]
 * 输出：2.00000
 * 解释：合并数组 = [1,2,3] ，中位数 2
 * 
 * 
 * 示例 2：
 * 
 * 输入：nums1 = [1,2], nums2 = [3,4]
 * 输出：2.50000
 * 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
 * 
 * 
 * 示例 3：
 * 
 * 输入：nums1 = [0,0], nums2 = [0,0]
 * 输出：0.00000
 * 
 * 
 * 示例 4：
 * 
 * 输入：nums1 = [], nums2 = [1]
 * 输出：1.00000
 * 
 * 
 * 示例 5：
 * 
 * 输入：nums1 = [2], nums2 = []
 * 输出：2.00000
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * nums1.length == m
 * nums2.length == n
 * 0 <= m <= 1000
 * 0 <= n <= 1000
 * 1 <= m + n <= 2000
 * -10^6 <= nums1[i], nums2[i] <= 10^6
 * 
 * 
 */

/**
 * @File    :   4.寻找两个正序数组的中位数.cpp
 * @Time    :   2020/10/05 19:10:24
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
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) {
            swap(nums1, nums2);
        }

        int m = nums1.size(), n = nums2.size();
        int totLeft = (m + n + 1) / 2;

        int left = 0, right = m;
        while (left < right) {
            int i = (left + right + 1) / 2;
            int j = totLeft - i;
            if (nums1[i - 1] <= nums2[j]) {
                left = i;
            } else {
                right = i - 1;
            }
        }

        int i = (left + right + 1) / 2;
        int j = totLeft - i;
        int maxLeft1 = i == 0 ? INT32_MIN : nums1[i - 1];
        int minRight1 = i == m ? INT32_MAX : nums1[i];
        int maxLeft2 = j == 0 ? INT32_MIN : nums2[j - 1];
        int minRight2 = j == n ? INT32_MAX : nums2[j];

        if ((m + n) % 2 == 0) {
            return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0;
        }
        return max(maxLeft1, maxLeft2);
    }
};
// @lc code=end
