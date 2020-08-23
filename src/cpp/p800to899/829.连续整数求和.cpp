/*
 * @lc app=leetcode.cn id=829 lang=cpp
 *
 * [829] 连续整数求和
 *
 * https://leetcode-cn.com/problems/consecutive-numbers-sum/description/
 *
 * algorithms
 * Hard (33.49%)
 * Likes:    76
 * Dislikes: 0
 * Total Accepted:    5.1K
 * Total Submissions: 15.3K
 * Testcase Example:  '5'
 *
 * 给定一个正整数 N，试求有多少组连续正整数满足所有数字之和为 N?
 * 
 * 示例 1:
 * 
 * 
 * 输入: 5
 * 输出: 2
 * 解释: 5 = 5 = 2 + 3，共有两组连续整数([5],[2,3])求和后为 5。
 * 
 * 示例 2:
 * 
 * 
 * 输入: 9
 * 输出: 3
 * 解释: 9 = 9 = 4 + 5 = 2 + 3 + 4
 * 
 * 示例 3:
 * 
 * 
 * 输入: 15
 * 输出: 4
 * 解释: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
 * 
 * 说明: 1 <= N <= 10 ^ 9
 * 
 */

/**
 * @File    :   829.连续整数求和.cpp
 * @Time    :   2020/08/23 22:16:51
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
class Solution {
public:
    int consecutiveNumbersSum(int n) {
        int ans = 0;
        for (int i = 1; n > 0; i++) {
            if (n % i == 0) {
                ans++;
            }
            n -= i;
        }
        return ans;
    }
};
// @lc code=end
