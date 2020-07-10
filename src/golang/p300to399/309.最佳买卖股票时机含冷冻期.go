package p300to399

/*
 * @lc app=leetcode.cn id=309 lang=golang
 *
 * [309] 最佳买卖股票时机含冷冻期
 *
 * https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
 *
 * algorithms
 * Medium (54.04%)
 * Likes:    451
 * Dislikes: 0
 * Total Accepted:    43.5K
 * Total Submissions: 77.5K
 * Testcase Example:  '[1,2,3,0,2]'
 *
 * 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
 *
 * 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
 *
 *
 * 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
 * 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
 *
 *
 * 示例:
 *
 * 输入: [1,2,3,0,2]
 * 输出: 3
 * 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
 *
 */

/**
 * @File    :   309.最佳买卖股票时机含冷冻期.go
 * @Time    :   2020/07/10 22:20:11
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * Dynamic Programming
 *
 * State:
 *   dp[i]: 表示第 i 天结束之后的「累计最大收益」。
 *   根据题目描述，由于最多只能同时买入（持有）一支股票，并且卖出股票后有冷冻期的限制，
 *   因此会有三种不同的状态：
 *   - 目前持有一支股票，对应的「累计最大收益」记为 dp[i][0]；
 *   - 目前不持有任何股票，并且处于冷冻期中，对应的「累计最大收益」记为 dp[i][1]；
 *   - 目前不持有任何股票，并且不处于冷冻期中，对应的「累计最大收益」记为 dp[i][2]；
 *
 * Initial State:
 *   dp[0][0] = -prices[0]
 *   dp[0][1] = 0
 *   dp[0][2] = 0
 *   在第 0 天时，如果持有股票，那么只能是在第 0 天买入的，对应负收益 −prices[0]；
 *   如果不持有股票，那么收益为零。注意到第 0 天实际上是不存在处于冷冻期的情况的，
 *   但仍可以将对应的状态 dp[0][1] 置为 0，可以理解为当天买入卖出，收益自然也是 0。
 *   而且会导致下一天冷冻期，显然是只有弊端，所以只要 dp[0][1]<=0 都不会影响结果。
 *
 * State Transition:
 *   在第 i 天时，我们可以在不违反规则的前提下进行「买入」或者「卖出」操作，此时
 *   第 i 天的状态会从第 i−1 天的状态转移而来；我们也可以不进行任何操作，此时
 *   第 i 天的状态就等同于第 i-1 天的状态。以此分别对上述的三种状态进行分析：
 *
 *   - 对于 dp[i][0]，目前持有的这一支股票可以是在第 i-1 天就已经持有的，对应的
 *     状态为 dp[i−1][0]；或者是第 i 天买入的，那么第 i-1 天就不能持有股票并且
 *     不处于冷冻期中，对应的状态为 dp[i−1][2] 加上买入股票的负收益 prices[i]。
 *     因此状态转移方程为：
 *         dp[i][0] = max(dp[i-1][0], dp[i-1][2]-prices[i])
 *
 *   - 对于 dp[i][1]，在第 i 天不持有任何股票并且处于冷冻期中，说明第 i−1 天时
 *     必须持有一支股票而且卖出了股票，那么对应的状态为 dp[i−1][0] 加上卖出股票
 *     的正收益 prices[i]。因此状态转移方程为：
 *         dp[i][1] = dp[i−1][0]+prices[i]
 *
 *   - 对于 dp[i][2]，在第 i 天不持有任何股票并且不处于冷冻期，说明当天没有进行
 *     任何操作，即第 i−1 天时不持有任何股票（如果第 i−1 天处于冷冻期，对应的
 *     状态为 dp[i−1][1]；如果第 i−1 天不处于冷冻期，对应的状态为 dp[i−1][2]）。
 *     因此状态转移方程为：
 *         dp[i][2] = max(dp[i−1][1], dp[i−1][2])
 *
 * 这样我们就得到了所有的状态转移方程。如果一共有 n 天，那么最终的答案即为：
 *     max(dp[n−1][0], dp[n−1][1], dp[n−1][2])
 * 注意到如果在最后一天（第 n−1 天）结束之后，手上仍然持有股票，那么显然是没有
 * 任何意义的。因此更加精确地，最终的答案实际上是 dp[n−1][1] 和 dp[n−1][2] 中
 * 的较大值，即：
 *     max(dp[n−1][1], dp[n−1][2])
 */
// @lc code=start
func maxProfit(prices []int) int {
	if prices == nil || len(prices) == 0 {
		return 0
	}

	n := len(prices)
	dp := make([][3]int, n)
	dp[0][0] = -prices[0]
	for i := 1; i < n; i++ {
		dp[i][0] = max(dp[i-1][0], dp[i-1][2]-prices[i])
		dp[i][1] = dp[i-1][0] + prices[i]
		dp[i][2] = max(dp[i-1][1], dp[i-1][2])
	}
	return max(dp[n-1][1], dp[n-1][2])
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

// @lc code=end
