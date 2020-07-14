package p1to99

import "math"

/*
 * @lc app=leetcode.cn id=7 lang=golang
 *
 * [7] 整数反转
 *
 * https://leetcode-cn.com/problems/reverse-integer/description/
 *
 * algorithms
 * Easy (34.38%)
 * Likes:    2023
 * Dislikes: 0
 * Total Accepted:    402.9K
 * Total Submissions: 1.2M
 * Testcase Example:  '123'
 *
 * 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
 *
 * 示例 1:
 *
 * 输入: 123
 * 输出: 321
 *
 *
 * 示例 2:
 *
 * 输入: -123
 * 输出: -321
 *
 *
 * 示例 3:
 *
 * 输入: 120
 * 输出: 21
 *
 *
 * 注意:
 *
 * 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回
 * 0。
 *
 */

/**
 * @File    :   7.整数反转.go
 * @Time    :   2020/07/14 23:07:58
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */
// @lc code=start
func reverse(x int) int {
	res := 0
	for x != 0 {
		pop := x % 10
		x /= 10
		if res > math.MaxInt32/10 || (res == math.MaxInt32 && pop > 7) {
			return 0
		}
		if res < math.MinInt32/10 || (res == math.MinInt32 && pop < -8) {
			return 0
		}
		res = res*10 + pop
	}
	return res
}

// @lc code=end
