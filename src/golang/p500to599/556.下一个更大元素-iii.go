package p500to599

import (
	"math"
	"strconv"
)

/*
 * @lc app=leetcode.cn id=556 lang=golang
 *
 * [556] 下一个更大元素 III
 *
 * https://leetcode.cn/problems/next-greater-element-iii/description/
 *
 * algorithms
 * Medium (34.69%)
 * Likes:    244
 * Dislikes: 0
 * Total Accepted:    23.8K
 * Total Submissions: 68.9K
 * Testcase Example:  '12'
 *
 * 给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。
 *
 * 注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 12
 * 输出：21
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 21
 * 输出：-1
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 2^31 - 1
 *
 *
 */

/**
 * @File    :   556.下一个更大元素-iii.go
 * @Time    :   2022/07/03 10:14:42
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func nextGreaterElement(n int) int {
	nums := []byte(strconv.Itoa(n))
	i := len(nums) - 2
	for i >= 0 && nums[i] >= nums[i+1] {
		i--
	}
	if i < 0 {
		return -1
	}

	j := len(nums) - 1
	for j >= 0 && nums[i] >= nums[j] {
		j--
	}

	reverse := func(a []byte) {
		for i, j := 0, len(a)-1; i < j; i, j = i+1, j-1 {
			a[i], a[j] = a[j], a[i]
		}
	}

	nums[i], nums[j] = nums[j], nums[i]
	reverse(nums[i+1:])

	ans, _ := strconv.Atoi(string(nums))
	if ans > math.MaxInt32 {
		return -1
	}
	return ans
}

// @lc code=end
