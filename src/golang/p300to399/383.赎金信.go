package p300to399

/*
 * @lc app=leetcode.cn id=383 lang=golang
 *
 * [383] 赎金信
 *
 * https://leetcode-cn.com/problems/ransom-note/description/
 *
 * algorithms
 * Easy (61.68%)
 * Likes:    210
 * Dislikes: 0
 * Total Accepted:    86.5K
 * Total Submissions: 140.3K
 * Testcase Example:  '"a"\n"b"'
 *
 * 为了不在赎金信中暴露字迹，从杂志上搜索各个需要的字母，组成单词来表达意思。
 *
 * 给你一个赎金信 (ransomNote) 字符串和一个杂志(magazine)字符串，判断 ransomNote 能不能由 magazines
 * 里面的字符构成。
 *
 * 如果可以构成，返回 true ；否则返回 false 。
 *
 * magazine 中的每个字符只能在 ransomNote 中使用一次。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：ransomNote = "a", magazine = "b"
 * 输出：false
 *
 *
 * 示例 2：
 *
 *
 * 输入：ransomNote = "aa", magazine = "ab"
 * 输出：false
 *
 *
 * 示例 3：
 *
 *
 * 输入：ransomNote = "aa", magazine = "aab"
 * 输出：true
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= ransomNote.length, magazine.length <= 10^5
 * ransomNote 和 magazine 由小写英文字母组成
 *
 *
 */

/**
 * @File    :   383.赎金信.go
 * @Time    :   2021/12/04 09:04:23
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func canConstruct(ransomNote string, magazine string) bool {
	cnt := [26]int{}
	m, n := len(ransomNote), len(magazine)

	for i := 0; i < n; i++ {
		cnt[magazine[i]-'a']++
	}

	for i := 0; i < m; i++ {
		cnt[ransomNote[i]-'a']--
		if cnt[ransomNote[i]-'a'] < 0 {
			return false
		}
	}

	return true
}

// @lc code=end
