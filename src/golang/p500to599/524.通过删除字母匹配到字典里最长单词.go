package p500to599

/*
 * @lc app=leetcode.cn id=524 lang=golang
 *
 * [524] 通过删除字母匹配到字典里最长单词
 *
 * https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/description/
 *
 * algorithms
 * Medium (47.83%)
 * Likes:    177
 * Dislikes: 0
 * Total Accepted:    43.3K
 * Total Submissions: 90.5K
 * Testcase Example:  '"abpcplea"\n["ale","apple","monkey","plea"]'
 *
 * 给你一个字符串 s 和一个字符串数组 dictionary 作为字典，找出并返回字典中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。
 *
 * 如果答案不止一个，返回长度最长且字典序最小的字符串。如果答案不存在，则返回空字符串。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
 * 输出："apple"
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "abpcplea", dictionary = ["a","b","c"]
 * 输出："a"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 1000
 * 1 <= dictionary.length <= 1000
 * 1 <= dictionary[i].length <= 1000
 * s 和 dictionary[i] 仅由小写英文字母组成
 *
 *
 */

/**
 * @File    :   524.通过删除字母匹配到字典里最长单词.go
 * @Time    :   2021/09/14 09:10:14
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func findLongestWord(s string, dictionary []string) string {
	ans := ""
	n := len(s)

	isSubsequence := func(w string) bool {
		i, j, m := 0, 0, len(w)
		for i < m && j < n {
			if w[i] == s[j] {
				i++
			}
			j++
		}
		return i == m
	}

	for _, word := range dictionary {
		if isSubsequence(word) {
			if len(word) > len(ans) {
				ans = word
			} else if len(word) == len(ans) && word < ans {
				ans = word
			}
		}
	}

	return ans
}

// @lc code=end
