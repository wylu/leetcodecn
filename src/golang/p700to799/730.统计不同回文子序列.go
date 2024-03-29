package p700to799

/*
 * @lc app=leetcode.cn id=730 lang=golang
 *
 * [730] 统计不同回文子序列
 *
 * https://leetcode.cn/problems/count-different-palindromic-subsequences/description/
 *
 * algorithms
 * Hard (57.01%)
 * Likes:    198
 * Dislikes: 0
 * Total Accepted:    6.8K
 * Total Submissions: 12K
 * Testcase Example:  '"bccb"'
 *
 * 给定一个字符串 s，返回 s 中不同的非空「回文子序列」个数 。
 *
 * 通过从 s 中删除 0 个或多个字符来获得子序列。
 *
 * 如果一个字符序列与它反转后的字符序列一致，那么它是「回文字符序列」。
 *
 * 如果有某个 i , 满足 ai != bi ，则两个序列 a1, a2, ... 和 b1, b2, ... 不同。
 *
 * 注意：
 *
 *
 * 结果可能很大，你需要对 10^9 + 7 取模 。
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = 'bccb'
 * 输出：6
 * 解释：6 个不同的非空回文子字符序列分别为：'b', 'c', 'bb', 'cc', 'bcb', 'bccb'。
 * 注意：'bcb' 虽然出现两次但仅计数一次。
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
 * 输出：104860361
 * 解释：共有 3104860382 个不同的非空回文子序列，104860361 对 10^9 + 7 取模后的值。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 1000
 * s[i] 仅包含 'a', 'b', 'c' 或 'd'
 *
 *
 */

/**
 * @File    :   730.统计不同回文子序列.go
 * @Time    :   2022/06/10 09:59:41
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func countPalindromicSubsequences(s string) int {
	const MOD int = 1e9 + 7
	n := len(s)
	dp := [4][][]int{}
	for i := range dp {
		dp[i] = make([][]int, n)
		for j := range dp[i] {
			dp[i][j] = make([]int, n)
		}
	}
	for i, c := range s {
		dp[c-'a'][i][i] = 1
	}

	for sz := 2; sz <= n; sz++ {
		for i, j := 0, sz-1; j < n; i, j = i+1, j+1 {
			for k, c := 0, byte('a'); k < 4; k, c = k+1, c+1 {
				if s[i] == c && s[j] == c {
					dp[k][i][j] = (2 + dp[0][i+1][j-1] + dp[1][i+1][j-1] +
						dp[2][i+1][j-1] + dp[3][i+1][j-1]) % MOD
				} else if s[i] == c {
					dp[k][i][j] = dp[k][i][j-1]
				} else if s[j] == c {
					dp[k][i][j] = dp[k][i+1][j]
				} else {
					dp[k][i][j] = dp[k][i+1][j-1]
				}
			}
		}
	}

	ans := 0
	for _, d := range dp {
		ans += d[0][n-1]
	}

	return ans % MOD
}

// @lc code=end
