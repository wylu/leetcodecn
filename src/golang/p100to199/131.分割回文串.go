package p100to199

/*
 * @lc app=leetcode.cn id=131 lang=golang
 *
 * [131] 分割回文串
 *
 * https://leetcode-cn.com/problems/palindrome-partitioning/description/
 *
 * algorithms
 * Medium (71.37%)
 * Likes:    558
 * Dislikes: 0
 * Total Accepted:    72.1K
 * Total Submissions: 101K
 * Testcase Example:  '"aab"'
 *
 * 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
 *
 * 返回 s 所有可能的分割方案。
 *
 * 示例:
 *
 * 输入: "aab"
 * 输出:
 * [
 * ⁠ ["aa","b"],
 * ⁠ ["a","a","b"]
 * ]
 *
 */

/**
 * @File    :   131.分割回文串.go
 * @Time    :   2021/03/09 23:06:34
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func partition(s string) [][]string {
	n := len(s)
	f := make([][]bool, n)
	for i := 0; i < n; i++ {
		f[i] = make([]bool, n)
		for j := 0; j < n; j++ {
			f[i][j] = true
		}
	}

	for i := n - 1; i >= 0; i-- {
		for j := i + 1; j < n; j++ {
			f[i][j] = f[i+1][j-1] && (s[i] == s[j])
		}
	}

	ans := [][]string{}
	stack := []string{}

	var dfs func(i int)
	dfs = func(i int) {
		if i == n {
			ans = append(ans, append([]string(nil), stack...))
			return
		}

		for j := i; j < n; j++ {
			if f[i][j] {
				stack = append(stack, s[i:j+1])
				dfs(j + 1)
				stack = stack[:len(stack)-1]
			}
		}
	}

	dfs(0)
	return ans
}

// @lc code=end
