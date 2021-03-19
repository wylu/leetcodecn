package p1to99

/*
 * @lc app=leetcode.cn id=59 lang=golang
 *
 * [59] 螺旋矩阵 II
 *
 * https://leetcode-cn.com/problems/spiral-matrix-ii/description/
 *
 * algorithms
 * Medium (79.71%)
 * Likes:    353
 * Dislikes: 0
 * Total Accepted:    79.1K
 * Total Submissions: 99K
 * Testcase Example:  '3'
 *
 * 给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 3
 * 输出：[[1,2,3],[8,9,4],[7,6,5]]
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 1
 * 输出：[[1]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 20
 *
 *
 */

/**
 * @File    :   59.螺旋矩阵-ii.go
 * @Time    :   2021/03/19 13:33:49
 * @Author  :   wylu
 * @Version :   1.0
 * @Contact :   15wylu@gmail.com
 * @License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
 * @Desc    :
 */

// @lc code=start
func generateMatrix(n int) [][]int {
	ans := make([][]int, n)
	for i := 0; i < n; i++ {
		ans[i] = make([]int, n)
	}

	for s, c := 0, 1; s <= (n-1)/2; s++ {
		e := n - s

		for i := s; i < e; i, c = i+1, c+1 {
			ans[s][i] = c
		}

		for i := s + 1; i < e; i, c = i+1, c+1 {
			ans[i][e-1] = c
		}

		for i := e - 2; i >= s; i, c = i-1, c+1 {
			ans[e-1][i] = c
		}

		for i := e - 2; i > s; i, c = i-1, c+1 {
			ans[i][s] = c
		}

	}

	return ans
}

// @lc code=end
