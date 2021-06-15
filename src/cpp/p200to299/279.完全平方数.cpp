/*
 * @lc app=leetcode.cn id=279 lang=cpp
 *
 * [279] 完全平方数
 *
 * https://leetcode-cn.com/problems/perfect-squares/description/
 *
 * algorithms
 * Medium (61.02%)
 * Likes:    905
 * Dislikes: 0
 * Total Accepted:    146.1K
 * Total Submissions: 239.3K
 * Testcase Example:  '12'
 *
 * 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
 * 
 * 给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。
 * 
 * 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11
 * 不是。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：n = 12
 * 输出：3 
 * 解释：12 = 4 + 4 + 4
 * 
 * 示例 2：
 * 
 * 
 * 输入：n = 13
 * 输出：2
 * 解释：13 = 4 + 9
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= n <= 10^4
 * 
 * 
 */

/**
 * @File    :   279.完全平方数.cpp
 * @Time    :   2021/06/11 09:07:22
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 
 * 完全背包
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int numSquares(int n) {
        vector<int> nums;
        for (int i = 1, m = sqrt(n); i <= m; i++) nums.push_back(i * i);

        vector<int> f(n + 1, INT32_MAX);
        f[0] = 0;

        for (auto num : nums) {
            for (int j = num; j <= n; j++) {
                f[j] = min(f[j], f[j - num] + 1);
            }
        }

        return f[n];
    }
};
// @lc code=end

int main(int argc, char const *argv[]) {
    Solution solu;
    cout << solu.numSquares(12) << endl;
    cout << solu.numSquares(13) << endl;
    cout << solu.numSquares(1) << endl;
    cout << solu.numSquares(25) << endl;
    return 0;
}
