/*
 * @lc app=leetcode.cn id=231 lang=cpp
 *
 * [231] 2 的幂
 *
 * https://leetcode-cn.com/problems/power-of-two/description/
 *
 * algorithms
 * Easy (49.47%)
 * Likes:    319
 * Dislikes: 0
 * Total Accepted:    116.7K
 * Total Submissions: 236K
 * Testcase Example:  '1'
 *
 * 给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
 * 
 * 如果存在一个整数 x 使得 n == 2^x ，则认为 n 是 2 的幂次方。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：n = 1
 * 输出：true
 * 解释：2^0 = 1
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：n = 16
 * 输出：true
 * 解释：2^4 = 16
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：n = 3
 * 输出：false
 * 
 * 
 * 示例 4：
 * 
 * 
 * 输入：n = 4
 * 输出：true
 * 
 * 
 * 示例 5：
 * 
 * 
 * 输入：n = 5
 * 输出：false
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
 * 进阶：你能够不使用循环/递归解决此问题吗？
 * 
 */

/**
 * @File    :   231.2-的幂.cpp
 * @Time    :   2021/05/30 08:20:48
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
    bool isPowerOfTwo(int n) { return n > 0 && n == pow(2, int(log2(n))); }
};
// @lc code=end

// class Solution {
// public:
//     bool isPowerOfTwo(int n) { return n > 0 && (n & (n - 1)) == 0; }
// };

int main(int argc, char const *argv[]) {
    Solution solu;
    cout << solu.isPowerOfTwo(1) << endl;
    cout << solu.isPowerOfTwo(16) << endl;
    cout << solu.isPowerOfTwo(3) << endl;
    cout << solu.isPowerOfTwo(4) << endl;
    cout << solu.isPowerOfTwo(5) << endl;
    cout << solu.isPowerOfTwo(-4) << endl;
    cout << solu.isPowerOfTwo(-5) << endl;
    return 0;
}
