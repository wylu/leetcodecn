package p600to699

/*
 * @lc app=leetcode.cn id=673 lang=golang
 *
 * [673] 最长递增子序列的个数
 *
 * https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/description/
 *
 * algorithms
 * Medium (40.83%)
 * Likes:    423
 * Dislikes: 0
 * Total Accepted:    34.5K
 * Total Submissions: 84.5K
 * Testcase Example:  '[1,3,5,4,7]'
 *
 * 给定一个未排序的整数数组，找到最长递增子序列的个数。
 *
 * 示例 1:
 *
 *
 * 输入: [1,3,5,4,7]
 * 输出: 2
 * 解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
 *
 *
 * 示例 2:
 *
 *
 * 输入: [2,2,2,2,2]
 * 输出: 5
 * 解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
 *
 *
 * 注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
 *
 */

/**
 * @File    :   673.最长递增子序列的个数.go
 * @Time    :   2021/09/20 12:20:16
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func findNumberOfLIS(nums []int) int {
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	n := len(nums)
	f := make([][2]int, n)
	f[0] = [2]int{1, 1}
	max_len := 1

	for i := 1; i < n; i++ {
		f[i][0], f[i][1] = 1, 1
		for j := 0; j < i; j++ {
			if nums[j] < nums[i] {
				if f[j][0]+1 > f[i][0] {
					f[i][1] = f[j][1]
				} else if f[j][0]+1 == f[i][0] {
					f[i][1] += f[j][1]
				}
				f[i][0] = max(f[i][0], f[j][0]+1)
			}
		}
		max_len = max(max_len, f[i][0])
	}

	ans := 0
	for i := 0; i < n; i++ {
		if f[i][0] == max_len {
			ans += f[i][1]
		}
	}

	return ans
}

// @lc code=end
