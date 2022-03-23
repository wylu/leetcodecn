/*
 * @lc app=leetcode.cn id=440 lang=cpp
 *
 * [440] 字典序的第K小数字
 *
 * https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order/description/
 *
 * algorithms
 * Hard (41.30%)
 * Likes:    412
 * Dislikes: 0
 * Total Accepted:    30.4K
 * Total Submissions: 73.7K
 * Testcase Example:  '13\n2'
 *
 * 给定整数 n 和 k，返回  [1, n] 中字典序第 k 小的数字。
 * 
 * 
 * 
 * 示例 1:
 * 
 * 
 * 输入: n = 13, k = 2
 * 输出: 10
 * 解释: 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入: n = 1, k = 1
 * 输出: 1
 * 
 * 
 * 
 * 
 * 提示:
 * 
 * 
 * 1 <= k <= n <= 10^9
 * 
 * 
 */

/**
 * @File    :   440.字典序的第k小数字.cpp
 * @Time    :   2022/03/23 19:58:43
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
    int findKthNumber(int n, int k) {
        int i = 1;
        k--;
        while (k > 0) {
            int steps = count(i, n);
            if (steps <= k) {
                k -= steps;
                i++;
            } else {
                i *= 10;
                k--;
            }
        }
        return i;
    }

    int count(int i, long n) {
        int cnt = 0;
        long first = i, last = i;
        while (first <= n) {
            cnt += min(last, n) - first + 1;
            first *= 10;
            last = last * 10 + 9;
        }
        return cnt;
    }
};
// @lc code=end
