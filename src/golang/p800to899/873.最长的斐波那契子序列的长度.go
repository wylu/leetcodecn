package p800to899

/*
 * @lc app=leetcode.cn id=873 lang=golang
 *
 * [873] 最长的斐波那契子序列的长度
 *
 * https://leetcode.cn/problems/length-of-longest-fibonacci-subsequence/description/
 *
 * algorithms
 * Medium (54.91%)
 * Likes:    310
 * Dislikes: 0
 * Total Accepted:    35K
 * Total Submissions: 63.8K
 * Testcase Example:  '[1,2,3,4,5,6,7,8]'
 *
 * 如果序列 X_1, X_2, ..., X_n 满足下列条件，就说它是 斐波那契式 的：
 *
 *
 * n >= 3
 * 对于所有 i + 2 ，都有 X_i + X_{i+1} = X_{i+2}
 *
 *
 * 给定一个严格递增的正整数数组形成序列 arr ，找到 arr 中最长的斐波那契式的子序列的长度。如果一个不存在，返回  0 。
 *
 * （回想一下，子序列是从原序列 arr 中派生出来的，它从 arr 中删掉任意数量的元素（也可以不删），而不改变其余元素的顺序。例如， [3, 5, 8]
 * 是 [3, 4, 5, 6, 7, 8] 的一个子序列）
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入: arr = [1,2,3,4,5,6,7,8]
 * 输出: 5
 * 解释: 最长的斐波那契式子序列为 [1,2,3,5,8] 。
 *
 *
 * 示例 2：
 *
 *
 * 输入: arr = [1,3,7,11,12,14,18]
 * 输出: 3
 * 解释: 最长的斐波那契式子序列有 [1,11,12]、[3,11,14] 以及 [7,11,18] 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 3 <= arr.length <= 1000
 * 1 <= arr[i] < arr[i + 1] <= 10^9
 *
 *
 *
 */

/**
 * @File    :   873.最长的斐波那契子序列的长度.go
 * @Time    :   2022/07/09 19:14:15
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func lenLongestFibSubseq(arr []int) int {
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	n := len(arr)
	indices := make(map[int]int, n)
	for i, x := range arr {
		indices[x] = i
	}

	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, n)
	}

	ans := 0
	for i, x := range arr {
		for j := i - 1; j >= 0 && arr[j]*2 > x; j-- {
			if k, ok := indices[x-arr[j]]; ok {
				dp[j][i] = max(dp[k][j]+1, 3)
				ans = max(ans, dp[j][i])
			}
		}
	}

	return ans
}

// @lc code=end

// func lenLongestFibSubseq(arr []int) int {
// 	n := len(arr)
// 	seen := make(map[int]bool, n)
// 	for _, num := range arr {
// 		seen[num] = true
// 	}

// 	ans := 0
// 	for i := 0; i < n-1; i++ {
// 		for j := i + 1; j < n; j++ {
// 			cnt := 0
// 			for a, b := arr[i], arr[j]; seen[a+b]; a, b = b, a+b {
// 				cnt++
// 			}
// 			if cnt > ans {
// 				ans = cnt
// 			}
// 		}
// 	}

// 	if ans > 0 {
// 		ans += 2
// 	}

// 	return ans
// }
