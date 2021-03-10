package p100to199

/*
 * @lc app=leetcode.cn id=132 lang=golang
 *
 * [132] 分割回文串 II
 *
 * https://leetcode-cn.com/problems/palindrome-partitioning-ii/description/
 *
 * algorithms
 * Hard (48.84%)
 * Likes:    380
 * Dislikes: 0
 * Total Accepted:    38.9K
 * Total Submissions: 79.6K
 * Testcase Example:  '"aab"'
 *
 * 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
 *
 * 返回符合要求的 最少分割次数 。
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "aab"
 * 输出：1
 * 解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "a"
 * 输出：0
 *
 *
 * 示例 3：
 *
 *
 * 输入：s = "ab"
 * 输出：1
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 2000
 * s 仅由小写英文字母组成
 *
 *
 *
 *
 */

/**
 * @File    :   132.分割回文串-ii.go
 * @Time    :   2021/03/10 09:05:37
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func minCut(s string) int {
	n := len(s)
	g := make([][]bool, n)
	for i := 0; i < n; i++ {
		g[i] = make([]bool, n)
		for j := 0; j < n; j++ {
			g[i][j] = true
		}
	}

	for i := n - 1; i >= 0; i-- {
		for j := i + 1; j < n; j++ {
			g[i][j] = g[i+1][j-1] && (s[i] == s[j])
		}
	}

	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}

	f := make([]int, n)
	for i := 0; i < n; i++ {
		f[i] = n
		if g[0][i] {
			f[i] = 0
		} else {
			for j := 0; j < i; j++ {
				if g[j+1][i] {
					f[i] = min(f[i], f[j]+1)
				}
			}
		}
	}

	return f[n-1]
}

// @lc code=end
