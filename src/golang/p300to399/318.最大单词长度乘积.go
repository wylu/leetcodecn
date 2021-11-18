package p300to399

/*
 * @lc app=leetcode.cn id=318 lang=golang
 *
 * [318] 最大单词长度乘积
 *
 * https://leetcode-cn.com/problems/maximum-product-of-word-lengths/description/
 *
 * algorithms
 * Medium (73.05%)
 * Likes:    268
 * Dislikes: 0
 * Total Accepted:    40.5K
 * Total Submissions: 55.4K
 * Testcase Example:  '["abcw","baz","foo","bar","xtfn","abcdef"]'
 *
 * 给定一个字符串数组 words，找到 length(word[i]) * length(word[j])
 * 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
 * 输出: 16
 * 解释: 这两个单词为 "abcw", "xtfn"。
 *
 * 示例 2:
 *
 *
 * 输入: ["a","ab","abc","d","cd","bcd","abcd"]
 * 输出: 4
 * 解释: 这两个单词为 "ab", "cd"。
 *
 * 示例 3:
 *
 *
 * 输入: ["a","aa","aaa","aaaa"]
 * 输出: 0
 * 解释: 不存在这样的两个单词。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 2 <= words.length <= 1000
 * 1 <= words[i].length <= 1000
 * words[i] 仅包含小写字母
 *
 *
 */

/**
 * @File    :   318.最大单词长度乘积.go
 * @Time    :   2021/11/17 19:14:32
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func maxProduct(words []string) int {
	n := len(words)
	states := make([]int, n)

	for i, word := range words {
		for _, ch := range word {
			states[i] |= 1 << (ch - 'a')
		}
	}

	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	ans := 0
	for i, x := range states {
		for j, y := range states[:i] {
			if x&y == 0 {
				ans = max(ans, len(words[i])*len(words[j]))
			}
		}
	}

	return ans
}

// @lc code=end
