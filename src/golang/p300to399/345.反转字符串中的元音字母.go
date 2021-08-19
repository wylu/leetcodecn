package p300to399

/*
 * @lc app=leetcode.cn id=345 lang=golang
 *
 * [345] 反转字符串中的元音字母
 *
 * https://leetcode-cn.com/problems/reverse-vowels-of-a-string/description/
 *
 * algorithms
 * Easy (52.77%)
 * Likes:    197
 * Dislikes: 0
 * Total Accepted:    90.5K
 * Total Submissions: 171.6K
 * Testcase Example:  '"hello"'
 *
 * 给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。
 *
 * 元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "hello"
 * 输出："holle"
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "leetcode"
 * 输出："leotcede"
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 3 * 10^5
 * s 由 可打印的 ASCII 字符组成
 *
 *
 */

// @lc code=start
func reverseVowels(s string) string {
	vowels := map[byte]struct{}{}
	for _, ch := range "aeiouAEIOU" {
		vowels[byte(ch)] = struct{}{}
	}

	bs := []byte(s)
	i, j := 0, len(bs)-1
	for i < j {
		for _, ok := vowels[bs[i]]; !ok && i < j; _, ok = vowels[bs[i]] {
			i++
		}
		for _, ok := vowels[bs[j]]; !ok && i < j; _, ok = vowels[bs[j]] {
			j--
		}
		if i < j {
			bs[i], bs[j] = bs[j], bs[i]
			i++
			j--
		}
	}

	return string(bs)
}

// @lc code=end
