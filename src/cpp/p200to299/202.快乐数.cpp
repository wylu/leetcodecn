/*
 * @lc app=leetcode.cn id=202 lang=cpp
 *
 * [202] 快乐数
 *
 * https://leetcode-cn.com/problems/happy-number/description/
 *
 * algorithms
 * Easy (60.86%)
 * Likes:    492
 * Dislikes: 0
 * Total Accepted:    109.5K
 * Total Submissions: 180K
 * Testcase Example:  '19'
 *
 * 编写一个算法来判断一个数 n 是不是快乐数。
 * 
 * 「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到
 * 1。如果 可以变为  1，那么这个数就是快乐数。
 * 
 * 如果 n 是快乐数就返回 True ；不是，则返回 False 。
 * 
 * 
 * 
 * 示例：
 * 
 * 输入：19
 * 输出：true
 * 解释：
 * 1^2 + 9^2 = 82
 * 8^2 + 2^2 = 68
 * 6^2 + 8^2 = 100
 * 1^2 + 0^2 + 0^2 = 1
 * 
 * 
 */

/**
 * @File    :   202.快乐数.cpp
 * @Time    :   2020/12/03 14:27:07
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
    bool isHappy(int n) {
        unordered_set<long> seen;
        while (n != 1 && seen.count(n) == 0) {
            seen.insert(n);
            n = happy(n);
        }
        return n == 1;
    }

    int happy(int n) {
        int res = 0;
        while (n) {
            int d = n % 10;
            res += d * d;
            n /= 10;
        }
        return res;
    }
};
// @lc code=end
