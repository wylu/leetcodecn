package p1to99

/*
 * @lc app=leetcode.cn id=14 lang=golang
 *
 * [14] 最长公共前缀
 *
 * https://leetcode-cn.com/problems/longest-common-prefix/description/
 *
 * algorithms
 * Easy (38.80%)
 * Likes:    1291
 * Dislikes: 0
 * Total Accepted:    371.1K
 * Total Submissions: 956.5K
 * Testcase Example:  '["flower","flow","flight"]'
 *
 * 编写一个函数来查找字符串数组中的最长公共前缀。
 *
 * 如果不存在公共前缀，返回空字符串 ""。
 *
 * 示例 1:
 *
 * 输入: ["flower","flow","flight"]
 * 输出: "fl"
 *
 *
 * 示例 2:
 *
 * 输入: ["dog","racecar","car"]
 * 输出: ""
 * 解释: 输入不存在公共前缀。
 *
 *
 * 说明:
 *
 * 所有输入只包含小写字母 a-z 。
 *
 */

/**
 * @File    :   14.最长公共前缀.go
 * @Time    :   2020/10/02 14:32:40
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}

	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}

	ans := strs[0]
	for i := 1; i < len(strs); i++ {
		j, n := 0, min(len(ans), len(strs[i]))
		for j < n && ans[j] == strs[i][j] {
			j++
		}

		ans = ans[:j]
		if len(ans) == 0 {
			break
		}
	}

	return ans
}

// @lc code=end
