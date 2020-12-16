package p200to299

import "strings"

/*
 * @lc app=leetcode.cn id=290 lang=golang
 *
 * [290] 单词规律
 *
 * https://leetcode-cn.com/problems/word-pattern/description/
 *
 * algorithms
 * Easy (45.56%)
 * Likes:    276
 * Dislikes: 0
 * Total Accepted:    58.6K
 * Total Submissions: 128.5K
 * Testcase Example:  '"abba"\n"dog cat cat dog"'
 *
 * 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
 *
 * 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
 *
 * 示例1:
 *
 * 输入: pattern = "abba", str = "dog cat cat dog"
 * 输出: true
 *
 * 示例 2:
 *
 * 输入:pattern = "abba", str = "dog cat cat fish"
 * 输出: false
 *
 * 示例 3:
 *
 * 输入: pattern = "aaaa", str = "dog cat cat dog"
 * 输出: false
 *
 * 示例 4:
 *
 * 输入: pattern = "abba", str = "dog dog dog dog"
 * 输出: false
 *
 * 说明:
 * 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。
 *
 */

/**
 * @File    :   290.单词规律.go
 * @Time    :   2020/12/16 22:01:18
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func wordPattern(pattern string, s string) bool {
	words := strings.Split(s, " ")
	if len(words) != len(pattern) {
		return false
	}

	w2c := map[string]byte{}
	seen := map[byte]bool{}

	for i := 0; i < len(pattern); i++ {
		if _, ok := w2c[words[i]]; !ok {
			if seen[pattern[i]] {
				return false
			}
			w2c[words[i]] = pattern[i]
			seen[pattern[i]] = true
		} else if w2c[words[i]] != pattern[i] {
			return false
		}
	}

	return true
}

// @lc code=end
