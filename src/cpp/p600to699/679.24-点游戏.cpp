/*
 * @lc app=leetcode.cn id=679 lang=cpp
 *
 * [679] 24 点游戏
 *
 * https://leetcode-cn.com/problems/24-game/description/
 *
 * algorithms
 * Hard (44.76%)
 * Likes:    199
 * Dislikes: 0
 * Total Accepted:    14.8K
 * Total Submissions: 27.8K
 * Testcase Example:  '[4,1,8,7]'
 *
 * 你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。
 * 
 * 示例 1:
 * 
 * 输入: [4, 1, 8, 7]
 * 输出: True
 * 解释: (8-4) * (7-1) = 24
 * 
 * 
 * 示例 2:
 * 
 * 输入: [1, 2, 1, 2]
 * 输出: False
 * 
 * 
 * 注意:
 * 
 * 
 * 除法运算符 / 表示实数除法，而不是整数除法。例如 4 / (1 - 2/3) = 12 。
 * 每个运算符对两个数进行运算。特别是我们不能用 - 作为一元运算符。例如，[1, 1, 1, 1] 作为输入时，表达式 -1 - 1 - 1 - 1
 * 是不允许的。
 * 你不能将数字连接在一起。例如，输入为 [1, 2, 1, 2] 时，不能写成 12 + 12 。
 * 
 * 
 */

/**
 * @File    :   679.24-点游戏.cpp
 * @Time    :   2020/08/27 22:33:49
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
    double EPSILON = 1e-6;
    int ADD = 0, MUL = 1, SUB = 2, DIV = 3;

    bool judgePoint24(vector<int>& nums) {
        if (nums.size() == 0) {
            return false;
        }
        vector<double> newNums;
        for (auto num : nums) {
            newNums.emplace_back(num);
        }
        return dfs(newNums);
    }

    bool dfs(vector<double>& nums) {
        if (nums.size() == 1) {
            return fabs(nums[0] - 24) < EPSILON;
        }
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    continue;
                }
                vector<double> newNums = {};
                for (int k = 0; k < n; k++) {
                    if (k != i && k != j) {
                        newNums.emplace_back(nums[k]);
                    }
                }
                for (int k = 0; k < 4; k++) {
                    if (k < 2 && i > j) {
                        continue;
                    }
                    if (k == ADD) {
                        newNums.emplace_back(nums[i] + nums[j]);
                    } else if (k == MUL) {
                        newNums.emplace_back(nums[i] * nums[j]);
                    } else if (k == SUB) {
                        newNums.emplace_back(nums[i] - nums[j]);
                    } else if (k == DIV) {
                        if (fabs(nums[j]) < EPSILON) {
                            continue;
                        }
                        newNums.emplace_back(nums[i] / nums[j]);
                    }
                    if (dfs(newNums)) {
                        return true;
                    }
                    newNums.pop_back();
                }
            }
        }
        return false;
    }
};
// @lc code=end
