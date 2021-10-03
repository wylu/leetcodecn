package p100to199

import (
	"strconv"
)

/*
 * @lc app=leetcode.cn id=166 lang=golang
 *
 * [166] 分数到小数
 *
 * https://leetcode-cn.com/problems/fraction-to-recurring-decimal/description/
 *
 * algorithms
 * Medium (30.60%)
 * Likes:    276
 * Dislikes: 0
 * Total Accepted:    28.4K
 * Total Submissions: 93.5K
 * Testcase Example:  '1\n2'
 *
 * 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。
 *
 * 如果小数部分为循环小数，则将循环的部分括在括号内。
 *
 * 如果存在多个答案，只需返回 任意一个 。
 *
 * 对于所有给定的输入，保证 答案字符串的长度小于 10^4 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：numerator = 1, denominator = 2
 * 输出："0.5"
 *
 *
 * 示例 2：
 *
 *
 * 输入：numerator = 2, denominator = 1
 * 输出："2"
 *
 *
 * 示例 3：
 *
 *
 * 输入：numerator = 2, denominator = 3
 * 输出："0.(6)"
 *
 *
 * 示例 4：
 *
 *
 * 输入：numerator = 4, denominator = 333
 * 输出："0.(012)"
 *
 *
 * 示例 5：
 *
 *
 * 输入：numerator = 1, denominator = 5
 * 输出："0.2"
 *
 *
 *
 *
 * 提示：
 *
 *
 * -2^31 <= numerator, denominator <= 2^31 - 1
 * denominator != 0
 *
 *
 */

/**
 * @File    :   166.分数到小数.go
 * @Time    :   2021/10/03 10:20:16
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func fractionToDecimal(numerator int, denominator int) string {
	if numerator%denominator == 0 {
		return strconv.Itoa(numerator / denominator)
	}

	abs := func(x int) int {
		if x >= 0 {
			return x
		}
		return -x
	}

	seen := map[int]int{}
	stk := []byte{}

	if (numerator < 0) != (denominator < 0) {
		stk = append(stk, '-')
	}
	numerator, denominator = abs(numerator), abs(denominator)
	quotient, remainder := numerator/denominator, numerator%denominator
	stk = append(stk, []byte(strconv.Itoa(quotient))...)
	stk = append(stk, '.')

	for remainder != 0 && seen[remainder] == 0 {
		seen[remainder] = len(stk)

		cnt := -1
		for remainder < denominator {
			remainder *= 10
			cnt++
		}

		for i := 0; i < cnt; i++ {
			stk = append(stk, '0')
		}

		stk = append(stk, '0'+byte(remainder/denominator))
		remainder %= denominator
	}

	if remainder > 0 {
		idx := seen[remainder]
		return string(stk[:idx]) + "(" + string(stk[idx:]) + ")"
	}

	return string(stk)
}

// @lc code=end
