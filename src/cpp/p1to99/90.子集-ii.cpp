/*
 * @lc app=leetcode.cn id=90 lang=cpp
 *
 * [90] 子集 II
 *
 * https://leetcode-cn.com/problems/subsets-ii/description/
 *
 * algorithms
 * Medium (62.93%)
 * Likes:    484
 * Dislikes: 0
 * Total Accepted:    86.2K
 * Total Submissions: 136.9K
 * Testcase Example:  '[1,2,2]'
 *
 * 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
 * 
 * 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
 * 
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：nums = [1,2,2]
 * 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：nums = [0]
 * 输出：[[],[0]]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= nums.length <= 10
 * -10 <= nums[i] <= 10
 * 
 * 
 * 
 * 
 */

/**
 * @File    :   90.子集-ii.cpp
 * @Time    :   2021/04/01 09:03:01
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：迭代法实现子集枚举
 * 思路
 * 
 * 考虑数组 [1,2,2]，选择前两个数，或者第一、三个数，都会得到相同的子集。
 * 
 * 也就是说，对于当前选择的数 x，若前面有与其相同的数 y，且没有选择 y，
 * 此时包含 x 的子集，必然会出现在包含 y 的所有子集中。
 * 
 * 我们可以通过判断这种情况，来避免生成重复的子集。代码实现时，可以先将
 * 数组排序；迭代时，若发现没有选择上一个数，且当前数字与上一个数相同，
 * 则可以跳过当前生成的子集。
 * 
 * 方法二：递归法实现子集枚举
 * 思路
 * 
 * 与方法一类似，在递归时，若发现没有选择上一个数，且当前数字与上一个数相同，
 * 则可以跳过当前生成的子集。
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> stk;
        sort(nums.begin(), nums.end());
        dfs(0, false, nums, stk, ans);
        return ans;
    }

    void dfs(int cur, bool choosePre, vector<int>& nums, vector<int>& stk,
             vector<vector<int>>& ans) {
        if (cur == nums.size()) {
            ans.push_back(stk);
            return;
        }

        dfs(cur + 1, false, nums, stk, ans);
        if (!choosePre && cur > 0 && nums[cur - 1] == nums[cur]) return;
        stk.push_back(nums[cur]);
        dfs(cur + 1, true, nums, stk, ans);
        stk.pop_back();
    }
};
// @lc code=end
