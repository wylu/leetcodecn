/*
 * @lc app=leetcode.cn id=172 lang=cpp
 *
 * [172] 阶乘后的零
 *
 * https://leetcode-cn.com/problems/factorial-trailing-zeroes/description/
 *
 * algorithms
 * Medium (46.59%)
 * Likes:    604
 * Dislikes: 0
 * Total Accepted:    116.2K
 * Total Submissions: 249.5K
 * Testcase Example:  '3'
 *
 * 给定一个整数 n ，返回 n! 结果中尾随零的数量。
 * 
 * 提示 n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：n = 3
 * 输出：0
 * 解释：3! = 6 ，不含尾随 0
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：n = 5
 * 输出：1
 * 解释：5! = 120 ，有一个尾随 0
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：n = 0
 * 输出：0
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 0 <= n <= 10^4
 * 
 * 
 * 
 * 
 * 进阶：你可以设计并实现对数时间复杂度的算法来解决此问题吗？
 * 
 */

/**
 * @File    :   172.阶乘后的零.cpp
 * @Time    :   2022/03/25 11:20:24
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
    int trailingZeroes(int n) {
        int ans = 0, exp = 5;
        while (n / exp) {
            ans += n / exp;
            exp *= 5;
        }
        return ans;
    }
};
// @lc code=end
