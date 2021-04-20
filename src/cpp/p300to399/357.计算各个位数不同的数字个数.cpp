/*
 * @lc app=leetcode.cn id=357 lang=cpp
 *
 * [357] 计算各个位数不同的数字个数
 *
 * https://leetcode-cn.com/problems/count-numbers-with-unique-digits/description/
 *
 * algorithms
 * Medium (51.39%)
 * Likes:    132
 * Dislikes: 0
 * Total Accepted:    21K
 * Total Submissions: 40.9K
 * Testcase Example:  '2'
 *
 * 给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10^n 。
 * 
 * 示例:
 * 
 * 输入: 2
 * 输出: 91 
 * 解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。
 * 
 * 
 */

/**
 * @File    :   357.计算各个位数不同的数字个数.cpp
 * @Time    :   2021/04/20 19:32:24
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
    int countNumbersWithUniqueDigits(int n) {
        int ans = 1;
        for (int i = 0, m = min(n, 10); i < m; i++) {
            int base = 9, delta = 9;
            for (int j = 0; j < i; j++) {
                base *= delta--;
            }
            ans += base;
        }
        return ans;
    }
};
// @lc code=end

int main(int argc, char const *argv[]) {
    Solution solu;
    cout << solu.countNumbersWithUniqueDigits(0) << endl;
    cout << solu.countNumbersWithUniqueDigits(1) << endl;
    cout << solu.countNumbersWithUniqueDigits(2) << endl;
    cout << solu.countNumbersWithUniqueDigits(3) << endl;
    return 0;
}
