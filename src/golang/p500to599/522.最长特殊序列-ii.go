package p500to599

/*
 * @lc app=leetcode.cn id=522 lang=golang
 *
 * [522] 最长特殊序列 II
 *
 * https://leetcode.cn/problems/longest-uncommon-subsequence-ii/description/
 *
 * algorithms
 * Medium (46.84%)
 * Likes:    148
 * Dislikes: 0
 * Total Accepted:    23.2K
 * Total Submissions: 49.5K
 * Testcase Example:  '["aba","cdc","eae"]'
 *
 * 给定字符串列表 strs ，返回其中 最长的特殊序列 。如果最长特殊序列不存在，返回 -1 。
 *
 * 特殊序列 定义如下：该序列为某字符串 独有的子序列（即不能是其他字符串的子序列）。
 *
 * s 的 子序列可以通过删去字符串 s 中的某些字符实现。
 *
 *
 * 例如，"abc" 是 "aebdc" 的子序列，因为您可以删除"aebdc"中的下划线字符来得到 "abc"
 * 。"aebdc"的子序列还包括"aebdc"、 "aeb" 和 "" (空字符串)。
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入: strs = ["aba","cdc","eae"]
 * 输出: 3
 *
 *
 * 示例 2:
 *
 *
 * 输入: strs = ["aaa","aaa","aa"]
 * 输出: -1
 *
 *
 *
 *
 * 提示:
 *
 *
 * 2 <= strs.length <= 50
 * 1 <= strs[i].length <= 10
 * strs[i] 只包含小写英文字母
 *
 *
 */

/**
 * @File    :   522.最长特殊序列-ii.go
 * @Time    :   2022/06/27 20:56:16
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func findLUSlength522(strs []string) int {
	isSubseq := func(s, t string) bool {
		i := 0
		for j := range t {
			if s[i] == t[j] {
				if i++; i == len(s) {
					return true
				}
			}
		}
		return false
	}

	ans := -1

next:
	for i, s := range strs {
		for j, t := range strs {
			if i != j && isSubseq(s, t) {
				continue next
			}
		}
		if len(s) > ans {
			ans = len(s)
		}
	}

	return ans
}

// @lc code=end
