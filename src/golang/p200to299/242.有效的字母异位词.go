package p200to299

/*
 * @lc app=leetcode.cn id=242 lang=golang
 *
 * [242] 有效的字母异位词
 *
 * https://leetcode-cn.com/problems/valid-anagram/description/
 *
 * algorithms
 * Easy (61.95%)
 * Likes:    298
 * Dislikes: 0
 * Total Accepted:    170.9K
 * Total Submissions: 271.8K
 * Testcase Example:  '"anagram"\n"nagaram"'
 *
 * 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
 *
 * 示例 1:
 *
 * 输入: s = "anagram", t = "nagaram"
 * 输出: true
 *
 *
 * 示例 2:
 *
 * 输入: s = "rat", t = "car"
 * 输出: false
 *
 * 说明:
 * 你可以假设字符串只包含小写字母。
 *
 * 进阶:
 * 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
 *
 */

/**
 * @File    :   242.有效的字母异位词.go
 * @Time    :   2020/11/22 17:22:09
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	cnts := [26]int{}
	for i := 0; i < len(s); i++ {
		cnts[s[i]-'a']++
		cnts[t[i]-'a']--
	}
	for i := 0; i < 26; i++ {
		if cnts[i] != 0 {
			return false
		}
	}
	return true
}

// @lc code=end
