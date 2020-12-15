/*
 * @lc app=leetcode.cn id=738 lang=cpp
 *
 * [738] 单调递增的数字
 *
 * https://leetcode-cn.com/problems/monotone-increasing-digits/description/
 *
 * algorithms
 * Medium (45.96%)
 * Likes:    92
 * Dislikes: 0
 * Total Accepted:    9K
 * Total Submissions: 19.6K
 * Testcase Example:  '10'
 *
 * 给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。
 * 
 * （当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）
 * 
 * 示例 1:
 * 
 * 输入: N = 10
 * 输出: 9
 * 
 * 
 * 示例 2:
 * 
 * 输入: N = 1234
 * 输出: 1234
 * 
 * 
 * 示例 3:
 * 
 * 输入: N = 332
 * 输出: 299
 * 
 * 
 * 说明: N 是在 [0, 10^9] 范围内的一个整数。
 * 
 */

/**
 * @File    :   738.单调递增的数字.cpp
 * @Time    :   2020/12/15 20:20:32
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：贪心
 * 我们可以从高到低按位构造这个小于等于 N 的最大单调递增的数字。假设
 * 不考虑 N 的限制，那么对于一个长度为 n 的数字，最大单调递增的数字
 * 一定是每一位都为 9 的数字。
 * 
 * 记 strN[i] 表示数字 N 从高到低的第 i 位的数字（i 从 0 开始）。
 * 
 * 如果整个数字 N 本身已经是按位单调递增的，那么最大的数字即为 N。
 * 
 * 如果找到第一个位置 i 使得 [0,i-1] 的数位单调递增且
 * strN[i−1]>strN[i]，此时 [0,i] 的数位都与 N 的对应数位相等，
 * 仍然被 N 限制着，即我们不能随意填写 [i+1,n-1] 位置上的数字。
 * 为了得到最大的数字，我们需要解除 N 的限制，来让剩余的低位全部
 * 变成 9 ，即能得到小于 N 的最大整数。而从贪心的角度考虑，我们
 * 需要尽量让高位与 N 的对应数位相等，故尝试让 strN[i−1] 自身
 * 数位减 1。此时已经不再受 N 的限制，直接将 [i,n−1] 的位置上
 * 的数全部变为 9 即可。
 * 
 * 但这里存在一个问题：当 strN[i−1] 自身数位减 1 后可能会使得
 * strN[i−1] 和 strN[i−2] 不再满足递增的关系，因此我们需要从
 * i-1 开始递减比较相邻数位的关系，直到找到第一个位置 j 使得
 * strN[j] 自身数位减 1 后 strN[j−1] 和 strN[j] 仍然保持递增
 * 关系，或者位置 j 已经到最左边（即 j 的值为 0），此时我们将
 * [j+1,n-1] 的数全部变为 9 才能得到最终正确的答案。
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int monotoneIncreasingDigits(int N) {
        string s = to_string(N);
        int i = 1;
        while (i < s.length() && s[i - 1] <= s[i]) i++;

        if (i == s.length()) return N;

        while (i < s.length() && s[i - 1] > s[i]) {
            s[i - 1] -= 1;
            i--;
        }

        for (i += 1; i < s.length(); i++) {
            s[i] = '9';
        }

        return stoi(s);
    }
};
// @lc code=end
