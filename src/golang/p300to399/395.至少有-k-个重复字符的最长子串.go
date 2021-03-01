package p300to399

import "strings"

/*
 * @lc app=leetcode.cn id=395 lang=golang
 *
 * [395] 至少有 K 个重复字符的最长子串
 *
 * https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
 *
 * algorithms
 * Medium (51.82%)
 * Likes:    426
 * Dislikes: 0
 * Total Accepted:    38.9K
 * Total Submissions: 75.1K
 * Testcase Example:  '"aaabb"\n3'
 *
 * 给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "aaabb", k = 3
 * 输出：3
 * 解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "ababbc", k = 2
 * 输出：5
 * 解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 10^4
 * s 仅由小写英文字母组成
 * 1 <= k <= 10^5
 *
 *
 */

/**
 * @File    :   395.至少有-k-个重复字符的最长子串.go
 * @Time    :   2021/03/01 20:08:09
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：分治
 * 对于字符串 s，如果存在某个字符 ch，它的出现次数大于 0 且小于 k，
 * 则任何包含 ch 的子串都不可能满足要求。也就是说，我们将字符串按照
 * ch 切分成若干段，则满足要求的最长子串一定出现在某个被切分的段内，
 * 而不能跨越一个或多个段。因此，可以考虑分治的方式求解本题。
 */

// @lc code=start
func longestSubstring(s string, k int) int {
	cnts := [26]int{}
	for _, ch := range s {
		cnts[ch-'a']++
	}

	sep := ""
	for i := 0; i < 26; i++ {
		if cnts[i] > 0 && cnts[i] < k {
			sep = string('a' + byte(i))
			break
		}
	}

	if sep == "" {
		return len(s)
	}

	ans := 0
	for _, ss := range strings.Split(s, sep) {
		tmp := longestSubstring(ss, k)
		if tmp > ans {
			ans = tmp
		}
	}

	return ans
}

// @lc code=end
