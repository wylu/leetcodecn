package p600to699

import "sort"

/*
 * @lc app=leetcode.cn id=698 lang=golang
 *
 * [698] 划分为k个相等的子集
 *
 * https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/description/
 *
 * algorithms
 * Medium (42.11%)
 * Likes:    792
 * Dislikes: 0
 * Total Accepted:    80K
 * Total Submissions: 190K
 * Testcase Example:  '[4,3,2,3,5,2,1]\n4'
 *
 * 给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
 * 输出： True
 * 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
 *
 * 示例 2:
 *
 *
 * 输入: nums = [1,2,3,4], k = 3
 * 输出: false
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= k <= len(nums) <= 16
 * 0 < nums[i] < 10000
 * 每个元素的频率在 [1,4] 范围内
 *
 *
 */

/**
 * @File    :   698.划分为k个相等的子集.go
 * @Time    :   2022/09/20 21:34:25
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func canPartitionKSubsets(nums []int, k int) bool {
	sort.Ints(nums)
	n, total := len(nums), 0
	for _, num := range nums {
		total += num
	}

	d, r := total/k, total%k
	if nums[n-1] > d || r != 0 {
		return false
	}

	dp := make([]bool, 1<<n)
	for i := range dp {
		dp[i] = true
	}

	var dfs func(int, int) bool
	dfs = func(s, p int) bool {
		if s == 0 {
			return true
		}
		if !dp[s] {
			return false
		}
		dp[s] = false
		for i, num := range nums {
			if num+p > d {
				break
			}
			if s&(1<<i) > 0 && dfs(s^(1<<i), (p+num)%d) {
				return true
			}
		}
		return false
	}
	return dfs(1<<n-1, 0)
}

// @lc code=end
