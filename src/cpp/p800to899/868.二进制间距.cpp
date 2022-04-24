/*
 * @lc app=leetcode.cn id=868 lang=cpp
 *
 * [868] 二进制间距
 *
 * https://leetcode-cn.com/problems/binary-gap/description/
 *
 * algorithms
 * Easy (68.87%)
 * Likes:    119
 * Dislikes: 0
 * Total Accepted:    39.7K
 * Total Submissions: 57.7K
 * Testcase Example:  '22'
 *
 * 给定一个正整数 n，找到并返回 n 的二进制表示中两个 相邻 1 之间的 最长距离 。如果不存在两个相邻的 1，返回 0 。
 * 
 * 如果只有 0 将两个 1 分隔开（可能不存在 0 ），则认为这两个 1 彼此 相邻 。两个 1
 * 之间的距离是它们的二进制表示中位置的绝对差。例如，"1001" 中的两个 1 的距离为 3 。
 * 
 * 
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：n = 22
 * 输出：2
 * 解释：22 的二进制是 "10110" 。
 * 在 22 的二进制表示中，有三个 1，组成两对相邻的 1 。
 * 第一对相邻的 1 中，两个 1 之间的距离为 2 。
 * 第二对相邻的 1 中，两个 1 之间的距离为 1 。
 * 答案取两个距离之中最大的，也就是 2 。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：n = 8
 * 输出：0
 * 解释：8 的二进制是 "1000" 。
 * 在 8 的二进制表示中没有相邻的两个 1，所以返回 0 。
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：n = 5
 * 输出：2
 * 解释：5 的二进制是 "101" 。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= n <= 10^9
 * 
 * 
 */

#include <bits/stdc++.h>
using namespace std;

/**
 * @File    :   868.二进制间距.cpp
 * @Time    :   2022/04/24 19:50:18
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
class Solution {
public:
    int binaryGap(int n) {
        int ans = 0, j = -1;
        for (int i = 0; n; i++) {
            if (n & 1) {
                if (j != -1) ans = max(ans, i - j);
                j = i;
            }
            n >>= 1;
        }
        return ans;
    }
};
// @lc code=end
