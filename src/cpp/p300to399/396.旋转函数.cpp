/*
 * @lc app=leetcode.cn id=396 lang=cpp
 *
 * [396] 旋转函数
 *
 * https://leetcode-cn.com/problems/rotate-function/description/
 *
 * algorithms
 * Medium (49.12%)
 * Likes:    134
 * Dislikes: 0
 * Total Accepted:    18K
 * Total Submissions: 36.7K
 * Testcase Example:  '[4,3,2,6]'
 *
 * 给定一个长度为 n 的整数数组 nums 。
 * 
 * 假设 arrk 是数组 nums 顺时针旋转 k 个位置后的数组，我们定义 nums 的 旋转函数  F 为：
 * 
 * 
 * F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1]
 * 
 * 
 * 返回 F(0), F(1), ..., F(n-1)中的最大值 。
 * 
 * 生成的测试用例让答案符合 32 位 整数。
 * 
 * 
 * 
 * 示例 1:
 * 
 * 
 * 输入: nums = [4,3,2,6]
 * 输出: 26
 * 解释:
 * F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
 * F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
 * F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
 * F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
 * 所以 F(0), F(1), F(2), F(3) 中的最大值是 F(3) = 26 。
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入: nums = [100]
 * 输出: 0
 * 
 * 
 * 
 * 
 * 提示:
 * 
 * 
 * n == nums.length
 * 1 <= n <= 10^5
 * -100 <= nums[i] <= 100
 * 
 * 
 */

#include <bits/stdc++.h>
using namespace std;

/**
 * @File    :   396.旋转函数.cpp
 * @Time    :   2022/04/22 10:04:10
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
class Solution {
public:
    int maxRotateFunction(vector<int>& nums) {
        int n = nums.size(), cur = 0, total = 0;
        for (int i = 0; i < n; i++) {
            cur += i * nums[i];
            total += nums[i];
        }

        int ans = cur;
        // printf("i: 0, cur: %d\n", cur);
        for (int i = 1; i < n; i++) {
            int sub = total - nums[i - 1];
            int add = (n - 1) * nums[i - 1];
            // printf("i: %d, sub: %d, add: %d\n", i, sub, add);
            cur += add - sub;
            ans = max(ans, cur);
            // printf("i: %d, cur: %d\n", i, cur);
        }

        return ans;
    }
};
// @lc code=end
