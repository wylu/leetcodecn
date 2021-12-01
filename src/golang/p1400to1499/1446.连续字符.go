package p1400to1499

/*
 * @lc app=leetcode.cn id=1446 lang=golang
 *
 * [1446] 连续字符
 *
 * https://leetcode-cn.com/problems/consecutive-characters/description/
 *
 * algorithms
 * Easy (61.11%)
 * Likes:    68
 * Dislikes: 0
 * Total Accepted:    38.2K
 * Total Submissions: 62.4K
 * Testcase Example:  '"leetcode"'
 *
 * 给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。
 *
 * 请你返回字符串的能量。
 *
 *
 *
 * 示例 1：
 *
 * 输入：s = "leetcode"
 * 输出：2
 * 解释：子字符串 "ee" 长度为 2 ，只包含字符 'e' 。
 *
 *
 * 示例 2：
 *
 * 输入：s = "abbcccddddeeeeedcba"
 * 输出：5
 * 解释：子字符串 "eeeee" 长度为 5 ，只包含字符 'e' 。
 *
 *
 * 示例 3：
 *
 * 输入：s = "triplepillooooow"
 * 输出：5
 *
 *
 * 示例 4：
 *
 * 输入：s = "hooraaaaaaaaaaay"
 * 输出：11
 *
 *
 * 示例 5：
 *
 * 输入：s = "tourist"
 * 输出：1
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 500
 * s 只包含小写英文字母。
 *
 *
 */

/**
 * @File    :   1446.连续字符.go
 * @Time    :   2021/12/01 19:42:19
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func maxPower(s string) int {
	n := len(s)
	ans, cnt := 1, 1
	for i := 1; i < n; i++ {
		if s[i] == s[i-1] {
			cnt++
			if cnt > ans {
				ans = cnt
			}
		} else {
			cnt = 1
		}
	}
	return ans
}

// @lc code=end
