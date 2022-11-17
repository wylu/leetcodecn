package p700to799

/*
 * @lc app=leetcode.cn id=792 lang=golang
 *
 * [792] 匹配子序列的单词数
 *
 * https://leetcode.cn/problems/number-of-matching-subsequences/description/
 *
 * algorithms
 * Medium (50.36%)
 * Likes:    336
 * Dislikes: 0
 * Total Accepted:    32.3K
 * Total Submissions: 64.1K
 * Testcase Example:  '"abcde"\n["a","bb","acd","ace"]'
 *
 * 给定字符串 s 和字符串数组 words, 返回  words[i] 中是s的子序列的单词个数 。
 *
 * 字符串的 子序列 是从原始字符串中生成的新字符串，可以从中删去一些字符(可以是none)，而不改变其余字符的相对顺序。
 *
 *
 * 例如， “ace” 是 “abcde” 的子序列。
 *
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: s = "abcde", words = ["a","bb","acd","ace"]
 * 输出: 3
 * 解释: 有三个是 s 的子序列的单词: "a", "acd", "ace"。
 *
 *
 * Example 2:
 *
 *
 * 输入: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
 * 输出: 2
 *
 *
 *
 *
 * 提示:
 *
 *
 * 1 <= s.length <= 5 * 10^4
 * 1 <= words.length <= 5000
 * 1 <= words[i].length <= 50
 * words[i]和 s 都只由小写字母组成。
 *
 * ​​​​
 */

/**
 * @File    :   792.匹配子序列的单词数.go
 * @Time    :   2022/11/17 22:01:35
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func numMatchingSubseq(s string, words []string) int {
	p := [128][][2]int{}
	for i, w := range words {
		p[w[0]] = append(p[w[0]], [2]int{i, 0})
	}

	ans := 0
	for _, c := range s {
		q := p[c]
		p[c] = [][2]int{}
		for _, v := range q {
			i, j := v[0], v[1]+1
			if j == len(words[i]) {
				ans++
			} else {
				p[words[i][j]] = append(p[words[i][j]], [2]int{i, j})
			}
		}
	}

	return ans
}

// @lc code=end
