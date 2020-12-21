package p1000to1099

/*
 * @lc app=leetcode.cn id=1081 lang=golang
 *
 * [1081] 不同字符的最小子序列
 *
 * https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters/description/
 *
 * algorithms
 * Medium (56.32%)
 * Likes:    73
 * Dislikes: 0
 * Total Accepted:    8.4K
 * Total Submissions: 14.9K
 * Testcase Example:  '"bcabc"'
 *
 * 返回字符串 text 中按字典序排列最小的子序列，该子序列包含 text 中所有不同字符一次。
 *
 *
 *
 * 示例 1：
 *
 * 输入："cdadabcc"
 * 输出："adbc"
 *
 *
 * 示例 2：
 *
 * 输入："abcd"
 * 输出："abcd"
 *
 *
 * 示例 3：
 *
 * 输入："ecbacba"
 * 输出："eacb"
 *
 *
 * 示例 4：
 *
 * 输入："leetcode"
 * 输出："letcod"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= text.length <= 1000
 * text 由小写英文字母组成
 *
 *
 *
 *
 * 注意：本题目与 316 https://leetcode-cn.com/problems/remove-duplicate-letters/ 相同
 *
 */

/**
 * @File    :   1081.不同字符的最小子序列.go
 * @Time    :   2020/12/21 10:52:57
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * 方法一：贪心 + 栈
 * 思路与算法
 *
 * 首先考虑一个简单的问题：给定一个字符串 s，如何去掉其中的一个字符 ch，
 * 使得得到的字符串字典序最小呢？答案是：找出最小的满足 s[i] > s[i+1]
 * 的下标 i，并去除字符 s[i]。为了叙述方便，下文中称这样的字符为
 * 「关键字符」。
 *
 * 在理解这一点之后，就可以着手本题了。一个直观的思路是：我们在字符串
 * s 中找到「关键字符」，去除它，然后不断进行这样的循环。但是这种朴素
 * 的解法会创建大量的中间字符串，我们有必要寻找一种更优的方法。
 *
 * 我们从前向后扫描原字符串。每扫描到一个位置，我们就尽可能地处理所有
 * 的「关键字符」。假定在扫描位置 s[i-1] 之前的所有「关键字符」都已经
 * 被去除完毕，在扫描字符 s[i] 时，新出现的「关键字符」只可能出现在
 * s[i] 或者其后面的位置。
 *
 * 于是，我们使用栈来维护去除「关键字符」后得到的字符串。如果栈顶字符
 * 大于当前字符 s[i]，说明栈顶字符为「关键字符」，故应当被去除。去除后，
 * 新的栈顶字符就与 s[i] 相邻了，我们继续比较新的栈顶字符与 s[i] 的
 * 大小。重复上述操作，直到栈为空或者栈顶字符不大于 s[i]。
 *
 * 我们还遗漏了一个要求：原字符串 s 中的每个字符都需要出现在新字符串中，
 * 且只能出现一次。为了让新字符串满足该要求，之前讨论的算法需要进行以下
 * 两点的更改。
 *
 * 在考虑字符 s[i] 时，如果它已经存在于栈中，则不能加入字符 s[i]。为此，
 * 需要记录每个字符是否出现在栈中。
 *
 * 在弹出栈顶字符时，如果字符串在后面的位置上再也没有这一字符，则不能
 * 弹出栈顶字符。为此，需要记录每个字符的剩余数量，当这个值为 0 时，
 * 就不能弹出栈顶字符了。
 */

// @lc code=start
func smallestSubsequence(s string) string {
	last := [26]int{}
	for i := 0; i < len(s); i++ {
		last[s[i]-'a'] = i
	}
	ans, visit := []byte{}, [26]bool{}

	for i := 0; i < len(s); i++ {
		if visit[s[i]-'a'] {
			continue
		}

		n := len(ans)
		for n > 0 && ans[n-1] > s[i] && last[ans[n-1]-'a'] > i {
			visit[ans[n-1]-'a'] = false
			ans = ans[:n-1]
			n--
		}

		visit[s[i]-'a'] = true
		ans = append(ans, s[i])
	}

	return string(ans)
}

// @lc code=end
