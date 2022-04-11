package p300to399

/*
 * @lc app=leetcode.cn id=357 lang=golang
 *
 * [357] 统计各位数字都不同的数字个数
 *
 * https://leetcode-cn.com/problems/count-numbers-with-unique-digits/description/
 *
 * algorithms
 * Medium (58.79%)
 * Likes:    263
 * Dislikes: 0
 * Total Accepted:    52.5K
 * Total Submissions: 89.4K
 * Testcase Example:  '2'
 *
 * 给你一个整数 n ，统计并返回各位数字都不同的数字 x 的个数，其中 0 <= x < 10^n^ 。
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 2
 * 输出：91
 * 解释：答案应为除去 11、22、33、44、55、66、77、88、99 外，在 0 ≤ x < 100 范围内的所有数字。
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 0
 * 输出：1
 *
 *
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= n <= 8
 *
 *
 */

/**
 * @File    :   357.统计各位数字都不同的数字个数.go
 * @Time    :   2022/04/11 21:46:17
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func countNumbersWithUniqueDigits(n int) int {
	ans := 1
	for i := 0; i < n; i++ {
		base, delta := 9, 9
		for j := 0; j < i; j++ {
			base *= delta
			delta -= 1
		}
		ans += base
	}
	return ans
}

// @lc code=end
