/*
 * @lc app=leetcode.cn id=29 lang=cpp
 *
 * [29] 两数相除
 *
 * https://leetcode-cn.com/problems/divide-two-integers/description/
 *
 * algorithms
 * Medium (20.16%)
 * Likes:    448
 * Dislikes: 0
 * Total Accepted:    67.2K
 * Total Submissions: 333.2K
 * Testcase Example:  '10\n3'
 *
 * 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
 * 
 * 返回被除数 dividend 除以除数 divisor 得到的商。
 * 
 * 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) =
 * -2
 * 
 * 
 * 
 * 示例 1:
 * 
 * 输入: dividend = 10, divisor = 3
 * 输出: 3
 * 解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
 * 
 * 示例 2:
 * 
 * 输入: dividend = 7, divisor = -3
 * 输出: -2
 * 解释: 7/-3 = truncate(-2.33333..) = -2
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 被除数和除数均为 32 位有符号整数。
 * 除数不为 0。
 * 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。
 * 
 * 
 */

/**
 * @File    :   29.两数相除.cpp
 * @Time    :   2020/10/28 14:10:13
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * The key observation is that the quotient of a division is just the
 * number of times that we can subtract the divisor from the dividend
 * without making it negative.
 * 
 * Suppose dividend = 15 and divisor = 3, 15 - 3 > 0. We now try to
 * subtract more by shifting 3 to the left by 1 bit (6).
 * Since 15 - 6 > 0, shift 6 again to 12. Now 15 - 12 > 0, shift 12
 * again to 24, which is larger than 15. So we can at most subtract
 * 12 from 15. Since 12 is obtained by shifting 3 to left twice,
 * it is 1 << 2 = 4 times of 3. We add 4 to an answer variable
 * (initialized to be 0). The above process is like 15 = 3 * 4 + 3.
 * We now get part of the quotient (4), with a remaining dividend 3.
 * 
 * Then we repeat the above process by subtracting divisor = 3 from
 * the remaining dividend = 3 and obtain 0. We are done. In this
 * case, no shift happens. We simply add 1 << 0 = 1 to the answer
 * variable.
 * 
 * This is the full algorithm to perform division using bit
 * manipulations. The sign also needs to be taken into consideration.
 * And we still need to handle one overflow case: dividend = INT_MIN
 * and divisor = -1.
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == INT32_MIN && divisor == -1) return INT32_MAX;

        long ans = 0, dvd = labs(dividend), dvs = labs(divisor);
        while (dvd >= dvs) {
            long tmp = dvs, cnt = 0;
            while ((tmp << 1) <= dvd) {
                tmp <<= 1;
                cnt += 1;
            }

            dvd -= tmp;
            ans += 1 << cnt;
        }

        return dividend < 0 == divisor < 0 ? ans : -ans;
    }
};
// @lc code=end

int main(int argc, char const *argv[]) {
    Solution solu;
    cout << solu.divide(2147483647, 1) << endl;
    cout << solu.divide(-2147483648, 1) << endl;
    cout << solu.divide(-2147483648, -1) << endl;
    return 0;
}
