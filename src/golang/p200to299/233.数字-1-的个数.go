package p200to299

/*
 * @lc app=leetcode.cn id=233 lang=golang
 *
 * [233] 数字 1 的个数
 *
 * https://leetcode-cn.com/problems/number-of-digit-one/description/
 *
 * algorithms
 * Hard (46.06%)
 * Likes:    304
 * Dislikes: 0
 * Total Accepted:    28.6K
 * Total Submissions: 62.2K
 * Testcase Example:  '13'
 *
 * 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 13
 * 输出：6
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 0
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= n <= 2 * 10^9
 *
 *
 */

/**
 * @File    :   233.数字-1-的个数.go
 * @Time    :   2021/08/13 21:24:03
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 *
 * https://blog.csdn.net/yi_Afly/article/details/52012593
 *
 * 对每一位来说，记每一位的权值为 base，位值为 weight，该位之前的数是 former，
 * 举例如下：
 *
 *		   Round   Weight   Former       Base=10
 *	         |       |        |
 * 	n   =    5       3        4
 *
 * 则有：
 *
 * 若 weight = 0，则 1 出现的次数为 round * base
 * 若 weight = 1，则 1 出现的次数为 round * base + former + 1
 * 若 weight > 1，则 1 出现的次数为 round * base + base
 *
 * 注：base=10^i，i 为当前位右边位的个数，如当前位为个位，则 i=0
 */

// @lc code=start
func countDigitOne(n int) int {
	if n < 1 {
		return 0
	}

	counter, base, round := 0, 1, n
	for round > 0 {
		weight := round % 10
		round /= 10
		counter += round * base
		if weight == 1 {
			counter += (n%base + 1)
		} else if weight > 1 {
			counter += base
		}
		base *= 10
	}

	return counter
}

// @lc code=end
