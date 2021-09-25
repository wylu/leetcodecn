package p500to599

/*
 * @lc app=leetcode.cn id=583 lang=golang
 *
 * [583] 两个字符串的删除操作
 *
 * https://leetcode-cn.com/problems/delete-operation-for-two-strings/description/
 *
 * algorithms
 * Medium (60.10%)
 * Likes:    255
 * Dislikes: 0
 * Total Accepted:    34.1K
 * Total Submissions: 56.8K
 * Testcase Example:  '"sea"\n"eat"'
 *
 * 给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。
 *
 *
 *
 * 示例：
 *
 * 输入: "sea", "eat"
 * 输出: 2
 * 解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 给定单词的长度不超过500。
 * 给定单词中的字符只含有小写字母。
 *
 *
 */

/**
 * @File    :   583.两个字符串的删除操作.go
 * @Time    :   2021/09/25 10:21:30
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func minDistance(word1 string, word2 string) int {
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	m, n := len(word1), len(word2)
	f := make([][]int, m+1)
	for i := 0; i < m+1; i++ {
		f[i] = make([]int, n+1)
	}

	for i, c1 := range word1 {
		for j, c2 := range word2 {
			if c1 == c2 {
				f[i+1][j+1] = f[i][j] + 1
			} else {
				f[i+1][j+1] = max(f[i+1][j], f[i][j+1])
			}
		}
	}

	return m + n - 2*f[m][n]
}

// @lc code=end
