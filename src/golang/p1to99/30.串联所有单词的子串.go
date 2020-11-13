package p1to99

/*
 * @lc app=leetcode.cn id=30 lang=golang
 *
 * [30] 串联所有单词的子串
 *
 * https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/description/
 *
 * algorithms
 * Hard (32.56%)
 * Likes:    377
 * Dislikes: 0
 * Total Accepted:    48.8K
 * Total Submissions: 149.9K
 * Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
 *
 * 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
 *
 * 注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
 *
 *
 *
 * 示例 1：
 *
 * 输入：
 * ⁠ s = "barfoothefoobarman",
 * ⁠ words = ["foo","bar"]
 * 输出：[0,9]
 * 解释：
 * 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
 * 输出的顺序不重要, [9,0] 也是有效答案。
 *
 *
 * 示例 2：
 *
 * 输入：
 * ⁠ s = "wordgoodgoodgoodbestword",
 * ⁠ words = ["word","good","best","word"]
 * 输出：[]
 *
 *
 */

/**
 * @File    :   30.串联所有单词的子串.go
 * @Time    :   2020/11/13 12:39:32
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func findSubstring(s string, words []string) []int {
	cnts := map[string]int{}
	for _, word := range words {
		cnts[word]++
	}

	m, n, wl := len(s), len(words), len(words[0])
	check := func(ss string) bool {
		seen := map[string]int{}
		for i := 0; i < len(ss); i += wl {
			seen[ss[i:i+wl]]++
		}

		if len(seen) != len(cnts) {
			return false
		}
		for k, v := range seen {
			if c, ok := cnts[k]; !ok || v != c {
				return false
			}
		}
		return true
	}

	ans := []int{}
	for i := 0; i < m-n*wl+1; i++ {
		if check(s[i : i+n*wl]) {
			ans = append(ans, i)
		}
	}
	return ans
}

// @lc code=end
