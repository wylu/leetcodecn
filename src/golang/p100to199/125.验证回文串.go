package p100to199

/*
 * @lc app=leetcode.cn id=125 lang=golang
 *
 * [125] 验证回文串
 *
 * https://leetcode-cn.com/problems/valid-palindrome/description/
 *
 * algorithms
 * Easy (45.71%)
 * Likes:    248
 * Dislikes: 0
 * Total Accepted:    141.9K
 * Total Submissions: 309.5K
 * Testcase Example:  '"A man, a plan, a canal: Panama"'
 *
 * 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
 *
 * 说明：本题中，我们将空字符串定义为有效的回文串。
 *
 * 示例 1:
 *
 * 输入: "A man, a plan, a canal: Panama"
 * 输出: true
 *
 *
 * 示例 2:
 *
 * 输入: "race a car"
 * 输出: false
 *
 *
 */

/**
 * @File    :   125.验证回文串.go
 * @Time    :   2020/07/17 23:02:06
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */
// @lc code=start
func isPalindrome(s string) bool {
	if len(s) == 0 {
		return true
	}

	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		for !isAlphabetDigit(s[i]) && i < j {
			i++
		}
		for !isAlphabetDigit(s[j]) && i < j {
			j--
		}
		if toLower(s[i]) != toLower(s[j]) {
			return false
		}
	}
	return true
}

func isAlphabetDigit(ch byte) bool {
	if ('0' <= ch && ch <= '9') || ('a' <= ch && ch <= 'z') ||
		('A' <= ch && ch <= 'Z') {
		return true
	}
	return false
}

func toLower(ch byte) byte {
	if 'A' <= ch && ch <= 'Z' {
		ch += 32
	}
	return ch
}

// @lc code=end
