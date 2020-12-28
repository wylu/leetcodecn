/*
 * @lc app=leetcode.cn id=188 lang=cpp
 *
 * [188] 买卖股票的最佳时机 IV
 *
 * https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/description/
 *
 * algorithms
 * Hard (34.21%)
 * Likes:    390
 * Dislikes: 0
 * Total Accepted:    50.1K
 * Total Submissions: 146.4K
 * Testcase Example:  '2\n[2,4,1]'
 *
 * 给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
 * 
 * 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
 * 
 * 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：k = 2, prices = [2,4,1]
 * 输出：2
 * 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
 * 
 * 示例 2：
 * 
 * 
 * 输入：k = 2, prices = [3,2,6,5,0,3]
 * 输出：7
 * 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
 * ⁠    随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 =
 * 3 。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 0 <= k <= 10^9
 * 0 <= prices.length <= 1000
 * 0 <= prices[i] <= 1000
 * 
 * 
 */

/**
 * @File    :   188.买卖股票的最佳时机-iv.cpp
 * @Time    :   2020/12/28 20:19:23
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * Dynamic Programming
 * 
 * State:
 *   dp[i][j][0]: 表示第 i+1 天结束时，至今最多完成 j 笔交易，且不持有股票，
 *                所能获得的最大利润。
 *   dp[i][j][1]: 表示第 i+1 天结束时，至今最多完成 j 笔交易，且持有股票
 *                所能获得的最大利润。
 * 
 * Initial State:
 *   dp[0][j][0] = 0, (0<= j <=k)
 *   dp[0][j][1] = -prices[0], (0<= j <=k)
 * 
 * State Transition:
 *   dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i]), i > 0
 *   dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i]), i > 0
 */

#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int n = prices.size();
        if (k <= 0 || n <= 1) return 0;

        if (k >= n / 2) return maxInfinite(prices);

        vector<vector<vector<int>>> f(
            n, vector<vector<int>>(k + 1, vector<int>(2)));
        for (int j = 0; j <= k; j++) f[0][j][1] = -prices[0];

        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= k; j++) {
                f[i][j][0] = max(f[i - 1][j][0], f[i - 1][j][1] + prices[i]);
                f[i][j][1] =
                    max(f[i - 1][j][1], f[i - 1][j - 1][0] - prices[i]);
            }
        }

        return f[n - 1][k][0];
    }

    int maxInfinite(vector<int>& prices) {
        int ans = 0;
        for (int i = 1, n = prices.size(); i < n; i++) {
            if (prices[i] - prices[i - 1] > 0) {
                ans += prices[i] - prices[i - 1];
            }
        }
        return ans;
    }
};
// @lc code=end

int main(int argc, char const* argv[]) {
    Solution solu;
    vector<int> prices = {3, 2, 6, 5, 0, 3};
    cout << solu.maxProfit(2, prices) << endl;
    return 0;
}
