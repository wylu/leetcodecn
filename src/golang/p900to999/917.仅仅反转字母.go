package p900to999

import "unicode"

/*
 * @lc app=leetcode.cn id=917 lang=golang
 *
 * [917] 仅仅反转字母
 *
 * https://leetcode-cn.com/problems/reverse-only-letters/description/
 *
 * algorithms
 * Easy (59.96%)
 * Likes:    148
 * Dislikes: 0
 * Total Accepted:    56.9K
 * Total Submissions: 94.9K
 * Testcase Example:  '"ab-cd"'
 *
 * 给你一个字符串 s ，根据下述规则反转字符串：
 *
 *
 * 所有非英文字母保留在原有位置。
 * 所有英文字母（小写或大写）位置反转。
 *
 *
 * 返回反转后的 s 。
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "ab-cd"
 * 输出："dc-ba"
 *
 *
 *
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "a-bC-dEf-ghIj"
 * 输出："j-Ih-gfE-dCba"
 *
 *
 *
 *
 *
 * 示例 3：
 *
 *
 * 输入：s = "Test1ng-Leet=code-Q!"
 * 输出："Qedo1ct-eeLg=ntse-T!"
 *
 *
 *
 *
 * 提示
 *
 *
 * 1 <= s.length <= 100
 * s 仅由 ASCII 值在范围 [33, 122] 的字符组成
 * s 不含 '\"' 或 '\\'
 *
 *
 */

/**
 * @File    :   917.仅仅反转字母.go
 * @Time    :   2022/02/23 20:02:41
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func reverseOnlyLetters(s string) string {
	ss := []byte(s)
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		for i < j && !unicode.IsLetter(rune(s[i])) {
			i++
		}
		for i < j && !unicode.IsLetter(rune(s[j])) {
			j--
		}
		if i < j {
			ss[i], ss[j] = ss[j], ss[i]
		}
	}

	return string(ss)
}

// @lc code=end
