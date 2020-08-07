package p300to399

/*
 * @lc app=leetcode.cn id=336 lang=golang
 *
 * [336] 回文对
 *
 * https://leetcode-cn.com/problems/palindrome-pairs/description/
 *
 * algorithms
 * Hard (34.50%)
 * Likes:    143
 * Dislikes: 0
 * Total Accepted:    14.4K
 * Total Submissions: 37.5K
 * Testcase Example:  '["abcd","dcba","lls","s","sssll"]'
 *
 * 给定一组 互不相同 的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j]
 * ，可拼接成回文串。
 *
 *
 *
 * 示例 1：
 *
 * 输入：["abcd","dcba","lls","s","sssll"]
 * 输出：[[0,1],[1,0],[3,2],[2,4]]
 * 解释：可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
 *
 *
 * 示例 2：
 *
 * 输入：["bat","tab","cat"]
 * 输出：[[0,1],[1,0]]
 * 解释：可拼接成的回文串为 ["battab","tabbat"]
 *
 */

// @lc code=start
func palindromePairs(words []string) [][]int {
	reverse := func(s string) string {
		r := []rune(s)
		for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
			r[i], r[j] = r[j], r[i]
		}
		return string(r)
	}

	n := len(words)
	indices := make(map[string]int, n)
	for i := 0; i < n; i++ {
		indices[reverse(words[i])] = i
	}

	findWord := func(s string, i, j int) int {
		if idx, ok := indices[s[i:j+1]]; ok {
			return idx
		}
		return -1
	}

	isPalindrome := func(s string, i, j int) bool {
		for ; i < j; i, j = i+1, j-1 {
			if s[i] != s[j] {
				return false
			}
		}
		return true
	}

	ans := [][]int{}
	for i := 0; i < n; i++ {
		m := len(words[i])
		for j := 0; j < m+1; j++ {
			if isPalindrome(words[i], j, m-1) {
				rightID := findWord(words[i], 0, j-1)
				if rightID != -1 && rightID != i {
					ans = append(ans, []int{i, rightID})
				}
			}

			if j > 0 && isPalindrome(words[i], 0, j-1) {
				leftID := findWord(words[i], j, m-1)
				if leftID != -1 && leftID != i {
					ans = append(ans, []int{leftID, i})
				}
			}
		}
	}

	return ans
}

// @lc code=end
