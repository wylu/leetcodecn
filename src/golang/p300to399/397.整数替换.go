package p300to399

/*
 * @lc app=leetcode.cn id=397 lang=golang
 *
 * [397] 整数替换
 *
 * https://leetcode-cn.com/problems/integer-replacement/description/
 *
 * algorithms
 * Medium (37.68%)
 * Likes:    184
 * Dislikes: 0
 * Total Accepted:    40.7K
 * Total Submissions: 96K
 * Testcase Example:  '8'
 *
 * 给定一个正整数 n ，你可以做如下操作：
 *
 *
 * 如果 n 是偶数，则用 n / 2替换 n 。
 * 如果 n 是奇数，则可以用 n + 1或n - 1替换 n 。
 *
 *
 * n 变为 1 所需的最小替换次数是多少？
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 8
 * 输出：3
 * 解释：8 -> 4 -> 2 -> 1
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 7
 * 输出：4
 * 解释：7 -> 8 -> 4 -> 2 -> 1
 * 或 7 -> 6 -> 3 -> 2 -> 1
 *
 *
 * 示例 3：
 *
 *
 * 输入：n = 4
 * 输出：2
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 2^31 - 1
 *
 *
 */

/**
 * @File    :   397.整数替换.go
 * @Time    :   2021/11/19 20:42:50
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func integerReplacement(n int) int {
	cache := map[int]int{1: 0}

	min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}

	var dfs func(int) int
	dfs = func(n int) int {
		if val, ok := cache[n]; ok {
			return val
		}

		if n%2 == 0 {
			cache[n] = 1 + dfs(n/2)
		} else {
			// cache[n] = 1 + min(dfs(n+1), dfs(n-1))
			cache[n] = 2 + min(dfs(n/2), dfs(n/2+1))
		}

		return cache[n]
	}

	return dfs(n)
}

// @lc code=end
