package p900to999

/*
 * @lc app=leetcode.cn id=926 lang=golang
 *
 * [926] 将字符串翻转到单调递增
 *
 * https://leetcode-cn.com/problems/flip-string-to-monotone-increasing/description/
 *
 * algorithms
 * Medium (52.18%)
 * Likes:    111
 * Dislikes: 0
 * Total Accepted:    6.7K
 * Total Submissions: 12.9K
 * Testcase Example:  '"00110"'
 *
 * 如果一个由 '0' 和 '1' 组成的字符串，是以一些 '0'（可能没有 '0'）后面跟着一些 '1'（也可能没有
 * '1'）的形式组成的，那么该字符串是单调递增的。
 *
 * 我们给出一个由字符 '0' 和 '1' 组成的字符串 S，我们可以将任何 '0' 翻转为 '1' 或者将 '1' 翻转为 '0'。
 *
 * 返回使 S 单调递增的最小翻转次数。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入："00110"
 * 输出：1
 * 解释：我们翻转最后一位得到 00111.
 *
 *
 * 示例 2：
 *
 *
 * 输入："010110"
 * 输出：2
 * 解释：我们翻转得到 011111，或者是 000111。
 *
 *
 * 示例 3：
 *
 *
 * 输入："00011000"
 * 输出：2
 * 解释：我们翻转得到 00000000。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= S.length <= 20000
 * S 中只包含字符 '0' 和 '1'
 *
 *
 */

/**
 * @File    :   926.将字符串翻转到单调递增.go
 * @Time    :   2022/06/11 10:55:14
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func minFlipsMonoIncr(s string) int {
	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}

	d0, d1 := 0, 0
	for _, c := range s {
		c0, c1 := d0, min(d0, d1)
		if c == '1' {
			c0++
		} else {
			c1++
		}
		d0, d1 = c0, c1
	}

	return min(d0, d1)
}

// @lc code=end

// func minFlipsMonoIncr(s string) int {
// 	n := len(s)
// 	ps := make([]int, n+1)
// 	for i, ch := range s {
// 		ps[i+1] = ps[i]
// 		if ch == '1' {
// 			ps[i+1]++
// 		}
// 	}

// 	min := func(x, y int) int {
// 		if x < y {
// 			return x
// 		}
// 		return y
// 	}

// 	ans := n
// 	for i := 0; i <= n; i++ {
// 		ans = min(ans, ps[i]+(n-i-(ps[n]-ps[i])))
// 	}

// 	return ans
// }
