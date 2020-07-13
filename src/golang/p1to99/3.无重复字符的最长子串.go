package p1to99

/*
 * @lc app=leetcode.cn id=3 lang=golang
 *
 * [3] 无重复字符的最长子串
 *
 * https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
 *
 * algorithms
 * Medium (34.91%)
 * Likes:    3957
 * Dislikes: 0
 * Total Accepted:    564.5K
 * Total Submissions: 1.6M
 * Testcase Example:  '"abcabcbb"'
 *
 * 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
 *
 * 示例 1:
 *
 * 输入: "abcabcbb"
 * 输出: 3
 * 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
 *
 *
 * 示例 2:
 *
 * 输入: "bbbbb"
 * 输出: 1
 * 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
 *
 *
 * 示例 3:
 *
 * 输入: "pwwkew"
 * 输出: 3
 * 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
 * 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 *
 *
 */

/**
 * @File    :   3.无重复字符的最长子串.go
 * @Time    :   2020/07/13 23:03:56
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */
// @lc code=start
func lengthOfLongestSubstring(s string) int {
	ch2idx := map[byte]int{}
	maxLen := 0
	for i, leftEdge := 0, 0; i < len(s); i++ {
		if idx, ok := ch2idx[s[i]]; ok && idx >= leftEdge {
			leftEdge = idx + 1
		} else if i-leftEdge+1 > maxLen {
			maxLen = i - leftEdge + 1
		}
		ch2idx[s[i]] = i
	}
	return maxLen
}

// @lc code=end
