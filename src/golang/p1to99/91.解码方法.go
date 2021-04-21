package p1to99

/*
 * @lc app=leetcode.cn id=91 lang=golang
 *
 * [91] 解码方法
 *
 * https://leetcode-cn.com/problems/decode-ways/description/
 *
 * algorithms
 * Medium (26.21%)
 * Likes:    673
 * Dislikes: 0
 * Total Accepted:    95.5K
 * Total Submissions: 364.3K
 * Testcase Example:  '"12"'
 *
 * 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
 *
 *
 * 'A' -> 1
 * 'B' -> 2
 * ...
 * 'Z' -> 26
 *
 *
 * 要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"111" 可以将 "1" 中的每个 "1" 映射为
 * "A" ，从而得到 "AAA" ，或者可以将 "11" 和 "1"（分别为 "K" 和 "A" ）映射为 "KA" 。注意，"06" 不能映射为 "F"
 * ，因为 "6" 和 "06" 不同。
 *
 * 给你一个只含数字的 非空 字符串 num ，请计算并返回 解码 方法的 总数 。
 *
 * 题目数据保证答案肯定是一个 32 位 的整数。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "12"
 * 输出：2
 * 解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "226"
 * 输出：3
 * 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
 *
 *
 * 示例 3：
 *
 *
 * 输入：s = "0"
 * 输出：0
 * 解释：没有字符映射到以 0 开头的数字。含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20"
 * 。由于没有字符，因此没有有效的方法对此进行解码，因为所有数字都需要映射。
 *
 *
 * 示例 4：
 *
 *
 * 输入：s = "06"
 * 输出：0
 * 解释："06" 不能映射到 "F" ，因为字符串开头的 0 无法指向一个有效的字符。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 100
 * s 只包含数字，并且可能包含前导零。
 *
 *
 */

/**
 * @File    :   91.解码方法.go
 * @Time    :   2021/04/21 22:02:43
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * Dynamic Programming
 *
 * State
 *   dp[i+1]: 表是 s[0...i] 的解码方法总数
 *
 * 分情况讨论：
 *     若 s[i] = '0'：
 *         若 s[i-1] = '1' or s[i-1] = '2，则 dp[i+1] = dp[i-1];
 *         否则 return 0；
 *     否则：
 *         若 10 < int(s[i - 1:i + 1]) <= 26，则 dp[i + 1] = dp[i] + dp[i - 1]；
 *         否则 dp[i + 1] = dp[i]
 *
 * 由分析可知，dp[i] 仅与前两项有关，故可以用单变量代替 dp[] 数组，
 * 将空集复杂度从 O(n) 降至 O(1)
 */

// @lc code=start
func numDecodings(s string) int {
	if s[0] == '0' {
		return 0
	}

	pre, cur := 1, 1

	for i, n := 1, len(s); i < n; i++ {
		next := cur
		if s[i] == '0' {
			if s[i-1] != '1' && s[i-1] != '2' {
				return 0
			}
			next = pre
		} else if s[i-1] == '1' || (s[i-1] == '2' && s[i] <= '6') {
			next = pre + cur
		}
		pre, cur = cur, next
	}

	return cur
}

// @lc code=end

// func numDecodings(s string) int {
// 	if s[0] == '0' {
// 		return 0
// 	}

// 	n := len(s)
// 	f := make([]int, n+1)
// 	f[0], f[1] = 1, 1

// 	for i := 1; i < n; i++ {
// 		if s[i] == '0' {
// 			if s[i-1] != '1' && s[i-1] != '2' {
// 				return 0
// 			}
// 			f[i+1] = f[i-1]
// 		} else {
// 			if s[i-1] == '1' || (s[i-1] == '2' && s[i] <= '6') {
// 				f[i+1] = f[i] + f[i-1]
// 			} else {
// 				f[i+1] = f[i]
// 			}
// 		}
// 	}

// 	return f[n]
// }
