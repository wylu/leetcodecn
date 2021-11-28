package p400to499

/*
 * @lc app=leetcode.cn id=438 lang=golang
 *
 * [438] 找到字符串中所有字母异位词
 *
 * https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/description/
 *
 * algorithms
 * Medium (52.42%)
 * Likes:    670
 * Dislikes: 0
 * Total Accepted:    107.5K
 * Total Submissions: 205.3K
 * Testcase Example:  '"cbaebabacd"\n"abc"'
 *
 * 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
 *
 * 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: s = "cbaebabacd", p = "abc"
 * 输出: [0,6]
 * 解释:
 * 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
 * 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
 *
 *
 * 示例 2:
 *
 *
 * 输入: s = "abab", p = "ab"
 * 输出: [0,1,2]
 * 解释:
 * 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
 * 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
 * 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
 *
 *
 *
 *
 * 提示:
 *
 *
 * 1 <= s.length, p.length <= 3 * 10^4
 * s 和 p 仅包含小写字母
 *
 *
 */

/**
 * @File    :   438.找到字符串中所有字母异位词.go
 * @Time    :   2021/11/28 09:58:25
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func findAnagrams(s string, p string) []int {
	n, m := len(s), len(p)
	if n < m {
		return []int{}
	}

	ans := []int{}
	want := [26]int{}
	cnt := [26]int{}
	for i := 0; i < m; i++ {
		want[p[i]-'a']++
		cnt[s[i]-'a']++
	}
	if cnt == want {
		ans = append(ans, 0)
	}

	for i := 0; i < n-m; i++ {
		cnt[s[i]-'a']--
		cnt[s[i+m]-'a']++
		if cnt == want {
			ans = append(ans, i+1)
		}
	}

	return ans
}

// @lc code=end
