package p1to99

/*
 * @lc app=leetcode.cn id=28 lang=golang
 *
 * [28] 实现 strStr()
 *
 * https://leetcode-cn.com/problems/implement-strstr/description/
 *
 * algorithms
 * Easy (39.69%)
 * Likes:    586
 * Dislikes: 0
 * Total Accepted:    239.6K
 * Total Submissions: 603.8K
 * Testcase Example:  '"hello"\n"ll"'
 *
 * 实现 strStr() 函数。
 *
 * 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置
 * (从0开始)。如果不存在，则返回  -1。
 *
 * 示例 1:
 *
 * 输入: haystack = "hello", needle = "ll"
 * 输出: 2
 *
 *
 * 示例 2:
 *
 * 输入: haystack = "aaaaa", needle = "bba"
 * 输出: -1
 *
 *
 * 说明:
 *
 * 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
 *
 * 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
 *
 */

/**
 * @File    :   28.实现-str-str.go
 * @Time    :   2020/10/02 16:08:47
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func strStr(s string, p string) int {
	m, n := len(s), len(p)
	if n == 0 {
		return 0
	}

	fail := make([]int, n)
	fail[0] = -1
	k, j := -1, 0
	for j < n-1 {
		if k == -1 || p[k] == p[j] {
			k++
			j++
			fail[j] = k
		} else {
			k = fail[k]
		}
	}

	i := 0
	j = 0
	for i < m && j < n {
		if j == -1 || s[i] == p[j] {
			i++
			j++
		} else {
			j = fail[j]
		}
	}

	if j == n {
		return i - j
	}
	return -1
}

// @lc code=end
