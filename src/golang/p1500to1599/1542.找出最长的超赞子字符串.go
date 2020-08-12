package p1500to1599

/*
 * @lc app=leetcode.cn id=1542 lang=golang
 *
 * [1542] 找出最长的超赞子字符串
 *
 * https://leetcode-cn.com/problems/find-longest-awesome-substring/description/
 *
 * algorithms
 * Hard (31.16%)
 * Likes:    17
 * Dislikes: 0
 * Total Accepted:    1K
 * Total Submissions: 3.4K
 * Testcase Example:  '"3242415"'
 *
 * 给你一个字符串 s 。请返回 s 中最长的 超赞子字符串 的长度。
 *
 * 「超赞子字符串」需满足满足下述两个条件：
 *
 *
 * 该字符串是 s 的一个非空子字符串
 * 进行任意次数的字符交换后，该字符串可以变成一个回文字符串
 *
 *
 *
 *
 * 示例 1：
 *
 * 输入：s = "3242415"
 * 输出：5
 * 解释："24241" 是最长的超赞子字符串，交换其中的字符后，可以得到回文 "24142"
 *
 *
 * 示例 2：
 *
 * 输入：s = "12345678"
 * 输出：1
 *
 *
 * 示例 3：
 *
 * 输入：s = "213123"
 * 输出：6
 * 解释："213123" 是最长的超赞子字符串，交换其中的字符后，可以得到回文 "231132"
 *
 *
 * 示例 4：
 *
 * 输入：s = "00"
 * 输出：2
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 10^5
 * s 仅由数字组成
 *
 *
 */

/**
 * @File    :   1542.找出最长的超赞子字符串.go
 * @Time    :   2020/08/12 22:15:07
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func longestAwesome(s string) int {
	good := [11]int{}
	for i := 0; i < 10; i++ {
		good[i+1] = 1 << i
	}

	first := [1 << 10]int{}
	for i := 1; i < 1024; i++ {
		first[i] = -1
	}

	ans := 0
	state := 0
	for i := 1; i < len(s)+1; i++ {
		c := s[i-1] - '0'
		state ^= (1 << c)

		if first[state] == -1 {
			first[state] = i
		}

		for _, g := range good {
			need := g ^ state
			if first[need] != -1 {
				ans = max1542(ans, i-first[need])
			}
		}
	}

	return ans
}

func max1542(x, y int) int {
	if x > y {
		return x
	}
	return y
}

// @lc code=end
