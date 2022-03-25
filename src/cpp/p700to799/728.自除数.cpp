/*
 * @lc app=leetcode.cn id=728 lang=cpp
 *
 * [728] 自除数
 *
 * https://leetcode-cn.com/problems/self-dividing-numbers/description/
 *
 * algorithms
 * Easy (74.78%)
 * Likes:    151
 * Dislikes: 0
 * Total Accepted:    37.9K
 * Total Submissions: 50.7K
 * Testcase Example:  '1\n22'
 *
 * 自除数 是指可以被它包含的每一位数整除的数。
 * 
 * 
 * 例如，128 是一个 自除数 ，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
 * 
 * 
 * 自除数 不允许包含 0 。
 * 
 * 给定两个整数 left 和 right ，返回一个列表，列表的元素是范围 [left, right] 内所有的 自除数 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：left = 1, right = 22
 * 输出：[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入：left = 47, right = 85
 * 输出：[48,55,66,77]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= left <= right <= 10^4
 * 
 * 
 */

/**
 * @File    :   728.自除数.cpp
 * @Time    :   2022/03/25 20:02:21
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
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> ans;
        for (int num = left; num <= right; num++) {
            bool flag = true;
            int cur = num;
            while (cur) {
                if ((cur % 10 == 0) || (num % (cur % 10))) {
                    flag = false;
                    break;
                }
                cur /= 10;
            }

            if (flag) ans.emplace_back(num);
        }
        return ans;
    }
};
// @lc code=end
