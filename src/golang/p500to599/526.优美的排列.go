package p500to599

/*
 * @lc app=leetcode.cn id=526 lang=golang
 *
 * [526] 优美的排列
 *
 * https://leetcode-cn.com/problems/beautiful-arrangement/description/
 *
 * algorithms
 * Medium (71.68%)
 * Likes:    198
 * Dislikes: 0
 * Total Accepted:    23.6K
 * Total Submissions: 33K
 * Testcase Example:  '2'
 *
 * 假设有从 1 到 N 的 N 个整数，如果从这 N 个数字中成功构造出一个数组，使得数组的第 i 位 (1 <= i <= N)
 * 满足如下两个条件中的一个，我们就称这个数组为一个优美的排列。条件：
 *
 *
 * 第 i 位的数字能被 i 整除
 * i 能被第 i 位上的数字整除
 *
 *
 * 现在给定一个整数 N，请问可以构造多少个优美的排列？
 *
 * 示例1:
 *
 *
 * 输入: 2
 * 输出: 2
 * 解释:
 *
 * 第 1 个优美的排列是 [1, 2]:
 * ⁠ 第 1 个位置（i=1）上的数字是1，1能被 i（i=1）整除
 * ⁠ 第 2 个位置（i=2）上的数字是2，2能被 i（i=2）整除
 *
 * 第 2 个优美的排列是 [2, 1]:
 * ⁠ 第 1 个位置（i=1）上的数字是2，2能被 i（i=1）整除
 * ⁠ 第 2 个位置（i=2）上的数字是1，i（i=2）能被 1 整除
 *
 *
 * 说明:
 *
 *
 * N 是一个正整数，并且不会超过15。
 *
 *
 */

/**
 * @File    :   526.优美的排列.go
 * @Time    :   2021/08/16 17:34:01
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func countArrangement(n int) int {
	size := 1 << n
	f := make([]int, size)
	f[0] = 1

	binCount := func(x int) int {
		cnt := 0
		for x > 0 {
			cnt += x & 1
			x >>= 1
		}
		return cnt
	}

	for mask := 1; mask < size; mask++ {
		num := binCount(mask)
		for i := 0; i < n; i++ {
			if mask&(1<<i) != 0 && (num%(i+1) == 0 || (i+1)%num == 0) {
				f[mask] += f[mask^(1<<i)]
			}
		}
	}

	return f[size-1]
}

// @lc code=end

// func countArrangement(n int) int {
// 	used := make([]bool, n+1)

// 	var dfs func(cur int) int
// 	dfs = func(cur int) int {
// 		if cur == n+1 {
// 			return 1
// 		}

// 		res := 0
// 		for i := 1; i <= n; i++ {
// 			if !used[i] && (cur%i == 0 || i%cur == 0) {
// 				used[i] = true
// 				res += dfs(cur + 1)
// 				used[i] = false
// 			}
// 		}
// 		return res
// 	}

// 	return dfs(1)
// }
