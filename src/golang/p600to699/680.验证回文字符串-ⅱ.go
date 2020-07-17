package p600to699

/*
 * @lc app=leetcode.cn id=680 lang=golang
 *
 * [680] 验证回文字符串 Ⅱ
 *
 * https://leetcode-cn.com/problems/valid-palindrome-ii/description/
 *
 * algorithms
 * Easy (39.51%)
 * Likes:    231
 * Dislikes: 0
 * Total Accepted:    46K
 * Total Submissions: 116.4K
 * Testcase Example:  '"aba"'
 *
 * 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
 *
 * 示例 1:
 *
 *
 * 输入: "aba"
 * 输出: True
 *
 *
 * 示例 2:
 *
 *
 * 输入: "abca"
 * 输出: True
 * 解释: 你可以删除c字符。
 *
 *
 * 注意:
 *
 *
 * 字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
 *
 *
 */

/**
 * @File    :   680.验证回文字符串-ⅱ.go
 * @Time    :   2020/07/17 23:27:33
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */
// @lc code=start
func validPalindrome(s string) bool {
	for i, j := 0, len(s)-1; i < j; {
		if s[i] == s[j] {
			i, j = i+1, j-1
			continue
		}
		return isPalindrome(s, i+1, j) || isPalindrome(s, i, j-1)
	}
	return true
}

func isPalindrome(s string, i, j int) bool {
	for ; i < j; i, j = i+1, j-1 {
		if s[i] != s[j] {
			return false
		}
	}
	return true
}

// @lc code=end

// func validPalindrome(s string) bool {
// 	return valid(s, true)
// }

// func valid(s string, flag bool) bool {
// 	for i, j := 0, len(s)-1; i < j; {
// 		if s[i] == s[j] {
// 			i, j = i+1, j-1
// 			continue
// 		}
// 		if flag {
// 			return valid(string(s[i+1:j+1]), false) || valid(string(s[i:j]), false)
// 		}
// 		return false
// 	}
// 	return true
// }
