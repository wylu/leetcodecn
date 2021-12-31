package p500to599

import "math"

/*
 * @lc app=leetcode.cn id=507 lang=golang
 *
 * [507] 完美数
 *
 * https://leetcode-cn.com/problems/perfect-number/description/
 *
 * algorithms
 * Easy (47.96%)
 * Likes:    154
 * Dislikes: 0
 * Total Accepted:    56K
 * Total Submissions: 116.9K
 * Testcase Example:  '28'
 *
 * 对于一个 正整数，如果它和除了它自身以外的所有 正因子 之和相等，我们称它为 「完美数」。
 *
 * 给定一个 整数 n， 如果是完美数，返回 true，否则返回 false
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：num = 28
 * 输出：true
 * 解释：28 = 1 + 2 + 4 + 7 + 14
 * 1, 2, 4, 7, 和 14 是 28 的所有正因子。
 *
 * 示例 2：
 *
 *
 * 输入：num = 6
 * 输出：true
 *
 *
 * 示例 3：
 *
 *
 * 输入：num = 496
 * 输出：true
 *
 *
 * 示例 4：
 *
 *
 * 输入：num = 8128
 * 输出：true
 *
 *
 * 示例 5：
 *
 *
 * 输入：num = 2
 * 输出：false
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= num <= 10^8
 *
 *
 */

/**
 * @File    :   507.完美数.go
 * @Time    :   2021/12/31 20:14:48
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func checkPerfectNumber(num int) bool {
	total := 0
	n := int(math.Floor(math.Sqrt(float64(num))))
	for i := 1; i <= n; i++ {
		if num%i == 0 {
			total += i + num/i
		}
	}
	return total-num == num && num != 1
	// return num == 6 || num == 28 || num == 496 || num == 8128 || num == 33550336
}

// @lc code=end
