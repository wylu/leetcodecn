/*
 * @lc app=leetcode.cn id=167 lang=cpp
 *
 * [167] 两数之和 II - 输入有序数组
 *
 * https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/description/
 *
 * algorithms
 * Easy (56.19%)
 * Likes:    359
 * Dislikes: 0
 * Total Accepted:    135.8K
 * Total Submissions: 241.6K
 * Testcase Example:  '[2,7,11,15]\n9'
 *
 * 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
 *
 * 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
 *
 * 说明:
 *
 *
 * 返回的下标值（index1 和 index2）不是从零开始的。
 * 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
 *
 *
 * 示例:
 *
 * 输入: numbers = [2, 7, 11, 15], target = 9
 * 输出: [1,2]
 * 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
 *
 */

/**
 * @File    :   167.两数之和-ii-输入有序数组.cpp
 * @Time    :   2020/07/20 23:00:05
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0, j = nums.size() - 1; i < j;) {
            if (nums[i] + nums[j] == target) {
                return {i + 1, j + 1};
            } else if (nums[i] + nums[j] < target) {
                i++;
            } else {
                j--;
            }
        }
        return {-1, -1};
    }
};
// @lc code=end
