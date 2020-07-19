package p300to399

/*
 * @lc app=leetcode.cn id=312 lang=golang
 *
 * [312] 戳气球
 *
 * https://leetcode-cn.com/problems/burst-balloons/description/
 *
 * algorithms
 * Hard (61.08%)
 * Likes:    416
 * Dislikes: 0
 * Total Accepted:    21.1K
 * Total Submissions: 32.7K
 * Testcase Example:  '[3,1,5,8]'
 *
 * 有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
 *
 * 现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的
 * left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
 *
 * 求所能获得硬币的最大数量。
 *
 * 说明:
 *
 *
 * 你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
 * 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
 *
 *
 * 示例:
 *
 * 输入: [3,1,5,8]
 * 输出: 167
 * 解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
 * coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
 *
 *
 */

/**
 * @File    :   312.戳气球.go
 * @Time    :   2020/07/19 21:45:55
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * Dynamic Programming
 *
 * State:
 *   dp[i][j]: 表示戳破第 i 个到第 j 个之间的所有气球（包括 i 和 j）能够得到的
 *             最大硬币数量。
 *
 * Initial State:
 *
 * State Transition:
 *   设 k 为 i 到 j 之间最后被戳破的气球，则有：
 *   dp[i][j] = dp[i][k−1] + dp[k+1][j] + nums[i−1]∗nums[k]∗nums[j+1] (i<=k<=j)
 */
// @lc code=start
func maxCoins(nums []int) int {
	n := len(nums)
	dp := make([][]int, n+2)
	for i := 0; i < n+2; i++ {
		dp[i] = make([]int, n+2)
	}

	nums = append([]int{1}, nums...)
	nums = append(nums, 1)

	for ln := 1; ln <= n; ln++ {
		for i := 1; i <= n-ln+1; i++ {
			j := i + ln - 1
			for k := i; k <= j; k++ {
				dp[i][j] = max312(dp[i][j], dp[i][k-1]+dp[k+1][j]+nums[i-1]*nums[k]*nums[j+1])
			}
		}
	}

	return dp[1][n]
}

func max312(x, y int) int {
	if x > y {
		return x
	}
	return y
}

// @lc code=end
