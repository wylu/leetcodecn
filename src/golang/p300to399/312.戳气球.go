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
 *
 *   采用自底向上的方法计算，首先计算区间长度为 1 的值，然后逐步扩展到 n，
 *   则 dp[1][n] 为最终结果。
 */
// @lc code=start
func maxCoins(nums []int) int {
	if nums == nil {
		return -1
	}

	n := len(nums)
	nums = append([]int{1}, nums...)
	nums = append(nums, 1)

	dp := make([][]int, n+2)
	for i := 0; i < n+2; i++ {
		dp[i] = make([]int, n+2)
	}

	for ln := 1; ln <= n; ln++ {
		for i := 1; i <= n-ln+1; i++ {
			j := i + ln - 1
			for k := i; k <= j; k++ {
				delta := nums[i-1] * nums[k] * nums[j+1]
				dp[i][j] = max312(dp[i][j], dp[i][k-1]+dp[k+1][j]+delta)
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

// Vesion 2: 记忆化递归（备忘录法）自顶向下
// func maxCoins(nums []int) int {
// 	if nums == nil {
// 		return -1
// 	}

// 	n := len(nums)
// 	nums = append([]int{1}, nums...)
// 	nums = append(nums, 1)

// 	dp := make([][]int, n+2)
// 	for i := 0; i < n+2; i++ {
// 		dp[i] = make([]int, n+2)
// 	}

// 	return burst(nums, 1, n, &dp)
// }

// func burst(nums []int, i, j int, dp *[][]int) int {
// 	if i > j {
// 		return 0
// 	}
// 	if (*dp)[i][j] > 0 {
// 		return (*dp)[i][j]
// 	}

// 	for k := i; k <= j; k++ {
// 		left := burst(nums, i, k-1, dp)
// 		right := burst(nums, k+1, j, dp)
// 		delta := nums[i-1] * nums[k] * nums[j+1]
// 		(*dp)[i][j] = max312((*dp)[i][j], left+right+delta)
// 	}

// 	return (*dp)[i][j]
// }

// func max312(x, y int) int {
// 	if x > y {
// 		return x
// 	}
// 	return y
// }

// Vesion 1: 回溯法暴破 TLE
// func maxCoins(nums []int) int {
// 	if nums == nil || len(nums) == 0 {
// 		return 0
// 	}
// 	ans := 0
// 	burst(&nums, 0, &ans)
// 	return ans
// }

// func burst(nums *[]int, coins int, ans *int) {
// 	if len(*nums) == 0 {
// 		(*ans) = max312(*ans, coins)
// 		return
// 	}

// 	for i := 0; i < len(*nums); i++ {
// 		tmp := (*nums)[i]
// 		delta := (*nums)[i]
// 		if i-1 >= 0 {
// 			delta *= (*nums)[i-1]
// 		}
// 		if i+1 < len(*nums) {
// 			delta *= (*nums)[i+1]
// 		}

// 		(*nums) = append((*nums)[:i], (*nums)[i+1:]...)
// 		burst(nums, coins+delta, ans)
// 		rear := append([]int{}, (*nums)[i:]...)
// 		(*nums) = append((*nums)[:i], tmp)
// 		(*nums) = append(*nums, rear...)
// 	}
// }

// func max312(x, y int) int {
// 	if x > y {
// 		return x
// 	}
// 	return y
// }
