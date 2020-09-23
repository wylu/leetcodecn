package p100to199

/*
 * @lc app=leetcode.cn id=152 lang=golang
 *
 * [152] 乘积最大子数组
 *
 * https://leetcode-cn.com/problems/maximum-product-subarray/description/
 *
 * algorithms
 * Medium (40.32%)
 * Likes:    766
 * Dislikes: 0
 * Total Accepted:    95K
 * Total Submissions: 235.6K
 * Testcase Example:  '[2,3,-2,4]'
 *
 * 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
 *
 *
 *
 * 示例 1:
 *
 * 输入: [2,3,-2,4]
 * 输出: 6
 * 解释: 子数组 [2,3] 有最大乘积 6。
 *
 *
 * 示例 2:
 *
 * 输入: [-2,0,-1]
 * 输出: 0
 * 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
 *
 */

/**
 * @File    :   152.乘积最大子数组.go
 * @Time    :   2020/09/23 14:15:48
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * Dynamic Programming
 *
 * State:
 *   dp[i][0]: 以 nums[i] 为结尾的最大乘积
 *   dp[i][1]: 以 nums[i] 为结尾的最小乘积
 *
 * State Transition：
 *   i > 0
 *   dp[i][0] = max(nums[i], dp[i-1][0] * nums[i], dp[i-1][1] * nums[i])
 *   dp[i][1] = min(nums[i], dp[i-1][0] * nums[i], dp[i-1][1] * nums[i])
 *
 * Initial State:
 *   dp[0][0] = nums[0]
 *   dp[0][1] = nums[0]
 */

// @lc code=start
func maxProduct(nums []int) int {
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}

	ans, maxVal, minVal := nums[0], nums[0], nums[0]
	for i := 1; i < len(nums); i++ {
		av, iv := nums[i]*maxVal, nums[i]*minVal
		maxVal = max(nums[i], max(av, iv))
		minVal = min(nums[i], min(av, iv))
		ans = max(ans, maxVal)
	}

	return ans
}

// @lc code=end
