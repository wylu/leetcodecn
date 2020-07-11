package p100to199

/*
 * @lc app=leetcode.cn id=188 lang=golang
 *
 * [188] 买卖股票的最佳时机 IV
 *
 * https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/description/
 *
 * algorithms
 * Hard (29.83%)
 * Likes:    248
 * Dislikes: 0
 * Total Accepted:    23.7K
 * Total Submissions: 79.3K
 * Testcase Example:  '2\n[2,4,1]'
 *
 * 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
 *
 * 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
 *
 * 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
 *
 * 示例 1:
 *
 * 输入: [2,4,1], k = 2
 * 输出: 2
 * 解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
 *
 *
 * 示例 2:
 *
 * 输入: [3,2,6,5,0,3], k = 2
 * 输出: 7
 * 解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4
 * 。
 * 随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
 *
 *
 */

/**
 * @File    :   188.买卖股票的最佳时机-iv.go
 * @Time    :   2020/07/11 12:15:10
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
 *   dp[0][0][0] = 0
 *   dp[0][0][1] = Integer.MIN_VALUE
 *   dp[0][j][0] = 0, (1<= j <=k)
 *   dp[0][j][1] = -prices[0], (1<= j <=k)
 *
 * State Transition:
 *   dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i]), i > 0
 *   dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i]), i > 0
 */
// @lc code=start
func maxProfit4(k int, prices []int) int {
	if prices == nil || len(prices) <= 1 || k <= 0 {
		return 0
	}

	n := len(prices)
	// 当 k >= n/2 时，最多可完成 n/2 笔有效交易（买入后至少要到第二天才卖出），
	// 此时 k 等同于无穷大，也即效果等同于可以进行无数笔交易。
	if k >= n/2 {
		// k >= n/2 时，可在 O(n) 时间内求解
		return infProfit(prices)
	}

	// k < n/2 时，时间复杂度为 O(nk)
	dp := make([][][2]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([][2]int, k+1)
	}

	for i := 1; i <= k; i++ {
		dp[0][i][1] = -prices[0]
	}

	for i := 1; i < n; i++ {
		for j := 1; j <= k; j++ {
			dp[i][j][0] = max188(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
			dp[i][j][1] = max188(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])
		}
	}
	return dp[n-1][k][0]
}

// 优化 n >= k 的情况
func infProfit(prices []int) int {
	res := 0
	for i := 1; i < len(prices); i++ {
		if prices[i] > prices[i-1] {
			res += prices[i] - prices[i-1]
		}
	}
	return res
}

func max188(x, y int) int {
	if x > y {
		return x
	}
	return y
}

// @lc code=end

// 超时，需要优化
// func maxProfit(k int, prices []int) int {
// 	if prices == nil || len(prices) <= 1 || k <= 0 {
// 		return 0
// 	}

// 	n := len(prices)
// 	// 当 k > n/2 时，最多可完成 n/2 笔有效交易（当前买入至少要到第二天才卖出）
// 	if k > n/2 {
// 		k = n / 2
// 	}

// 	dp := make([][][2]int, n)
// 	for i := 0; i < n; i++ {
// 		dp[i] = make([][2]int, k+1)
// 	}

// 	for i := 1; i <= k; i++ {
// 		dp[0][i][1] = -prices[0]
// 	}

// 	for i := 1; i < n; i++ {
// 		for j := 1; j <= k; j++ {
// 			dp[i][j][0] = max188(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
// 			dp[i][j][1] = max188(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])
// 		}
// 	}
// 	return dp[n-1][k][0]
// }

// func max188(x, y int) int {
// 	if x > y {
// 		return x
// 	}
// 	return y
// }
