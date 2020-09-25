package p1to99

/*
 * @lc app=leetcode.cn id=58 lang=golang
 *
 * [58] 最后一个单词的长度
 *
 * https://leetcode-cn.com/problems/length-of-last-word/description/
 *
 * algorithms
 * Easy (33.70%)
 * Likes:    243
 * Dislikes: 0
 * Total Accepted:    127.4K
 * Total Submissions: 378K
 * Testcase Example:  '"Hello World"'
 *
 * 给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。
 *
 * 如果不存在最后一个单词，请返回 0 。
 *
 * 说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。
 *
 *
 *
 * 示例:
 *
 * 输入: "Hello World"
 * 输出: 5
 *
 *
 */

/**
 * @File    :   58.最后一个单词的长度.go
 * @Time    :   2020/09/25 23:44:16
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func lengthOfLastWord(s string) int {
	n := len(s)
	j := n - 1
	for j >= 0 && s[j] == ' ' {
		j--
	}
	if j < 0 {
		return 0
	}
	i := j - 1
	for i >= 0 && s[i] != ' ' {
		i--
	}
	return j - i
}

// @lc code=end
