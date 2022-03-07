package p500to599

import (
	"math"
)

/*
 * @lc app=leetcode.cn id=504 lang=golang
 *
 * [504] 七进制数
 *
 * https://leetcode-cn.com/problems/base-7/description/
 *
 * algorithms
 * Easy (51.96%)
 * Likes:    147
 * Dislikes: 0
 * Total Accepted:    52.4K
 * Total Submissions: 100.8K
 * Testcase Example:  '100'
 *
 * 给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: num = 100
 * 输出: "202"
 *
 *
 * 示例 2:
 *
 *
 * 输入: num = -7
 * 输出: "-10"
 *
 *
 *
 *
 * 提示：
 *
 *
 * -10^7 <= num <= 10^7
 *
 *
 */

// @lc code=start
func convertToBase7(num int) string {
	if num == 0 {
		return "0"
	}
	flag := num < 0

	num = int(math.Abs(float64(num)))
	stk := []byte{}
	for num > 0 {
		stk = append(stk, '0'+byte(num%7))
		num /= 7
	}

	if flag {
		stk = append(stk, '-')
	}

	for i, j := 0, len(stk)-1; i < j; i, j = i+1, j-1 {
		stk[i], stk[j] = stk[j], stk[i]
	}
	return string(stk)
}

// @lc code=end
