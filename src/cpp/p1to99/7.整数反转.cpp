/*
 * @lc app=leetcode.cn id=7 lang=cpp
 *
 * [7] 整数反转
 *
 * https://leetcode-cn.com/problems/reverse-integer/description/
 *
 * algorithms
 * Easy (35.17%)
 * Likes:    2750
 * Dislikes: 0
 * Total Accepted:    677.5K
 * Total Submissions: 1.9M
 * Testcase Example:  '123'
 *
 * 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
 * 
 * 如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。
 * 假设环境不允许存储 64 位整数（有符号或无符号）。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：x = 123
 * 输出：321
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：x = -123
 * 输出：-321
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：x = 120
 * 输出：21
 * 
 * 
 * 示例 4：
 * 
 * 
 * 输入：x = 0
 * 输出：0
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * -2^31 <= x <= 2^31 - 1
 * 
 * 
 */

/**
 * @File    :   7.整数反转.cpp
 * @Time    :   2021/05/03 11:32:58
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
    int reverse(int x) {
        int ans = 0;
        while (x) {
            int digit = x % 10;
            x /= 10;

            if (ans > INT32_MAX / 10 || (ans == INT32_MAX / 10 && digit > 7))
                return 0;
            if (ans < INT32_MIN / 10 || (ans == INT32_MIN / 10 && digit < -8))
                return 0;

            ans = ans * 10 + digit;
        }
        return ans;
    }
};
// @lc code=end

int main(int argc, char const *argv[]) {
    Solution solu;
    cout << solu.reverse(0) << endl;
    cout << solu.reverse(-1) << endl;
    cout << solu.reverse(1) << endl;
    cout << solu.reverse(2147483647) << endl;
    cout << solu.reverse(-2147483648) << endl;
    return 0;
}
