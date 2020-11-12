/*
 * @lc app=leetcode.cn id=45 lang=cpp
 *
 * [45] 跳跃游戏 II
 *
 * https://leetcode-cn.com/problems/jump-game-ii/description/
 *
 * algorithms
 * Hard (37.94%)
 * Likes:    747
 * Dislikes: 0
 * Total Accepted:    90.2K
 * Total Submissions: 237.7K
 * Testcase Example:  '[2,3,1,1,4]'
 *
 * 给定一个非负整数数组，你最初位于数组的第一个位置。
 * 
 * 数组中的每个元素代表你在该位置可以跳跃的最大长度。
 * 
 * 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
 * 
 * 示例:
 * 
 * 输入: [2,3,1,1,4]
 * 输出: 2
 * 解释: 跳到最后一个位置的最小跳跃数是 2。
 * 从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
 * 
 * 
 * 说明:
 * 
 * 假设你总是可以到达数组的最后一个位置。
 * 
 */

/**
 * @File    :   45.跳跃游戏-ii.cpp
 * @Time    :   2020/11/12 16:31:53
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 贪心：正向查找可到达的最大位置
 * 
 * 如果我们「贪心」地进行正向查找，每次找到可到达的最远位置，就可以
 * 在线性时间内得到最少的跳跃次数。
 * 
 * 例如，对于数组 [2,3,1,2,4,2,3]，初始位置是下标 0，从下标 0 出发，
 * 最远可到达下标 2。下标 0 可到达的位置中，下标 1 的值是 3，从下标
 * 1 出发可以达到更远的位置，因此第一步到达下标 1。
 * 
 * 从下标 1 出发，最远可到达下标 4。下标 1 可到达的位置中，下标 4
 * 的值是 4 ，从下标 4 出发可以达到更远的位置，因此第二步到达下标 4。
 * 
 * 在具体的实现中，我们维护当前能够到达的最大下标位置，记为边界。我们
 * 从左到右遍历数组，到达边界时，更新边界并将跳跃次数增加 1。
 * 
 * 在遍历数组时，我们不访问最后一个元素，这是因为在访问最后一个元素
 * 之前，我们的边界一定大于等于最后一个位置，否则就无法跳到最后一个
 * 位置了。如果访问最后一个元素，在边界正好为最后一个位置的情况下，
 * 我们会增加一次「不必要的跳跃次数」，因此我们不必访问最后一个元素。
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int jump(vector<int>& nums) {
        int step = 0, end = 0, most = 0, n = nums.size();
        for (int i = 0; i < n - 1; i++) {
            most = max(most, i + nums[i]);
            if (i == end) {
                step++;
                end = most;
            }
        }
        return step;
    }
};
// @lc code=end
