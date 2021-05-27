/*
 * @lc app=leetcode.cn id=461 lang=cpp
 *
 * [461] 汉明距离
 *
 * https://leetcode-cn.com/problems/hamming-distance/description/
 *
 * algorithms
 * Easy (80.64%)
 * Likes:    465
 * Dislikes: 0
 * Total Accepted:    139.1K
 * Total Submissions: 172.5K
 * Testcase Example:  '1\n4'
 *
 * 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
 * 
 * 给出两个整数 x 和 y，计算它们之间的汉明距离。
 * 
 * 注意：
 * 0 ≤ x, y < 2^31.
 * 
 * 示例:
 * 
 * 
 * 输入: x = 1, y = 4
 * 
 * 输出: 2
 * 
 * 解释:
 * 1   (0 0 0 1)
 * 4   (0 1 0 0)
 * ⁠      ↑   ↑
 * 
 * 上面的箭头指出了对应二进制位不同的位置。
 * 
 * 
 */

/**
 * @File    :   461.汉明距离.cpp
 * @Time    :   2021/05/27 19:12:01
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
    int hammingDistance(int x, int y) {
        int z = x ^ y, ans = 0;
        while (z) {
            ans++;
            z &= (z - 1);
        }
        return ans;
    }
};
// @lc code=end

// class Solution {
// public:
//     int hammingDistance(int x, int y) { return __builtin_popcount(x ^ y); }
// };
