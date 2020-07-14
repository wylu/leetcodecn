package p100to199

/*
 * @lc app=leetcode.cn id=120 lang=golang
 *
 * [120] 三角形最小路径和
 *
 * https://leetcode-cn.com/problems/triangle/description/
 *
 * algorithms
 * Medium (65.03%)
 * Likes:    482
 * Dislikes: 0
 * Total Accepted:    77.9K
 * Total Submissions: 117.9K
 * Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
 *
 * 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
 *
 * 相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
 *
 *
 *
 * 例如，给定三角形：
 *
 * [
 * ⁠    [2],
 * ⁠   [3,4],
 * ⁠  [6,5,7],
 * ⁠ [4,1,8,3]
 * ]
 *
 *
 * 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
 *
 *
 *
 * 说明：
 *
 * 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
 *
 */

/**
 * @File    :   120.三角形最小路径和.go
 * @Time    :   2020/07/14 12:45:58
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 * Dynamic Programming
 *
 * State:
 *   dp[j]: 表示自顶向下到达该层的第 j+1 个结点的最小路径和。
 *
 * Initial State:
 *   dp[0] = triangle[0][0]  // i = 0
 *
 * State Transition:
 *   1 <= i < n
 *   dp[i] = dp[i-1] + triangle[i][i]  // j == i
 *   dp[j] = min(dp[j-1], dp[j]) + triangle[i][i];  // 1 <= j <= i-1
 *   dp[0] += triangle[i][0];  // j == 0
 */
// @lc code=start
func minimumTotal(triangle [][]int) int {
	if triangle == nil || len(triangle) == 0 {
		return -1
	}

	n := len(triangle)
	dp := make([]int, len(triangle[n-1]))
	dp[0] = triangle[0][0]

	for i := 1; i < n; i++ {
		dp[i] = dp[i-1] + triangle[i][i]
		for j := i - 1; j > 0; j-- {
			dp[j] = min120(dp[j-1], dp[j]) + triangle[i][j]
		}
		dp[0] += triangle[i][0]
	}

	res := dp[0]
	for i := 1; i < len(dp); i++ {
		if dp[i] < res {
			res = dp[i]
		}
	}
	return res
}

func min120(x, y int) int {
	if x < y {
		return x
	}
	return y
}

// @lc code=end
