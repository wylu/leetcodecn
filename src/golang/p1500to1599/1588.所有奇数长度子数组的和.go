package p1500to1599

/*
 * @lc app=leetcode.cn id=1588 lang=golang
 *
 * [1588] 所有奇数长度子数组的和
 *
 * https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays/description/
 *
 * algorithms
 * Easy (82.05%)
 * Likes:    87
 * Dislikes: 0
 * Total Accepted:    25.9K
 * Total Submissions: 31.5K
 * Testcase Example:  '[1,4,2,5,3]'
 *
 * 给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。
 *
 * 子数组 定义为原数组中的一个连续子序列。
 *
 * 请你返回 arr 中 所有奇数长度子数组的和 。
 *
 *
 *
 * 示例 1：
 *
 * 输入：arr = [1,4,2,5,3]
 * 输出：58
 * 解释：所有奇数长度子数组和它们的和为：
 * [1] = 1
 * [4] = 4
 * [2] = 2
 * [5] = 5
 * [3] = 3
 * [1,4,2] = 7
 * [4,2,5] = 11
 * [2,5,3] = 10
 * [1,4,2,5,3] = 15
 * 我们将所有值求和得到 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
 *
 * 示例 2：
 *
 * 输入：arr = [1,2]
 * 输出：3
 * 解释：总共只有 2 个长度为奇数的子数组，[1] 和 [2]。它们的和为 3 。
 *
 * 示例 3：
 *
 * 输入：arr = [10,11,12]
 * 输出：66
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= arr.length <= 100
 * 1 <= arr[i] <= 1000
 *
 *
 */

/**
 * @File    :   1588.所有奇数长度子数组的和.go
 * @Time    :   2021/08/29 10:24:37
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func sumOddLengthSubarrays(arr []int) int {
	n := len(arr)
	ans := 0

	ps := make([]int, n+1)
	for i := 0; i < n; i++ {
		ps[i+1] = ps[i] + arr[i]
	}

	for size := 1; size <= n; size += 2 {
		for i := size; i < n+1; i++ {
			ans += ps[i] - ps[i-size]
		}
	}

	return ans
}

// @lc code=end
