package p1400to1499

import "math"

/*
 * @lc app=leetcode.cn id=1417 lang=golang
 *
 * [1417] 重新格式化字符串
 *
 * https://leetcode.cn/problems/reformat-the-string/description/
 *
 * algorithms
 * Easy (55.62%)
 * Likes:    79
 * Dislikes: 0
 * Total Accepted:    39.9K
 * Total Submissions: 71.8K
 * Testcase Example:  '"a0b1c2"'
 *
 * 给你一个混合了数字和字母的字符串 s，其中的字母均为小写英文字母。
 *
 * 请你将该字符串重新格式化，使得任意两个相邻字符的类型都不同。也就是说，字母后面应该跟着数字，而数字后面应该跟着字母。
 *
 * 请你返回 重新格式化后 的字符串；如果无法按要求重新格式化，则返回一个 空字符串 。
 *
 *
 *
 * 示例 1：
 *
 * 输入：s = "a0b1c2"
 * 输出："0a1b2c"
 * 解释："0a1b2c" 中任意两个相邻字符的类型都不同。 "a0b1c2", "0a1b2c", "0c2a1b" 也是满足题目要求的答案。
 *
 *
 * 示例 2：
 *
 * 输入：s = "leetcode"
 * 输出：""
 * 解释："leetcode" 中只有字母，所以无法满足重新格式化的条件。
 *
 *
 * 示例 3：
 *
 * 输入：s = "1229857369"
 * 输出：""
 * 解释："1229857369" 中只有数字，所以无法满足重新格式化的条件。
 *
 *
 * 示例 4：
 *
 * 输入：s = "covid2019"
 * 输出："c2o0v1i9d"
 *
 *
 * 示例 5：
 *
 * 输入：s = "ab123"
 * 输出："1a2b3"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 500
 * s 仅由小写英文字母和/或数字组成。
 *
 *
 */

/**
 * @File    :   1417.重新格式化字符串.go
 * @Time    :   2022/08/11 22:46:34
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func reformat(s string) string {
	first, second := []byte{}, []byte{}
	for _, ch := range s {
		if ch >= '0' && ch <= '9' {
			second = append(second, byte(ch))
		} else {
			first = append(first, byte(ch))
		}
	}

	if math.Abs(float64(len(first)-len(second))) > 1 {
		return ""
	}

	if len(first) < len(second) {
		first, second = second, first
	}

	ans := make([]byte, 0, len(s))
	m, n := len(first), len(second)
	for i, j := 0, 0; i < m || j < n; i, j = i+1, j+1 {
		if i < m {
			ans = append(ans, first[i])
		}
		if j < n {
			ans = append(ans, second[j])
		}
	}

	return string(ans)
}

// @lc code=end
