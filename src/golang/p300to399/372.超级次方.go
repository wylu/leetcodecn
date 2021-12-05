package p300to399

/*
 * @lc app=leetcode.cn id=372 lang=golang
 *
 * [372] 超级次方
 *
 * https://leetcode-cn.com/problems/super-pow/description/
 *
 * algorithms
 * Medium (52.45%)
 * Likes:    158
 * Dislikes: 0
 * Total Accepted:    17.4K
 * Total Submissions: 33.3K
 * Testcase Example:  '2\n[3]'
 *
 * 你的任务是计算 a^b 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：a = 2, b = [3]
 * 输出：8
 *
 *
 * 示例 2：
 *
 *
 * 输入：a = 2, b = [1,0]
 * 输出：1024
 *
 *
 * 示例 3：
 *
 *
 * 输入：a = 1, b = [4,3,3,8,5,2]
 * 输出：1
 *
 *
 * 示例 4：
 *
 *
 * 输入：a = 2147483647, b = [2,0,0]
 * 输出：1198
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= a <= 2^31 - 1
 * 1 <= b.length <= 2000
 * 0 <= b[i] <= 9
 * b 不含前导 0
 *
 *
 */

/**
 * @File    :   372.超级次方.go
 * @Time    :   2021/12/05 09:40:08
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func superPow(a int, b []int) int {
	MOD := 1337

	quickPower := func(a, b int) int {
		res := 1
		for b > 0 {
			if b&1 == 1 {
				res = res * a % MOD
			}
			a = a * a % MOD
			b >>= 1
		}
		return res
	}

	ans := 1
	for _, e := range b {
		ans = quickPower(ans, 10) * quickPower(a, e) % MOD
	}

	return ans
}

// @lc code=end

// func superPow(a int, b []int) int {
// 	MOD := 1337

// 	quickPower := func(a, b int) int {
// 		res := 1
// 		for b > 0 {
// 			if b&1 == 1 {
// 				res = res * a % MOD
// 			}
// 			a = a * a % MOD
// 			b >>= 1
// 		}
// 		return res
// 	}

// 	var dfs func(int, []int, int) int
// 	dfs = func(a int, b []int, c int) int {
// 		if c < 0 {
// 			return 1
// 		}
// 		return quickPower(dfs(a, b, c-1), 10) * quickPower(a, b[c]) % MOD
// 	}

// 	return dfs(a, b, len(b)-1)
// }
