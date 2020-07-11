package p100to199

/*
 * @lc app=leetcode.cn id=123 lang=golang
 *
 * [123] 买卖股票的最佳时机 III
 *
 * https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/description/
 *
 * algorithms
 * Hard (43.41%)
 * Likes:    439
 * Dislikes: 0
 * Total Accepted:    43.1K
 * Total Submissions: 98.6K
 * Testcase Example:  '[3,3,5,0,0,3,1,4]'
 *
 * 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
 *
 * 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
 *
 * 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
 *
 * 示例 1:
 *
 * 输入: [3,3,5,0,0,3,1,4]
 * 输出: 6
 * 解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
 * 随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
 *
 * 示例 2:
 *
 * 输入: [1,2,3,4,5]
 * 输出: 4
 * 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4
 * 。
 * 注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
 * 因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
 *
 *
 * 示例 3:
 *
 * 输入: [7,6,4,3,1]
 * 输出: 0
 * 解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
 *
 */

/**
 * @File    :   123.买卖股票的最佳时机-iii.go
 * @Time    :   2020/07/11 09:18:50
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * Dynamic Programming
 *
 * State:
 *   dp[i][k][0]: 表示第 i+1 天结束时，至今最多完成 k 笔交易，且不持有股票，
 *                所能获得的最大利润。
 *   dp[i][k][1]: 表示第 i+1 天结束时，至今最多完成 k 笔交易，且持有股票
 *                所能获得的最大利润。
 *
 * Initial State:
 *   dp[0][0][0] = 0
 *   dp[0][0][1] = Integer.MIN_VALUE
 *   dp[0][k][0] = 0, (1<= k <=2)
 *   dp[0][k][1] = -prices[0], (1<= k <=2)
 *
 * State Transition:
 *   dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i]), i > 0
 *   dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i]), i > 0
 */
// @lc code=start
func maxProfit3(prices []int) int {
	if prices == nil || len(prices) <= 1 {
		return 0
	}

	n := len(prices)
	dp := make([][3][2]int, n)
	// 使用 0 表示不可能的状态如 dp[0][0][1] ，与使用 math.MinInt32
	// 对最终结果的影响一致，实际上所有小于等于 0 的值都可用于表示这种
	// 不可能的状态。
	// dp[0][0][1] 表示第 1 天结束时，至今最多完成 0 笔交易，且持有股票，
	// 因为初始时不持有股票，所以这是一个不可能的状态。
	dp[0][1][1], dp[0][2][1] = -prices[0], -prices[0]
	for i := 1; i < n; i++ {
		for k := 1; k <= 2; k++ {
			dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
			dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])
		}
	}
	return dp[n-1][2][0]
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

// @lc code=end
