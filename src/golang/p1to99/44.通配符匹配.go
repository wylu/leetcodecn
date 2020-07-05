package p1to99

/*
 * @lc app=leetcode.cn id=44 lang=golang
 *
 * [44] 通配符匹配
 *
 * https://leetcode-cn.com/problems/wildcard-matching/description/
 *
 * algorithms
 * Hard (28.07%)
 * Likes:    405
 * Dislikes: 0
 * Total Accepted:    36.9K
 * Total Submissions: 126.6K
 * Testcase Example:  '"aa"\n"a"'
 *
 * 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
 *
 * '?' 可以匹配任何单个字符。
 * '*' 可以匹配任意字符串（包括空字符串）。
 *
 *
 * 两个字符串完全匹配才算匹配成功。
 *
 * 说明:
 *
 *
 * s 可能为空，且只包含从 a-z 的小写字母。
 * p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
 *
 *
 * 示例 1:
 *
 * 输入:
 * s = "aa"
 * p = "a"
 * 输出: false
 * 解释: "a" 无法匹配 "aa" 整个字符串。
 *
 * 示例 2:
 *
 * 输入:
 * s = "aa"
 * p = "*"
 * 输出: true
 * 解释: '*' 可以匹配任意字符串。
 *
 *
 * 示例 3:
 *
 * 输入:
 * s = "cb"
 * p = "?a"
 * 输出: false
 * 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
 *
 *
 * 示例 4:
 *
 * 输入:
 * s = "adceb"
 * p = "*a*b"
 * 输出: true
 * 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
 *
 *
 * 示例 5:
 *
 * 输入:
 * s = "acdcb"
 * p = "a*c?b"
 * 输出: false
 *
 */

/**
 * @File    :   44.通配符匹配.go
 * @Time    :   2020/07/05 12:18:24
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * Dynamic Programming
 *
 * State:
 *   dp[i][j]: 表示字符串 s 的前 i 个字符和模式 p 的前 j 个字符是否能匹配
 *
 * Initial State:
 *   dp[0][0] = true, 即当字符串 s 和模式 p 均为空时，匹配成功；
 *   dp[i][0] = flase, 0 <= i < len(A), 即空模式无法匹配非空字符串；
 *   dp[0][j], 0 <= j < len(B), 需要分情况讨论：因为星号才能匹配空字符串，
 *      所以只有当模式 p 的前 j 个字符均为星号时，dp[0][j] 才为 true。
 *
 * State Transition:
 *   if (s[i] == p[j] || p[j] == '?') dp[i][j] = dp[i-1][j-1];
 *   else if (p[j] == '*') dp[i][j] = dp[i][j-1] || dp[i-1][j];
 *   else dp[i][j] = false
 *
 * 考虑模式 p 的第 j 个字符 p[j]，与之对应的是字符串 s 中的第 i 个字符 s[i]:
 * - 如果 p[j] 是小写字母，那么 s[i] 必须为相同的小写字母，状态转移方程为：
 *       dp[i][j] = (s[i] == p[j]) && dp[i-1][j-1]
 * - 如果 p[j] 是 '?'，那么对 s[i] 没有任何要求，状态转移方程为：
 *       dp[i][j] = dp[i-1][j-1]
 * - 如果 p[j] 是 '*'，那么同样对 s[i] 没有任何要求，但是 '*' 可以匹配 0 或
 *   任意多个小写字母，因此状态转移方程分为两种情况，即使用或不使用这个 '*'：
 *       dp[i][j] = dp[i][j-1] || dp[i-1][j]
 *   不使用这个 '*'，那么就会从 dp[i][j-1] 转移而来；如果使用这个 '*'，那么
 *   就会从 dp[i-1][j] 转移而来。
 */
// @lc code=start
func isMatch(s string, p string) bool {
	ls, lp := len(s), len(p)
	dp := make([][]bool, ls+1)
	for i := 0; i <= ls; i++ {
		dp[i] = make([]bool, lp+1)
	}
	dp[0][0] = true
	for i := 1; i <= lp; i++ {
		if p[i-1] != '*' {
			break
		}
		dp[0][i] = true
	}

	for i := 1; i <= ls; i++ {
		for j := 1; j <= lp; j++ {
			if s[i-1] == p[j-1] || p[j-1] == '?' {
				dp[i][j] = dp[i-1][j-1]
			} else if p[j-1] == '*' {
				dp[i][j] = dp[i][j-1] || dp[i-1][j]
			}
		}
	}

	return dp[ls][lp]
}

// @lc code=end
