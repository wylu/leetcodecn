package p1200to1299

/*
 * @lc app=leetcode.cn id=1220 lang=golang
 *
 * [1220] 统计元音字母序列的数目
 *
 * https://leetcode-cn.com/problems/count-vowels-permutation/description/
 *
 * algorithms
 * Hard (60.71%)
 * Likes:    130
 * Dislikes: 0
 * Total Accepted:    21.6K
 * Total Submissions: 35.5K
 * Testcase Example:  '1'
 *
 * 给你一个整数 n，请你帮忙统计一下我们可以按下述规则形成多少个长度为 n 的字符串：
 *
 *
 * 字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'）
 * 每个元音 'a' 后面都只能跟着 'e'
 * 每个元音 'e' 后面只能跟着 'a' 或者是 'i'
 * 每个元音 'i' 后面 不能 再跟着另一个 'i'
 * 每个元音 'o' 后面只能跟着 'i' 或者是 'u'
 * 每个元音 'u' 后面只能跟着 'a'
 *
 *
 * 由于答案可能会很大，所以请你返回 模 10^9 + 7 之后的结果。
 *
 *
 *
 * 示例 1：
 *
 * 输入：n = 1
 * 输出：5
 * 解释：所有可能的字符串分别是："a", "e", "i" , "o" 和 "u"。
 *
 *
 * 示例 2：
 *
 * 输入：n = 2
 * 输出：10
 * 解释：所有可能的字符串分别是："ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" 和
 * "ua"。
 *
 *
 * 示例 3：
 *
 * 输入：n = 5
 * 输出：68
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 2 * 10^4
 *
 *
 */

/**
 * @File    :   1220.统计元音字母序列的数目.go
 * @Time    :   2022/01/17 23:03:50
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func countVowelPermutation(n int) int {
	MOD := int(1e9 + 7)
	f := make([][5]int, n+1)
	f[1] = [5]int{1, 1, 1, 1, 1}
	for i := 2; i <= n; i++ {
		f[i][0] = (f[i-1][1] + f[i-1][2] + f[i-1][4]) % MOD
		f[i][1] = (f[i-1][0] + f[i-1][2]) % MOD
		f[i][2] = (f[i-1][1] + f[i-1][3]) % MOD
		f[i][3] = f[i-1][2]
		f[i][4] = (f[i-1][2] + f[i-1][3]) % MOD
	}

	return (f[n][0] + f[n][1] + f[n][2] + f[n][3] + f[n][4]) % MOD
}

// @lc code=end
