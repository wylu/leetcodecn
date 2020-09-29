package p1500to1599

/*
 * @lc app=leetcode.cn id=1513 lang=golang
 *
 * [1513] 仅含 1 的子串数
 *
 * https://leetcode-cn.com/problems/number-of-substrings-with-only-1s/description/
 *
 * algorithms
 * Medium (36.27%)
 * Likes:    9
 * Dislikes: 0
 * Total Accepted:    7.7K
 * Total Submissions: 21.3K
 * Testcase Example:  '"0110111"'
 *
 * 给你一个二进制字符串 s（仅由 '0' 和 '1' 组成的字符串）。
 *
 * 返回所有字符都为 1 的子字符串的数目。
 *
 * 由于答案可能很大，请你将它对 10^9 + 7 取模后返回。
 *
 *
 *
 * 示例 1：
 *
 * 输入：s = "0110111"
 * 输出：9
 * 解释：共有 9 个子字符串仅由 '1' 组成
 * "1" -> 5 次
 * "11" -> 3 次
 * "111" -> 1 次
 *
 * 示例 2：
 *
 * 输入：s = "101"
 * 输出：2
 * 解释：子字符串 "1" 在 s 中共出现 2 次
 *
 *
 * 示例 3：
 *
 * 输入：s = "111111"
 * 输出：21
 * 解释：每个子字符串都仅由 '1' 组成
 *
 *
 * 示例 4：
 *
 * 输入：s = "000"
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * s[i] == '0' 或 s[i] == '1'
 * 1 <= s.length <= 10^5
 *
 *
 */

/**
 * @File    :   1513.仅含-1-的子串数.go
 * @Time    :   2020/09/29 20:02:51
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func numSub(s string) int {
	ans, cnt := 0, 0
	for i := 0; i < len(s); i++ {
		if s[i] == '0' {
			ans += (1 + cnt) * cnt / 2
			ans %= 1000000007
			cnt = 0
		} else {
			cnt++
		}
	}

	ans += (1 + cnt) * cnt / 2
	return ans % 1000000007
}

// @lc code=end
