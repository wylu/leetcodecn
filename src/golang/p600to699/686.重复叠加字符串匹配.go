package p600to699

import "strings"

/*
 * @lc app=leetcode.cn id=686 lang=golang
 *
 * [686] 重复叠加字符串匹配
 *
 * https://leetcode-cn.com/problems/repeated-string-match/description/
 *
 * algorithms
 * Medium (38.65%)
 * Likes:    216
 * Dislikes: 0
 * Total Accepted:    33.5K
 * Total Submissions: 86.8K
 * Testcase Example:  '"abcd"\n"cdabcdab"'
 *
 * 给定两个字符串 a 和 b，寻找重复叠加字符串 a 的最小次数，使得字符串 b 成为叠加后的字符串 a 的子串，如果不存在则返回 -1。
 *
 * 注意：字符串 "abc" 重复叠加 0 次是 ""，重复叠加 1 次是 "abc"，重复叠加 2 次是 "abcabc"。
 *
 *
 *
 * 示例 1：
 *
 * 输入：a = "abcd", b = "cdabcdab"
 * 输出：3
 * 解释：a 重复叠加三遍后为 "abcdabcdabcd", 此时 b 是其子串。
 *
 *
 * 示例 2：
 *
 * 输入：a = "a", b = "aa"
 * 输出：2
 *
 *
 * 示例 3：
 *
 * 输入：a = "a", b = "a"
 * 输出：1
 *
 *
 * 示例 4：
 *
 * 输入：a = "abc", b = "wxyz"
 * 输出：-1
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= a.length <= 10^4
 * 1 <= b.length <= 10^4
 * a 和 b 由小写英文字母组成
 *
 *
 */

/**
 * @File    :   686.重复叠加字符串匹配.go
 * @Time    :   2021/12/22 18:35:42
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func repeatedStringMatch(a string, b string) int {
	m, n := len(a), len(b)
	if m > n && strings.Contains(a, b) {
		return 1
	}

	mid_begin := strings.Index(b, a)
	if mid_begin == -1 {
		if strings.Contains(a+a, b) {
			return 2
		}
		return -1
	}

	mid_end := mid_begin
	for ; mid_end+m <= n; mid_end += m {
		for i, j := 0, mid_end; i < m; i, j = i+1, j+1 {
			if a[i] != b[j] {
				return -1
			}
		}
	}

	ans := (mid_end - mid_begin) / m
	prefix, suffix := b[:mid_begin], b[mid_end:]
	if prefix != "" {
		if !strings.HasSuffix(a, prefix) {
			return -1
		}
		ans++
	}

	if suffix != "" {
		if !strings.HasPrefix(a, suffix) {
			return -1
		}
		ans++
	}

	return ans
}

// @lc code=end
