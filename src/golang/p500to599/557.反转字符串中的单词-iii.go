package p500to599

/*
 * @lc app=leetcode.cn id=557 lang=golang
 *
 * [557] 反转字符串中的单词 III
 *
 * https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/description/
 *
 * algorithms
 * Easy (71.59%)
 * Likes:    217
 * Dislikes: 0
 * Total Accepted:    73K
 * Total Submissions: 102K
 * Testcase Example:  `"Let's take LeetCode contest"`
 *
 * 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
 *
 *
 *
 * 示例：
 *
 * 输入："Let's take LeetCode contest"
 * 输出："s'teL ekat edoCteeL tsetnoc"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
 *
 *
 */

// @lc code=start
func reverseWords(s string) string {
	sts := []byte(s)

	reverse := func(left, right int) {
		for left < right {
			sts[left], sts[right] = sts[right], sts[left]
			left++
			right--
		}
	}

	n, start := len(sts), 0
	for i := 1; i < n; i++ {
		if sts[i] == ' ' {
			reverse(start, i-1)
			start = i + 1
		}
	}
	reverse(start, n-1)

	return string(sts)
}

// @lc code=end
