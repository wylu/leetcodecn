package p500to599

/*
 * @lc app=leetcode.cn id=541 lang=golang
 *
 * [541] 反转字符串 II
 *
 * https://leetcode-cn.com/problems/reverse-string-ii/description/
 *
 * algorithms
 * Easy (59.35%)
 * Likes:    159
 * Dislikes: 0
 * Total Accepted:    49.4K
 * Total Submissions: 83.2K
 * Testcase Example:  '"abcdefg"\n2'
 *
 * 给定一个字符串 s 和一个整数 k，从字符串开头算起，每 2k 个字符反转前 k 个字符。
 *
 *
 * 如果剩余字符少于 k 个，则将剩余字符全部反转。
 * 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "abcdefg", k = 2
 * 输出："bacdfeg"
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "abcd", k = 2
 * 输出："bacd"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 10^4
 * s 仅由小写英文组成
 * 1 <= k <= 10^4
 *
 *
 */

/**
 * @File    :   541.反转字符串-ii.go
 * @Time    :   2021/08/20 09:53:59
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func reverseStr(s string, k int) string {
	bs := []byte(s)
	reverse := func(i, j int) {
		for i < j {
			bs[i], bs[j] = bs[j], bs[i]
			i++
			j--
		}
	}
	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}

	n := len(bs)
	i, j := 0, 2*k-1
	for ; j < n; i, j = j+1, j+2*k {
		reverse(i, i+k-1)
	}
	if i < n-1 {
		reverse(i, min(i+k-1, n-1))
	}

	return string(bs)
}

// @lc code=end
