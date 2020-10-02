package p200to299

/*
 * @lc app=leetcode.cn id=209 lang=golang
 *
 * [209] 长度最小的子数组
 *
 * https://leetcode-cn.com/problems/minimum-size-subarray-sum/description/
 *
 * algorithms
 * Medium (44.37%)
 * Likes:    463
 * Dislikes: 0
 * Total Accepted:    90.5K
 * Total Submissions: 203.9K
 * Testcase Example:  '7\n[2,3,1,2,4,3]'
 *
 * 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续
 * 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
 *
 *
 *
 * 示例：
 *
 * 输入：s = 7, nums = [2,3,1,2,4,3]
 * 输出：2
 * 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
 *
 *
 *
 *
 * 进阶：
 *
 *
 * 如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
 *
 *
 */

/**
 * @File    :   209.长度最小的子数组.go
 * @Time    :   2020/10/02 17:48:05
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func minSubArrayLen(s int, nums []int) int {
	n := len(nums)
	if n == 0 {
		return 0
	}

	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}

	ans := n + 1
	i, j, tot := 0, 0, 0

	for j < n {
		tot += nums[j]
		for tot >= s {
			ans = min(ans, j-i+1)
			tot -= nums[i]
			i++
		}
		j++
	}

	if ans == n+1 {
		return 0
	}
	return ans
}

// @lc code=end
