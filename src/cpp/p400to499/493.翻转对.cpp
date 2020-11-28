/*
 * @lc app=leetcode.cn id=493 lang=cpp
 *
 * [493] 翻转对
 *
 * https://leetcode-cn.com/problems/reverse-pairs/description/
 *
 * algorithms
 * Hard (31.06%)
 * Likes:    203
 * Dislikes: 0
 * Total Accepted:    15.3K
 * Total Submissions: 49.4K
 * Testcase Example:  '[1,3,2,3,1]'
 *
 * 给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
 * 
 * 你需要返回给定数组中的重要翻转对的数量。
 * 
 * 示例 1:
 * 
 * 
 * 输入: [1,3,2,3,1]
 * 输出: 2
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入: [2,4,3,5,1]
 * 输出: 3
 * 
 * 
 * 注意:
 * 
 * 
 * 给定数组的长度不会超过50000。
 * 输入数组中的所有数字都在32位整数的表示范围内。
 * 
 * 
 */

/**
 * @File    :   493.翻转对.cpp
 * @Time    :   2020/11/28 21:29:23
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：归并排序
 * 思路及解法
 * 
 * 在归并排序的过程中，假设对于数组 nums[l..r] 而言，我们已经分别求出了
 * 子数组 nums[l..m] 与 nums[m+1..r] 的翻转对数目，并已将两个子数组
 * 分别排好序，则 nums[l..r] 中的翻转对数目，就等于两个子数组的翻转对
 * 数目之和，加上左右端点分别位于两个子数组的翻转对数目。
 * 
 * 我们可以为两个数组分别维护指针 i,j。对于任意给定的 i 而言，我们不断地
 * 向右移动 j，直到 nums[i] <= 2*nums[j]。此时，意味着以 i 为左端点
 * 的翻转对数量为 j-m-1。随后，我们再将 i 向右移动一个单位，并用相同的
 * 方式计算以 i 为左端点的翻转对数量。不断重复这样的过程，就能够求出所有
 * 左右端点分别位于两个子数组的翻转对数目。
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int reversePairs(vector<int>& nums) {
        return nums.empty() ? 0 : mergeSort(nums, 0, nums.size() - 1);
    }

    int mergeSort(vector<int>& nums, int left, int right) {
        int ans = 0;
        if (left < right) {
            int mid = (left + right) / 2;
            ans += mergeSort(nums, left, mid);
            ans += mergeSort(nums, mid + 1, right);
            ans += merge(nums, left, mid, right);
        }
        return ans;
    }

    int merge(vector<int>& nums, int left, int mid, int right) {
        // 首先统计下标对的数量
        int i = left, j = mid + 1, ans = 0, k = 0;
        while (i <= mid) {
            while (j <= right && nums[i] > (long)2 * nums[j]) j++;
            ans += j - mid - 1;
            i++;
        }

        // 随后合并两个排序数组
        vector<int> tmp(right - left + 1);
        i = left, j = mid + 1;
        while (i <= mid || j <= right) {
            if (i > mid) {
                tmp[k++] = nums[j++];
            } else if (j > right) {
                tmp[k++] = nums[i++];
            } else {
                tmp[k++] = nums[i] <= nums[j] ? nums[i++] : nums[j++];
            }
        }

        for (i = 0; i < k; i++) nums[left + i] = tmp[i];
        return ans;
    }
};
// @lc code=end
