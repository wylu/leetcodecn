/*
 * @lc app=leetcode.cn id=342 lang=cpp
 *
 * [342] 4的幂
 *
 * https://leetcode-cn.com/problems/power-of-four/description/
 *
 * algorithms
 * Easy (51.35%)
 * Likes:    196
 * Dislikes: 0
 * Total Accepted:    51.7K
 * Total Submissions: 100.6K
 * Testcase Example:  '16'
 *
 * 给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。
 * 
 * 整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4^x
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：n = 16
 * 输出：true
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：n = 5
 * 输出：false
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：n = 1
 * 输出：true
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * -2^31 <= n <= 2^31 - 1
 * 
 * 
 * 
 * 
 * 进阶：
 * 
 * 
 * 你能不使用循环或者递归来完成本题吗？
 * 
 * 
 */

/**
 * @File    :   342.4-的幂.cpp
 * @Time    :   2021/05/31 09:17:44
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
    bool isPowerOfFour(int n) {
        return n > 0 && (n & (n - 1)) == 0 && (n & 0xAAAAAAAA) == 0;
    }
};
// @lc code=end

// class Solution {
// public:
//     bool isPowerOfFour(int n) {
//         return n > 0 && (n & (n - 1)) == 0 && n % 3 == 1;
//     }
// };

// class Solution {
// public:
//     bool isPowerOfFour(int n) {
//         return n > 0 && (n & (n - 1)) == 0 &&
//                __builtin_popcount(n - 1) % 2 == 0;
//     }
// };

int main(int argc, char const *argv[]) {
    Solution solu;
    cout << solu.isPowerOfFour(4) << endl;
    cout << solu.isPowerOfFour(4 * 4) << endl;
    cout << solu.isPowerOfFour(4 * 4 * 4) << endl;
    cout << solu.isPowerOfFour(0) << endl;
    cout << solu.isPowerOfFour(-4) << endl;
    return 0;
}
