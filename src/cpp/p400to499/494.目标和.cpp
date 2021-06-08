/*
 * @lc app=leetcode.cn id=494 lang=cpp
 *
 * [494] 目标和
 *
 * https://leetcode-cn.com/problems/target-sum/description/
 *
 * algorithms
 * Medium (46.77%)
 * Likes:    705
 * Dislikes: 0
 * Total Accepted:    91.9K
 * Total Submissions: 196.6K
 * Testcase Example:  '[1,1,1,1,1]\n3'
 *
 * 给你一个整数数组 nums 和一个整数 target 。
 * 
 * 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
 * 
 * 
 * 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
 * 
 * 
 * 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：nums = [1,1,1,1,1], target = 3
 * 输出：5
 * 解释：一共有 5 种方法让最终目标和为 3 。
 * -1 + 1 + 1 + 1 + 1 = 3
 * +1 - 1 + 1 + 1 + 1 = 3
 * +1 + 1 - 1 + 1 + 1 = 3
 * +1 + 1 + 1 - 1 + 1 = 3
 * +1 + 1 + 1 + 1 - 1 = 3
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：nums = [1], target = 1
 * 输出：1
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= nums.length <= 20
 * 0 <= nums[i] <= 1000
 * 0 <= sum(nums[i]) <= 1000
 * -1000 <= target <= 100
 * 
 * 
 */

/**
 * @File    :   494.目标和.cpp
 * @Time    :   2021/06/07 09:10:00
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：DFS 枚举
 * 
 * 方法二：动态规划
 * 记数组的元素和为 sum，添加 - 号的元素之和为 neg，则其余添加 + 的元素之和为
 * sum-neg，得到的表达式的结果为
 * 
 *     (sum-neg) - neg = sum - 2 * neg = target
 * 
 * 即
 * 
 *     neg = (sum-target) / 2​
 * 
 * 由于数组 nums 中的元素都是非负整数，neg 也必须是非负整数，所以上式成立的
 * 前提是 sum-target 是非负偶数。若不符合该条件可直接返回 0。
 * 
 * 若上式成立，问题转化成在数组 nums 中选取若干元素，使得这些元素之和等于
 * neg，计算选取元素的方案数。我们可以使用动态规划的方法求解。
 * 
 * 定义二维数组 dp，其中 dp[i][j] 表示在数组 nums 的前 i 个数中选取元素，
 * 使得这些元素之和等于 j 的方案数。假设数组 nums 的长度为 n，则最终答案为
 * dp[n][neg]。
 * 
 * 当没有任何元素可以选取时，元素和只能是 0，对应的方案数是 1，因此动态规划
 * 的边界条件是：
 * 
 *     dp[0][j] = 1,  j = 0
 *     dp[0][j] = 0,  j >= 1
 * 
 * 当 1 <= i <= n 时，对于数组 nums 中的第 i 个元素 num（i 的计数从 1 开始），
 * 遍历 0 <= j <= neg，计算 dp[i][j] 的值：
 * 
 * - 如果 j < num，则不能选 num，此时有 dp[i][j] = dp[i - 1][j]；
 * - 如果 j >= num，则如果不选 num，方案数是 dp[i - 1][j]，如果选 num，
 *   方案数是 dp[i - 1][j - num]，此时有 dp[i][j] = dp[i - 1][j] + dp[i - 1][j - num]。
 * 
 * 因此状态转移方程如下：
 * 
 *     dp[i][j] = dp[i - 1][j],  j < nums[i]
 *     dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i]],  j >= nums[i]
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        int diff = sum - target;
        if (diff < 0 || diff % 2 != 0) return 0;

        int n = nums.size(), neg = diff / 2;
        vector<vector<int>> f(n + 1, vector<int>(neg + 1));
        f[0][0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= neg; j++) {
                f[i][j] = f[i - 1][j];
                if (j >= nums[i - 1]) {
                    f[i][j] += f[i - 1][j - nums[i - 1]];
                }
            }
        }

        return f[n][neg];
    }
};
// @lc code=end

// class Solution {
// public:
//     int findTargetSumWays(vector<int>& nums, int target) {
//         int f[1010][2010] = {0};
//         int n = nums.size();
//         f[0][nums[0] + 1000] = 1;
//         f[0][-nums[0] + 1000] += 1;
//         for (int i = 1; i < n; i++) {
//             for (int j = -1000; j <= 1000; j++) {
//                 if (f[i - 1][j + 1000] > 0) {
//                     f[i][j - nums[i] + 1000] += f[i - 1][j + 1000];
//                     f[i][j + nums[i] + 1000] += f[i - 1][j + 1000];
//                 }
//             }
//         }
//         return f[n - 1][target + 1000];
//     }
// };

// class Solution {
//     int ans = 0;

// public:
//     int findTargetSumWays(vector<int>& nums, int target) {
//         dfs(nums, target, 0, 0);
//         return ans;
//     }

//     void dfs(vector<int>& nums, int target, int tot, int cur) {
//         if (cur == nums.size()) {
//             if (tot == target) ans++;
//             return;
//         }
//         dfs(nums, target, tot + nums[cur], cur + 1);
//         dfs(nums, target, tot - nums[cur], cur + 1);
//     }
// };

int main(int argc, char const* argv[]) {
    Solution solu;
    vector<int> nums = {1, 1, 1};
    cout << solu.findTargetSumWays(nums, 3) << endl;
    return 0;
}
