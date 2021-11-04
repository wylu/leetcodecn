package p300to399

/*
 * @lc app=leetcode.cn id=367 lang=golang
 *
 * [367] 有效的完全平方数
 *
 * https://leetcode-cn.com/problems/valid-perfect-square/description/
 *
 * algorithms
 * Easy (44.71%)
 * Likes:    284
 * Dislikes: 0
 * Total Accepted:    98.6K
 * Total Submissions: 220.6K
 * Testcase Example:  '16'
 *
 * 给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
 *
 * 进阶：不要 使用任何内置的库函数，如  sqrt 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：num = 16
 * 输出：true
 *
 *
 * 示例 2：
 *
 *
 * 输入：num = 14
 * 输出：false
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= num <= 2^31 - 1
 *
 *
 */

/**
 * @File    :   367.有效的完全平方数.go
 * @Time    :   2021/11/04 13:01:20
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func isPerfectSquare(num int) bool {
	left, right := 1, num
	for left <= right {
		mid := left + (right-left)/2
		square := int64(mid * mid)
		if square == int64(num) {
			return true
		} else if square > int64(num) {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	return false
}

// @lc code=end
