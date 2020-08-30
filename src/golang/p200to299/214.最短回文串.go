package p200to299

/*
 * @lc app=leetcode.cn id=214 lang=golang
 *
 * [214] 最短回文串
 *
 * https://leetcode-cn.com/problems/shortest-palindrome/description/
 *
 * algorithms
 * Hard (32.54%)
 * Likes:    246
 * Dislikes: 0
 * Total Accepted:    19.3K
 * Total Submissions: 55.2K
 * Testcase Example:  '"aacecaaa"'
 *
 * 给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。
 *
 * 示例 1:
 *
 * 输入: "aacecaaa"
 * 输出: "aaacecaaa"
 *
 *
 * 示例 2:
 *
 * 输入: "abcd"
 * 输出: "dcbabcd"
 *
 */

/**
 * @File    :   214.最短回文串.go
 * @Time    :   2020/08/30 23:26:51
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * KMP算法
 *
 * 问题可转化为求字符串的最长前缀回文串，使用 KMP 字符串匹配算法可以避免
 * 待匹配的串回退，提高查找速度。
 *
 * 具体地，记 s' 为 s 的反序，由于 s1 是 s 的前缀，那么 s1' 就是 s' 的后缀。
 * 考虑到 s1 是一个回文串，因此 s1 = s1'，s1 同样是 s' 的后缀。
 *
 * 这样一来，我们将 s 作为模式串，s' 作为查询串进行匹配。当遍历到 s' 的末尾时，
 * 如果匹配到 s 中的第 i 个字符，那么说明 s 的前 i 个字符与 s' 的后 i 个字符
 * 相匹配（即相同），s 的前 i 个字符对应 s1，s' 的后 i 个字符对应 s1'，由于
 * s1 = s1'，因此 s1 就是一个回文串。
 *
 * 如果存在更长的回文串，那么 KMP 算法的匹配结果也会大于 i，
 * 因此 s1 就是最长的前缀回文串。
 */

// @lc code=start
func shortestPalindrome(s string) string {
	n := len(s)
	if n == 0 {
		return s
	}

	fail := make([]int, n)
	fail[0] = -1
	k, j := -1, 0
	for j < n-1 {
		if k == -1 || s[k] == s[j] {
			k++
			j++
			fail[j] = k
		} else {
			k = fail[k]
		}
	}

	best := -1
	for i := n - 1; i >= 0; i-- {
		for best != -1 && s[best+1] != s[i] {
			best = fail[best]
		}
		if s[best+1] == s[i] {
			best++
		}
	}

	add := []rune("")
	if best != -1 {
		add = []rune(s[best+1:])
	}

	for i, j := 0, len(add)-1; i < j; i, j = i+1, j-1 {
		add[i], add[j] = add[j], add[i]
	}

	return string(add) + s
}

// @lc code=end
