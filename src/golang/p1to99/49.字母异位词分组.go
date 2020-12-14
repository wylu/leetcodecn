package p1to99

import "sort"

/*
 * @lc app=leetcode.cn id=49 lang=golang
 *
 * [49] 字母异位词分组
 *
 * https://leetcode-cn.com/problems/group-anagrams/description/
 *
 * algorithms
 * Medium (64.09%)
 * Likes:    596
 * Dislikes: 0
 * Total Accepted:    146.9K
 * Total Submissions: 225.7K
 * Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
 *
 * 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
 *
 * 示例:
 *
 * 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
 * 输出:
 * [
 * ⁠ ["ate","eat","tea"],
 * ⁠ ["nat","tan"],
 * ⁠ ["bat"]
 * ]
 *
 * 说明：
 *
 *
 * 所有输入均为小写字母。
 * 不考虑答案输出的顺序。
 *
 *
 */

/**
 * @File    :   49.字母异位词分组.go
 * @Time    :   2020/12/14 22:08:28
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func groupAnagrams(strs []string) [][]string {
	words := map[string][]string{}

	for _, s := range strs {
		chs := []byte(s)
		sort.Slice(chs, func(i, j int) bool {
			return chs[i] <= chs[j]
		})
		wd := string(chs)
		words[wd] = append(words[wd], s)
	}

	ans := make([][]string, 0, len(words))
	for _, v := range words {
		ans = append(ans, v)
	}
	return ans
}

// @lc code=end
