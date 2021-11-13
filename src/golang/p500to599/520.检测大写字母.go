package p500to599

import "unicode"

/*
 * @lc app=leetcode.cn id=520 lang=golang
 *
 * [520] 检测大写字母
 *
 * https://leetcode-cn.com/problems/detect-capital/description/
 *
 * algorithms
 * Easy (57.50%)
 * Likes:    175
 * Dislikes: 0
 * Total Accepted:    58.9K
 * Total Submissions: 102.5K
 * Testcase Example:  '"USA"'
 *
 * 我们定义，在以下情况时，单词的大写用法是正确的：
 *
 *
 * 全部字母都是大写，比如 "USA" 。
 * 单词中所有字母都不是大写，比如 "leetcode" 。
 * 如果单词不只含有一个字母，只有首字母大写， 比如 "Google" 。
 *
 *
 * 给你一个字符串 word 。如果大写用法正确，返回 true ；否则，返回 false 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：word = "USA"
 * 输出：true
 *
 *
 * 示例 2：
 *
 *
 * 输入：word = "FlaG"
 * 输出：false
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= word.length <= 100
 * word 由小写和大写英文字母组成
 *
 *
 */

/**
 * @File    :   520.检测大写字母.go
 * @Time    :   2021/11/13 19:22:48
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start

func detectCapitalUse(word string) bool {
	// 若第 1 个字母为小写，则需额外判断第 2 个字母是否为小写
	if len(word) >= 2 && unicode.IsLower(rune(word[0])) && unicode.IsUpper(rune(word[1])) {
		return false
	}

	// 无论第 1 个字母是否大写，其他字母必须与第 2 个字母的大小写相同
	for i := 2; i < len(word); i++ {
		if unicode.IsLower(rune(word[i])) != unicode.IsLower(rune(word[1])) {
			return false
		}
	}
	return true
}

// @lc code=end

// func detectCapitalUse(word string) bool {
// 	cnt, n := 0, len(word)
// 	for i := 0; i < n; i++ {
// 		if word[i] >= 'A' && word[i] <= 'Z' {
// 			cnt++
// 		}
// 	}

// 	return cnt == 0 || cnt == n || (cnt == 1 && word[0] >= 'A' && word[0] <= 'Z')
// }
